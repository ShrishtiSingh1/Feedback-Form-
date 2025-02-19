from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from feedback_form.views import *

urlpatterns = [
    path('', home, name='home'),
    
    path('feedback_form/', feedback_form , name="feedback_form"),

    path('admin/', admin.site.urls),
]
