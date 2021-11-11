from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, PostComment
from django.db.models import Q
from .forms import PostForm, PostCommentForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect

class AddLike(View):
    def post(self, request, id, *args, **kwargs):
        post = Post.objects.get(pk=id)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break


        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddDislike(View):
    def post(self, request, id, *args, **kwargs):
        post = Post.objects.get(pk=id)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break


        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

def home(request):
    # For Post objects
    posts = Post.objects.all()[:11]
    # For Category objects
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
    }

    return render(request, 'home.html', context)

@login_required(login_url='login')
def addpost(request):
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            new_post = postform.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('addpost')
        else:
            raise ValueError('Somethink went wrong')
    else:
        postform = PostForm()

    context = {
        'postform': postform,
    }
    return render(request, 'postform.html', context)




def post(request, url):
    post = Post.objects.get(url=url)

    cats = Category.objects.all()
    context = {
        'post': post,
        'cats': cats
    }

    return render(request, 'post.html', context)


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)

    context = {
        'cat': cat,
        'posts': posts,
    }
    return render(request, 'category.html', context)

@login_required(login_url='login')
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            posts = Post.objects.filter(Q(url__icontains=keyword) | Q(title__icontains=keyword))
    context = {
        'posts': posts,
    }

    return render(request, 'search.html', context)


@login_required(login_url='login')
def delete(request, id):
    if request.method == 'POST':
        dl = Post.objects.get(pk=id)
        dl.delete()
        return redirect('home')

@login_required(login_url='login')
def update_post(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        post_form = PostForm(request.POST, instance=pi)
        if post_form.is_valid():
            post_form.save()
    else:
        pi = Post.objects.get(pk=id)
        post_form = PostForm(instance=pi)
    context = {
        'post_form': post_form,
    }
    return render(request, 'updatepost.html', context)


def add_comment(request, id):
    post = Post.objects.get(pk=id)
    try:
        form = PostCommentForm()
        if request.method == 'POST':
            form = PostCommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.post = post
                new_comment.save()
                form = PostCommentForm()
    except Exception as e:
        return e

    comments = PostComment.objects.filter(post=post)
    comments_count = comments.count()
    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'comments_count': comments_count,
    }
    return render(request, 'comment.html', context)
