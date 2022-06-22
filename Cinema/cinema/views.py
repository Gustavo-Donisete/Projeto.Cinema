from django.shortcuts import render, redirect

from cinema.forms import FilmeForm, SessaoForm, IngressoForm
from cinema.models import Filme
from cinema.models import Sessao
from cinema.models import Ingresso

#Filme, Sessao, Ingresso

def list_Filme(request):
    filmes = Filme.objects.all()
    return render(request, 'cinema.html', {'filmes': filmes})

def list_Sessao(request):
    sessoes = Sessao.objects.all()
    return render(request, 'cinema.html', {'sessoes': sessoes})

def list_Ingresso(request):
    ingressos = Ingresso.objects.all()
    return render(request, 'cinema.html', {'ingressos': ingressos})

def create_Filme(request):
    form = FilmeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_Filme')

    return render(request, 'filme-form.html', {'form': form})

def create_Sessao(request):
    form = SessaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_Sessao')

    return render(request, 'sessao-form.html', {'form': form})

def create_Ingresso(request):
    form = IngressoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_Ingresso')

    return render(request, 'cinema-form.html', {'form': form})


def update_Filme(request, id):
    filmes = Filme.objects.get(id=id)
    form = FilmeForm(request.POST or None, instance=Filme)

    if form.is_valid():
        form.save()
        return redirect('list_Filme')

    return render(request, 'filme-form.html', {'form': form, 'filmes': filmes})

def update_Sessao(request, id):
    sessoes = Sessao.objects.get(id=id)
    form = SessaoForm(request.POST or None, instance=Sessao)

    if form.is_valid():
        form.save()
        return redirect('list_Sessao')

    return render(request, 'sessao-form.html', {'form': form, 'sessoes':sessoes})

def update_Ingresso(request, id):
    ingressos = Ingresso.objects.get(id=id)
    form = IngressoForm(request.POST or None, instance=ingressos)

    if form.is_valid():
        form.save()
        return redirect('list_Ingresso')

    return render(request, 'cinema-form.html', {'form': form, 'ingressos': ingressos})

def delete_Filme(request, id):
    filmes = Filme.objects.get(id=id)

    if request.method == 'POST':
        filmes.delete()
        return redirect('list_Filme')

    return render(request, 'filme-delete-confirm.html', {'filmes': filmes})

def delete_Sessao(request, id):
    sessoes = Sessao.objects.get(id=id)

    if request.method == 'POST':
        sessoes.delete()
        return redirect('list_Sessao')

    return render(request, 'sessao-delete-confirm.html', {'sessoes': sessoes})

def delete_Ingresso(request, id):
    ingressos = Ingresso.objects.get(id=id)

    if request.method == 'POST' :
        ingressos.delete()
        return redirect('list_Ingresso')

    return render(request, 'cinema-delete-confirm.html', {'ingressos': ingressos})