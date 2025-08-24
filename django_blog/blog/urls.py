from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# Comment-related views will be added later once implemented
# from .views import CommentUpdateView, CommentDeleteView

urlpatterns = [
    # Authentication routes
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Blog post CRUD routes
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment routes (to be re-enabled once views are defined)
    # path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    # path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]