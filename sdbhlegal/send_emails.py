# send_emails.py
import time
from pages.models import Contact
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import django
import os

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

def send_email_task():
    contacts = Contact.objects.filter(mailSent=False)
    for contact in contacts:
        html_content = render_to_string('userConfirmation.html')
        
        email = EmailMultiAlternatives(
            subject=f"Thank you for contacting SDBH Legal",
            body=contact.message,
            to=contact.email,
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        contact.mailSent = True
        contact.save()

def main():
    while True:
        send_email_task()
        time.sleep(60)  # Sleep for 60 seconds before checking for new tasks

if __name__ == "__main__":
    main()