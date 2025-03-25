from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


#logic to print toward the cient side
def print_hello(request):
    return HttpResponse("Hello i am djangooooooooooooooooo")


def load_template(request):
    return render(request,"Auth_app/index.html")