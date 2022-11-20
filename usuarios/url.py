from django.urls import path
from .views import registro

urlpatterns = [
    path('', ('tasks.urls')),
]