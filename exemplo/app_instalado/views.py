from django.shortcuts import render, redirect
from .models import Nome_do_modelo
from .forms import NomeDaClasseParaForm

def funcao_chamada_pela_url(request):
    variavel_do_modelo = Nome_do_modelo.objects.all()
    return render(request, 'nome_da_pasta/template_arquivo-2.html', {'variavel_do_modelo': variavel_do_modelo})

def funcao_chamada_pela_url(request):
    if request.method == 'POST':
        variavel_para_formulario = NomeDaClasseParaForm(request.POST)
        variavel_para_formulario.save()
    else:
        variavel_para_formulario = NomeDaClasseParaForm()
    return render(request, 'nome_da_pasta/template_arquivo.html', {'variavel_para_usar_no_template': variavel_para_formulario})
