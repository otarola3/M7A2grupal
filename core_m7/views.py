from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from core_m7.forms.formulario_1 import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from .models import Cliente, Producto
from django.http import HttpResponse
from django.core import mail
import random
import string

connection = mail.get_connection()
connection.open()

# Create your views here.
def index_welcome(request):
    return render(request, 'welcome.html')


class BienvenidaView(TemplateView):
    template_name = "bienvenida_login.html"
    
class TareasView(TemplateView):
    template_name = "tareas.html"
    
    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Formulario Valido")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    print("Usuario activo")
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/')

                else:
                    print("Usuario inactivo")
                    return HttpResponse('Cuenta deshabilitada')
            else:
                print("Usuario o contraseña incorrectos")
                return HttpResponse('Login no Valido')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def generate_random_password():
    caracter = string.ascii_letters + string.digits
    password = "".join(random.choice(caracter) for i in range(6))
    return password


def register(request):
   
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            direccion = form.cleaned_data["direccion"]
            telefono = form.cleaned_data["telefono"]
            credito = form.cleaned_data["credito"]
            email = form.cleaned_data["email"]
            grupo = form.cleaned_data['group']
            
            password1 = generate_random_password()
            
            
            # Crear el nuevo usuario en la base de datos "default"
            usuario_nuevo = User(username=username, first_name=first_name, last_name=last_name, email=email)
            
            usuario_nuevo.set_password(password1)
            usuario_nuevo.save(using='default')
            
            emails = mail.EmailMessage(
                    'Verificación de correo electrónico',
                    f'Tu contraseña de verificación es:{password1}',
                    'talento@fabricadecodigo.dev',
                    [email],
                    connection=connection
                )
            emails.send()  
            
            # Agregar el usuario al grupo en la misma base de datos
            grupo.user_set.add(usuario_nuevo)
            grupo.save(using='default')
            
            
    
            # Autenticar y redirigir al usuario
            #user = authenticate(request, username=username, password=password)
            #login(request, user)
            datos_usuario =Cliente(id_user=usuario_nuevo, direccion=direccion, telefono=telefono, credito=credito)
            datos_usuario.save()
            #enviar_correo(request)
            return redirect('http://127.0.0.1:8000/login')  # Cambia 'home' por la URL de tu página de inicio
        else:
            print('no paso el if', form.errors)
    else:
        form = RegistrationForm(groups=Group.objects.all())  # Pasar los grupos al formulario
    
    return render(request, 'registro.html', {'form': form})


def listar_productos(request):
    print('Antes de extraer producto')
    productos = Producto.objects.all()  # Obtener los primeros 5 productos disponibles
    print('Despues de extraer producto')
    print(productos)
    contexto = {'productos': productos}
    return render(request, 'productos.html', contexto)


