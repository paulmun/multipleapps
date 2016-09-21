from django.shortcuts import render
import datetime

def index(request):
	timeDisplay = {
	"time":datetime.datetime.now()
	}
	return render(request, "index.html", timeDisplay)
