from django.urls import path

from . views import *

app_name='sns'

urlpatterns = [
    path('', index),
    path('sns/', sns),
]