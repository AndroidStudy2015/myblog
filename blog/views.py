from django.shortcuts import render
from django.http import HttpResponse
from blog import models


# Create your views here.


# 每一个请求都由一个函数来处理，
# 接收请求的参数 request
# 记得在urls里配置这个函数
def index(request):
    # article = models.Article.objects.get(pk=3)
    articles = models.Article.objects.all()
    return render(request, "blog/index.html", {'articles': articles})
    # return render(request, "index.html", {'key': 'ddddddd'})


def hello(request):
    title = request.POST.get('aaa', '值为空时')

    if request.method == 'POST':
        return HttpResponse('接收到post请求，接收到值: ' + title)

    return HttpResponse('error' + title)


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/article_page.html", {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    # 从html取出来title和content
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        # 拿着title和content去创建Article对象
        models.Article.objects.create(title=title, content=content)
        # 返回首页
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, "blog/article_page.html", {'article': article})
