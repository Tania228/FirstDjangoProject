from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from datetime import datetime, time


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time.time()}'
    return HttpResponse(msg)


def workdir_view(request):
    try:
        list_files = os.listdir(path='.')
        files = ', '.join(list_files)
        return HttpResponse(f'Список файлов в рабочей директории:\n{files}')
    except Exception as e:
        return f'Произошла ошибка {e}'




