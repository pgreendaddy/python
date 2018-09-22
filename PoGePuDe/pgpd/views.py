from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
#---User Register
from django.contrib.auth.models import User
from django.contrib import messages
#----API-----
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import usersSerializer, DevicesSerializer
#---Login
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,'index.html')
def newfile(request):
    return render(request,'NewFile.html')

#------User Registration---------

def userregistration(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    confirm_password =request.POST.get('confirm_password')
   
    if User.objects.filter(username=username):
        messages.info(request,'This username is already existing.')
        return redirect('/index')
    if User.objects.filter(email=email):
        messages.info(request,'This email address is already existing.')
        return redirect('/index')
    if password != confirm_password:
    #if password and confirm_password and password != confirm_password:
        messages.info(request,'The two password fields must match.')
        return redirect('/index')
    else:            
        User.objects.create_user(username= username, email= email, password= password) 
        messages.success(request,'User Successfully Registered')
        return redirect('/index')
    

#-------Login-------#
def userlogin(request):
    
        
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
    #if User.objects.filter(username.object.filter(superuser=username), password.filter(superuser=password)):
            
        try:
            user=auth.authenticate(username=username, password=password)
            
            #if user.username==username:   # admin login
            #if user.is_superuser==1:
               # return redirect('/devicelist')
            if user is not None:
                auth.login(request,user)
                if user.is_superuser==1: # admin login
                    return redirect('/devicelist')
                return HttpResponseRedirect('/userdevice')
            else:
                messages.error(request,'Email and Password mismatch')
        except auth.ObjectDoesNotExist:
                messages.error(request,'Invalid User')
    return HttpResponseRedirect('/index')  



def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, '/devicelist', context)

def logout(request):
    auth.logout(request)
    return redirect('/index')
#------------REST API---------
class userslist(APIView):
    def get(self,request):
        users=User.objects.all()
        serializer=usersSerializer(users, many=True)
        return Response(serializer.data)
    def post(self):
        pass
    
class deviceslist(APIView):
    def get(self,request):
        devices=Devices.objects.all()
        serializer=DevicesSerializer(devices, many=True)
        return Response(serializer.data)
    def post(self):
        pass    
        
#------------RSET API END------
#---------Device Functinality-------
from pgpd.forms import DevicesForm
from pgpd.models import Devices

@login_required(login_url='/index') # Decorator using for login required
def device(request):
    if request.method=="POST":
        form=DevicesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/userdevice')
            except:
                pass
    else:
        form=DevicesForm()
    return render(request,'devices.html',{'form':form})

@login_required(login_url='/index') # Decorator using for login required
def devicelist(request):
    device=Devices.objects.all()
    return render(request,"devicelist.html",{'device':device})

@login_required(login_url='/index') # Decorator using for login required
def userdevice(request):
    #user=User.objects.all()
    #for k in se:
    #df=User.objects.get(username)
    #device=Devices.objects.username={{user.username}}
    return render(request,'userdevice.html',{'device':device})


@login_required(login_url='/index') # Decorator using for login required
def devedit(request,id):
    devices=Devices.objects.get(id=id)
    return render(request,'devedit.html',{'devices':devices})

@login_required(login_url='/index') # Decorator using for login required
def update(request,id):
    devices=Devices.objects.get(id=id)
    form=DevicesForm(request.POST or None,instance=devices)
    if form.is_valid():
        form.save()
        return redirect("/devicelist")
    return render(request,'devedit.html',{'devices':devices})

@login_required(login_url='/index') # Decorator using for login required
def onoffbutton(request,id):
    devices=Devices.objects.get(id=id)
    devicestatus=request.POST.get('devstatus')
    Devices.objects.filter(id=id).update(devicestatus=devicestatus)
    return redirect("/devicelist")

@login_required(login_url='/index') # Decorator using for login required          
def destroy(request,id):
    devices=Devices.objects.get(id=id)
    devices.delete()
    return redirect("/devicelist")
            
#----------Device Functionality---------            

