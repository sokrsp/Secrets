from django.shortcuts import render, redirect

def index(request):
	return render(request, 'secretapp/index.html')

def process(request):
	if 'secretwall' not in session:
		request.session['secretwall'] = []

	log = request.session['secretwall']

	return redirect('/')

def secrets(request):
	return render(request, 'secretapp/secrets.html')