from django.shortcuts import render

# Create your views here.

def homepage(request):
	return render(request=request, template_name='main/index.html')

def contact(request):
	return render(request=request, template_name='main/contact.html')

def donatefood(request):
	return render(request=request, template_name='main/donatefood.html')

def volunteer_registration(request):
	return render(request=request, template_name='main/volunteer_registration.html')

def ngo_registration(request):
	return render(request=request, template_name='main/ngo_registration.html')

def donatemoney(request):
	return render(request=request, template_name='main/donatemoney.html')