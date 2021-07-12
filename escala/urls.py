from django.urls import path
from .views import HomeView, ListEscalaView, create_escala, update_escala, DeleteEscalaView


app_name = 'escala'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('escala/', ListEscalaView.as_view(), name='escala'),
    path('add-escala/', create_escala, name='add-escala'),
    path('upd-escala/<int:pk>/', update_escala, name='upd-escala'),
    path('del-escala/<int:pk>/', DeleteEscalaView.as_view(), name='del-escala'),
]
