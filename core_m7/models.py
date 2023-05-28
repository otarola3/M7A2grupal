from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='core_m7/imagenes/')

    def __str__(self):
        return self.nombre


class DatosUsuarioExtra(models.Model):
   id_user = models.OneToOneField(User, on_delete=models.CASCADE)
   rut = models.TextField()
   
   class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Datos de Usuarios"
        ordering = ["-id_user"]


        def __str__(self):
            return self.id_user.username
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    email = models.EmailField(max_length=50, verbose_name="Email")
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-nombre"]
        
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    direccion = models.CharField(max_length=50, verbose_name="Direccion")
    telefono = models.IntegerField(verbose_name="Telefono")
    credito = models.IntegerField(verbose_name="Credito", default=0)
    email = models.EmailField(max_length=50, verbose_name="Email")
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-direccion"]
        
    def __str__(self):
        return self.id_user.username
    
class Estado(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Estado")
    
    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["-nombre"]
        
    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name="Estado")
    fecha = models.DateField(verbose_name="Fecha")
 
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-fecha"]
        
    def __str__(self):
        return str(self.id_cliente)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = imagen = models.ImageField(verbose_name='imagenes', upload_to='imagen_producto/')  # Relación con el modelo Imagen

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-nombre"]

    def __str__(self):
        return self.nombre

    def obtener_imagen(self):
        if self.imagen:
            return self.imagen.imagen.url
        return None
    

class Detalle(models.Model):
    id_productos = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name="Pedido")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    total_detalle = models.IntegerField(verbose_name="Total")
   
    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"
        ordering = ["-cantidad"]
    
    def __str__(self):
        return str(self.id_pedido)
    
    
    
    

    

