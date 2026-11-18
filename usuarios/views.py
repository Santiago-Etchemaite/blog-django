from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('lista_posts')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})


@login_required
def perfil(request):
    posts = request.user.posts.all()
    return render(request, 'usuarios/perfil.html', {'posts': posts})