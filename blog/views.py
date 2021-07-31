from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context={'blogs':BlogModel.objects.all()}
    return render(request, 'home.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

@login_required
def see_blog(request):
    context={}
    try:
        blog_objs=BlogModel.objects.filter(user=request.user)
        context['blog_objs']=blog_objs
    except Exception as e:
        print(e)
    print(context)
    return render(request, 'see_block.html',context)

@login_required
def blog_detail(request,slug):
    context={}
    try:
        blog_obj=BlogModel.objects.filter(slug=slug).first()
        context['blog_obj']=blog_obj
    except Exception as e:
        print(e)

    return render(request, 'blog_detail.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def detail(request):
    return render(request, 'detail.html')


@login_required
def update_blog(request, slug):
    context={}
    try:
        blog_obj=BlogModel.objects.get(slug=slug)

        if blog_obj.user!=request.user:
            return redirect('/')
        
        initial_dict={'content':blog_obj.content}
        form=BlogForm(initial=initial_dict)
        if request.method=="POST":
            form=BlogForm(request.POST)
            image=request.FILES.get('image',None)
            title=request.POST.get('title')
            user=request.user
            print(user)
            if form.is_valid():
                content=form.cleaned_data['content']

            BlogModel.objects.update(
                user=user, title=title, 
                content=content, image=image
            )

        context['blog_obj']=blog_obj
        context['form']=form
    except Exception as e:
        print(e)
    return render(request,'update_blog.html',context)


@login_required
def delete_blog(request, id):
    try:
        blog_obj=BlogModel.objects.get(id=id)
        if blog_obj.user==request.user:
            blog_obj.delete()
    
    except Exception as e:
        print(e)
    return redirect('/see_blog')



@login_required
def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method=="POST":
            print("post")
            form=BlogForm(request.POST)
            print(form)
            image=request.FILES.get('image',None)
            print("image")
            title=request.POST.get('title')
            user=request.user
            print(user)
            if form.is_valid():
                content=form.cleaned_data['content']

            BlogModel.objects.create(
                user=user, title=title, 
                content=content, image=image
            )
            print(BlogModel)
            
            return redirect('add_blog')

    except Exception as e:
        print(e)

    return render(request, 'add_blog.html',context)