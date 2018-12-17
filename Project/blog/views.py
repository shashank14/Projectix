from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


@login_required
def get_blog_posts(request):
    template_name = 'blog/blog_posts.html'
    object_list = Post.objects.all()
    paginator = Paginator(object_list,2)
    page_number = request.GET.get('page')
    context = {'object_list':object_list}


    try:
        obj_list = paginator.page(page_number)
    except PageNotAnInteger:
        obj_list = paginator.page(1)
    except EmptyPage:
        obj_list = paginator.page(paginator.num_pages)

    return render(request,template_name,context)

#def post_detail_view(request,year,month,day,post):
@login_required
def post_detail_view(request,id):
    obj = Post.objects.get(id=id)
    template_name = 'blog/post_detail.html'

    context={'obj':obj}
    return render(request,template_name,context)


@login_required
def post_detail_views(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year
                                )
    template_name = 'blog/post_detail.html'
    return render(request,template_name,{'post':post})


@login_required
def post_like_view(request):
    pass
