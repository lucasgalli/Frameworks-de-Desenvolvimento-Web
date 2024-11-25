from django import forms # forms é uma biblioteca do django usada nos formulários
from .models import Nome_do_modelo

class NomeDaClasseParaForm(forms.ModelForm): # ModelForm é uma classe fornecida que serve para criar formulários baseados em um modelo de banco de dados
    class Meta: # A classe interna que fornece metadados ou configurações adicionais para classes como ModelForm, Model, Admin
        model = Nome_do_modelo
        fields = ['nome_do_campo', 'nome_do_campo', 'nome_do_campo', 'nome_do_campo']
