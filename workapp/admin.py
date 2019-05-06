# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Contact, CompanyRegister, UserRegister, Jobnotification, Candidate_notification, Job_Post

# Register your models here.
admin.site.register(Contact)
admin.site.register(UserRegister)
admin.site.register(CompanyRegister)
admin.site.register(Jobnotification)
admin.site.register(Candidate_notification)

admin.site.register(Job_Post)

