from django import forms
from django.contrib.auth.models import User
from .models import Profile



class Phone(Profile):
    model = Profile
    fields = ('phone', 'dolgnost')
