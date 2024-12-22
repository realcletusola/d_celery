from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True, retry_backoff=5, max_retries=3)
def send_email_task(self, subject, message, recipient_list):
    """
    Celery task to send mail. This retries automatically on failure
    """
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )
    except Exception as exc:
        raise self.retry(exc=exc) # retires on task failure