from django.urls import path

from app.views import mostra_lista, edita_apaga_lista

urlpatterns = [
    path('', mostra_lista),
    path('<int:pk>/', edita_apaga_lista)
]