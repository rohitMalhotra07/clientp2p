#views.py
from clientNode import *
from files import RegistrationForm 
from files import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import RequestContext
from uuid import getnode as get_mac
import json
import requests
from django.contrib.auth.models import User

ServerAddress="http://localhost:8010"

def login(request):
    global ServerAddress
    if request.method=='POST':
        print 'we are here'
        form = LoginForm(request.POST) # A form bound to the POST data
        url=ServerAddress+'/logincheck'
        mac_address=get_mac()
        dataq={
            'username':request.POST['username'],
            'password':request.POST['password'],
            'mac_address':mac_address,
        }
        print dataq
        r = requests.get(url,data=json.dumps(dataq))
        try:
            if r.text== "logged in":
                u=User.objects.create(username=request.POST['username'],password=request.POST['password'])
                print u
                u.is_active=True
                u.save()
                data={
                    'username':request.POST['username']
                }
                return HttpResponseRedirect("http://127.0.0.1:8000/home?"+"username="+request.POST['username'])
            else:
                return HttpResponseRedirect('http://127.0.0.1:8000')


        except:
            if r.text=="logged in":
                u=User.objects.get(username=request.POST['username'])
                print u
                u.is_active=True
                u.save()
                print u.is_active
                data={
                    'username':request.POST['username']
                }
                return HttpResponseRedirect("http://127.0.0.1:8000/home?"+"username="+request.POST['username'])
                #return HttpResponseRedirect("http://127.0.0.1:8000/home")
            else:
                return HttpResponseRedirect('http://127.0.0.1:8000')
    else:
        form =LoginForm()
        variables=RequestContext(request,
            {
                'form':form
            })
        return render_to_response('registration/login.html',variables,)

@csrf_exempt
def register(request):
    global ServerAddress
    if request.method == 'POST':
        form = RegistrationForm(request.POST) # A form bound to the POST data
        url=ServerAddress
        mac_address = get_mac()
        print 'reached here'
        dataq={
            'mac_address':mac_address,
            'username': request.POST['username'],
            'email':request.POST['email'],
            'roll_no':request.POST['roll_no'],
            'password':request.POST['password1'],
            'college_name': request.POST['college_name']
        }
        print dataq
        r = requests.get(url,data=json.dumps(dataq) )
        form=LoginForm()
        return HttpResponseRedirect('http://127.0.0.1:8000')

    else:
        form = RegistrationForm()
        variables = RequestContext(request, 
            {
                'form': form 
            })
        return render_to_response(
        'registration/register.html',
        variables,
        )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

#@login_required(login_url='/')
def home(request):
    username=request.GET['username']
    print username
    user=User.objects.get(username=username)
    return render_to_response(
    'home.html',
    { 'user': user}
    )

def checkvalidusername(request):
    global ServerAddress
    print 'something'
    url=ServerAddress+'/checkvalidusername'
    dataq={'username': request.POST.get('Username')}
    print dataq
    r=requests.get(url,data=json.dumps(dataq))
    return HttpResponse(r)
