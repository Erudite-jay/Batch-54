from django.urls import path
from . import views

urlpatterns = [
    path("ph/",views.print_hello),
    path("lt/",views.load_template),
    path("data/",views.data)
]
