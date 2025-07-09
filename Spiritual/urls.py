from django.urls import path
from . import views

urlpatterns = [
    path('', views.spiritual_talks, name='spiritual_talks'),
]