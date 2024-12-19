"""
Definition of views.
"""

from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpRequest 
from django import forms
from .forms import AnketaForm  


from django.db import models
from .models import Blog



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Man' , '2': 'Femaile'}
    internet={'1': 'Every day', '2': 'Every',
              '3': 'Every day several', '4': 'Every several'
               }
    if request.method == 'POST':
        form=AnketaForm(request.POST)
        if form.is_valid():
           data=dict() 
           data['name']=form.cleaned_data['name']
           data['city']=form.cleaned_data['city']
           data['job']=form.cleaned_data['job']
           data['gender']=gender[form.cleaned_data['gender']]
           data['internet']=internet[form.cleaned_data['internet']]
           if (form.cleaned_data['notice']==True):
               data['notice']='Yes'
           else:
               data['notice']='No'
               data['email']=form.cleaned_data['email']
               data['message']=form.cleaned_data['message']
               form = None
    else:
            form=AnketaForm()
    return render(request,
                  'app/anketa.html',
                  {
                           'form':form,
                           'data':data
                  }
    )
def registration(request):
    """Renders the registration page."""
    
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()
            return redirect('home')
    else:
            regform = UserCreationForm()
            assert isinstance(request, HttpRequest)
            return render (
                request, 'app/registrator.html',
                {
                    'regform': regform,
                    'year':datetime.now().year,
                    }
                )
def blogpost(request, parametr):
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr) 

    return render(request, 'app/blogpost.html',
                  {
                     'post_1': post_1,
                     'year': datetime.now().year,
                      
                  }
                  
    )

def design(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/design.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def videopost(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def blog(request):
    
    posts =Blog.objects.all()
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Blog',
            'posts':posts,
            'year': datetime.now().year,
            
            
        }
        
     )
                
