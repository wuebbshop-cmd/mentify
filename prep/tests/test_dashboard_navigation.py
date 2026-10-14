from django.test import TestCase
from django.urls import reverse

from accounts.models import User


class DashboardNavigationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="dashboard-nav-user",
            email="dashboard-nav@example.test",
            password="SecurePass123!",
            first_name="Dashboard",
            last_name="User",
        )
        self.client.force_login(self.user)

    def test_main_dashboard_has_retractable_sidebar_and_no_top_page_links(self):
        response = self.client.get(reverse("accounts:learner_dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="main-sidebar-collapse-btn"')
        self.assertContains(response, "main_sidebar_collapsed")
        self.assertNotContains(response, 'class="navbar-nav"')
        self.assertNotContains(response, 'class="btn btn-ghost btn-sm">Dashboard</a>')

    def test_prep_dashboard_does_not_show_banked_questions_metric(self):
        response = self.client.get(reverse("prep:dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Banked Questions")
