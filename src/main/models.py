from django.db import models
from django.contrib.auth.models import User


# Respondent model

class Respondent(models.Model):
    user_id = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    email   = models.EmailField(max_length=100, unique=True)
    
    
# Form model

THEMES = (
            ('t1','theme1'),
            ('t2','theme2'),
            ('t3','theme3'),
        )

class Form(models.Model):
    name = models.CharField(max_length=100)
    description  = models.TextField(blank=True, null=True)
    created_att  = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active    = models.BooleanField(default=True)
    theme         = models.CharField(max_length=7,
                                    choices=THEMES,
                                    default="t1"
                                    )


#faild model

TYPES = (
            ('text','text'),
            ('number','number'),
            ('email','email'),
            ('date','date'),
            ('time','time'),
            ('datetime-local','datetime-local'),
            ('color','color'),
            ('range','range'),
            ('tel','tel'),
            ('url','url'),
            ('password','password'),
            ('checkbox','checkbox'),
            ('radio','radio'),
            ('select','select'),
            ('textarea','textarea'),
        )

class Field(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type       = models.CharField(max_length=7,
                                    choices=THEMES,
                                    default="text"
                                )       
    is_required = models.BooleanField(default=False)
    order = models.IntegerField()
    


# options model From radoi and select field

class Option(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
