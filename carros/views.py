from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Carro
# Create your views here.

def listar_carros(request):
    carros = Carro.objects.all()
    paginator = Paginator(carros, 5)  # 5 carros por página
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'carros/listar_carros.html', context)

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')
