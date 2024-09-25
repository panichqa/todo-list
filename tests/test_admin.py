from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from tasks.models import Task, Tag
from tasks.admin import TaskAdmin, TagAdmin

class AdminTest(TestCase):

    def setUp(self):
        self.site = AdminSite()

    def test_task_admin_registered(self):
        task_admin = TaskAdmin(Task, self.site)
        self.assertIn('content', task_admin.list_display)
        self.assertIn('is_done', task_admin.list_filter)

    def test_tag_admin_registered(self):
        tag_admin = TagAdmin(Tag, self.site)
        self.assertIn('name', tag_admin.list_display)
