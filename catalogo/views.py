from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

class HomeView(TemplateView):
    template_name = 'home.html'

class CreditosView(TemplateView):
    template_name = 'credits.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

# Productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'products/product_list.html'
    context_object_name = 'productos'
    paginate_by = 10

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'products/product_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('catalogo:producto_lista')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'products/product_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('catalogo:producto_lista')

# Categorías
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categories/category_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('catalogo:categoria_lista')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categories/category_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('catalogo:categoria_lista')

