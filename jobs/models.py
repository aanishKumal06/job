from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  
    is_active = models.BooleanField(default=True)  
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    job_type = models.CharField(max_length=50, choices=[('Full-time', 'Full-time'), 
                                                        ('Part-time', 'Part-time'), 
                                                        ('Internship', 'Internship')], default='Full-time')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
