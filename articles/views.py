from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def about(request):
    return render(request, 'articles/about.html')

def contact(request):
    return render(request, 'articles/contact.html')

def post(request, *args, **kwargs):
    article = Article.objects.get(id=kwargs["id"])
    context = {
        'article': article
    }
    return render(request, 'articles/post.html', context)

def contact_form(request, *args, **kwargs):

    return HttpResponse("Thanks for contacting us")

def add_article(request, *args, **kwargs):

    form = ArticleForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data["title"]
        subtitle = form.cleaned_data["subtitle"]
        description = form.cleaned_data["description"]
        a = Article(title=title,
                    subtitle=subtitle,
                    description=description)
        a.save()
    return redirect('/post/'+str(a.id)+'/')

def post_article(request):
    return render(request, 'articles/add_article.html')
