from django.shortcuts import render, redirect
from . import models
from django.db.models import Count

# Create your views here.
def index(request):
	context={
		'courses':models.Courses.objects.all()
	}
	return render(request,'logreg/index.html', context)

def create(request):
	models.Courses.objects.create(name=request.POST['name'], description = request.POST['description'])
	return redirect('index')

def destroy(request, id):
	course = models.Courses.objects.get(id=id)
	if request.method == 'POST':
		course.delete()
		return redirect('index')
	else:
		context = {
			"course": course
		}
		return render(request, "delete.html", context)

def register(request):
	models.Courses.objects.register(student=request.POST['student'], classroom=request.POST['classroom'])
	return redirect('index')

def enrollments(request):
	courseList = models.Courses.objects.all().annotate(totalUsers=Count('user_id__id')).order_by('-totalUsers')
	print courseList
	return render(request, 'courses/enrollments.html')