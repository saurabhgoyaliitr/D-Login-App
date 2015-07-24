from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register (request): 

  if request.POST :
	user =   User.objects.create_user(request.POST['username'], request.POST['email'] ,  request.POST['password']        )

	user.first_name = request.POST['firstname'] 
	user.last_name = request.POST['lastname'] 
	user.save()   
	
	return HttpResponseRedirect (  '/login/' )


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

def logoutu ( request ) : 
	logout (request ) 
	return HttpResponseRedirect ( '/login/' )


def main (request):
   return render ( request ,'login/profile.html' ,  ) 


def change (request ) : 
  if request.POST : 
	if request.POST['password'] == request.POST['password2'] : 
            request.user.password = request.POST['password']
 	    request.user.save()	
            return render ( request , 'login/profile.html' )
	else : 
	    return render (request , 'login/change.html' , {'error': "Passwords Donot  Match" } )   
  return render ( request , 'login/change.html' )    


