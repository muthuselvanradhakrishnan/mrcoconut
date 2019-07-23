from django.shortcuts import render
from django.http import *
from .models import Buyer
from django.db.models import Max
from .Forms import *
from django.contrib import messages
from twilio.rest import Client

def Home(request):
    form = InputForm()
    return render(request, 'input.html',{'form':form})

def Update(request):
    name = request.POST['name']
    address = request.POST['address']
    mobnum = request.POST['mobile_number']
    qty = request.POST['qty_required']
    datereq = request.POST['date_required']

    order_details = 'New Order Received'+'Hotel Name:'+name + 'Adress:'+address+'Modile Number:'+mobnum+'Quantity:'+qty\
                    +'Date Required:'+datereq
    account_sid = 'AC4202b86208e78adb32861a5072e8ad71'
    auth_token = 'e1db5c7de3b27265a590b1467ab03bd3'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body= order_details,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919566202380'
    )
    buyer = Buyer(name =request.POST['name'],address = request.POST['address'],
                  mobile_number = int(request.POST['mobile_number']),qty_required = int(request.POST['qty_required']),
                  date_required=request.POST['date_required'])
    buyer.save()
    messages.success(request,'Order Placed Sucessfully our Sales team will call you')
    return HttpResponseRedirect('/home/')