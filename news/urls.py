from django.urls import path
from . import views


urlpatterns = [
  path('', views.index , name='index'),
  path('<slug:pk>', views.category , name='category'),
  path('news/<slug:sk>', views.news , name='news'),]