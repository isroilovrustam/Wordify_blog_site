from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse
from .models import Article, Comment, Tag, Category
from author.models import Profile
from .forms import CommentForm


# Create your views here.


def home_view(request):
    article = Article.objects.order_by('-id')[:3]
    obj = Article.objects.order_by('-id')
    profile = Profile.objects.get(id=1)
    category = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if cat:
        obj = obj.filter(category__title__exact=cat)
    if tag:
        obj = obj.filter(tags__title__icontains=tag)
    search = request.GET.get('search')
    if search:
        obj = obj.filter(title__icontains=search)
    p = Paginator(obj, 2)
    page = request.GET.get('page')
    obj = p.get_page(page)
    ctx = {
        "articles": article,
        'objs': obj,
        'profile': profile,
        'categorys': category,
        'tags': tags,
    }
    return render(request, 'wordify/index.html', ctx)


def article_view(request):
    obj = Article.objects.order_by('-id')
    article = Article.objects.all()[:3]
    profile = Profile.objects.get(id=1)
    category = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if cat:
        obj = obj.filter(category__title__exact=cat)
    if tag:
        obj = obj.filter(tags__title__icontains=tag)
    p = Paginator(obj, 2)
    page = request.GET.get('page')
    obj = p.get_page(page)
    ctx = {
        'objs': obj,
        'articles': article,
        'profile': profile,
        'categorys': category,
        'tags': tags,
        'cat': cat
    }
    return render(request, 'wordify/category.html', ctx)


def post_views_up(request, pk):
    obj = Article.objects.get(id=pk)
    obj.views += 1
    obj.save()
    return redirect(reverse('detail', kwargs={"pk": pk}))


def detail(request, pk):
    obj = Article.objects.get(id=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.article = obj
        com.author_id = request.user.profile.id
        com.save()
        return redirect('.')
    article = Article.objects.order_by('-id')[:3]
    profile = Profile.objects.get(id=1)
    category = Category.objects.all()
    tag = Tag.objects.all()
    ctx = {
        'obj': obj,
        'form': form,
        "articles": article,
        'profile': profile,
        'categorys': category,
        'tags': tag,
    }
    return render(request, 'wordify/blog-single.html', ctx)


def login_view(request):
    if not request.user.is_anonymous:
        return redirect('/')
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            if next_path:
                return redirect(next_path)
            return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'login.html', ctx)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request, 'logout.html')


def registration(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
