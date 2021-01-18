from django.shortcuts import render


def index(request):
    title = 'SoftUni Django  101'
    context = {
        'title': title
    }
    return render(request, 'index.html', context)
