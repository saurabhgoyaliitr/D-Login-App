from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import views 

from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,Http404
from django.contrib import messages
from django.contrib.auth.models import User
from login.forms import ProfileForm,PhotoUploadForm
from login.models import ProfileData



def register (request): 

  if request.POST :
	user1 =   User.objects.create_user(request.POST['username'], request.POST['email'] ,  request.POST['password']        )
        ProfileData.objects.create (user = user1 )
	user1.first_name = request.POST['firstname'] 
	user1.last_name = request.POST['lastname'] 
	user1.save()   
	
	return HttpResponseRedirect (  '/completeprofile' )


def login_user (request ): 
	#import ipdb;ipdb.set_trace()
 if request.POST :
	
	username = request.POST['username'] 
	password = request.POST['password']  
	user = authenticate ( username = username , password = password ) 
 
	if user is not None:
		#if user.is_active : 
		login (request , user ) 
		return HttpResponseRedirect ('main/') 
        else :
		return render (request , 'login/login.html' , { 'error' :"Incorrect Username or Password" } , )   
 
	  
 return render_to_response ('login/login.html' , context_instance = RequestContext (request ))  

  # @login_required (login_url = '/login/' ) 

@login_required ( login_url = '/login/' ) 
def logoutu ( request ) : 
	logout (request ) 
	return HttpResponseRedirect ( '/login/' )


@login_required ( login_url = '/login/' ) 
def main (request):
  p = ProfileData.objects.get (user = request.user )  
  return render ( request ,'login/profile.html' , { 'Pro' : p}         ) 

@login_required ( login_url = '/login/')
def change(request):
#    global username
    #import pdb; pdb.set_trace() ;
    if request.method=='POST':
	   if request.POST['password1']== request.POST['password2']:
                if request.POST['password1']!="" :    
                  request.user.set_password(request.POST['password1'])
                  request.user.save()
                  return HttpResponseRedirect('/login/main/')
                else:
                  return render (request , 'login/change.html' , { 'error' : "Please enter Password" } , ) 
           
           return render (request , 'login/change.html' , { 'error' : "Passwords Donot Match" } , ) 
    return render (request , 'login/change.html')

@login_required (login_url = '/login') 
def listi (request ) : 
      if request.method =='POST' :
           form = PhotoUploadForm( request.POST , request.FILES) 
           if form.is_valid() : 
              try :
            			m = ProfileData.objects.get(user=request.user)
     		       		m.profile = form.cleaned_data['profile']
            			m.save()
				messages.add_message(request,messages.SUCCESS,"Profile Picture Successfully Updated")
            			return HttpResponseRedirect("/login/main/")
              except(Http404):
				m = ProfileData.objects.create(user=request.user)
				m.profile= form.cleaned_data['profile']
				m.save()
				messages.add_message(request,messages.SUCCESS,"Profile Picture Successfully Updated")
            			return HttpResponseRedirect("/login/main/")
           else : 
              messages.add_message(request,message.ERROR,"you done something fucking wrong") 
              return HttpResponseRedirect("/login/main/")
 
      return HttpResponseRedirect ("/login/main/") 
