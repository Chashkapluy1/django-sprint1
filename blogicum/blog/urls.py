from django.urls import path

from . import views


app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('posts/<int:post_id>/',
         views.post_detail,
         name='post_detail'),  # Страница с деталями поста
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts'),  # Страница с постами по категории
]
