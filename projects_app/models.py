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
    created = models.DateField(blank=True, null=True, help_text="Project creation date (day, month, year)")
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

    @property
    def image_url(self):
        """Get the correct image URL, handling both local and Cloudinary images."""
        if self.image:
            return self.image.url
        return None

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

    @property
    def company_logo_url(self):
        """Get the correct logo URL, handling both local and Cloudinary images."""
        if self.company_logo:
            return self.company_logo.url
        return None


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
    Home content model for storing home page content like profile picture, name, title, etc.
    Only one instance should exist.
    """
    # Profile Picture
    profile_picture = models.ImageField(
        upload_to='home_content/',
        blank=True,
        null=True,
        help_text="Profile picture to display on home page (stored in Cloudinary)"
    )
    profile_picture_url = models.URLField(
        blank=True,
        null=True,
        help_text="Or use external URL for profile picture"
    )
    
    # Home Page Content
    name = models.CharField(
        max_length=200,
        default="HARSHIT RAJ",
        help_text="Your name to display on home page"
    )
    title = models.CharField(
        max_length=500,
        default="Full Stack Developer | Cybersecurity Enthusiast",
        help_text="Your job title/description"
    )
    education = models.CharField(
        max_length=300,
        default="B.Tech CSE @ LPU",
        help_text="Your education details"
    )
    
    # Contact Info
    email = models.EmailField(
        blank=True,
        null=True,
        help_text="Email address"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Phone number"
    )
    github_url = models.URLField(
        blank=True,
        null=True,
        help_text="GitHub profile URL"
    )
    linkedin_url = models.URLField(
        blank=True,
        null=True,
        help_text="LinkedIn profile URL"
    )
    
    # Status
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
    
    @classmethod
    def get_active_content(cls):
        """Get the active home content or create a default one"""
        content = cls.objects.filter(is_active=True).first()
        if not content:
            content = cls.objects.create(
                is_active=True,
                name="HARSHIT RAJ",
                title="Full Stack Developer | Cybersecurity Enthusiast",
                education="B.Tech CSE @ LPU"
            )
        return content


class AboutContent(models.Model):
    """
    About page content model for storing about section content.
    Only one instance should exist.
    """
    # Bio/Introduction
    bio = models.TextField(
        blank=True,
        null=True,
        help_text="Main bio/introduction text for the about page"
    )
    
    # Skills stored as JSON text
    skills_languages = models.TextField(
        blank=True,
        null=True,
        help_text="Comma-separated programming languages"
    )
    skills_frameworks = models.TextField(
        blank=True,
        null=True,
        help_text="Comma-separated frameworks"
    )
    skills_tools = models.TextField(
        blank=True,
        null=True,
        help_text="Comma-separated tools and platforms"
    )
    skills_soft = models.TextField(
        blank=True,
        null=True,
        help_text="Comma-separated soft skills"
    )
    
    # Internships stored as JSON text
    internship_1_company = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="First internship company name"
    )
    internship_1_position = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="First internship position"
    )
    internship_1_date = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="First internship date range"
    )
    internship_1_description = models.TextField(
        blank=True,
        null=True,
        help_text="First internship description (one point per line)"
    )
    internship_1_tech = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        help_text="First internship technologies used"
    )
    
    internship_2_company = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Second internship company name"
    )
    internship_2_position = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Second internship position"
    )
    internship_2_date = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Second internship date range"
    )
    internship_2_description = models.TextField(
        blank=True,
        null=True,
        help_text="Second internship description (one point per line)"
    )
    internship_2_tech = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        help_text="Second internship technologies used"
    )
    
    # Certificates stored as JSON text (one per line)
    certificates = models.TextField(
        blank=True,
        null=True,
        help_text="Certificates (one per line in format: Certificate Name | Issuing Organization | Date)"
    )
    
    # Education
    education_1_institution = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="First education institution"
    )
    education_1_degree = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="First education degree"
    )
    education_1_date = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="First education date range"
    )
    education_1_cgpa = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="First education CGPA/Grade"
    )
    education_1_location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="First education location"
    )
    
    education_2_institution = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Second education institution"
    )
    education_2_degree = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Second education degree"
    )
    education_2_date = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Second education date range"
    )
    education_2_cgpa = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Second education CGPA/Grade"
    )
    education_2_location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Second education location"
    )
    
    # Status
    is_active = models.BooleanField(
        default=True,
        help_text="Make this the active about content"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About Content'
        verbose_name_plural = 'About Content'

    def __str__(self):
        return "About Content"
    
    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other AboutContent instances
            AboutContent.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)
    
    def get_skills_languages_list(self):
        if self.skills_languages:
            return [skill.strip() for skill in self.skills_languages.split(',')]
        return []
    
    def get_skills_frameworks_list(self):
        if self.skills_frameworks:
            return [skill.strip() for skill in self.skills_frameworks.split(',')]
        return []
    
    def get_skills_tools_list(self):
        if self.skills_tools:
            return [skill.strip() for skill in self.skills_tools.split(',')]
        return []
    
    def get_skills_soft_list(self):
        if self.skills_soft:
            return [skill.strip() for skill in self.skills_soft.split(',')]
        return []
    
    def get_internship_1_description_list(self):
        if self.internship_1_description:
            return [desc.strip() for desc in self.internship_1_description.split('\n') if desc.strip()]
        return []
    
    def get_internship_2_description_list(self):
        if self.internship_2_description:
            return [desc.strip() for desc in self.internship_2_description.split('\n') if desc.strip()]
        return []
    
    def get_certificates_list(self):
        if self.certificates:
            return [cert.strip() for cert in self.certificates.split('\n') if cert.strip()]
        return []
    
    @classmethod
    def get_active_content(cls):
        """Get the active about content or create a default one"""
        content = cls.objects.filter(is_active=True).first()
        if not content:
            content = cls.objects.create(
                is_active=True,
                bio="I am a passionate Full Stack Developer and Cybersecurity Enthusiast currently pursuing my B.Tech in Computer Science and Engineering at Lovely Professional University. With hands-on experience in Python, Django, React, and various cybersecurity tools, I am eager to contribute to innovative projects and continue learning new technologies.",
                skills_languages="Python, Java, C++",
                skills_frameworks="React, Django",
                skills_tools="MySQL, Git, AWS, Kali Linux",
                skills_soft="Creative, Problem Solver, Active Listener, Adaptability",
                internship_1_company="Conquest Tech Solutions",
                internship_1_position="Intern Computer Analyst",
                internship_1_date="June-July 2023",
                internship_1_description="Conducted software test evaluations, identified issues, and reviewed system functionalities\nCreated and maintained structured documentation, reports, and workflow summaries\nInteracted with team members to understand requirements",
                internship_1_tech="Git/Github, MS Office, Bug Tracking Systems",
                internship_2_company="Coincent.ai",
                internship_2_position="Cyber Security & Ethical Hacking Training",
                internship_2_date="January-March 2023",
                internship_2_description="Gained Hands-on experience in network security, penetration testing, and threat analysis\nWorked with tools to identify vulnerabilities and understand secure solutions\nImproved understanding of system security and ethical hacking principles",
                internship_2_tech="Kali Linux Tools, Nmap, Burp Suite, Wireshark",
                certificates="Master Generative AI & Generative AI tools by Infosys Springboard (Aug 2025)\nPrivacy and Security in Online Social Media by NPTEL (April 2025)\nAmazon Web Service (AWS) Certified by Infosys Springboard (April 2024)\nFundamentals of Network Communication by University of Colorado, Coursera (Sept 2024)\nGCP Cloud Digital Leader Certification by KodeKloud (April 2023)\nCyber Security and Ethical Hacking by Coincent.ai (March 2023)",
                education_1_institution="Lovely Professional University",
                education_1_degree="B.Tech - Computer Science and Engineering",
                education_1_date="Since August 2024",
                education_1_cgpa="CGPA: 6.65",
                education_1_location="Phagwara, Punjab",
                education_2_institution="Lovely Professional University",
                education_2_degree="Diploma Computer Science and Engineering",
                education_2_date="August 2021 - June 2024",
                education_2_cgpa="CGPA: 7.3",
                education_2_location="Phagwara, Punjab"
            )
        return content
