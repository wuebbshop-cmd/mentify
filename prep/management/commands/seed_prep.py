from django.core.management.base import BaseCommand
from prep.models import PrepCourse, PrepTopic, PrepPaper, PrepQuestion


class Command(BaseCommand):
    help = "Seed initial canonical course units, syllabus topics, and past papers into Mentify Prep."

    def handle(self, *args, **options):
        self.stdout.write("Seeding Mentify Prep canonical courses and past papers...")

        courses_data = [
            {
                "code": "SMA 300",
                "title": "Real Analysis I",
                "slug": "sma-300",
                "category": "Mathematics",
                "level": "Undergraduate",
                "description": "Rigorous treatment of metric spaces, topology of Euclidean spaces, sequences, completeness, compactness, and continuous functions.",
                "topics": [
                    {
                        "order": 1,
                        "title": "Set Theory & Real Number System",
                        "summary": "Completeness axiom, Supremum and Infimum properties, Archimedean property of the real numbers.",
                        "subtopics": ["Supremum & Infimum", "Completeness Axiom", "Archimedean Property", "Dedekind Cuts"],
                    },
                    {
                        "order": 2,
                        "title": "Metric Spaces & Topology",
                        "summary": "Metric definitions, open and closed sets, interior points, boundary, limit points, and closure in metric spaces.",
                        "subtopics": ["Open & Closed Sets", "Interior, Closure & Boundary", "Cauchy Sequences", "Completeness of Metric Spaces"],
                    },
                    {
                        "order": 3,
                        "title": "Compactness & Connectedness",
                        "summary": "Heine-Borel theorem, Bolzano-Weierstrass theorem, sequential compactness, and connected sets in metric spaces.",
                        "subtopics": ["Heine-Borel Theorem", "Bolzano-Weierstrass", "Sequential Compactness", "Connected Sets"],
                    },
                    {
                        "order": 4,
                        "title": "Continuity & Uniform Continuity",
                        "summary": "Epsilon-delta definitions, characterization by open sets, Intermediate Value Theorem, and uniform continuity.",
                        "subtopics": ["Epsilon-Delta Definition", "Continuity via Open Sets", "Intermediate Value Theorem", "Uniform Continuity Proofs"],
                    },
                ],
                "papers": [
                    {
                        "id": "sma300-cat1-2025",
                        "title": "Continuous Assessment Test 1 (CAT 1)",
                        "year": "2025 Semester 1",
                        "total_marks": 30,
                        "questions": [
                            {
                                "number": 1,
                                "marks": 10,
                                "topic_label": "Metric Spaces",
                                "question_latex": r"Let $(X, d)$ be a metric space. Prove that every open ball $B_r(x) = \{y \in X : d(x, y) < r\}$ is an open set in $(X, d)$.",
                                "solution_latex": r"\textbf{Proof:}\newline Let $y \in B_r(x)$. Then $d(x, y) < r$. Let $\epsilon = r - d(x, y) > 0$.\newline We claim $B_\epsilon(y) \subseteq B_r(x)$. Let $z \in B_\epsilon(y)$, so $d(y, z) < \epsilon$.\newline By the triangle inequality: $d(x, z) \leq d(x, y) + d(y, z) < d(x, y) + (r - d(x, y)) = r$.\newline Thus $z \in B_r(x)$, proving $B_\epsilon(y) \subseteq B_r(x)$, hence $B_r(x)$ is open.",
                            },
                            {
                                "number": 2,
                                "marks": 10,
                                "topic_label": "Discrete Topology",
                                "question_latex": r"Show that the discrete metric $d(x, y) = 1$ if $x \neq y$ and $0$ if $x = y$ induces the discrete topology on any non-empty set $X$.",
                                "solution_latex": r"\textbf{Proof:}\newline For any point $x \in X$, consider the open ball $B_{1/2}(x) = \{y \in X : d(x, y) < 1/2\} = \{x\}$.\newline Since each singleton $\{x\}$ is an open ball, every singleton subset of $X$ is open.\newline Any arbitrary subset $U \subseteq X$ can be written as the union of singletons: $U = \bigcup_{x \in U} \{x\}$.\newline Since any union of open sets is open, every subset of $X$ is open. This is precisely the discrete topology.",
                            },
                            {
                                "number": 3,
                                "marks": 10,
                                "topic_label": "Sequential Compactness",
                                "question_latex": r"State the Bolzano-Weierstrass theorem for $\mathbb{R}^n$ and prove that every bounded sequence in $\mathbb{R}^n$ contains a convergent subsequence.",
                                "solution_latex": r"\textbf{Theorem (Bolzano-Weierstrass):}\newline Every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence.\newline\textbf{Proof Outline:}\newline A bounded sequence in $\mathbb{R}^n$ is contained in a compact hypercube $[a_1, b_1] \times \dots \times [a_n, b_n]$. By successive bisection of the intervals and nested intervals property, one extracts coordinate-wise convergent subsequences, giving convergence in $\mathbb{R}^n$ under the Euclidean metric.",
                            },
                        ],
                    },
                    {
                        "id": "sma300-cat2-2024",
                        "title": "Continuous Assessment Test 2 (CAT 2)",
                        "year": "2024 Semester 1",
                        "total_marks": 30,
                        "questions": [],
                    },
                    {
                        "id": "sma300-exam-2024",
                        "title": "Main University Examination Paper",
                        "year": "2023/2024 Academic Year",
                        "total_marks": 70,
                        "questions": [],
                    },
                ],
            },
            {
                "code": "SST 304",
                "title": "Multivariate Methods I",
                "slug": "sst-304",
                "category": "Statistics",
                "level": "Undergraduate",
                "description": "Multivariate normal distribution, estimation of mean vectors and covariance matrices, Hotelling's T-squared, and Principal Component Analysis.",
                "topics": [
                    {
                        "order": 1,
                        "title": "Multivariate Normal Distribution",
                        "summary": "Density function, properties of mean vectors, variance-covariance matrices, and linear combinations.",
                        "subtopics": ["Random Vectors", "Mean & Covariance Matrix", "Characteristic Functions", "Independence of Sub-vectors"],
                    },
                    {
                        "order": 2,
                        "title": "Sample Geometry & Random Sampling",
                        "summary": "Sample mean vector, Wishart distribution, and generalized variance.",
                        "subtopics": ["Wishart Distribution", "Generalized Sample Variance", "Geometric Interpretation of Sample Data"],
                    },
                ],
                "papers": [
                    {
                        "id": "sst304-cat1-2025",
                        "title": "Continuous Assessment Test 1 (CAT 1)",
                        "year": "2025 Semester 1",
                        "total_marks": 30,
                        "questions": [],
                    },
                    {
                        "id": "sst304-exam-2024",
                        "title": "Final Examination Paper",
                        "year": "2024",
                        "total_marks": 70,
                        "questions": [],
                    },
                ],
            },
            {
                "code": "CS 201",
                "title": "Data Structures & Algorithms",
                "slug": "cs-201",
                "category": "Computing",
                "level": "Undergraduate",
                "description": "Asymptotic analysis, advanced trees, graphs, heaps, dynamic programming, and greedy algorithms.",
                "topics": [
                    {
                        "order": 1,
                        "title": "Asymptotic Analysis & Recurrences",
                        "summary": "Big-O, Omega, Theta notations, Master Theorem, and substitution methods.",
                        "subtopics": ["Big-O and Theta bounds", "Master Theorem", "Recursion Trees"],
                    },
                ],
                "papers": [
                    {
                        "id": "cs201-cat1-2025",
                        "title": "Midterm CAT Assessment",
                        "year": "2025",
                        "total_marks": 30,
                        "questions": [],
                    },
                ],
            },
        ]

        for c_data in courses_data:
            course, _ = PrepCourse.objects.get_or_create(
                code=c_data["code"],
                defaults={
                    "title": c_data["title"],
                    "slug": c_data["slug"],
                    "category": c_data["category"],
                    "level": c_data["level"],
                    "description": c_data["description"],
                },
            )

            # Topics
            for t_data in c_data.get("topics", []):
                PrepTopic.objects.get_or_create(
                    course=course,
                    order=t_data["order"],
                    defaults={
                        "title": t_data["title"],
                        "summary": t_data["summary"],
                        "subtopics": t_data["subtopics"],
                    },
                )

            # Papers
            for p_data in c_data.get("papers", []):
                paper, _ = PrepPaper.objects.get_or_create(
                    id=p_data["id"],
                    defaults={
                        "course": course,
                        "title": p_data["title"],
                        "year": p_data["year"],
                        "total_marks": p_data["total_marks"],
                        "is_published": True,
                    },
                )

                # Questions
                from services.prep_ai_router import normalize_math_delimiters
                for q_data in p_data.get("questions", []):
                    PrepQuestion.objects.get_or_create(
                        paper=paper,
                        number=q_data["number"],
                        defaults={
                            "marks": q_data["marks"],
                            "topic_label": q_data["topic_label"],
                            "question_latex": normalize_math_delimiters(q_data["question_latex"]),
                            "solution_latex": normalize_math_delimiters(q_data.get("solution_latex", "")),
                            "verification_status": "verified",
                        },
                    )

        self.stdout.write(self.style.SUCCESS("Successfully seeded Mentify Prep database!"))
