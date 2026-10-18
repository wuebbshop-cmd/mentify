import json
from django.test import TestCase
from django.contrib.auth import get_user_model
from prep.models import (
    PrepCourse,
    PrepTopic,
    PrepTopicQuizQuestion,
    PrepTopicQuizAttempt,
    PrepStudentSpacedCard,
    PrepStudentQuizSeen,
    PrepStudentQuestionUnlock,
    PrepQuestion,
)
from services.prep_topic_quiz import evaluate_quiz_answer, get_or_create_topic_quiz

User = get_user_model()


class PrepTopicQuizServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="quiz_student",
            email="quiz_student@example.com",
            password="secretpassword",
        )
        self.course = PrepCourse.objects.create(
            code="TEST 101",
            title="Introduction to Testing",
            is_active=True,
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            title="Software Architecture",
            slug="software-architecture",
            is_active=True,
        )
        self.q1 = PrepTopicQuizQuestion.objects.create(
            topic=self.topic,
            question_text="Which architectural pattern separates presentation from business logic?",
            options={
                "A": "Model-View-Controller (MVC)",
                "B": "Monolithic Pipeline",
                "C": "Peer-to-Peer Mesh",
                "D": "Shared Memory Pool",
            },
            correct_option="A",
            explanation={
                "summary": "MVC isolates domain logic, user interface, and user input controller.",
                "why_others_wrong": {
                    "B": "Monolithic pipeline tightly couples processing steps without presentation isolation.",
                    "C": "P2P is a distributed network topology, not a presentation/logic separation pattern.",
                    "D": "Shared memory pool is an inter-process communication mechanism.",
                },
            },
            difficulty="medium",
            is_active=True,
        )
        self.q2 = PrepTopicQuizQuestion.objects.create(
            topic=self.topic,
            question_text="What is the primary benefit of loose coupling between software modules?",
            options={
                "A": "Modules become dependent on internal state of other modules",
                "B": "Changes to one module have minimal ripple effect on other modules",
                "C": "It guarantees zero memory allocation overhead",
                "D": "It forces synchronous remote procedure calls",
            },
            correct_option="B",
            explanation={
                "summary": "Loose coupling minimizes cascading failures and allows independent maintainability.",
                "why_others_wrong": {
                    "A": "This describes tight coupling, which is the opposite of loose coupling.",
                    "C": "Coupling is a design quality attribute and does not directly control memory allocation.",
                    "D": "Loose coupling often favors asynchronous event-driven or decoupled messaging.",
                },
            },
            difficulty="easy",
            is_active=True,
        )

    def test_evaluate_correct_answer(self):
        result = evaluate_quiz_answer(
            quiz_question_id=self.q1.id,
            selected_option="A",
            user=self.user,
        )
        self.assertTrue(result["success"])
        self.assertTrue(result["is_correct"])
        self.assertEqual(result["correct_option"], "A")
        self.assertEqual(result["selected_option"], "A")
        self.assertIn("MVC isolates", result["summary_explanation"])

        # Check attempt was recorded in DB
        attempt = PrepTopicQuizAttempt.objects.filter(user=self.user, quiz_question=self.q1).first()
        self.assertIsNotNone(attempt)
        self.assertTrue(attempt.is_correct)
        self.assertEqual(attempt.selected_option, "A")

    def test_evaluate_incorrect_answer_records_distractor_and_spaced_card(self):
        result = evaluate_quiz_answer(
            quiz_question_id=self.q1.id,
            selected_option="C",
            user=self.user,
        )
        self.assertTrue(result["success"])
        self.assertFalse(result["is_correct"])
        self.assertEqual(result["correct_option"], "A")
        self.assertEqual(result["selected_option"], "C")
        self.assertIn("P2P is a distributed network topology", result["why_selected_is_wrong"])

        # Check attempt was recorded
        attempt = PrepTopicQuizAttempt.objects.filter(user=self.user, quiz_question=self.q1).first()
        self.assertIsNotNone(attempt)
        self.assertFalse(attempt.is_correct)

        # Check FSRS Spaced Card was created for this mistake
        spaced_card = PrepStudentSpacedCard.objects.filter(user=self.user, quiz_question=self.q1).first()
        self.assertIsNotNone(spaced_card)
        self.assertEqual(spaced_card.topic, self.topic)
        self.assertIn("Option A", spaced_card.answer_text)

    def test_get_or_create_topic_quiz_from_existing(self):
        questions = get_or_create_topic_quiz(self.topic, count=2, user=self.user)
        self.assertEqual(len(questions), 2)
        q_ids = {q.id for q in questions}
        self.assertEqual(q_ids, {self.q1.id, self.q2.id})

    def test_invalid_option_handling(self):
        result = evaluate_quiz_answer(
            quiz_question_id=self.q1.id,
            selected_option="Z",
            user=self.user,
        )
        self.assertFalse(result["success"])
        self.assertIn("Invalid option", result["error"])

    def test_quiz_get_api_withholds_answers_and_deducts_credits(self):
        self.client.force_login(self.user)
        resp = self.client.get(f"/prep/api/topic/{self.topic.id}/quiz/")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(data["success"])
        self.assertGreaterEqual(len(data["questions"]), 2)
        self.assertIn("credits_deducted", data)
        self.assertGreater(data["credits_deducted"], 0)
        self.assertIn("credits_balance", data)
        q = data["questions"][0]
        # Critical security check: answer & explanation MUST be withheld
        self.assertNotIn("correct_option", q)
        self.assertNotIn("explanation", q)
        self.assertIn("options", q)
        self.assertIn("A", q["options"])

    def test_quiz_get_api_requires_authentication(self):
        resp = self.client.get(f"/prep/api/topic/{self.topic.id}/quiz/")
        self.assertEqual(resp.status_code, 401)
        data = resp.json()
        self.assertFalse(data["success"])
        self.assertIn("Please sign in", data["error"])

    def test_quiz_get_api_insufficient_credits(self):
        # Create user with 0 credits
        poor_user = User.objects.create_user(
            username="broke_student",
            email="broke_student@example.com",
            password="secretpassword",
        )
        from prep.models import PrepWallet
        wallet = PrepWallet.get_or_create_wallet(poor_user)
        wallet.credits_balance = 0
        wallet.credit_grants.all().update(remaining_credits=0)
        wallet.save()

        self.client.force_login(poor_user)
        resp = self.client.get(f"/prep/api/topic/{self.topic.id}/quiz/")
        self.assertEqual(resp.status_code, 402)
        data = resp.json()
        self.assertFalse(data["success"])
        self.assertIn("Insufficient credits", data["error"])

    def test_quiz_submit_api(self):
        self.client.force_login(self.user)
        # Test correct submission
        resp = self.client.post(
            f"/prep/api/topic/{self.topic.id}/quiz/submit/",
            data=json.dumps({"question_id": self.q1.id, "selected_option": "A"}),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(data["is_correct"])
        self.assertEqual(data["correct_option"], "A")
        self.assertIn("MVC isolates", data["summary_explanation"])

        # Test incorrect submission with distractor explanation
        resp2 = self.client.post(
            f"/prep/api/topic/{self.topic.id}/quiz/submit/",
            data=json.dumps({"question_id": self.q1.id, "selected_option": "B"}),
            content_type="application/json",
        )
        self.assertEqual(resp2.status_code, 200)
        data2 = resp2.json()
        self.assertFalse(data2["is_correct"])
        self.assertIn("Monolithic pipeline", data2["why_selected_is_wrong"])

    def test_tutor_prompt_contains_quiz_me_protocol(self):
        from services.prep_topic_tutor import _build_prompt

        sys_prompt, user_prompt = _build_prompt(
            topic=self.topic,
            notes="Architectural patterns include MVC, Microservices, and Layered architecture.",
            course_material="",
            history=[],
            user_message="Quiz me on this topic",
            uploads=[],
        )
        # Verify instructions are in prompts
        self.assertIn("INTERACTIVE RETRIEVAL PRACTICE & QUIZ ME PROTOCOL", user_prompt)
        self.assertIn("Present exactly ONE conceptual or computational multiple-choice question", user_prompt)
        self.assertIn("DO NOT reveal the correct option or explanation yet", user_prompt)
        self.assertIn("pedagogical breakdown", user_prompt)
        self.assertIn("When the learner asks to be quizzed, present one 4-option multiple-choice question", sys_prompt)

    def test_topic_study_template_contains_quiz_quick_action(self):
        from django.test import RequestFactory
        from prep.views import prep_topic_study

        rf = RequestFactory()
        request = rf.get(f"/prep/topic/{self.topic.id}/")
        request.user = self.user
        resp = prep_topic_study(request, topic_id=self.topic.id)
        self.assertEqual(resp.status_code, 200)
        content = resp.content.decode("utf-8")
        self.assertIn("Quiz me", content)
        self.assertIn("Core concept", content)
        self.assertIn("Past exam question", content)
        self.assertIn("triggerTopicTutorPrompt", content)
        self.assertIn('id="pillar-quiz"', content)
        self.assertIn("Start Active Recall Drill", content)

    def test_active_recall_drill_deduplication(self):
        # Initial delivery serves 1 question and marks it seen
        questions = get_or_create_topic_quiz(self.topic, count=1, user=self.user)
        self.assertEqual(len(questions), 1)
        served_id = questions[0].id

        # Verify seen record was created in database
        seen_count = PrepStudentQuizSeen.objects.filter(user=self.user, topic=self.topic).count()
        self.assertEqual(seen_count, 1)

        # Second delivery must exclude served_id and return the remaining unseen question
        questions_second = get_or_create_topic_quiz(self.topic, count=1, user=self.user)
        self.assertEqual(len(questions_second), 1)
        self.assertNotEqual(questions_second[0].id, served_id)

    def test_practice_variant_persistence_and_privacy(self):
        # Create generated variant in DB
        variant = PrepQuestion.objects.create(
            topic=self.topic,
            question_type="generated",
            number=1,
            marks=5,
            topic_label="Architecture",
            question_latex="Design a modular microservices architecture.",
            solution_latex="Break into bounded contexts with asynchronous event buses.",
            verification_status="verified",
        )

        # 1. User has NOT unlocked variant -> generated_questions is empty (no free viewing!)
        self.client.force_login(self.user)
        resp1 = self.client.get(f"/prep/topic/{self.topic.id}/")
        self.assertEqual(resp1.status_code, 200)
        self.assertEqual(resp1.context["generated_questions"], [])
        self.assertIn("Ready to practice exam-standard variants?", resp1.content.decode("utf-8"))

        # 2. User unlocks the variant
        PrepStudentQuestionUnlock.objects.create(
            user=self.user,
            question=variant,
            topic=self.topic,
        )

        # 3. User revisits page -> unlocked variant persists and displays!
        resp2 = self.client.get(f"/prep/topic/{self.topic.id}/")
        self.assertEqual(resp2.status_code, 200)
        unlocked_qs = resp2.context["generated_questions"]
        self.assertEqual(len(unlocked_qs), 1)
        self.assertEqual(unlocked_qs[0]["id"], variant.id)
        self.assertIn("Design a modular microservices architecture", resp2.content.decode("utf-8"))

        # 4. A different user visits -> cannot see variant for free!
        other_user = User.objects.create_user(
            username="other_student",
            email="other_student@example.com",
            password="secretpassword",
        )
        self.client.force_login(other_user)
        resp3 = self.client.get(f"/prep/topic/{self.topic.id}/")
        self.assertEqual(resp3.status_code, 200)
        self.assertEqual(resp3.context["generated_questions"], [])
        self.assertNotIn("Design a modular microservices architecture", resp3.content.decode("utf-8"))


