from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro

# LISTAR
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista.html', {'livros': livros})

# CRIAR
def criar_livro(request):
    if request.method == 'POST':
        Livro.objects.create(
            titulo=request.POST['titulo'],
            autor=request.POST['autor'],
            ano=request.POST['ano']
        )
        return redirect('lista_livros')
    
    return render(request, 'form.html')

# EDITAR
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        livro.titulo = request.POST['titulo']
        livro.autor = request.POST['autor']
        livro.ano = request.POST['ano']
        livro.save()
        return redirect('lista_livros')

    return render(request, 'form.html', {'livro': livro})

# DELETAR
def deletar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('lista_livros')