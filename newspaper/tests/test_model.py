from django.test import TestCase

from newspaper.models import Topic, Newspaper, Redactor


class TestModels(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(
            name="test_name",
        )
        self.assertEqual(
            str(topic),
            f"{topic.name}"
        )

    def test_redactor_str(self):
        redactor = Redactor.objects.create_user(
            username="name",
            first_name="first",
            last_name="last"
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.first_name} {redactor.last_name}"
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(
            name="test_name",
        )
        newspaper = Newspaper.objects.create(
            topic=topic
        )
        self.assertEqual(str(newspaper), newspaper.topic.name)
