"""
Настройка URL-адресов для проекта blogicum.

Список `urlpatterns` направляет URL-адреса к представлениям.
Документация Django по URL-адресам:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Примеры:
    1. Для обычных представлений (function views):
        - Импортируйте views: from my_app import views
        - Добавьте URL: path('', views.home, name='home')
    2. Для класс-базированных представлений:
        - Импортируйте класс: from other_app.views import Home
        - Добавьте URL: path('', Home.as_view(), name='home')
    3. Для включения других URL-конфигураций:
        - Импортируйте include: from django.urls import include, path
        - Добавьте URL: path('blog/', include('blog.urls'))
"""
from django.urls import include, path

# Пространство имен для URL всего проекта
app_name = 'blogicum'

# Основные URL-шаблоны проекта
urlpatterns = [
    # Подключение URL-адресов приложения blog
    # Базовый URL: / (корень сайта)
    path('', include('blog.urls', namespace='blog')),
    # Подключение URL-адресов приложения pages
    # Базовый URL: /pages/
    path('pages/', include('pages.urls', namespace='pages')),
]