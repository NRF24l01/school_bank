from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello'),
]