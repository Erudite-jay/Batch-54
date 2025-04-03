from django.http import JsonResponse
from django.shortcuts import render
from . forms import ContactForm
from . models import Contact
# Create your views here.

def contact_file(request):
    if request.method=="POST":
        form=ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # record=Contact(name=form.cleaned_data['name'],message=form.cleaned_data['message'],file=form.cleaned_data['file'])
            # record.save()

            form.save() # model form

            return JsonResponse({"success":True})
        else:
            return JsonResponse({
                "success":False,
                "errors":form.errors.as_json()
            })

    
    else: 
        form=ContactForm()

    
    return render(request,"Forms_app/contactFile.html",{'form':form})