from decimal import Context
from email.headerregistry import MessageIDHeader
from tkinter import E
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from datetime import datetime
from home.models import Contact
from home.models import Sign

# Create your views here.
def home(request):
#    return HttpResponse("This is Homepage")
    context ={ "variable1":"before are the parahraaphas",
               "variable2":"this is second veriable"  ,  
                     }
    return render(request,'index.html',context)
      

def about(request):
    #return HttpResponse("About Us")
      return render(request,'about.html')

def services(request):
    #return HttpResponse("We Provide")
    return render(request,'services.html')
 
def contact(request):
    #return HttpResponse("Contact Us")

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        contact = Contact(name=name,email=email,phone=phone,comment=comment,date=datetime.today())
        contact.save()
       
    return render(request,'contact.html')

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
           
            return redirect("/")

        else:
                messages.info(request,"Invalid Credentials")
                return redirect('signin')

    else:
        
        return render(request,'signin.html')

    return render(request,'signin.html') 

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        signup = Sign(name=name,email=email,password=password,password2=password2)
        signup.save()
       

    return render(request,'signup.html')


