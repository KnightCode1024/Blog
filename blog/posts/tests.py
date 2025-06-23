from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from django.contrib.auth import get_user_model

from posts.models import Post


class GetPagesTestCase(TestCase):
    fixtures = [
        "users/fixtures/users_user.json",
        "posts/fixtures/posts_posts.json",
        "posts/fixtures/posts_category.json",
        "posts/fixtures/posts_tagpost.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123",
            email="test@example.com",
        )

    def test_indexpage(self):
        path = reverse("index")
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # self.assertTemplateUsed(response, "index.html")

    def test_redirect_add_post(self):
        path = reverse("posts:add_post")
        redirect_uri = reverse("users:login") + "?next=" + path
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_uri)

    def test_data_indexpage(self):
        p = (
            Post.published.all()
            .order_by("-time_create")
            .select_related("cat")
            .prefetch_related("tags")
        )
        path = reverse("index")
        response = self.client.get(path)
        self.assertQuerySetEqual(response.context_data["posts"], p[:12])

    def test_paginate_mainpage(self):
        path = reverse("index")
        page = 1
        paginate_by = 12
        response = self.client.get(path + f"?page={page}")
        p = Post.published.all().select_related("cat")
        self.assertQuerySetEqual(
            response.context_data["posts"],
            p[(page - 1) * paginate_by: page * paginate_by],
        )

    def test_content_post(self):
        p = Post.published.get(pk=2)
        path = reverse("posts:post", args=[p.slug])
        response = self.client.get(path)
        self.assertEqual(p.content, response.context_data["post"].content)
