from django.urls import path
from . import views

urlpatterns = [
    # Autores
    path('autores/', views.AutorListView.as_view(), name='lista_autores'),
    path('autores/nuevo/', views.AutorCreateView.as_view(), name='crear_autor'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='detalle_autor'),
    path('autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='editar_autor'),
    path('autores/<int:pk>/eliminar/', views.AutorDeleteView.as_view(), name='eliminar_autor'),

    # Libros
    path('libros/', views.LibroListView.as_view(), name='lista_libros'),
    path('libros/nuevo/', views.LibroCreateView.as_view(), name='crear_libro'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='detalle_libro'),
    path('libros/<int:pk>/editar/', views.LibroUpdateView.as_view(), name='editar_libro'),
    path('libros/<int:pk>/eliminar/', views.LibroDeleteView.as_view(), name='eliminar_libro'),
]