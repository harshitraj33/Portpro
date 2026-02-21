# Generated migration for HomeContent model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0002_skill_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, help_text='Profile picture to display on home page (stored in Cloudinary)', null=True, upload_to='home_content/')),
                ('profile_picture_url', models.URLField(blank=True, help_text='Or use external URL for profile picture', null=True)),
                ('name', models.CharField(default='HARSHIT RAJ', help_text='Your name to display on home page', max_length=200)),
                ('title', models.CharField(default='Full Stack Developer | Cybersecurity Enthusiast', help_text='Your job title/description', max_length=500)),
                ('education', models.CharField(default='B.Tech CSE @ LPU', help_text='Your education details', max_length=300)),
                ('email', models.EmailField(blank=True, help_text='Email address', max_length=254, null=True)),
                ('phone', models.CharField(blank=True, help_text='Phone number', max_length=20, null=True)),
                ('github_url', models.URLField(blank=True, help_text='GitHub profile URL', null=True)),
                ('linkedin_url', models.URLField(blank=True, help_text='LinkedIn profile URL', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Make this the active home content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Home Content',
                'verbose_name_plural': 'Home Content',
            },
        ),
    ]
