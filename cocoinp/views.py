from django.shortcuts import render
from django.http import *
from .models import Buyer
from django.db.models import Max
from .Forms import *
from django.contrib import messages

def Home(request):
    form = InputForm()
    return render(request, 'input.html',{'form':form})
def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Update(request):
    buyer = Buyer(name =request.POST['name'],address = request.POST['address'],
                  mobile_number = int(request.POST['mobile_number']),qty_required = int(request.POST['qty_required']),
                  date_required=request.POST['date_required'])
    buyer.save()
    messages.success(request,'Order Placed Sucessfully our Sales team will call you')
    return HttpResponseRedirect('/home/')