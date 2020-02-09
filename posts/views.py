from django.contrib import messages, auth
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone

from .times import (
    years,
    months,
    days
)
from .models import Post
from .forms import PostCreateForm


def post_list(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
    if request.user.is_staff or request.user.is_superuser:
        qs_list = Post.objects.all()
    else:
        qs_list = Post.objects.active()
    paginator = Paginator(qs_list, 5)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    context = {
        'posts': qs,
        'paginator': paginator,
        'current': timezone.now()
    }
    return render(request, 'post_list.html', context)


def post_detail(request, post_slug):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
    instance = get_object_or_404(Post, slug=post_slug)
    if instance.draft:
        if not request.user.is_staff and not request.user.is_superuser:
            raise Http404
    context = {
        'post': instance
    }
    return render(request, 'post_detail.html', context)


def post_create(request):
    if not request.user.is_staff and not request.user.is_superuser:
        raise Http404
    form = PostCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        messages.success(request, "Post created successfully :)")
        return redirect('posts:post_detail', post_slug=instance.slug)
        messages.error(request, "Oops! An error occured :(")
    context = {
        'form': form,
        'years': years,
        'months': months,
        'days': days,
        'current': timezone.now()
    }
    return render(request, 'post_create.html', context)


def post_update(request, post_slug):
    instance = get_object_or_404(Post, slug=post_slug)
    if not request.user == instance.author and not request.user.is_superuser:
        raise Http404
    form = PostCreateForm(request.POST or None,
                          request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        if form.has_changed():
            instance.is_updated = True
            messages.success(request, "Post updated successfully :)")
        else:
            messages.info(request, "No changes applied :|")
        instance.save()
        return redirect('posts:post_detail', post_slug=instance.slug)
    context = {
        'form': form,
        'years': years,
        'months': months,
        'days': days
    }
    return render(request, 'post_update.html', context)


def post_delete(request, post_slug):
    instance = get_object_or_404(Post, slug=post_slug)
    if not request.user == instance.author and not request.user.is_superuser:
        raise Http404
    instance.delete()
    return redirect('posts:post_list')
