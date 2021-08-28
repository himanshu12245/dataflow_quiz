from django import forms
from .models import *
  
class IssueForm(forms.ModelForm):
  
    class Meta:
        model = issue
        fields = ['name', 'image', 'issue','gender']



class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['body', 'issue']        

      