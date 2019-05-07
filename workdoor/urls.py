"""workdoor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from workapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('candidate', views.candidate, name='candidate'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('user_register', views.user_register, name='user_register'),
    path('company_register', views.company_register, name='company_register'),
    path('listing', views.listing, name='listing'),
    path('dashboard', views.user_dashboard, name='dashboard'),
    path('jobnoti', views.job_notification, name='jobnoti'),
    path('appliedjobs', views.applied_jobs, name='appliedjobs'),
    path('jobsearch', views.job_search, name='jobsearch'),
    path('resume', views.resume, name='resume'),
    path('editprofile', views.edit_profile, name='editprofile'),
    path('cdashboard', views.company_dashboard, name='cdashboard'),
    path('candisearch', views.candidate_search, name='candisearch'),
    path('selectcandi', views.select_candidate, name='selectcandi'),
    path('candinoti', views.candidate_notification, name='candinoti'),
    path('jobpost', views.job_post, name='jobpost'),
    path('questions', views.questions, name='questions'),
    


]
