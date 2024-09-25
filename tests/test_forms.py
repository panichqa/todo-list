from django.test import TestCase
from django.utils import timezone
from tasks.forms import TagForm

class TagFormTest(TestCase):

    def test_valid_tag_form(self):
        form = TagForm(data={"name": "Important"})
        self.assertTrue(form.is_valid())

    def test_invalid_tag_form(self):
        form = TagForm(data={"name": ""})
        self.assertFalse(form.is_valid())
