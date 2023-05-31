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
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(verbose_name='imagenes', upload_to='imagen_producto/')  # Relación con el modelo Imagen
    stock = models.IntegerField(verbose_name='stock', default=0)
    
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
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_productos = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    total_detalle = models.IntegerField(verbose_name="Total")
   
    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"
        ordering = ["-cantidad"]
    
    def __str__(self):
        return f"Detalle {self.id} ------ Producto: {self.id_productos_id} ------ Cantidad: {self.cantidad} -------- Total: {self.total_detalle}"

class Pedido(models.Model):
    ESTADO_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado'),
    )

    id_cliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cliente")
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fecha = models.DateField(verbose_name="Fecha")
    detalle = models.ForeignKey(Detalle, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-fecha"]
        
    def __str__(self):
        return str(self.id_cliente)



    

