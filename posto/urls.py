from django.urls import path
from posto.views import IndexView, CreatePostoView, UpdatePostoView


app_name = 'posto'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-posto/', CreatePostoView.as_view(), name='add-posto'),
    path('upd-posto/<int:pk>/', UpdatePostoView.as_view(), name='upd-posto'),
]
