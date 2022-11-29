from django.shortcuts import render


def novo_servico(request):
    return render(request, 'novo_servico.html')
