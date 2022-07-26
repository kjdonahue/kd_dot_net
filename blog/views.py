from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.
def blog(request):
    posts = Post.published.all()
    
    paginator = Paginator(posts, 5) # 5 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # not a valid page? give em the first
        posts = paginator.page(1)
    except EmptyPage:
        # out of range? give em the last
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/blog.html', {
        'posts': posts,
        'pages': page,
        "content_style": "blog has-background",
        "nav_type": "thin"
    })

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'nav_type': 'thin',
        'content_style': 'post-detail has-background'
    })