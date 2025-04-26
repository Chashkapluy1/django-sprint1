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
