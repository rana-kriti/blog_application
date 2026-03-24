from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import Post

def user_login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')

        userr = authenticate(request, username=name, password=password)

        if userr is not None:
            auth_login(request, userr)
            return redirect('home')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})

    return render(request, 'blog/login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')

        # 🔴 check if user already exists
        if User.objects.filter(username=name).exists():
            return render(request, 'blog/signup.html', {
                'error': 'Username already exists'
            })

        # create user
        newUser = User.objects.create_user(
            username=name,
            email=email,
            password=password
        )
        newUser.save()

        return redirect('login')

    return render(request, 'blog/signup.html')


@login_required(login_url='login')
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def newpost(request):   
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        npost = Post(
            title=title,
            content=content,
            author=request.user
        )
        npost.save()

        return redirect('home')

    return render(request, 'blog/newpost.html')


def myposts(request):   
    context = {
        'posts': Post.objects.filter(author=request.user)
    }
    return render(request, 'blog/myposts.html', context)

def signout(request):
    logout(request)
    return redirect('/login')






