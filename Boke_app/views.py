from django.shortcuts import render
from .models import Post, Enjoy


# Create your views here.


def index(request):
    repost_list = Post.objects.filter(is_recomment=True)

    post_list = Post.objects.order_by('-pub_date')

    for post in repost_list:
        post.title = post.title

    enjoy_list = Enjoy.objects.all()

    zbc = {
        'repost_list': repost_list,
        'post_list': post_list,
        'enjoy_list': enjoy_list,
    }

    return render(request, 'index.html', zbc)
