from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.http import HttpResponseRedirect

# Create your views here.

def homepage(request):
	return render(request=request, template_name='main/index.html')

def contact(request):
	return render(request=request, template_name='main/contact.html')

def aboutus(request):
	return render(request=request, template_name='main/aboutus.html')

def donatefood(request):

    return render(request=request, template_name='main/Donate_Food_Form.html')

###########################  LOGIN AND REGISTRATION SYSTEM  #######################################

def volunteer_registration(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")

######################################  END  ################################################

def ngo_registration(request):
	return render(request=request, template_name='main/ngo_registration.html')

def donatemoney(request):
	return render(request=request, template_name='main/donatemoney.html')