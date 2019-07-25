from django.shortcuts import render
from django.http import *
from .models import Buyer
from django.db.models import Max
from .Forms import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def Home(request):
    form = InputForm()
    return render(request, 'input.html',{'form':form})
def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')
def Products(request):
    return render(request, 'products.html')

def Update(request):
    subject = 'New Order palced'
    message = 'NAME:'+ request.POST['name'] + ' ADDRESS:'+request.POST['address'] +' MOBILE NUMBER:'+ request.POST['mobile_number'] +' QTY REQUIRED:'+ request.POST['qty_required']+' DATE:'+request.POST['date_required']
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['namajithma@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    buyer = Buyer(name =request.POST['name'],address = request.POST['address'],
                  mobile_number = int(request.POST['mobile_number']),qty_required = int(request.POST['qty_required']),
                  date_required=request.POST['date_required'])
    buyer.save()
    messages.success(request,'Order Placed Sucessfully our Sales team will call you')
    return HttpResponseRedirect('/home/')