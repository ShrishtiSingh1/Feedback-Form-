from django.db import models # type: ignore

# Create your models here.
class Feedback_form(models.Model):
    feedback_user_name = models.CharField(max_length=100)
    feedback_user_description = models.TextField()
    feedback_user_image = models.ImageField(upload_to="feedback_form")
