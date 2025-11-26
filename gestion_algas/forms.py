"""
Formularios para la aplicación de gestión de algas
"""
from django import forms
from .models import Usuario, RegistroProduccion, TipoAlga, CapacidadProductiva, ConfiguracionReporte
import re


class UsuarioCreationForm(forms.ModelForm):
    """Formulario para crear nuevos usuarios"""
    
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mínimo 6 caracteres'
        })
    )
    
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })
    )
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'telefono', 'password', 'rol']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56 9 1234 5678'
            }),
            'rol': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError('La contraseña debe tener al menos 6 caracteres')
        return password
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError('El nombre de usuario debe tener al menos 3 caracteres')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('Ya existe un usuario con este nombre de usuario')
        return username
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        patron = re.compile(r'^\+?\d+$')
        if telefono and not patron.match(telefono):
            raise forms.ValidationError('El teléfono solo puede contener números y el símbolo "+"')
        return telefono
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
        return user


class CustomLoginForm(forms.Form):
    """Formulario de login personalizado"""
    
    username = forms.CharField(
        label='Nombre de Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre de usuario',
            'autofocus': True
        })
    )
    
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu contraseña'
        })
    )


class RegistroProduccionForm(forms.ModelForm):
    """Formulario para registrar producción de algas"""
    
    class Meta:
        model = RegistroProduccion
        fields = ['tipo_alga', 'cantidad_cosechada', 'sector', 'observaciones']
        widgets = {
            'tipo_alga': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'cantidad_cosechada': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.01',
                'required': True
            }),
            'sector': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Sector Norte, Bahía Sur',
                'required': True
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Notas adicionales...'
            }),
        }
        labels = {
            'tipo_alga': 'Tipo de Alga',
            'cantidad_cosechada': 'Cantidad Cosechada (kg)',
            'sector': 'Sector de Cosecha',
            'observaciones': 'Observaciones'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo tipos de alga activos
        self.fields['tipo_alga'].queryset = TipoAlga.objects.filter(activo=True)


class TipoAlgaForm(forms.ModelForm):
    """Formulario para gestionar tipos de algas"""
    
    class Meta:
        model = TipoAlga
        fields = ['nombre', 'factor_conversion', 'descripcion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del tipo de alga'
            }),
            'factor_conversion': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0.01'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del tipo de alga'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class CapacidadProductivaForm(forms.ModelForm):
    """Formulario para gestionar capacidad productiva"""
    
    class Meta:
        model = CapacidadProductiva
        fields = [
            'mes', 'capacidad_mensual_maxima', 'capacidad_anual_maxima',
            'volumen_producido', 'volumen_comprometido', 'observaciones'
        ]
        widgets = {
            'mes': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'month',
                'required': True
            }),
            'capacidad_mensual_maxima': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.00',
                'required': True
            }),
            'capacidad_anual_maxima': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.00',
                'required': True
            }),
            'volumen_producido': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.00'
            }),
            'volumen_comprometido': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.00'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Notas adicionales...'
            }),
        }
        labels = {
            'mes': 'Mes',
            'capacidad_mensual_maxima': 'Capacidad Mensual Máxima (kg)',
            'capacidad_anual_maxima': 'Capacidad Anual Máxima (kg)',
            'volumen_producido': 'Volumen Producido (kg)',
            'volumen_comprometido': 'Volumen Comprometido (kg)',
            'observaciones': 'Observaciones'
        }


class ConfiguracionReporteForm(forms.ModelForm):
    """Formulario para configurar reportes personalizados para clientes"""
    
    class Meta:
        model = ConfiguracionReporte
        fields = [
            'empresa', 'pais', 'contacto', 'email', 'unidad_medida',
            'formato_preferido', 'mostrar_capacidad_instalada', 
            'mostrar_disponibilidad', 'mostrar_historial_produccion',
            'periodo_historial_meses', 'activo'
        ]
        widgets = {
            'empresa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la empresa cliente',
                'required': True
            }),
            'pais': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'País del cliente',
                'required': True
            }),
            'contacto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del contacto'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'contacto@empresa.com',
                'required': True
            }),
            'unidad_medida': forms.Select(attrs={
                'class': 'form-select'
            }),
            'formato_preferido': forms.Select(attrs={
                'class': 'form-select'
            }),
            'mostrar_capacidad_instalada': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'mostrar_disponibilidad': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'mostrar_historial_produccion': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'periodo_historial_meses': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '24',
                'value': '6'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'empresa': 'Empresa',
            'pais': 'País',
            'contacto': 'Persona de Contacto',
            'email': 'Email de Contacto',
            'unidad_medida': 'Unidad de Medida',
            'formato_preferido': 'Formato Preferido',
            'mostrar_capacidad_instalada': 'Mostrar Capacidad Instalada',
            'mostrar_disponibilidad': 'Mostrar Disponibilidad',
            'mostrar_historial_produccion': 'Mostrar Historial de Producción',
            'periodo_historial_meses': 'Período de Historial (meses)',
            'activo': 'Configuración Activa'
        }
