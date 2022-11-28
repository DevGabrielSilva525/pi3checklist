from django.db import models

from django.conf import settings

USER = settings.AUTH_USER_MODEL


# Create your models here.
 
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(USER, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
      return self.title