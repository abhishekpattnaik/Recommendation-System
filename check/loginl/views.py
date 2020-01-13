from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from loginl.forms import login_form
from loginl.tf_idf import get_search


def index(request):
	template_name = 'index.html'
	if request.method == 'GET':
		form = login_form()
		return render(request, template_name, {'form':form})

	if request.method == 'POST':
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
