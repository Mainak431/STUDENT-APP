from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from .models import Post,marks,Subwise_marks,Course,department,faculty
from django.utils import timezone
from django.contrib.auth import logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import Group,User
from django.urls import reverse
from django.db.models import Q
from .forms import MarksForm


def home(request):
    users_in_group = Group.objects.get(name="FACULTY").user_set.all()
    if request.user in users_in_group:
        return redirect('accounts/profile')
    student_details = Course.objects.all()
    return render(request,'student\home.html',{'d':student_details})


def updatemarks(request):
    users_in_group = Group.objects.get(name="Student").user_set.all()
    if request.user not in users_in_group:
        enroll = request.user.username
        di = Course.objects.filter(Instructor=enroll)
        d = Subwise_marks.objects.filter(C_ID__in=di)
        form = MarksForm(request.POST)
        if request.method == "POST" and form.is_valid():
        #obj = Subwise_marks.objects.get(C_ID='IAAP',EnrollmentID='iro2017009');
            form.save()
            return render(request, 'accounts\profile\studentmarks.html', { 'di':di,'did':d,'form':form})
        else:
            error="empty fields"
            return render(request,'accounts\profile\studentmarks.html',{'error':error,'did':d,'form':form})
    else:
        return render(request, 'accounts\profile\permissiondenied.html', {})


def logout_i(request):
    logout(request)
    return render(request,'accounts\profile\logged_out.html',{})


@login_required()
def courses(request):
    users_in_group=Group.objects.get(name="Student").user_set.all()
    if request.user in users_in_group:
        enroll = request.user.username
        d=Subwise_marks.objects.filter(EnrollmentID=enroll)
        return render(request,'accounts\profile\studentcourses.html',{'d':d})
    else:
        enroll = request.user.username
        d = Course.objects.filter(Instructor=enroll)
        return render(request,'accounts\profile\cultycourses.html',{'d':d})


@login_required()
def studmarks(request):
    users_in_group=Group.objects.get(name="Student").user_set.all()
    if request.user in users_in_group:
        enroll = request.user.username
        d= marks.objects.filter(EnrollmentID=enroll)
        return render(request,'accounts\profile\marks.html',{'did':d})
    else:
        return render(request,'accounts\profile\permissiondenied.html',{})


@login_required()
def profile(request):
    users_in_group = Group.objects.get(name="Student").user_set.all()
    if request.user in users_in_group:
        d = Post.objects.all()[0]
        details = d
        for d in Post.objects.all():
            if (d.EnrollmentID == request.user.username):
                details = d
        return render(request,'accounts\profile\studentprofile.html',{'details':details})

    users_in_group = Group.objects.get(name="FACULTY").user_set.all()
    if request.user in users_in_group:
        d = faculty.objects.all()[0]
        details = d
        for d in faculty.objects.all():
            if (d.Name == request.user.username):
                details = d
        return render(request, 'accounts\profile\cultyprofile.html', {'di': details})

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            logout(request)
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts\profile\change_password.html', {'form': form })
