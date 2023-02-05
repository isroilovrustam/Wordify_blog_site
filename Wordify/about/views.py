from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Category, Tag, Article
from .models import About
from author.models import Profile


# Create your views here.


def about_view(request):
    object = About.objects.all()
    profile = Profile.objects.get(id=1)
    obj = Article.objects.order_by('-id')
    article = Article.objects.order_by("-id")[:3]
    category = Category.objects.all()
    tag = Tag.objects.all()
    p = Paginator(obj, 2)
    page = request.GET.get('page')
    obj = p.get_page(page)
    ctx = {
        'objects': object,
        'objs': obj,
        'profile': profile,
        'articles': article,
        'categorys': category,
        'tags': tag,
    }
    return render(request, 'wordify/about.html', ctx)
