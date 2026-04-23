from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# ── AUTORES ──────────────────────────────────────────

class AutorListView(ListView):
    model = Autor
    template_name = 'gestion/lista_autores.html'
    context_object_name = 'autores'

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'gestion/autor_detail.html'
    context_object_name = 'autor'

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('lista_autores')

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('lista_autores')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'gestion/autor_confirm_delete.html'
    success_url = reverse_lazy('lista_autores')

# ── LIBROS ───────────────────────────────────────────

class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/lista_libros.html'
    context_object_name = 'libros'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'gestion/libro_detail.html'
    context_object_name = 'libro'

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('lista_libros')

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('lista_libros')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/libro_confirm_delete.html'
    success_url = reverse_lazy('lista_libros')