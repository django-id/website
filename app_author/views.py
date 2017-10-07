from .models import Profile
from .forms import ProfileForm
from app_forum.models import Forum, Comment
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def author_single_view(request, slug):
    """
    Render Single User
    :param request:
    :param slug:
    :return:
    """
    author = get_object_or_404(Profile, slug=slug)
    author_forum_list = Forum.objects.filter(forum_author=author.id).order_by("-is_created")
    author_comments = Comment.objects.filter(comment_author=author.id).order_by("-is_created")
    paginator = Paginator(author_comments, 3)
    page = request.GET.get('page', 1)
    try:
        author_comments = paginator.page(page)
    except PageNotAnInteger:
        author_comments = paginator.page(1)
    except EmptyPage:
        author_comments = paginator.page(paginator.num_pages)
    template = 'app_author/author_single.html'
    context = {'author': author, 'author_forum_list': author_forum_list, 'author_comments': author_comments}
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
