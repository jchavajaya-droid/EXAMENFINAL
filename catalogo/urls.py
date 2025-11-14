from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('productos/', views.ProductoListView.as_view(), name='producto_lista'),
    path('productos/agregar/', views.ProductoCreateView.as_view(), name='producto_agregar'),
    path('productos/<slug:slug>/', views.ProductoDetailView.as_view(), name='producto_detalle'),
    path('productos/<slug:slug>/editar/', views.ProductoUpdateView.as_view(), name='producto_editar'),

    path('categorias/', views.CategoriaListView.as_view(), name='categoria_lista'),
    path('categorias/agregar/', views.CategoriaCreateView.as_view(), name='categoria_agregar'),
    path('categorias/<slug:slug>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_editar'),

    path('creditos/', views.CreditosView.as_view(), name='creditos'),
    path('contacto/', views.ContactView.as_view(), name='contacto'),
]
