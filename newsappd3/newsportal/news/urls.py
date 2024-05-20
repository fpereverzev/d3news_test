from django.urls import path
from .views import news_list, news_detail

urlpatterns = [
    path('', news_list, name='news_list'),  # URL для списка новостей
    path('<int:article_id>/', news_detail, name='news_detail'),  # URL для детальной информации о новости
]
