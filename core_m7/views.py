from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from core_m7.forms.formulario_1 import LoginForm, RegistrationForm, CompraForm
from django.contrib.auth import authenticate, login
from .models import Cliente, Producto, Detalle, Pedido
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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

class HistorialView(TemplateView):
    template_name = "historial.html"
    
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
    productos = Producto.objects.all()  # Obtener los primeros 5 productos disponibles)
    contexto = {'productos': productos}
    
    return render(request, 'productos.html', contexto)

@login_required
def get_user(request):
    user_id = request.user.id
    return user_id

def compra(request):
    id = get_user(request)
    print('######## ID => ',id)
    if request.method == 'POST':
        print(request.POST)
        cantidad = int(request.POST['cantidad'])
        producto_id = int(request.POST['producto'])
        producto = Producto.objects.get(pk=producto_id)
        total = cantidad * producto.precio

        compra_nuevo = Detalle(id_productos=producto, cantidad=cantidad, total_detalle=total, usuario_id=id)
        compra_nuevo.save()   
        
  
        # Aquí puedes realizar las acciones necesarias con los datos de la compra
        
        print(f"Cantidad: {cantidad}")
        print(f"Producto ID: {producto_id}")
        print(f"Total: {total}")
        
    return redirect('listar_productos')

def ver_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'ver_pedidos.html', {'pedidos': pedidos})

def historial_compras(request):
    # Obtener el historial de compras y el estado del pedido para el usuario actual
    id = get_user(request)
    historial = Detalle.objects.filter(usuario_id=id)
    estado_pedido = Pedido.objects.filter(id_cliente_id=id)
    
    # Obtener el nombre del producto de cada pedido en el historial
    nombres_productos = [detalle.id_productos.nombre for detalle in historial]
    print(f'Nombre del producto: {nombres_productos}')
    
    # Renderizar el template y pasar los datos del historial y estado del pedido
    return render(request, 'historial.html', {'historial': historial, 'estado_pedido': estado_pedido, 'nombres_productos': nombres_productos})
