from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home),
    path('portfolio', views.portfolio),
    path('contact', views.send_email_view, name='send_email_view'),
]