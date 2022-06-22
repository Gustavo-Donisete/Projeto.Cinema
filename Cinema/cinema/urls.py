from django.urls import path
from .views import list_Filme, list_Sessao, list_Ingresso, \
    create_Filme, create_Sessao, create_Ingresso, \
    update_Filme, update_Sessao, update_Ingresso, \
    delete_Filme, delete_Sessao, delete_Ingresso

urlpatterns = [
    path('Filme', list_Filme, name='list_Filme'),
    path('Sessao', list_Sessao, name='list_Sessao'),
    path('Ingresso', list_Ingresso, name='list_Ingresso'),
    path('new_Filme', create_Filme, name='create_Filme'),
    path('new_Sessao', create_Sessao, name='create_Sessao'),
    path('new_Ingresso', create_Ingresso, name='create_Ingresso'),
    path('update_Filme/<int:id>/', update_Filme, name='update_Filme'),
    path('update-Sessao/<int:id>/', update_Sessao, name='update_Sessao'),
    path('update_Ingresso/<int:id>/', update_Ingresso, name='update_Ingresso'),
    path('delete_Filme/<int:id>/', delete_Filme, name='delete_Filme'),
    path('delete_Sessao/<int:id>/', delete_Sessao, name='delete_Sessao'),
    path('delete_Ingresso/<int:id>', delete_Ingresso, name='delete_Ingresso')
]