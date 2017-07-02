from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pid):
    post = get_object_or_404(Post, pk=pid)
    return render(request, 'blog/post_detail.html', {'post':post})
    