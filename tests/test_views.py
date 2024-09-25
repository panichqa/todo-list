from django.test import TestCase
from django.urls import reverse
from tasks.models import Task, Tag


class TaskListViewTest(TestCase):

    def setUp(self):
        self.task1 = Task.objects.create(content="Test task 1", is_done=False)
        self.task2 = Task.objects.create(content="Test task 2", is_done=True)

    def test_task_list_view(self):
        response = self.client.get(reverse("tasks:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/index.html")
        self.assertContains(response, "Test task 1")
        self.assertContains(response, "Test task 2")


class TagCreateViewTest(TestCase):

    def test_tag_create_view(self):
        response = self.client.post(reverse("tasks:tag_create"), {
            "name": "New Tag"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.first().name, "New Tag")


class TagUpdateViewTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="Old Tag")

    def test_tag_update_view(self):
        response = self.client.post(reverse("tasks:tag_update", args=[self.tag.pk]), {
            "name": "Updated Tag"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.tag.name, "Updated Tag")


class TaskDeleteViewTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(content="Test task")

    def test_task_delete_view(self):
        response = self.client.post(reverse("tasks:task_delete", args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
