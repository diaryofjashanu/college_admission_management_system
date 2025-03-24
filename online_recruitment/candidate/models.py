from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    name = models.CharField( max_length=255)
    place = models.CharField( max_length=255)
    type = models.CharField( max_length=255)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    salary = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.id} {self.name}'
    

class Application(models.Model):
    application_status = [
        ('P' , 'pending'),
        {'A', 'accepted'}, 
        ('D', 'decline'),
    ]
    job_id = models.ForeignKey("candidate.Job",  on_delete=models.CASCADE)
    candidate_name = models.CharField( max_length=255)
    candidate_email = models.EmailField( max_length=255)
    resume_url = models.URLField( max_length=2000)
    status = models.CharField(max_length=10, choices=application_status, default='P')

    def __str__(self):
        return self.candidate_name
    
