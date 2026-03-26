from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0008_auto_20260314_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcontent',
            name='certificate_link',
            field=models.URLField(blank=True, help_text='Optional URL for certificate details/verification page', null=True),
        ),
    ]
