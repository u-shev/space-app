from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
import asyncio
from django.shortcuts import render
from .helpers import get_posts_list, get_data_from_api
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
from django.core.paginator import Paginator


'''Index view takes picture of the day and posts (4 posts each page)
list from async helpers,also make async chek if user is authenticated
to show diffrent links in navbar'''


@async_to_sync
async def index_view(request):
    posts, context = await asyncio.gather(get_posts_list(), get_data_from_api())
    paginator = Paginator(posts, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "index.html", {
                "posts": posts,
                'info': context[0],
                'picture': context[1],
                'video': context[2],
                "user.is_authenticated": await sync_to_async(
                    lambda: request.user.is_authenticated)(),
                "page_obj": page_obj
                },
            )


'''Standart LoginView with added succes message'''


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('home')
    success_message = 'You are logged in'
    extra_context = {
        'title': 'Login',
        'button_text': 'Enter',
    }


'''Standart LogoutView with added succes message'''


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('home')
    success_message = 'You are logged out'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You are logged out')
        return super().dispatch(request, *args, **kwargs)
