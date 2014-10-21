from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog(request):
    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created')
    })


def post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)
    # grabs an object with pk if

    return render(request, 'post.html', {
        'post': post_obj
    })


def blog_tag(request, tag_name):
    return render(request, 'blog.html', {
        'posts': Post.objects.filter(tags__name=tag_name),
        'subheading': tag_name
    })


def blog_author(request, author_pk):
    posts = Post.objects.filter(author__pk=author_pk)
    return render(request, 'blog.html', {
        'posts': posts,
        'subheading': posts.author.name
    })