from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Contact
from . serializers import ContactSerilizer
import json

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


#logic to print toward the cient side
def print_hello(request):
    return HttpResponse("Hello i am djangooooooooooooooooo")


def load_template(request):
    return render(request,"Auth_app/index.html")


@csrf_exempt
def data(request):
    if request.method=='GET':
        all_data=Contact.objects.all() #queryset -> list of object
        sd=ContactSerilizer(all_data,many=True) #serialized data ==~ 99.99999999 JSON
        return JsonResponse({
            "success":True,
            "Data":sd.data
        })

    if request.method=="POST":
        input_data=json.loads(request.body) # json
        sd=ContactSerilizer(data=input_data) #deserialization

        if sd.is_valid(): #if data is valid
            sd.save()
            return JsonResponse({
               " success":True,
                "message":"Data saved successfully"
            },status=201)


@csrf_exempt
def single_user_data(request,pk):
    if request.method=="GET":
        try: 
            user=Contact.objects.get(pk=pk)
            sd=ContactSerilizer(user)

            return JsonResponse({
                "success":True,
                "Data":sd.data
            },status=200)
        
        except Exception as e:
            return JsonResponse({
                "success": False,
                "Message": str(e)
            },status=500)
        
    if request.method=="PUT":
        try:
            user=Contact.objects.get(pk=pk) # finding the user
            input_data=json.loads(request.body) # getting data from client

            sd=ContactSerilizer(user,data=input_data) # updating the data with help of serailzer

            if sd.is_valid():
                sd.save()
                return JsonResponse({
                    "success":True,
                    "message":"Data updated successfully"
                })
            
        except Exception as e:
            return JsonResponse({
                "success": False,
                "Message": str(e)
            },status=500)

    if request.method=="PATCH":
        try: 
            user=Contact.objects.get(pk=pk)
            input_data=json.loads(request.body)

            sd=ContactSerilizer(user,data=input_data,partial=True)

            if sd.is_valid():
                sd.save()

                return JsonResponse({
                    "success":True,
                    "message":" Partial Data updated successfully"
                },status=200)
            
            else:
                return JsonResponse({
                     "success":False,
                    "message":" Partial Data update failed"
                },status=401)
        except Exception as e:
             return JsonResponse({
                    "success":False,
                    "message":str(e)
                },status=500)
        
    if request.method=="DELETE":
        try:
            user=Contact.objects.get(pk=pk)
            user.delete()
            return JsonResponse({
                "success":True,
                "Message": "User deleted successfully"
            })
        except Exception as e:
            return JsonResponse({
                    "success":False,
                    "message":str(e)
                },status=500)