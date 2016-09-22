from django.shortcuts import render, redirect
from . import models
from django.db.models import Count

# Create your views here.
def index(request):
	context={
		'courses':models.Courses.objects.all()
	}
	return render(request,'courses/index.html', context)

def create(request):
	models.Courses.objects.create(name=request.POST['name'], description = request.POST['description'])
	return redirect('courses:index')

def destroy(request, id):
	course = models.Courses.objects.get(id=id)
	if request.method == 'POST':
		course.delete()
		return redirect('courses:index')
	else:
		context = {
			"course": course
		}
		return render(request, "delete.html", context)

def register(request):
	models.Courses.objects.register(student=request.POST['student'], classroom=request.POST['classroom'])
	return redirect('courses:index')

def enrollments(request):
	courses = models.Courses.objects.all()
	users = models.Users.objects.all()
	courseList = models.Courses.objects.all().annotate(totalUsers=Count('user_id__id')).order_by('-totalUsers')
	context = {'courses':courses, 'users':users, 'courseList':courseList}
	fail = models.Courses.objects.checkenroll(classroom=request.POST['classroom'], user=request.POST['student'])
	if not fail[0]:
		context = {'courses':courses, 'users':users, 'courseList':courseList, 'errors':fail[1]}
	return render(request, 'courses/enrollments.html', context)