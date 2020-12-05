from django.shortcuts import render
from django.http import HttpResponse
from resume.forms import UserSignupform
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	return render(request,'resume/homepage.html')

def msg(request):
	return HttpResponse('hi')
def signup(request):
	if request.method=='POST':
		form=UserSignupform(request.POST)
		if form.is_valid():
			 form.save()
			 return render(request,'resume/signin.html')
	form = UserSignupform()
	return render(request,'resume/signup.html',{'form':form})


def form(request):
    return render(request,'resume/form.html')


def themes(request):
	return render(request,'resume/themes.html')

def blankformat(request):
	return render(request,'resume/blankformat.html')

def tableformat(request):
	return render(request,'resume/tableformat.html')	