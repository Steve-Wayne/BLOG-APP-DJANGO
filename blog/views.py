from typing import Any
from django.urls import reverse
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ( ListView,DetailView ,CreateView,UpdateView,DeleteView )
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

#there are four types of views listview , detailview, CreateView , UpdateView

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request , 'blog/home.html' , context)


class PostListView(ListView):
    model=Post
    template_name='blog/home.html'  # <app>/<model>_<viewtype>,html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=6


class PostDetailView(DetailView):
    model=Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # Fields displayed in the form

    # Redirect after successful form submission
     # Change 'post-list' to your posts listing URL name

    # Override form_valid to automatically set the author to the logged-in user
    def form_valid(self, form):
        form.instance.authors = self.request.user
        return super().form_valid(form)





class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title' , 'content']
    def form_valid(self, form):
        form.instance.authors =self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.authors:
            return True
        return False




class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin ,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.authors:
            return True
        return False


class UserPostListView(ListView):
    model=Post
    template_name='blog/user_post.html'  # <app>/<model>_<viewtype>,html
    context_object_name='posts'
    
    paginate_by=6

    def get_queryset(self):
        user=get_object_or_404(User , username=self.kwargs.get('username'))
        return Post.objects.filter(authors=user).order_by('-date_posted')



def about(request):
    return render(request , 'blog/about.html' ,{'title':'ABOUT'})

def contact(request):
    return render(request , 'blog/contacts.html'  , {'title': 'Contact US'})


