from django.contrib import admin
from space_app.users.models import User
from space_app.posts.models import Post


admin.site.register(User)
admin.site.register(Post)
