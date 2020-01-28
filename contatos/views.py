from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ContatosForm
from .models import Contatos

def contatos(request):
    lista = Contatos.objects.order_by('nome')
    return render(request, 'contatos.html', {'lista' : lista})

def menu(request):
    return render(request, 'menu.html')


def criar(request):
    if request.method == 'POST':
        form = ContatosForm(request.POST)
        if form.is_valid():
            agenda = form.save()
            nome = form.cleaned_data.get("nome")
            email = form.cleaned_data.get("email")
            telefone_residencia = form.cleaned_data.get("telefone_residencia")
            telefone_celular = form.cleaned_data.get("telefone celular")
            endereço = form.cleaned_data.get("endereço")
            agenda.save()
            return redirect('recente')
    else:
        form = ContatosForm()

    return render(request, 'criar.html', {'form' : form})

def detalhe(request, pk):
    agenda = get_object_or_404(Contatos, pk=pk)
    return render(request, 'detalhes.html', {'agenda' : agenda})


def editar(request, pk):
    contato = get_object_or_404(Contatos, pk=pk)
    if request.method == 'POST':
        form = ContatosForm(request.POST, instance=contato)
        if form.is_valid():
            contato.save()
            return redirect('detalhe', pk=contato.pk)
    else:
        form = ContatosForm(instance=contato)
    return render(request, 'editar.html', {'form' : form})

def deletar(request, pk):
    contato = get_object_or_404(Contatos, pk=pk)
    contato.delete()
    return redirect('contatos')

def recente(request):
    recente = Contatos.objects.latest('id')
    return render(request, 'recente.html', {'recente' : recente})