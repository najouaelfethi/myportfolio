from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def send_email_view(request):
    if request.method == "POST":  
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New message from {fullname} via Contact Form"
        full_message = f"Full Name: {fullname}\nEmail: {email}\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],  
            fail_silently=False,
        )

        return render(request, 'portfolio.html', {'success': True}) 

    return render(request, 'portfolio.html')    
    
