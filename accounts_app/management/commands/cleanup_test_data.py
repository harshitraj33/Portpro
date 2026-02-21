from django.core.management.base import BaseCommand
from contact_app.models import ContactMessage
from projects_app.models import WorkExperience


class Command(BaseCommand):
    help = 'Clean up test data from the database'

    def handle(self, *args, **options):
        # Delete test contact messages
        test_messages = ContactMessage.objects.filter(
            name__icontains='Harshit'
        )
        count_messages = test_messages.count()
        test_messages.delete()
        
        # Delete test work experiences
        test_experiences = WorkExperience.objects.filter(
            company__icontains='Harshit'
        )
        count_experiences = test_experiences.count()
        test_experiences.delete()
        
        self.stdout.write(self.style.SUCCESS(
            f'Successfully deleted {count_messages} contact messages and {count_experiences} work experiences'
        ))
