from django.db import models


# Create your models here.
GENDER_CHOICES = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('others','OTHERS'),
)

class issue(models.Model): 
    name =  models.CharField(max_length=20)
    gender= models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    issue =  models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',null=True, blank=True, )   

    

class comment(models.Model):
    issue = models.ForeignKey(issue,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.issue.name, self.name)
    