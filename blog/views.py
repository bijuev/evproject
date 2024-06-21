from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
import django_filters
from .models import Blog
from .forms import BlogForm


class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ['title', 'body', 'is_published', 'is_active']


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    paginate_by = 1

    def get_queryset(self):
        if 'q' in self.request.GET:
            q = self.request.GET['q']
            return Blog.objects.filter(title__icontains=q)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cls_1'] = 'active'
        return context


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cls_1'] = 'active'
        return context


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cls_1'] = 'active'
        return context

    def get_success_url(self):
        return reverse('blog:blog_list')