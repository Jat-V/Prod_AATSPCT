from django.db import models
from ckeditor.fields import RichTextField


class Event(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    Title = models.CharField(max_length=50)
    Description_small = models.CharField(max_length=125)
    Body_desc = RichTextField(null=True)
    Start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    End_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    Active_check = models.BooleanField()

    def __str__(self):
        return self.Title
