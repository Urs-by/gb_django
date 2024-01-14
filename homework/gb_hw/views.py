from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1> Мой первый dgango проект. </h1>")


def about(request):
    """
    Для тестов добавил логировани, но логического смысла Exception не несет

    """
    try:
        logger.info('About page accessed')
        about_mi = "<h3> Привет, меня зовут Короткевич Артур. <br>" \
                   "<h4> Я junior python разработчик. <br>" \
                   "Я учусь в GeekBrains, на курсе Python-разработчик. <br>" \
                   "Участвовал в нескольких коммерческих проектах и стартапах. <br>"
        return HttpResponse(about_mi)
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")

