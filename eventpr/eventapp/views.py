from django.shortcuts import render,redirect
from . models import Event,Contact
from . forms import BookingForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def events(request):
    dict_eve={
        'eve':Event.objects.all()}
    return render(request,'events.html',dict_eve)

def contact(request): 
    
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')  
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()

        
        return redirect('thanks')
    return render(request,"contact.html") 
def thanks(request):
    return render(request,'thanks.html') 

def confirm(request):
    return render(request,'confirm.html')

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirm')
    
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

