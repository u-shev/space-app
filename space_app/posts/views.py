from django.urls import reverse_lazy
from django.views.generic import CreateView, \
    UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from space_app.mixins import UserLoginRequiredMixin
from .models import Post
from .forms import PostForm
from django.http import Http404
from django.shortcuts import render


'''Post view wich counts views'''


def view_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    post.view_count += 1
    post.save()
    return render(request, 'posts/post.html', context={'post': post})


class PostCreateView(UserLoginRequiredMixin,
                     SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    success_message = 'Post successfully created'
    extra_context = {
        'title': 'Create Post',
        'button_text': 'Create',
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserLoginRequiredMixin,
                     SuccessMessageMixin, UpdateView):

    template_name = 'form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    success_message = 'Post updated'
    extra_context = {
        'title': 'Update Post',
        'button_text': 'Update',
    }


class PostDeleteView(UserLoginRequiredMixin,
                     SuccessMessageMixin, DeleteView):

    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('home')
    success_message = 'Post deleted'
    protected_url = reverse_lazy('home')
    extra_context = {
        'title': 'Delete Post',
        'button_text': 'Yes, delete',
    }
