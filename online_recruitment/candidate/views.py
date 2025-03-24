import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def landingPage(request):
    jobList = Job.objects.all()
    categories = Category.objects.all()
    context = {
        'jobs': [ ],
        'categories' : []
    }
    for job in jobList:
        temp = {
            'id': job.id,
            'name': job.name,
            'place': job.place,
            'type': job.type,
            'salary': job.salary,
        }
        print(temp)
        context['jobs'].append(temp)
    
    for category in categories:
        temp ={
            'name' : category.name
        }
        context['categories'].append(temp)
        
    return render(request ,'landingPage.html', context)

def aboutPage(request):
    return render(request ,'about.html')

def categoryPage(request):
    return render(request ,'category.html')

def contactPage(request):
    return render(request ,'contact.html')

def jobdetailPage(request, id):
    print(id)
    job = Job.objects.filter(id=id)[0]
    print(job)
    context = {
        'job': {
            'id': job.id,
            'name': job.name,
            'place': job.place,
            'type': job.type,
            'salary': job.salary,
            'category': job.category.name,
        },
    }
    return render(request ,'job-detail.html', context)

def joblistPage(request):
    jobList = Job.objects.all()
    context = {
        'jobs': [ ]
    }
    for job in jobList:
        temp = {
            'id': job.id,
            'name': job.name,
            'place': job.place,
            'type': job.type,
            'salary': job.salary,
        }
        print(temp)
        context['jobs'].append(temp)

    return render(request ,'job-list.html', context)

def testimonialPage(request):
    return render(request ,'testimonial.html')

def resume_upload(request):
    return render(request ,'resume_upload.html')

def registrationform(request):
    if request.method == 'POST':
        print('post recieved')
        name = request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        gender = request.POST.get('gender')
        print(name, email, url, gender)

    return render(request ,'registration_form.html')

def dashboardPage(request):
    
    return render(request ,'dashboard.html')

@csrf_exempt
def applyJob(request):
    if request.method =="POST":
        data =json.loads(request.body)
        # print(data)

        resume_url = data.get('candidate_resume_url')
        email = data.get('candidate_email')
        name = data.get('candidate_name')
        job_id = data.get('job_id')

        print(resume_url)
        print(email)
        print(name)

        job = Job.objects.filter(id=job_id)[0]

        application = Application(candidate_email = email, candidate_name = name, job_id=job, resume_url = resume_url)
        application.save()
        return JsonResponse({'success' : True})



