from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from decouple import config

from website.apps.profiles.forms import SignUpForm, UpdateUserForm

@login_required
def index(request):
    if(request.user.profile.isOwner):
        return render(request, 'profile/businessprofile.html')
    else:
        return render(request, 'profile/profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Applies Profile fields
            user = form.save()
            user.refresh_from_db()
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
            #user.profile.bio = form.cleaned_data.get('bio')
            #Checks if they put in an owner key
            if form.cleaned_data.get('owner_key'):
                real_key = config('OWNER_KEY')
                attempted_key = form.cleaned_data.get('owner_key')
                # Set their profile as an owner if they have a correct key
                if real_key == attempted_key:
                    user.profile.isOwner = True
            # Either Create and add, or just add that owner to the owners group
            if user.profile.isOwner:
                try:
                    owners_group = Group.objects.get(name='owners')
                    user.groups.add(owners_group)
                except Group.DoesNotExist:
                    owners_group = Group(name='owners')
                    owners_group.save()
                    user.groups.add(owners_group)

            #user.profile.profile_image = form.cleaned_data.get('profile_image')
            user.save()

            # User requirements
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=raw_password)

            # Redirect home, new User is logged in
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_user(request):
    logout(request)
    return render(request, 'profile/logout.html')

@login_required
def update_user(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            user.refresh_from_db()

            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()

            return redirect('profile')
    else:
        form = UpdateUserForm(instance=request.user.profile)
    return render(request, 'profile/updateprofile.html', {'form':form})
