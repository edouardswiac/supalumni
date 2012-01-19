from django.views.generic.list_detail import object_list, object_detail
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.template import RequestContext
from .models import Post
from .forms import PostForm

post_queryset = Post.objects.all().order_by('-date_posted')

def post_list(request):
    return object_list(request, queryset=post_queryset)

def manage_posts(request):
    post_list = Post.objects.select_related().filter(author=request.user.get_profile().id_booster)
    return object_list(request, queryset=post_list)
   
def post_detail(request, post_id):
    return object_detail(request, queryset=post_queryset, 
                         object_id=post_id, template_object_name="post")

def post_create(request):    
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data['title']
            author = request.user.get_profile()
            category = form.cleaned_data['category']
            content = form.cleaned_data['content']
            post = Post(title=title,author=author,category=category,content=content)
            post.save()
            return redirect("board_post_list")
    else:
        form = PostForm()
    
    return render_to_response("board/post_form.html", {"form":form} , context_instance=RequestContext(request))

def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user.get_profile() != post.author:
        return HttpResponseForbidden()
        
    if request.method == "POST":
        form = PostForm(request.POST, post)
        
        if form.is_valid():
            author = request.user.get_profile()
            post.author = author
            form.save()
            return redirect("board_post_list")
    else:
        
        form = PostForm(instance=post)
    
    return render_to_response("board/post_form.html", {"form":form}, context_instance=RequestContext(request))

def post_delete(request, post_id):
    pass
    