from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class createview(LoginRequiredMixin, CreateView):
    model = article
    template_name = 'article_create.html'
    fields = ('title', 'body')
    login_url = 'login'  # new
    # will assign login user to author field

    def form_valid(self, form):  # new
        form.instance.author = self.request.user
        return super().form_valid(form)


class articleview(ListView):
    model = article
    template_name = 'article_list.html'


class detailview(LoginRequiredMixin, DetailView):
    model = article
    template_name = "article_detail.html"
    login_url = 'login'  # new


class updateview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = article
    template_name = "article_update.html"
    fields = ('title', 'body')
    login_url = 'login'  # new

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class deleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = article
    template_name = "article_delete.html"
    success_url = reverse_lazy('articleview')
    login_url = 'login'  # new

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user
