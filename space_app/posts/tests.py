from django.test import TestCase
from .models import User
from .models import Post
from django.urls import reverse_lazy
# import json

# with open('space_app/fixtures/nasa.json') as file:
#     nasa_data = json.loads(file.read())


class TestPostCreate(TestCase):

    fixtures = ['users.json', 'posts.json']

    def test_create_logout(self):
        response = self.client.get(reverse_lazy('create_post'))
        self.assertEqual(response.status_code, 302)

    def test_create_post(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse_lazy('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.all().count(), 2)
        post = Post.objects.create(name='post',
                                   description="The moon is wonderful!",
                                   picture="test.jpg",
                                   author=user,)
        post = Post.objects.get(pk=3)
        self.assertEqual(Post.objects.all().count(), 3)
        self.assertEqual(post.__str__(), post.name)
        self.assertEqual(post.picture.field.upload_to, 'upload/pictures/')


class TestUpdatePost(TestCase):

    fixtures = ['users.json', 'posts.json']

    def test_update_logout(self):
        response = self.client.get(reverse_lazy('update_post', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_post_update(self):
        user1 = User.objects.get(pk=1)
        self.client.force_login(user=user1)
        response = self.client.get(reverse_lazy('update_post', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        new_post = {
            'name': 'post',
        }
        response = self.client.post(
            reverse_lazy('update_post', kwargs={'pk': 1}), new_post)
        status = Post.objects.get(pk=1)
        self.assertEqual(status.name, 'post')


class TestDeletePost(TestCase):

    fixtures = ['users.json', 'posts.json']

    def test_delete_logout(self):
        response = self.client.get(reverse_lazy('delete_post', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_post(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse_lazy('delete_post', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse_lazy('delete_post', kwargs={'pk': 1})
        )
        self.assertEqual(Post.objects.all().count(), 1)


# class TestPostsList(TestCase):

#     nasa_json = nasa_data

#     def test_list(self):
#         response = self.client.get(reverse_lazy('home'))
#         self.assertEqual(response.status_code, 200)


class TestViewPost(TestCase):

    fixtures = ['users.json', 'posts.json']

    def test_post_doesnt_exist(self):
        response = self.client.get(reverse_lazy('post',
                                                kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 404)

    def test_post_exists(self):
        response = self.client.get(reverse_lazy('post', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
