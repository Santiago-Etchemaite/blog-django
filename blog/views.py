from django.shortcuts import get_object_or_404, render

from .models import Post


def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})