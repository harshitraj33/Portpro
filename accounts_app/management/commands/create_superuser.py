"""
Django management command to create the admin superuser.
Run with: python manage.py create_superuser
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os
from dotenv import load_dotenv

# Load .env file explicitly
load_dotenv()

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates the admin superuser with specified credentials'

    def handle(self, *args, **options):
        username = os.getenv('username')
        password = os.getenv('password')
        email = os.getenv('email')

        # Debug: Print the values to verify they are loaded
        self.stdout.write(f"Username: {username}")
        self.stdout.write(f"Email: {email}")
        self.stdout.write(f"Password: {'*' * len(password) if password else 'None'}")

        if not username or not password or not email:
            self.stdout.write(self.style.ERROR('Missing required environment variables!'))
            self.stdout.write(self.style.ERROR('Please ensure .env file contains:'))
            self.stdout.write(self.style.ERROR('  username=your_username'))
            self.stdout.write(self.style.ERROR('  password=your_password'))
            self.stdout.write(self.style.ERROR('  email=your_email'))
            return

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated password for superuser "{username}"'))
        else:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser "{username}"'))
        
        # Verify the user can authenticate
        if user.check_password(password):
            self.stdout.write(self.style.SUCCESS(f'Password verification: SUCCESS'))
        else:
            self.stdout.write(self.style.ERROR(f'Password verification: FAILED'))
