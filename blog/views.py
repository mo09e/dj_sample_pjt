from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm
from .models import Post


class PostListView(generic.ListView):
    model = Post  # 一覧表示させたいモデルを呼び出し


class PostCreateView(generic.CreateView):
    model = Post  # 作成したいModelを指定する
    form_class = PostCreateForm  # 作成したformクラスを指定
    success_url = reverse_lazy('blog:post_list')  # 記事作成に成功した時のリダイレクト先を指定


class PostDetailView(generic.DetailView):
    model = Post  # pk(primary key)はurls.pyで指定しているのでここではmodelを呼び出すだけで済む


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostCreateForm  # PostCreateFormをほぼそのまま活用できる
    success_url = reverse_lazy('blog:post_list')


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
