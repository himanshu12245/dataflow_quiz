from django.db.models.fields import PositiveBigIntegerField
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView , CreateView , UpdateView
from django.core.mail import send_mail
import csv
# Create your views here.

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['name','gender','issue','image'])

    for iss in issue.objects.all().values_list('name','gender','issue','image'):
        writer.writerow(iss)
    response['content-Disposition'] = 'attachment; filename="issue.csv"'
    return response    

def set_main(request):
    context={}
    return render(request,'.html',context)

def set_issue(request):
    context={}
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        image = issue.objects.create(image=request.POST.get('image'),name=request.POST.get('name'),gender=request.POST.get('gender'),issue=request.POST.get('issue'))
        if form.is_valid():
        #     send_mail(
        #     'issue raised',
        #     'your issue has been submitted',
        #     ['himanshu12245@gmail.com'],
        #     #You can add your email here to get the mail
        #     ['dataflow@gmail.com'],
        # )
            form.save()
            # return redirect('success')
        form = IssueForm()    
        # return render(request,'home.html',{'form' : form})
        redirect('home.html')
    form = IssueForm()
    return render(request,'issue.html',{'form' : form})   
  
class HomeView(ListView):
    model = issue
    template_name = 'home.html'

class AddCommentView(CreateView):
    model = comment
    template_name = "add_comment.html"
    # fields = '__all__'    

class Updateissue(UpdateView):
    model = issue
    template_name = 'edit.html'
    fields = ['name','gender','issue']
