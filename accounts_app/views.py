from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django import forms
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from projects_app.models import Project, WorkExperience, Skill, HomeContent
from contact_app.models import ContactMessage


class LoginView(View):
    template_name = 'admin/admin_login.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.is_superuser:
            return redirect('accounts:admin_dashboard')
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('accounts:admin_dashboard')
            else:
                messages.error(request, 'Invalid credentials or not an admin user.')
        else:
            messages.error(request, 'Invalid username or password.')
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You have been logged out successfully.')
        return redirect('home')


class AdminRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:admin_login')
        if not request.user.is_superuser:
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class AdminUnifiedDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'admin/admin_unified_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['total_projects'] = Project.objects.count()
        context['featured_projects'] = Project.objects.filter(featured=True).count()
        context['total_experiences'] = WorkExperience.objects.count()
        context['visible_experiences'] = WorkExperience.objects.filter(is_visible=True).count()
        context['total_skills'] = Skill.objects.count()
        context['visible_skills'] = Skill.objects.filter(is_visible=True).count()
        context['total_messages'] = ContactMessage.objects.count()
        context['unread_messages'] = ContactMessage.objects.filter(is_read=False).count()
        
        context['projects'] = Project.objects.all().order_by('order', '-created_at')
        context['experiences'] = WorkExperience.objects.all().order_by('-is_current', '-start_date', 'order')
        context['skills'] = Skill.objects.all().order_by('category', 'order', 'name')
        context['messages'] = ContactMessage.objects.all()[:20]
        
        return context


class AdminLogoutView(AdminRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You have been logged out successfully.')
        return redirect('accounts:admin_login')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'description', 'detailed_description', 'image', 
                  'github_link', 'live_link', 'technologies', 'category', 
                  'featured', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'detailed_description': forms.Textarea(attrs={'rows': 5}),
            'technologies': forms.TextInput(attrs={'placeholder': 'Python, Django, React'}),
        }

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug:
            from django.utils.text import slugify
            slug = slugify(self.cleaned_data.get('title', ''))
        
        qs = Project.objects.filter(slug=slug)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        
        if qs.exists():
            from django.core.exceptions import ValidationError
            raise ValidationError('This slug is already in use.')
        return slug


class ProjectListView(AdminRequiredMixin, ListView):
    model = Project
    template_name = 'admin/projects.html'
    context_object_name = 'projects'
    ordering = ['order', '-created_at']


class ProjectCreateView(AdminRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'admin/project_form.html'
    success_url = reverse_lazy('accounts:admin_projects')

    def form_valid(self, form):
        messages.success(self.request, 'Project created successfully!')
        return super().form_valid(form)


class ProjectUpdateView(AdminRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'admin/project_form.html'

    def get_success_url(self):
        return reverse('accounts:admin_projects')

    def form_valid(self, form):
        messages.success(self.request, 'Project updated successfully!')
        return super().form_valid(form)


class ProjectDeleteView(AdminRequiredMixin, DeleteView):
    model = Project
    template_name = 'admin/project_confirm_delete.html'
    success_url = reverse_lazy('accounts:admin_projects')

    def form_valid(self, form):
        messages.success(self.request, 'Project deleted successfully!')
        return super().form_valid(form)


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company', 'position', 'location', 'description', 'start_date',
                  'end_date', 'is_current', 'company_logo', 'technologies',
                  'order', 'is_visible']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'technologies': forms.TextInput(attrs={'placeholder': 'Python, Django, SQL'}),
        }


class ExperienceListView(AdminRequiredMixin, ListView):
    model = WorkExperience
    template_name = 'admin/experience.html'
    context_object_name = 'experiences'
    ordering = ['-is_current', '-start_date', 'order']


class ExperienceCreateView(AdminRequiredMixin, CreateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'admin/experience_form.html'
    success_url = reverse_lazy('accounts:admin_experience')

    def form_valid(self, form):
        messages.success(self.request, 'Work experience created successfully!')
        return super().form_valid(form)


class ExperienceUpdateView(AdminRequiredMixin, UpdateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'admin/experience_form.html'

    def get_success_url(self):
        return reverse('accounts:admin_experience')

    def form_valid(self, form):
        messages.success(self.request, 'Work experience updated successfully!')
        return super().form_valid(form)


class ExperienceDeleteView(AdminRequiredMixin, DeleteView):
    model = WorkExperience
    template_name = 'admin/experience_confirm_delete.html'
    success_url = reverse_lazy('accounts:admin_experience')

    def form_valid(self, form):
        messages.success(self.request, 'Work experience deleted successfully!')
        return super().form_valid(form)


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'category', 'proficiency_level', 'icon', 'is_visible', 'order']
        widgets = {
            'proficiency_level': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            'icon': forms.TextInput(attrs={'placeholder': 'fab fa-python'}),
        }


class SkillListView(AdminRequiredMixin, ListView):
    model = Skill
    template_name = 'admin/skills.html'
    context_object_name = 'skills'
    ordering = ['category', 'order', 'name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        skills_by_category = {}
        for skill in context['skills']:
            if skill.category not in skills_by_category:
                skills_by_category[skill.category] = []
            skills_by_category[skill.category].append(skill)
        context['skills_by_category'] = skills_by_category
        return context


class SkillCreateView(AdminRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'admin/skill_form.html'
    success_url = reverse_lazy('accounts:admin_skills')

    def form_valid(self, form):
        messages.success(self.request, 'Skill created successfully!')
        return super().form_valid(form)


class SkillUpdateView(AdminRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'admin/skill_form.html'

    def get_success_url(self):
        return reverse('accounts:admin_skills')

    def form_valid(self, form):
        messages.success(self.request, 'Skill updated successfully!')
        return super().form_valid(form)


class SkillDeleteView(AdminRequiredMixin, DeleteView):
    model = Skill
    template_name = 'admin/skill_confirm_delete.html'
    success_url = reverse_lazy('accounts:admin_skills')

    def form_valid(self, form):
        messages.success(self.request, 'Skill deleted successfully!')
        return super().form_valid(form)


class HomeContentForm(forms.ModelForm):
    class Meta:
        model = HomeContent
        fields = ['profile_picture', 'profile_picture_url', 'name', 'title', 'education', 
                  'email', 'phone', 'github_url', 'linkedin_url', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'HARSHIT RAJ'}),
            'title': forms.TextInput(attrs={'placeholder': 'Full Stack Developer | Cybersecurity Enthusiast'}),
            'education': forms.TextInput(attrs={'placeholder': 'B.Tech CSE @ LPU'}),
            'email': forms.EmailInput(attrs={'placeholder': 'harshitpriv.3@gmail.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+91 7654958933'}),
            'github_url': forms.URLInput(attrs={'placeholder': 'https://github.com/username'}),
            'linkedin_url': forms.URLInput(attrs={'placeholder': 'https://linkedin.com/in/username'}),
        }


class HomeContentEditView(AdminRequiredMixin, UpdateView):
    model = HomeContent
    form_class = HomeContentForm
    template_name = 'admin/homecontent_form.html'
    
    def get_object(self, queryset=None):
        # Get the active home content or create a new one if none exists
        home_content = HomeContent.objects.filter(is_active=True).first()
        if not home_content:
            home_content = HomeContent.objects.create(
                is_active=True,
                name="HARSHIT RAJ",
                title="Full Stack Developer | Cybersecurity Enthusiast",
                education="B.Tech CSE @ LPU"
            )
        return home_content

    def get_success_url(self):
        return reverse('accounts:admin_dashboard')

    def form_valid(self, form):
        messages.success(self.request, 'Home content updated successfully!')
        return super().form_valid(form)


@method_decorator(require_POST, name='dispatch')
class MarkMessageAsReadView(AdminRequiredMixin, View):
    """View to mark a message as read."""
    
    def post(self, request, pk):
        message = get_object_or_404(ContactMessage, pk=pk)
        message.is_read = True
        message.save()
        messages.success(request, f'Message from {message.name} marked as read.')
        return redirect('accounts:admin_dashboard')


@method_decorator(require_POST, name='dispatch')
class MarkMessageAsUnreadView(AdminRequiredMixin, View):
    """View to mark a message as unread."""
    
    def post(self, request, pk):
        message = get_object_or_404(ContactMessage, pk=pk)
        message.is_read = False
        message.save()
        messages.success(request, f'Message from {message.name} marked as unread.')
        return redirect('accounts:admin_dashboard')
