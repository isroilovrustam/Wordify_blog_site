from django.shortcuts import render, redirect
from .forms import ContactForm
from author.models import Profile
from blog.models import Article, Category

# Create your views here.


def contact_view(request):
    form = ContactForm(request.POST or None)
    article = Article.objects.all()[:3]
    category = Category.objects.all()
    profile = Profile.objects.get(id=1)
    if form.is_valid():
        form.save()
        return redirect('.')
    ctx = {
        'form': form,
        'articles': article,
        'categorys': category,
        'profile': profile,
    }
    return render(request, 'wordify/contact.html', ctx)
