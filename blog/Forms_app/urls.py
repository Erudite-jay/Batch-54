from django.urls import path
from . import views

urlpatterns=[
path("file/",views.contact_file)
]