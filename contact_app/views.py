from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage


class ContactView(View):
    template_name = 'contact_app/contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            ip_address=ip_address,
            user_agent=user_agent
        )

        try:
            send_mail(
                subject=f"Thank you for contacting us, {name}!",
                message=f"Hi {name},\n\nThank you for reaching out. We have received your message regarding '{subject}' and will get back to you soon.\n\nBest regards,\nThe Team",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

            if settings.EMAIL_HOST_USER:
                send_mail(
                    subject=f"New Contact Form Submission: {subject}",
                    message=f"New message from {name} ({email}):\n\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )

            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')

        return redirect('contact:contact')

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
