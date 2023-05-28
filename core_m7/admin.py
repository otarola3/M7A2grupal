from django.contrib import admin
from .models import  Usuario, Cliente, Estado, Pedido, Producto, Detalle

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
   list_display = ('nombre', 'descripcion', 'precio')
   
class ClienteAdmin(admin.ModelAdmin):
   list_display = ('id_user', 'credito')
   
class PedidoAdmin(admin.ModelAdmin):
   list_display = ('id_cliente','id', 'id_estado')
     
    
admin.site.register(Usuario)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Estado)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle)


