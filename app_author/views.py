from .forms import ProfileForm
from .models import Profile
from django.db.models import Count
from app_forum.models import Forum, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def author_single_view(request, slug):
    """
    Render Single User
    :param request:
    :param slug:
    :return:
    """
    author = get_object_or_404(Profile, slug=slug)
    author_forum_list = Forum.objects.filter(forum_author=author.id).order_by("-is_created")[:10]
    author_comments = Comment.objects.filter(comment_author=author.id).order_by("-is_created")[:10]
    total_forums = Forum.objects.filter(forum_author=author.id).annotate(num_comments=Count('forum_author'))
    total_comments = Comment.objects.filter(comment_author=author.id).annotate(num_comments=Count('comment_author'))
    template = 'app_author/author_single.html'
    context = {
        'author': author,
        'author_forum_list': author_forum_list,
        'author_comments': author_comments,
        'total_forums': total_forums,
        'total_comments': total_comments
    }
    return render(request, template, context)


@login_required
def author_edit_view(request, slug):
    """
    Render User Edit Form
    :param request:
    :param slug:
    :return:
    """
    author = get_object_or_404(Profile, slug=slug)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author_single', slug=slug)
    elif request.user != author.user:
        return redirect('forum_list')
    else:
        form = ProfileForm(instance=author)
    return render(request, 'app_author/author_edit.html', {'author': author, 'form': form})
