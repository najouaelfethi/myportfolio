from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.portfolio),
    path('portfolio', views.send_email_view, name='send_email_view'),
]