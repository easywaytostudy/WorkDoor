# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.TextField(null=True)
    subject = models.TextField(max_length=200, null=True)
    message = models.TextField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "contact"
        verbose_name = "Contact"


class UserRegister(models.Model):
    user = models.OneToOneField(User, on_delete=True)
    fathername = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    gender = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    qualification = models.CharField(max_length=200, null=True)
    experience = models.CharField(max_length=100, null=True)
    skills = models.CharField(max_length=100, null=True)
    certification = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=200, null=True)
    photo  = models.FileField(upload_to='image/userphoto', null=True, blank=True, help_text="Upload only .png, .jpg & .jpeg image extension.") 
    resume = models.FileField(upload_to='image/userresume', null=True, blank=True, help_text="Upload only .txt, .pdf & .word file extension.")

    def __unicode__(self):
        return self.user_name

    class Meta:
        db_table = "user_registration"
        verbose_name = "User Registration"


class CompanyRegister(models.Model):
    user = models.OneToOneField(User, on_delete=True)
    company_name = models.CharField(max_length=200, null=True)
    jobpost = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    website = models.CharField(max_length=200, null=True)
    address= models.TextField(max_length=200, null=True)

    def __unicode__(self):
        return self.company_name

    class Meta:
        db_table = "company_registration"
        verbose_name = "Company Registration"



class Jobnotification(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.TextField(null=True)
    job_skills = models.TextField(max_length=200, null=True)
    job_location = models.TextField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "Job_notification"
        verbose_name = "Job notification"

class Candidate_notification(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    candidate_skills = models.CharField(max_length=200, null=True)
    candidate_location = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "Candidate_notification"
        verbose_name = "Candidate notification"


class Job_Post(models.Model):
    company_name = models.CharField(max_length=200, null=True)
    post_name = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=200, null=True)
    package = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    skills = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.company_name

    class Meta:
        db_table = "Job_Post"
        verbose_name = "Job Post"

