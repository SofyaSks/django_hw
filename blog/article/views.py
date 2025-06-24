from django.shortcuts import render
from . import models
from datetime import datetime
from django.http import JsonResponse
# def article(request):
#     context = {  # Это словарь контекста, он целиком передается в страницу-шаблон
#         'posts': [ # Это список, в нем содержится много постов, которые блоггер запостил в блог
#             {  # Это первый словарь, он содержит информацию о первом посте 
#                 'title': 'Веселенький заголовочек',
#                 'text':  'Интересный рассказ',
#             }, # Это запятая, она разделяет элементы списка
#             {  # Это второй словарь, он содержит информацию о первом посте
#                 'title': 'Грустненький заголовочек',
#                 'text':  'Студенты плохо помнят списки и словари',
#             },  # context['posts']['title']
#             {
#                 'title': 'Циклом',
#                 'text':  'Это сделано циклом',
#             },
#             {
#                 'title': None,
#                 'text':  'Тут нет заголовка',
#             }
#         ]
#     }
#     return render(
#         request,
#         'article/page.html',
#         context
#     )

def article(request, uid):
    context = {
        'author': 'Я',
        # 'data': models.Article.objects.filter(dt__lt = datetime(2025,5,21)),
        'data': models.Article.objects.all(),
        # 'data': models.Article.objects.filter(user_id = uid),
    }
    return render(
        request,
        'article/page.html',
        context
    )

from . import forms
def new_article (request):
    context = {
        'new_blog_post_form': forms.BlogPostForm()
    }
    print(request.POST)
    form = forms.BlogPostForm(request.POST)
    
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
    return render(
        request,
        'article/new_article.html',
        context
    )

def myfetch(request):
    return render(
        request,
        'article/myfetch.html'
    )

def multTable(request):
    return render(
        request,
        'article/mult_table.html'
    )

def new_blog_posts(request):
    print('Старше какой даты прислать посты? ', request.GET.get('dt'))
    dtmin = request.GET.get('dt')
    newest_posts = []
    for post in models.Article.objects.filter(dt__gt=dtmin):
        newest_posts.append({
            'user': post.user.username,
            'title': post.title,
            'text': post.text,
            'dt': post.dt
        })
    context = {
        'posts': newest_posts
    }
    print(context)
    return JsonResponse(context)


def all_blog_posts(request):
    context = {
        'posts': models.Article.objects.all()
    }
    return render(
        request,
        'article/feed.html',
        context
    )

def update_article(request, article_id):
    if request.method == 'POST':
       title = request.POST['title']
       text = request.POST['text']
       
       article = models.Article.objects.get(id=article_id)
       article.title = title
       article.text = text
       article.save()

        