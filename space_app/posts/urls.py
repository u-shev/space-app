from django.urls import path
from posts import views
from .views import PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('<int:pk>/', views.view_post, name='post'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]
