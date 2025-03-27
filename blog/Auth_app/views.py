from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Contact
from . serializers import ContactSerilizer
# Create your views here.


#logic to print toward the cient side
def print_hello(request):
    return HttpResponse("Hello i am djangooooooooooooooooo")


def load_template(request):
    return render(request,"Auth_app/index.html")


def data(request):
    if request.method=='GET':
        all_data=Contact.objects.all() #queryset -> list of object
        sd=ContactSerilizer(all_data,many=True) #serialized data ==~ 99.99999999 JSON
        return JsonResponse({
            "success":True,
            "Data":sd.data
        })
