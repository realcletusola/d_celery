from django.contrib.auth.models import User
from django.http import JsonResponse
from .tasks import send_email_task

def user_registration(request):
    # simulate user registration
    user = User.objects.create_user(username='testuser', email='testemail@email.com', password='testUSER123$$')

    # call celery task
    send_email_task.delay(
        subject="Welcome to D_celery Platform",
        message= "Thank you for joining us",
        recipient_list=[user.email],
    )

    return JsonResponse({"message": "User registered successfully"})

def user_login(request):
    # simulate login logic
    user = User.objects.get(username='testuser')

    # call celery task
    send_email_task.delay(
        subject="Login Notification",
        message="You just logged into your account!",
        recipient_list=[user.email],
    )

    return JsonResponse({"message":"Login successful"})