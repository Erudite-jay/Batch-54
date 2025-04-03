from django.http import JsonResponse
from django.shortcuts import render
from . models import SessionUser
# Create your views here.

def login_view(request):
    if request.session.get('username'):
        return JsonResponse({
            "success":True,
            "message":"user already loggged in",
            "user is": request.session.get('username')
        })
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=SessionUser.objects.get(username=username)
        if user.password==password:

            request.session['username']=username
            request.session.set_expiry(20)

            return JsonResponse({
                "success":True,
                "Message":"user logged in successfully"
            },status=200)
        
    return render(request, "Session_app/login.html")