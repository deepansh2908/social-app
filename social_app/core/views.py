from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from itertools import chain
import random

# this decorator will redirect to sign in page if not authenticated
@login_required(login_url='signin')
def index(request):
    profiles = Profile.objects.all()
    names = []
    for profile in profiles.all():
        names.append(profile.user.username)
    return render(request, 'index.html', {'names': names})

def signup(request):
    if request.method == 'POST':
        # these are all the names of input fields of the form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in 
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        # these are all the names of input fields of the form
        username = request.POST['username']
        password = request.POST['password']

        # this return a user object if auth else None
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signin')

    else:
        return render(request, 'signin.html')
    

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def settings(request):
    profiles = Profile.objects.all()
    allusers = []
    for profile in profiles.all():
        allusers.append(profile.user.username)
    print(allusers)
    return render(request, 'setting.html', {'allusers': allusers})

@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def send_friend_request(request, pk):
    pass
    # from_user = request.user
    # to_user = User.objects.get(username=pk)
    # created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)
    # if created:
    #     return HttpResponse('friend request sent successfully')
    # else:
    #     return HttpResponse('friend request failed')
    
@login_required(login_url='signin')
def accept_friend_request(request, requestId):
    pass
    # friend_request = Friend_Request.objects.get(id=requestId)
    # if (friend_request.to_user == request.user):
    #     friend_request.to_user.friends.add(friend_request.from_user)
    #     friend_request.from_user.friends.add(friend_request.to_user)
    #     friend_request.delete()
    #     return HttpResponse('friend request accepeted successfully')
    # else:
    #     return HttpResponse('friend request not accepted')

@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        
        # converts the list of list into a list (flattens the list)
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})