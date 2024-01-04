from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from space_app.celery import app
from posts.models import Post


REPORT_TEMPLATE = """
Your've made a good job!:

{% for post in posts %}
Post "{{ post.name }}": viewed {{ post.view_count }} times |

{% endfor %}
"""

'''Creating letters for sending every author showing how many views their posts have'''


@app.task
def send_view_count_report():
    for user in get_user_model().objects.all():
        posts = Post.objects.filter(author=user)
        if not posts:
            continue
        template = Template(REPORT_TEMPLATE)
        send_mail(
            'Your Space app Activity',
            template.render(context=Context({'posts': posts})),
            'moypyaschik@mail.ru',
            [user.email],
            fail_silently=False,
        )
