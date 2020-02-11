from django.contrib import messages, auth
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostCreateForm
from .models import Post
from .utils import (
    years,
    months,
    days,
)


def post_list(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            messages.error(request, 'Username or Password is incorrect :x')
            return redirect('posts:post_list')
    if request.user.is_staff or request.user.is_superuser:
        qs_list = Post.objects.all()
    else:
        qs_list = Post.objects.active()
    q = request.GET.get('q')
    if q:
        qs_list = qs_list.filter(
            Q(title__icontains=q) |
            Q(author__username__icontains=q) |
            Q(content__icontains=q)
        ).distinct()
    paginator = Paginator(qs_list, 5)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    context = {
        'posts': qs,
        'paginator': paginator,
        'current': timezone.now()
    }
    return render(request, 'post_list.html', context)


def user_post_list(request, author):
    if request.user.username == author or request.user.is_superuser:
        qs_list = Post.objects.filter(author__username=author)
    else:
        qs_list = Post.objects.active().filter(author__username=author)
    paginator = Paginator(qs_list, 5)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    context = {
        'posts': qs,
        'user_post': author,
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
        'post': instance,
        'form': form,
        'years': years,
        'months': months,
        'days': days
    }
    return render(request, 'post_update.html', context)


def post_delete(request, post_slug):
    instance = get_object_or_404(Post, slug=post_slug)
    if not request.user == instance.author and not request.user.is_superuser:
        raise PermissionDenied
    instance.delete()
    return redirect('posts:post_list')
