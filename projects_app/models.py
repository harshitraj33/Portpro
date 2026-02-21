from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    """
    Profile model for storing user profile information.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    skills = models.TextField(blank=True, null=True, help_text="Comma-separated skills")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_skills_list(self):
        if self.skills:
            return [skill.strip() for skill in self.skills.split(',')]
        return []


class Project(models.Model):
    """
    Project model for portfolio projects with slug for SEO-friendly URLs.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    detailed_description = models.TextField(blank=True, null=True, help_text="Full project description")
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated technologies used")
    category = models.CharField(max_length=100, blank=True, null=True)
    featured = models.BooleanField(default=False, help_text="Show in featured projects")
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def get_technologies_list(self):
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []


class WorkExperience(models.Model):
    """
    Work Experience model for storing professional experience.
    """
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    technologies = models.CharField(max_length=500, blank=True, null=True, help_text="Comma-separated technologies")
    order = models.IntegerField(default=0, help_text="Display order")
    is_visible = models.BooleanField(default=True, help_text="Show in portfolio")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_current', '-start_date', 'order']
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experiences'

    def __str__(self):
        return f"{self.position} at {self.company}"

    def get_technologies_list(self):
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []


class Skill(models.Model):
    """
    Skill model for storing technical and soft skills.
    """
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks'),
        ('database', 'Databases'),
        ('tool', 'Tools & Platforms'),
        ('soft', 'Soft Skills'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='programming')
    proficiency_level = models.IntegerField(
        default=50,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Proficiency level from 0-100"
    )
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="Icon class or name")
    is_visible = models.BooleanField(default=True, help_text="Show in portfolio")
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class HomeContent(models.Model):
    """
    Home content model for storing home page content like profile picture.
    Only one instance should exist.
    """
    profile_picture = models.ImageField(
        upload_to='home_content/',
        blank=True,
        null=True,
        help_text="Profile picture to display on home page"
    )
    profile_picture_url = models.URLField(
        blank=True,
        null=True,
        help_text="Or use external URL for profile picture"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Make this the active home content"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Home Content'
        verbose_name_plural = 'Home Content'

    def __str__(self):
        return "Home Content"
    
    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other HomeContent instances
            HomeContent.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)
