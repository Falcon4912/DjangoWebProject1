"""
Definition of models.
"""
from django.contrib.auth.models import User

from collections import UserDict
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse



class Blog(models.Model):
   
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Heading")
    description = models.TextField(verbose_name =  "Summary")
    content = models.TextField(verbose_name ="Full content")
    posted =models.DateTimeField(default = datetime.now, db_index = True, verbose_name="To publish")
    
    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])
    def __str__(self):
        return self.title
    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "blog article"
        verbose_name_plural = "article"
    
    
admin.site.register( Blog ) 


   
    

    