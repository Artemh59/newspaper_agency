from django.test import TestCase

from django.urls import reverse
from django.contrib.auth import get_user_model
from newspaper.models import Topic


class PublicManufacturerLoginTest(TestCase):
    def test_login(self):
        get_result = self.client.get(reverse("newspaper:topic"))
        self.assertEqual(get_result.status_code, 200)


class PrivateTopicTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="qwerfghnm"
        )
        self.client.force_login(self.user)

    def test_login(self):
        get_result = self.client.get(reverse("newspaper:topic"))
        self.assertEqual(get_result.status_code, 200)

    def test_context_view(self):
        Topic.objects.create(name="test_1")
        Topic.objects.create(name="test_2")
        get_result = self.client.get(reverse("newspaper:topic"))
        topics = Topic.objects.all()
        self.assertEqual(
            list(get_result.context["topic_list"]),
            list(topics)
        )
