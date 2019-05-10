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
    data1 = UserRegister.objects.all()
    if (request.method=='POST'):
        skills1 = request.POST.get('skills')
        location1 = request.POST.get('location')
        experience1 = request.POST.get('exp')
        if (skills1 and location1 and experience1):
            data = UserRegister.objects.filter(skills=skills1, location=location1, experience=experience1)
            print('1111111111111111111111111111111111')
            return render(request, 'candidate_listing.html', {'data':data})
        
        elif (skills1 and location1):
            data = UserRegister.objects.filter(skills=skills1, location=location1)
            print(data)
            print('22222222222222222222222222222222222')
            return render(request, 'candidate_listing.html', {'data':data})
        
        elif (skills):
            data = UserRegister.objects.filter(skills=skills1)
            print('333333333333333333333333333333333333')
            return render(request, 'candidate_listing.html', {'data':data})
        # else:
            # return render(request, 'candidate_listing.html', {'data':data})

    return render(request, 'candidate_listing.html', {'data1':data1})


def listing(request):
    data = JobPost.objects.all()
    return render(request, 'listing_right.html', {'data':data})


def company_dashboard(request):
    return render(request, 'companydashboard.html')


def candidate_search(request):
    data = UserRegister.objects.all()
    if (request.method=='POST'):
        skills1 = request.POST.get('skills')
        location1 = request.POST.get('location')
        experience1 = request.POST.get('exp')
        if (skills1 and location1 and experience1):
            data = UserRegister.objects.filter(skills=skills1, location=location1, experience=experience1)
            print('1111111111111111111111111111111111')
            return render(request, 'candisearch.html', {'data':data})
        
        elif (skills1 and location1):
            data = UserRegister.objects.filter(skills=skills1, location=location1)
            print(data)
            print('22222222222222222222222222222222222')
            return render(request, 'candisearch.html', {'data':data})
        
        elif (skills):
            data = UserRegister.objects.filter(skills=skills1)
            print('333333333333333333333333333333333333')
            return render(request, 'candisearch.html', {'data':data})
            
    return render(request, 'candisearch.html', {'data':data})


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
                # email = i.email
                print (i.email)
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
        user1 = authenticate(username=user_name, password=password)

        print(user1)

        if user1 is not None:
            login1(request, user1)

            if CompanyRegister.objects.filter(user=user1):
                print('000000000000000000000000000')
                return render(request, 'companydashboard.html', {'username': user_name})
            elif UserRegister.objects.filter(user=user1):
                print('11111111111111111111111111')
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
        job_skills = request.POST.get('job_skills')
        job_location = request.POST.get('job_location')
        todo = JobNotifications(name=name, email=email, job_skills=job_skills, job_location=job_location)
        todo.save()
        data = JobPost.objects.all()
        print(job_skills)
        # print(i.skills)
        for i in data:
            # print(i.skills)
            if job_skills == i.skills:
                print (i.skills)
                # email = i.email
                print(email)
                print(i.company_name)
                print("...................................................")
                connection = smtplib.SMTP('smtp.gmail.com',587)
                connection.ehlo()
                connection.starttls()
                connection.login('workdoorofficial@gmail.com','workdoor123')
                connection.sendmail('workdoorofficial@gmail.com', email,
                            ("Subject: Job_notification"+"\n\n"+"New Job Availbale \n"+ str(i.company_name)+"\n Package "+str(i.package)+"\n Location "+str(i.location)+"\n you can check it out on our website "))

        return render(request, 'dasboard.html')
    else:
        return render(request, 'jobnoti.html')


def job_search(request):
    data1 = JobPost.objects.all()

    if (request.method=='POST'):
        skills1 = request.POST.get('skills')
        location1 = request.POST.get('location')
        experience1 = request.POST.get('exp')
        if (skills1 and location1 and experience1):
            data = JobPost.objects.filter(skills=skills1, location=location1, experience=experience1)
            print('1111111111111111111111111111111111')
            return render(request, 'jobsearch.html', {'data':data})
        
        elif (skills1 and location1):
            data = JobPost.objects.filter(skills=skills1, location=location1)
            print(data)
            print('22222222222222222222222222222222222')
            return render(request, 'jobsearch.html', {'data':data})
        
        elif (skills):
            data = JobPost.objects.filter(skills=skills1)
            print('333333333333333333333333333333333333')
            return render(request, 'jobsearch.html', {'data':data})

    return render(request, 'jobsearch.html', {'data':data1})


def edit_profile(request):

    data  = UserRegister.objects.get(user=request.user.id)
    
    if (request.method =='POST'):
        id1 = request.POST.get('id')
        username = request.POST.get('user_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
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

        # user = User.objects.create_user(username, email, password)
        data1 = UserRegister(
            id=id1,
            user=user,
            first_name=first_name,
            last_name=last_name,
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
        data1.save()

    return render(request, 'editresume.html', {'data': data})


def resume(request):
    data = UserRegister.objects.get(user=request.user.id)
    return render(request, 'resume.html', {'data': data})


def user_register(request):
    if(request.method == 'POST'):
        username = request.POST.get('user_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
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
            first_name=first_name,
            last_name=last_name,
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


def editjob(request):
    data = JobPost.objects.all()
    return render(request, 'editjob.html', {'data':data})


