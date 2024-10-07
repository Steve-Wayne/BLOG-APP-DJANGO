from django.urls import path
from . import views
from .views import ( PostListView ,PostDetailView,PostCreateView,PostUpdateView , PostDeleteView ,UserPostListView )
from users import views as user_views

urlpatterns = [
    path('search/', user_views.search_by_author, name='search-by-author'),
    path('', views.PostListView.as_view() ,name='blog-home'),
    path('users/<str:username>', views.UserPostListView.as_view() ,name='user-posts'),
    path('post/<int:pk>', views.PostDetailView.as_view() ,name='post-detail'),
    path('post/new/', views.PostCreateView.as_view() ,name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view() ,name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view() ,name='post-delete'),
    path('about/' , views.about  ,name='blog-about'),
    path('contacts/' , user_views.ContactUs, name='blog-contact'),
    
]


# <app>/<model>_<viewtype>,html
#blog/post_list.html
