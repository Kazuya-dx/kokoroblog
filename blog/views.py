from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import Blog, Tag
from django.db.models import Q

class IndexView(ListView):
    model = Blog
    template_name = 'base.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        context['tags'] = Tag.objects.all()
        context['word'] = ''
        word = self.request.GET.get('word')
        if word is not None:
            context['word'] = self.request.GET.get('word')

        return context

    def get_queryset(self):
        results = self.model.objects.all()
        word = self.request.GET.get('word')
        if word is not None:
            results = results.filter(title__icontains=word)
        return results.order_by('-created_datetime')

index = IndexView.as_view()

class TagView(ListView):
    model = Blog
    template_name = 'blog/tag_blog.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        context['tags'] = Tag.objects.all()
        context['selected_tag'] = Tag.objects.get(name=self.kwargs['pk'])
        context['word'] = ''
        word = self.request.GET.get('word')
        if word is not None:
            context['word'] = self.request.GET.get('word')

        return context

    def get_queryset(self):
        results = self.model.objects.all()
        results = results.filter(tag__name=self.kwargs['pk'])
        word = self.request.GET.get('word')
        if word is not None:
            results = results.filter(title__icontains=word)

        return results.order_by('-created_datetime')

tag_blog = TagView.as_view()


class AboutView(TemplateView):
    template_name = 'blog/about.html'

about = AboutView.as_view()


class ProfileView(TemplateView):
    template_name = 'blog/profile.html'

profile = ProfileView.as_view()


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        context['tags'] = Tag.objects.all()
        context['blog'] = Blog.objects.get(id=self.kwargs['pk'])

        return context

    def get_queryset(self, **kwargs):
        return self.model.objects.all()

detail = BlogDetailView.as_view()

class TestView(TemplateView):
    template_name = 'blog/test.html'

test = TestView.as_view()
