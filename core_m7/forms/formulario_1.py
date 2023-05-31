from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group



class RegistrationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('group',)


    
class FormularioUsuarioForm(forms.Form):
    direccion = forms.CharField(max_length=50, label="Direccion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su direccion'}))
    edad = forms.IntegerField(label="Edad", required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese su edad'}))
    profesion = forms.CharField(max_length=50, label="Profesion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su profesion'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Usuario", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su usuario'}),
                               error_messages={'required': 'El Usuario es requerida'})
    password = forms.CharField(max_length=20, label="Contraseña", required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingrese su contraseña'}),
                               error_messages={'required': 'La contraseña es requerida'})

class RegistrationForm(forms.Form):
    # Campos adicionales para el formulario de registro
    direccion = forms.CharField(max_length=50, label="Direccion", required=True, widget=forms.TextInput(attrs={ 'placeholder':'Ingrese su direccion'}))
    telefono = forms.IntegerField(label="Telefono", required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingrese su telefono'}))
    credito = forms.IntegerField(label="Credito", required=True, widget=forms.NumberInput(attrs={ 'placeholder':'Ingrese su credito'}))
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese su usuario'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese su nombre'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese su apellido'}))
    email = forms.CharField(max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder':'Ingrese su email'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    def __init__(self, *args, **kwargs):
        groups = kwargs.pop('groups', None)
        super().__init__(*args, **kwargs)
        if groups:
            self.fields['group'].queryset = groups

   
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('username', 'first_name', 'last_name', 'rut','email', 'group')

class CompraForm(forms.Form):
    cantidad = forms.IntegerField(min_value=0, label="cantidad", required=True, widget=forms.NumberInput(attrs={'placeholder': 'Ingrese cantidad'}))
    producto_id = forms.HiddenInput()
