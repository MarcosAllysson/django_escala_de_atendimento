from django.urls import path
from .views import IndexView, CreateFolgaView, UpdateFolgaView, DeleteFolgaView, home_page


app_name = 'folga'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', home_page, name='home'),
    path('add-folga/', CreateFolgaView.as_view(), name='add-folga'),
    path('upd-folga/<int:pk>/', UpdateFolgaView.as_view(), name='upd-folga'),
    path('del-folga<int:pk>/', DeleteFolgaView.as_view(), name='del-folga'),
]
