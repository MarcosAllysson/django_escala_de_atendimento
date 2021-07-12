from django.urls import path
from .views import IndexView, create_folga, update_folga, DeleteFolgaView


app_name = 'folga'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-folga/', create_folga, name='add-folga'),
    path('upd-folga/<int:pk>/', update_folga, name='upd-folga'),
    path('del-folga/<int:pk>/', DeleteFolgaView.as_view(), name='del-folga'),
]
