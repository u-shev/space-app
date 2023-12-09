from django.urls import reverse_lazy
from .forms import UserForm
from .models import User
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin


class UserCreateView(SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = 'User is successfully registered'
    extra_context = {
        'title': 'Create user',
        'button_text': 'Register',
    }
