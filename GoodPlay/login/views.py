from django.shortcuts import render, redirect, get_object_or_404
from . models import Juego, Compañia, Producto
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . forms import JuegoForm, CompañiaForm

# Create your views here.
def index(request):
    num_Juego = Juego.objects.all().count()
    num_Juego_available=Juego.objects.filter(juego__exact='E').count()
    num_compañias = Compañia.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_Juego': num_Juego, 
        'num_Juego_available': num_Juego_available, 'num_compañias' : num_compañias}, 
    )
def consolas(request):
    
    return render(
        request,
        'consolas.html',
    )

def juegos(request):
    
    return render(
        request,
        'juegos.html',
    )

def accesorio(request):
    
    return render(
        request,
        'accesorio.html',
    )

def computacion(request):
    
    return render(
        request,
        'computacion.html',
    )

class JuegoCreate(CreateView):
    model = Juego
    fields = '__all__'
 
class JuegoUpdate(UpdateView):
    model = Juego
    fields = ['codigo','nombre','compañia','fecha', 'juego']

class JuegoDelete(DeleteView):
    model = Juego
    success_url = reverse_lazy('juegos')

class JuegoDetailView(generic.DetailView):
    model = Juego


class JuegoListView(generic.ListView):
    model = Juego
    paginate_by=10


class CompañiaCreate(CreateView):
    model = Compañia
    fields = '__all__'
 
class CompañiaUpdate(UpdateView):
    model = Compañia
    fields = ['id_compañia','nombre_compañia']

class CompañiaDelete(DeleteView):
    model = Compañia
    success_url = reverse_lazy('compañias')

class CompañiaDetailView(generic.DetailView):
    model = Compañia


class CompañiaListView(generic.ListView):
    model = Compañia
    paginate_by=10

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
 
class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['id_producto','nombre_producto','precio','marca']

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')

class ProductoDetailView(generic.DetailView):
    model = Producto


class ProductoListView(generic.ListView):
    model = Producto
    paginate_by=10



def juego_new(request):
    if request.method == "POST":
        form = JuegoForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #form.save_m2m()
            return redirect('juego-detail', pk=post.pk)
    else:
        form = JuegoForm()
        return render(request, 'login/juego_form.html', {'form': form})

def juego_edit(request, pk):
    post = get_object_or_404(Juego, pk=pk)
    if request.method == "POST":
        form = JuegoForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('juego-detail', pk=post.pk)
    else:
        form = JuegoForm(instance=post)
    return render(request, 'login/juego_form.html', {'form': form})

def compañia_new(request):
    if request.method == "POST":
        form = CompañiaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('compañia-detail', pk=post.pk)
    else:
        form = CompañiaForm()
        return render(request, 'login/compañia_form.html', {'form': form})

def compañia_edit(request, pk):
    post = get_object_or_404(Compañia, pk=pk)
    if request.method == "POST":
        form = CompañiaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('compañia-detail', pk=post.pk)
    else:
        form = CompañiaForm(instance=post)
    return render(request, 'login/compañia_form.html', {'form': form})