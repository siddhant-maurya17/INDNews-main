from django.urls import path
from .import views

urlpatterns = [
  path('support/contactus', views.contact , name='contact'),]