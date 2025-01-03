"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('registration/', views.registration, name='registration'),
    path('anketa/', views.anketa, name='anketa'),
    path('about/', views.about, name='about'),
    path('design/', views.design, name='design'),
     path('videopost/', views.videopost, name='videopost'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/', views.blogpost, name='blogpost'),
    path('blogpost/<int:paramentr>/', views.blogpost, name='blogpost'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('',views.anketa),
]
