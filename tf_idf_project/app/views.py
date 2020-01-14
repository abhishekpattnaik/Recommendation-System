from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from app.forms import login_form
from app.tf_idf import get_search
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
class index(APIView):
	template_name = 'index.html'
	def get(self, request):
		form = login_form()
		return render(request, template_name, {'form':form})

	def post(self, request):
		form = login_form(request.POST)
		if form.is_valid():
			text = form.cleaned_data['search']
			url_dict = get_search(text)
		form = login_form()
		args = {'form':form,'text':text,'url_dict':url_dict.values()}
		return render(request, template_name, args)

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	context = {'form':form}
	return render(request, 'registration/register.html', context)
