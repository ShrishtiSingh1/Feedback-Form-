from django.shortcuts import render # type: ignore
from .models import *
from django.http import HttpResponse # type: ignore

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to my feedback form home page</h1>")

def feedback_form(request):
    if request.method == "POST":
       data = request.POST
       feedback_user_image = request.FILES.get('feedback_user_image')
       feedback_user_name = data.get('feedback_user_name')
       feedback_user_description = data.get('feedback_user_description')

       Feedback_form.objects.create(
           feedback_user_name = feedback_user_name, 
           feedback_user_description = feedback_user_description, 
           feedback_user_image = feedback_user_image, 
        )

    # print(data)
    return render(request, 'form.html')
