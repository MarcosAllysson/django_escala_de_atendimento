from django.urls import path
from .views import IndexView, CreateEscalaView, UpdateEscalaView, DeleteEscalaView


app_name = 'escala'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-escala', CreateEscalaView.as_view(), name='add-escala'),
    path('upd-escala/<int:pk>', UpdateEscalaView.as_view(), name='upd-escala'),
    path('del-escala/<int:pk>', DeleteEscalaView.as_view(), name='del-escala'),
]
