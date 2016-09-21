from django.shortcuts import render, redirect
import random, string

def index(request):	
	if request.session['attempt']:
		pass
	else:	
		request.session['attempt'] = 0
	return render(request, "index.html")	

def bob(request):
	request.session['ranstr'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
	request.session['attempt'] += 1
	return  redirect('/')
