from django.shortcuts import render, redirect

def index(request):
	return render(request, "index.html")

def create(request):
	request.session['yourName'] = request.POST['yourName']
	request.session['location'] = request.POST['location']
	request.session['favLang'] = request.POST['favLang']
	request.session['comment'] = request.POST['comment']
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1
	return redirect("/result")

def result(request):
	return render(request, "result.html")

def back(request):
	return redirect("")
