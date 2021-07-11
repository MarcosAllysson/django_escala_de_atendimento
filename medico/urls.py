from django.urls import path
from .views import IndexView, CreateMedicoView, UpdateMedicoView, DeleteMedicoView


app_name = 'medicos'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-medico/', CreateMedicoView.as_view(), name='add-medico'),
    path('upd-medico/<int:pk>/', UpdateMedicoView.as_view(), name='upd-medico'),
    path('del-medico/<int:pk>/', DeleteMedicoView.as_view(), name='del-medico'),
]
