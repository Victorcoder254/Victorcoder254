from django.shortcuts import render, redirect

from .models import Post

from .forms import CommentForm


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'tech/frontpage.html', {'posts': posts})


def detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

        return redirect('detail', slug=post.slug)

    else:
        form = CommentForm

    return render(request, 'tech/detail.html', {'post': post, 'form': form})
