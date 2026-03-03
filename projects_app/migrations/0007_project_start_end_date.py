# Generated migration for adding start_date and end_date to Project model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0006_visitcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, null=True, help_text='Project start date'),
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True, help_text='Project end date (leave empty if ongoing)'),
        ),
    ]
