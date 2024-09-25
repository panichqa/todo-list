from django.test import TestCase
from tasks.models import Task, Tag

class TaskModelTest(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(content="Test task", is_done=False)
        self.assertEqual(task.content, "Test task")
        self.assertFalse(task.is_done)

    def test_task_default_is_done(self):
        task = Task.objects.create(content="Test task")
        self.assertFalse(task.is_done)

class TagModelTest(TestCase):

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Urgent")
        self.assertEqual(tag.name, "Urgent")
