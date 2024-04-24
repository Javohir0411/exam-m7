from random import randint
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from uzbek_cuisine.settings import sended_mails, EMAIL_HOST_USER, emails_list


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST'])
def insert_email_4_change_password(request):
    email = request.data['email']
    user = get_user_model()
    if user.objects.filter(email=email).exist():
        num = randint(100000, 999999)
        emails_list[email] = num
        send_mail(
            subject='Code for reset password',
            message=f"Code for change your password: {num}\n",
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
        )
        return Response({'message': 'Code for reset password sent to your email'}, status=200)
    else:
        return Response({'message': 'Email does not exist'}, status=400)


@api_view(['POST'])
def reset_password(request):
    code = request.data['code']
    email = request.data['email']
    password1 = request.data['password1']
    password2 = request.data['password2']
    if password1 == password2:
        try:
            if code == emails_list[email]:
                user = get_user_model().objects.get(email=email)
                user.set_password(password1)
                user.save()
                del emails_list[email]
                return Response('Password reset seccessful', status=200)
            else:
                return Response({'message': 'Email or code do not match'}, status=400)
        except:
            return Response({'message': 'Email or code do not match'}, status=400)


@api_view
def login_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
    return Response({'error': 'Method not allowed'}, status=405)


@api_view
def change_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        user = authenticate(username=username, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password changed successfully'})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
    return Response({'error': 'Method not allowed'}, status=405)


@api_view
def password_recovery_api(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        try:
            user = User.objects.get(username=username_or_email)  # Assuming username is unique
            # Here you can implement your password recovery logic (e.g., sending an email with a recovery link)
            return Response({'message': 'Password recovery initiated'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
    return Response({'error': 'Method not allowed'}, status=405)


@api_view(['POST'])
def confirm_email(request):
    if request.method == 'POST':
        try:
            recipient_list = [request.POST.get('email')]
            sended_mails[request.POST.get('email')] = f"{randint(100, 999)}-{randint(100, 999)}"

            send_mail(
                subject='Confirm email',
                message=sended_mails[request.POST.get('email')],
                from_email=EMAIL_HOST_USER,
                recipient_list=recipient_list
            )
            return render(request, 'email/confirm_send_mail.html')
        except Exception as e:
            return HttpResponse(f"Wrong email or {e}")
