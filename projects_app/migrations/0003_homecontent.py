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
                ('profile_picture', models.ImageField(blank=True, help_text='Profile picture to display on home page', null=True, upload_to='home_content/')),
                ('profile_picture_url', models.URLField(blank=True, help_text='Or use external URL for profile picture', null=True)),
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
