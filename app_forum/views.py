from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from app_author.models import Profile
from .forms import ThreadForm, CommentForm
from .models import Forum, Comment


def forum_list_view(request):
    """
    Render All Threads List
    :param request:
    :return:
    """
    forum_list = Forum.objects.filter(is_hot=False).order_by("-is_modified")
    forum_list_sticky = Forum.objects.filter(is_hot=True).order_by("-is_created")[:1]
    template = 'app_forum/main/forum_list.html'
    paginator = Paginator(forum_list, 10)
    page = request.GET.get('page', 1)
    try:
        forum_list = paginator.page(page)
    except PageNotAnInteger:
        forum_list = paginator.page(1)
    except EmptyPage:
        forum_list = paginator.page(paginator.num_pages)
    context = {'forum_list': forum_list, 'forum_list_sticky': forum_list_sticky}
    return render(request, template, context)


def forum_single_view(request, pk):
    """
    Render Single Thread, Comments and Comment Form
    :param request:
    :param pk:
    :return:
    """
    try:
        forum = Forum.objects.get(pk=pk)
    except Forum.DoesNotExist:
        return redirect('forum:forum_list')
    forum_comments = Comment.objects.filter(forum=forum.id)
    form = CommentForm()
    template = 'app_forum/main/forum_single.html'
    context = {'forum': forum, 'forum_comments': forum_comments, 'form': form}
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_author = Profile.objects.get(user=request.user)
            comment.created_date = datetime.now()
            comment.forum = forum
            comment.save()
            return redirect('forum:forum_single', pk=forum.pk)
    else:
        return render(request, template, context)


@login_required
def forum_new_view(request):
    """
    Render New Thread Form
    :param request:
    :return:
    """
    template = 'app_forum/main/forum_new.html'
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.forum_author = Profile.objects.get(user=request.user)
            thread.misc_created = datetime.now()
            thread.save()
            return redirect('forum:forum_list')
    else:
        form = ThreadForm()
    context = {'form': form}
    return render(request, template, context)


@login_required
def forum_edit_view(request, pk):
    """
    Render Edit Form
    :param request:
    :param pk:
    :return:
    """
    try:
        forum = Forum.objects.get(pk=pk)
    except Forum.DoesNotExist:
        return redirect('forum:forum_list')
    template = 'app_forum/main/forum_edit.html'
    if request.method == "POST":
        form = ThreadForm(request.POST, instance=forum)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.forum_author = Profile.objects.get(user=request.user)
            forum.is_created = timezone.now()
            forum.save()
            return redirect('forum:forum_single', pk=forum.pk)
    elif request.user != forum.forum_author.user:
        raise PermissionDenied
    else:
        form = ThreadForm(instance=forum)
    context = {'forum': forum, 'form': form}
    return render(request, template, context)


@login_required
def forum_comment_edit_view(request, pk, id):
    """
    Render Edit Comment Form
    :param request:
    :param pk:
    :param id:
    :return:
    """
    try:
        forum = get_object_or_404(Forum, pk=pk)
        comment = get_object_or_404(Comment, id=id)
    except (Forum.DoesNotExist, Comment.DoesNotExist):
        return redirect('forum:forum_list')
    template = 'app_forum/main/forum_comment_edit.html'
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_author = Profile.objects.get(user=request.user)
            comment.created_date = datetime.now()
            comment.forum = forum
            comment.save()
            return redirect('forum:forum_single', pk=forum.pk)
    elif request.user != comment.comment_author.user:
        raise PermissionDenied
    else:
        form = CommentForm(instance=comment)
    context = {'forum': forum, 'comment': comment, 'form': form}
    return render(request, template, context)
