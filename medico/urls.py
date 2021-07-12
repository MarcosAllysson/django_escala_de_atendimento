from django.urls import path
from .views import IndexView, create_medico, update_medico


app_name = 'medicos'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-medico/', create_medico, name='add-medico'),
    path('upd-medico/<int:pk>/', update_medico, name='upd-medico'),
]
