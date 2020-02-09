from django.shortcuts import render, redirect, Http404
from .forms import SignupForm
from django.contrib import auth, messages


def signup(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already a registered user :|')
        return redirect('posts:post_list')
    form = SignupForm()
    if request.method == 'POST':
        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('home')
        else:
            ex_form = form.cleaned_data
            context = {
                'form': form,
                'ex_form': ex_form
            }
    else:
        context = {
            'form': form
        }

    return render(request, 'signup_form.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('posts:post_list')
