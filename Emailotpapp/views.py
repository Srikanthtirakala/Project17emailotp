from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.
class Home(View):
    def get(selfself,request):
        return render(request,'input.html')
class Send(View):
    def get(self,request):
        subject='thank for contacting'
        email_message=str(random.randint(100000,999999))
        print(email_message)
        from_email=settings.EMAIL_HOST_USER
        email=request.GET["t1"]
        to_list=[email]
        send_mail(subject,email_message,from_email,to_list,fail_silently=False)
        return HttpResponse("Email sent successfully")