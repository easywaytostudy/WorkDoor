# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Contact , CompanyRegister, UserRegister, JobNotifications, CandidateNotifications, JobPost
from django.contrib.auth import authenticate, login as login1, logout as logout1
from django.contrib.auth.models import User
import smtplib, ssl
from django.contrib import messages

# Create your views here.
def home(request):
    data = JobPost.objects.all()
    return render(request, 'index.html', {'data':data})


def about(request):
    return render(request, 'about.html')


def candidate(request):
    return render(request, 'candidate_listing.html')


def listing(request):
    return render(request, 'listing_right.html')


def company_dashboard(request):
    return render(request, 'companydashboard.html')


def candidate_search(request):
    return render(request, 'candisearch.html')


def select_candidate(request):
    return render(request, 'selectcandi.html')


def candidate_notification(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        candidate_skills = request.POST.get('candidate_skills')
        candidate_location = request.POST.get('candidate_location')
        todo = CandidateNotifications(name=name, email=email, candidate_skills=candidate_skills, candidate_location=candidate_location)
        todo.save()
        data = UserRegister.objects.all()
        for i in data:
            if candidate_skills == i.skills :
                print (i.skills)
                email = i.email
                print (email)
                print(request.user.username)
                print("...................................................")

                # connection = smtplib.SMTP('smtp.gmail.com',587)
                # connection.ehlo()
                # connection.starttls()
                # connection.login('workdoorofficial@gmail.com','workdoor123')
                # connection.sendmail('workdoorofficial@gmail.com', email,
                #             ("Subject: Candidate_notification"+"\n\n"+"New Candiate Availbale "+ str(user)+" you can check it out on our website "))

                # messages.add_message(request, messages.INFO, 'Thank you for using notification service. You will be notified soon.')

        return render(request, 'companydashboard.html')
    else:
        return render(request, 'candinoti.html')

def job_post(request):
    if(request.method == 'POST'):
        company_name = request.POST.get('company_name')
        post_name = request.POST.get('post_name')
        experience = request.POST.get('experience')
        package = request.POST.get('package')
        location = request.POST.get('location')
        skills = request.POST.get('skills')
        todo = JobPost(company_name=company_name, post_name=post_name, experience=experience, package=package, location=location, skills=skills)
        todo.save()

        return render(request, 'companydashboard.html')
    else:
        return render(request, 'jobpost.html')


def login(request):
    if (request.method == 'POST'):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        print(user)

        if user is not None:
            login1(request, user)
            return render(request, 'dasboard.html', {'username': user_name})
    else:
        return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def user_dashboard(request):
    return render(request, 'dasboard.html')


def applied_jobs(request):
    return render(request, 'appliedjobs.html')


def job_notification(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        job_skills = request.POST.get('skills')
        job_location = request.POST.get('joblocation')
        todo = JobNotifications(name=name, email=email, job_skills=job_skills, job_location=job_location)
        todo.save()
        data = JobPost.objects.all()
        print(job_skills)
        # print(i.skills)
        for i in data:
            print(i.skills)
            if job_skills == i.skills:
                print (i.skills)
                email = i.email
                print (email)
                print(request.JobPost.company_name)
                print("...................................................")
                # connection = smtplib.SMTP('smtp.gmail.com',587)
                # connection.ehlo()
                # connection.starttls()
                # connection.login('workdoorofficial@gmail.com','workdoor123')
                # connection.sendmail('workdoorofficial@gmail.com', email,
                #             ("Subject: Job_notification"+"\n\n"+"New Job Availbale \n"+ str(company_name)+"\n Package "+str(package)+"\n Location "+str(location)+"\n you can check it out on our website "))

        return render(request, 'dasboard.html')
    else:
        return render(request, 'jobnoti.html')


def job_search(request):
    return render(request, 'jobsearch.html')


def edit_profile(request):
    data = UserRegister.objects.get(user=request.user.id)
    id1 = request.POST.get('id')
    username = request.POST.get('user_name')
    fathername = request.POST.get('fathername')
    email = request.POST.get('email')
    password = request.POST.get('password')
    date = request.POST.get('date')
    location = request.POST.get('location')
    zipcode = request.POST.get('zipcode')
    gender = request.POST.get('gender')
    phone = request.POST.get('phone')
    qualification = request.POST.get('qualification')
    experience = request.POST.get('experience')
    skills = request.POST.get('skills')
    certification = request.POST.get('certification')
    language = request.POST.get('language')
    photo = request.POST.get('photo')
    resume = request.POST.get('resume')

    user1 = User.objects.create_user(username, email, password)

    data = UserRegister(
        id=id1,
        user1=user1,
        fathername=fathername,
        date=date,
        location=location,
        zipcode=zipcode,
        gender=gender,
        phone=phone,
        qualification=qualification,
        experience=experience,
        skills=skills,
        certification=certification,
        language=language,
        photo=photo,
        resume=resume

    )
    data.save()


    return render(request, 'editresume.html', {'data': data})


def resume(request):
    data = UserRegister.objects.get(user=request.user.id)
    return render(request, 'resume.html', {'data': data})


def user_register(request):
    if(request.method == 'POST'):
        username = request.POST.get('user_name')
        fathername = request.POST.get('fathername')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date = request.POST.get('date')
        location = request.POST.get('location')
        zipcode = request.POST.get('zipcode')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        certification = request.POST.get('certification')
        language = request.POST.get('language')
        photo = request.POST.get('photo')
        resume = request.POST.get('resume')

        user = User.objects.create_user(username, email, password)

        data = UserRegister(
            user=user,
            fathername=fathername,
            date=date,
            location=location,
            zipcode=zipcode,
            gender=gender,
            phone=phone,
            qualification=qualification,
            experience=experience,
            skills=skills,
            certification=certification,
            language=language,
            photo=photo,
            resume=resume

        )
        data.save()
        connection = smtplib.SMTP('smtp.gmail.com',587)
        connection.ehlo()
        connection.starttls()
        connection.login('workdoorofficial@gmail.com','workdoor123')
        connection.sendmail('workdoorofficial@gmail.com', email,
                            ("Subject: Registered Sucessfull"+"\n\n"+"Thank you "+ str(username)+" for registering in WorkDoor "))

        return render(request, 'login.html')
    else:
        return render(request, 'register.html')


def company_register(request):
    if(request.method == 'POST'):
        username  = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        company_name = request.POST.get('company_name')
        jobpost = request.POST.get('jobpost')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        address = request.POST.get('address')

        user = User.objects.create_user(username, email, password)
        data = CompanyRegister(
            user=user,
            company_name=company_name,
            jobpost=jobpost,
            phone=phone,
            website=website,
            address=address
        )
        data.save()
        connection = smtplib.SMTP('smtp.gmail.com',587)
        connection.ehlo()
        connection.starttls()
        connection.login('workdoorofficial@gmail.com','workdoor123')
        connection.sendmail('workdoorofficial@gmail.com',email,
                            ("Subject: Registered Sucessfull"+"\n\n"+"Thank you "+str(username)+" for registering in WorkDoor "))

        return render(request, 'login.html')
    else:
        return render(request, 'register.html')


def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        todo = Contact(name=name, email=email, subject=subject, message=message)
        todo.save()
        connection = smtplib.SMTP('smtp.gmail.com',587)
        connection.ehlo()
        connection.starttls()
        connection.login('workdoorofficial@gmail.com','workdoor123')
        connection.sendmail('workdoorofficial@gmail.com',email,
                            ("Subject: "+str(subject)+"\n\n"+"Hello "+str(name)+"\n Your email address:- "+str(email)+"\n Thank You for sending message \n"+str(message)))
        connection.sendmail('workdoorofficial@gmail.com','workdoorofficial@gmail.com',
                            ("Subject: "+str(subject)+"\n\n"+"Name of the sender :- "+str(name)+"\n email address:- "+str(email)+"\n Message:- \n"+str(message)))
        connection.quit()
        return redirect('/')
    else:
        return render(request, 'contact.html')


def logout(request):
    logout1(request)
    return redirect('login')


def questions(request):
    return render(request, 'questions.html')
