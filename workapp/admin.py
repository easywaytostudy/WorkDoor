# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Contact, CompanyRegister, UserRegister, JobNotifications, CandidateNotifications, JobPost, Appliedjobs, SelectCandidate

# Register your models here.
admin.site.register(Contact)
admin.site.register(UserRegister)
admin.site.register(CompanyRegister)
admin.site.register(JobNotifications)
admin.site.register(CandidateNotifications)
admin.site.register(JobPost)
admin.site.register(Appliedjobs)
admin.site.register(SelectCandidate)

 