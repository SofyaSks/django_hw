from django.shortcuts import render

def article(request):
    context = {
        'title': 'А зачем это',
        'dop' : 'Дополнение'
    }
    return render(
        request,
        'article/page.html',
        context
    )
