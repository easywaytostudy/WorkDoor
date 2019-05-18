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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('candidate', views.candidate, name='candidate'),
    path('accounts/login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('user_register', views.user_register, name='user_register'),
    path('company_register', views.company_register, name='company_register'),
    path('listing', views.listing, name='listing'),

    path('/dashboard', views.user_dashboard, name='dashboard'),
    path('candidate/job_notification', views.job_notification, name='jobnoti'),
    path('candidate/applied_jobs', views.applied_jobs, name='appliedjobs'),
    path('candidate/jobsearch', views.job_search, name='jobsearch'),
    path('candidate/resume/<int:id>', views.resume1, name='resume'),
    path('candidate/edit_profile', views.edit_profile, name='editprofile'),

    path('company/dashboard', views.company_dashboard, name='cdashboard'),
    path('company/candidate_search', views.candidate_search, name='candisearch'),
    path('company/select_candidate', views.select_candidate, name='selectcandi'),
    path('company/candidate_notification', views.candidate_notification, name='candinoti'),
    path('company/job_post', views.job_post, name='jobpost'),
    path('company/interview_questions', views.questions, name='questions'),
    path('company/edit_job', views.editjob, name='editjob'),
    path('company/your_post', views.yourpost, name='yourpost'),
    path('apply_job/<str:job_id>', views.apply_job, name='apply_job'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
