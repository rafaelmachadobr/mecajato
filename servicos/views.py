from django.shortcuts import render
from .forms import FormServico
from django.http import HttpResponse

def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)

        if not form.is_valid():
            return render(request, 'novo_servico.html', {'form': form})
        form.save()
        return HttpResponse('Salvo com sucesso')