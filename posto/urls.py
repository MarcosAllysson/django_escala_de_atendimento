from django.urls import path
from posto.views import IndexView, CreatePostoView, UpdatePostoView, DeletePostoView


app_name = 'posto'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-posto/', CreatePostoView.as_view(), name='add-posto'),
    path('upd-posto/<int:pk>/', UpdatePostoView.as_view(), name='upd-posto'),
    path('del-posto/<int:pk>/', DeletePostoView.as_view(), name='del-posto'),
]
