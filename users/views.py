from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

from .models import CustomUser as User, Account
from .forms import SignUpForm, AccountSignUpForm, EditprofileForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'account/user-signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = EditprofileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditprofileForm(instance=request.user)
    return render(request, 'account/my-profile.html', {'form':form})
   

@login_required
def updateaccount(request, username):
    profile = get_object_or_404(User, username=username)
    try:
        account = get_object_or_404(Account, profile=profile)
        if request.method == 'POST':
            form = AccountSignUpForm(request.POST, instance=account)
            if form.is_valid():
                commit = form.save(commit =False)
                commit.profile = profile
                form.save()
            else:
                form = AccountSignUpForm()
            return JsonResponse(form)
    except:
        account = Account.objects.create(
            profile=profile,
            yourTitle =  request.POST.get('yourTitle'),
            address =  request.POST.get('address'),
            city =  request.POST.get('city'),
            state =  request.POST.get('state'),
            zipcode =  request.POST.get('zipcode'),
            about =  request.POST.get('about'),
            facebook =  request.POST.get('facebook'),
            twitter =  request.POST.get('twitter'),
            googlePlus =  request.POST.get('googlePlus'),
            linkedIn =  request.POST.get('linkedIn'),
        )
        account.save()
        return HttpResponse('')
    return JsonResponse({'post':'false'})
