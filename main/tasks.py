from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings

@shared_task
def send_email_task(subject, message, recipient_list):
    try:
        email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
        email.send()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
