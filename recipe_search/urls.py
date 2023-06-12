from django.urls import path
from .import views

app_name = 'recipe_search'
urlpatterns = [
    # index.htmlがログイン前のトップページのことにする。
    path('', views.IndexView.as_view() ,name="index"),
]