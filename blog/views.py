from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pid):
    post = get_object_or_404(Post, pk=pid)
    return render(request, 'blog/post_detail.html', {'post':post})
    
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pid=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pid):
    post = get_object_or_404(Post, pk = pid)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pid = post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html', {'form':form})