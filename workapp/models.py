# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "contact"
        verbose_name = "Contact"


class UserRegister(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    fathername = models.CharField(max_length=100, null=True)
    date = models.DateField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    gender = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    qualification = models.CharField(max_length=200, null=True)
    experience = models.CharField(max_length=100, null=True)
    skills = models.CharField(max_length=100, null=True)
    certification = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=200, null=True)
    photo  = models.ImageField(upload_to='image/userphoto/', null=True, blank=False)
    resume = models.FileField(upload_to='image/userresume/', null=True, blank=False)

    def __unicode__(self):
        return self.first_name

    class Meta:
        db_table = "user_registration"
        verbose_name = "User Registration"


class CompanyRegister(models.Model):
    id = models.AutoField(primary_key=True)
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


class JobNotifications(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    job_skills = models.CharField(max_length=200, null=True)
    job_location = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "Job_notification"
        verbose_name = "Job notification"


class CandidateNotifications(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    candidate_skills = models.CharField(max_length=200, null=True)
    candidate_location = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "Candidate_notification"
        verbose_name = "Candidate notification"


class JobPost(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200, null=True)
    post_name = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=200, null=True)
    package = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    skills = models.CharField(max_length=200, null=True)
    registered = models.CharField(max_length=100, null=True, default="False")

    def __unicode__(self):
        return self.company_name

    class Meta:
        db_table = "Job_Post"
        verbose_name = "Job Post"

class Appliedjobs(models.Model):
    job_id = models.OneToOneField(JobPost, on_delete=True)
    candidate_id = models.OneToOneField(User, on_delete=True)

    def __unicode__(self):
        return self.job_id

    class Meta:
        db_table = "Applied_Jobs"
        verbose_name = "Applied Jobs"


class SelectCandidate(models.Model):
    user_id = models.OneToOneField(UserRegister, on_delete=True)
    company_id = models.OneToOneField(CompanyRegister, on_delete=True)

    def __unicode__(self):
        return self.candidate_id

    class Meta:
        db_table = "Selected_Candidate"
        verbose_name = "Selected Candidate"

