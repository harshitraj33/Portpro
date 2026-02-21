from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Profile, HomeContent


class HomeView(TemplateView):
    template_name = 'projects_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(featured=True)[:6]
        context['all_projects'] = Project.objects.filter(featured=False)[:3]
        context['home_content'] = HomeContent.objects.filter(is_active=True).first()
        return context


class AboutView(TemplateView):
    template_name = 'projects_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['projects'] = Project.objects.all().order_by('-created_at')
        return context


class ProjectListView(ListView):
    model = Project
    template_name = 'projects_app/projects.html'
    context_object_name = 'projects'
    paginate_by = 12

    def get_queryset(self):
        queryset = Project.objects.all()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Project.objects.values_list('category', flat=True).distinct()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects_app/project_detail.html'
    context_object_name = 'project'

    def get_object(self):
        return get_object_or_404(Project, slug=self.kwargs['slug'])


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'projects_app/dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
