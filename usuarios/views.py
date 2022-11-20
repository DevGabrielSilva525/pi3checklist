# from django.shortcuts import render
# from django.contrib import messages
# from .models import Usuarios

# def cadastro(request):
#     if request.method == 'POST':
#         nome_usuario = request.method['nome_usuario']
#         email = request.method['email']
#         senha = request.method['senha']

#         if Usuarios.objects.filter(email=email).exists():
#             messages.ERROR('Esse usuario já existe em nosso sistema')
#         usuario = Usuarios.objects.create_user(username=nome_usuario, email=email, password=senha)
#         usuario.save()
#     return request(render, 'registro.html')

