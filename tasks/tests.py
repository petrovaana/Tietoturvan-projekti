from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Task


User = get_user_model()


class TaskViewsTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username="alice", password="test-pass-123")
        self.bob = User.objects.create_user(username="bob", password="test-pass-123")

    def test_create_task_from_post(self):
        self.client.force_login(self.alice)
        response = self.client.post(reverse("tasks:create"), {"name": "Write tests"})

        self.assertRedirects(
            response,
            reverse("tasks:user_list", args=(self.alice.pk,)),
        )
        self.assertTrue(
            Task.objects.filter(
                name="Write tests",
                completed=False,
                owner=self.alice,
            ).exists()
        )

    def test_task_list_only_shows_incomplete_tasks(self):
        Task.objects.create(name="Still to do", owner=self.alice)
        Task.objects.create(name="Already done", completed=True, owner=self.alice)
        self.client.force_login(self.alice)

        response = self.client.get(reverse("tasks:user_list", args=(self.alice.pk,)))

        self.assertContains(response, "Still to do")
        self.assertNotContains(response, "Already done")

    def test_create_task_rejects_empty_name(self):
        self.client.force_login(self.alice)
        response = self.client.post(reverse("tasks:create"), {"name": "   "})

        self.assertEqual(response.status_code, 400)
        self.assertFalse(Task.objects.exists())

    def test_user_id_in_url_exposes_another_users_tasks(self):
        Task.objects.create(name="Alice private task", owner=self.alice)
        self.client.force_login(self.bob)

        response = self.client.get(reverse("tasks:user_list", args=(self.alice.pk,)))

        self.assertContains(response, "Alice private task")
        self.assertContains(response, "alice's To Do list")

    def test_users_cannot_delete_another_users_tasks(self):
        task = Task.objects.create(name="Alice private task", owner=self.alice)
        self.client.force_login(self.bob)

        response = self.client.post(reverse("tasks:delete", args=(task.pk,)))

        self.assertEqual(response.status_code, 404)
        self.assertTrue(Task.objects.filter(pk=task.pk).exists())
