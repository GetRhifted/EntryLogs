from django import forms
from django.forms.widgets import TimeInput, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Registro, RegistroFresa

# Formularios para el registro de la Mora.

class RegistroGeneralForm(forms.ModelForm):
    class Meta:
        model = Registro
        exclude = ['Usuario']
        fields = ['Canasta', 'Fecha']
        widgets = {
            'Fecha': DateInput(attrs={'type': 'date'})
        }

class RegistroCanastaForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Contenido_Total', 'Azucar', 'Sorbato', 'Producto_no_Conforme', 'Fruta_Seleccionada']

class RegistroTiemposForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Inicio_Jornada', 'Seleccion_del_Producto', 'Mora_Entra_a_la_Olla', 'Hervor_Inicio',
                  'Hervor_Final', 'Enfriamiento_Inicio', 'Enfriamiento_Final','Inicio_Despulpado', 'Final_Despulpado', 'Segunda_Coccion', 'Hora_Final_Mora', 'Inicio_de_Empaque', 'Finalizacion_de_la_Canasta']
        
        widgets = {
            'Inicio_Jornada': TimeInput(attrs={'type': 'time'}),
            'Seleccion_del_Producto': TimeInput(attrs={'type': 'time'}),
            'Mora_Entra_a_la_Olla': TimeInput(attrs={'type': 'time'}),
            'Hervor_Inicio': TimeInput(attrs={'type': 'time'}),
            'Hervor_Final': TimeInput(attrs={'type': 'time'}),
            'Enfriamiento_Inicio': TimeInput(attrs={'type': 'time'}),
            'Enfriamiento_Final' : TimeInput(attrs={'type': 'time'}),
            'Inicio_Despulpado' : TimeInput(attrs={'type': 'time'}),
            'Final_Despulpado' : TimeInput(attrs={'type': 'time'}),
            'Segunda_Coccion' : TimeInput(attrs={'type': 'time'}),
            'Hora_Final_Mora' : TimeInput(attrs={'type': 'time'}),
            'Inicio_de_Empaque' : TimeInput(attrs={'type': 'time'}),
            'Finalizacion_de_la_Canasta' : TimeInput(attrs={'type': 'time'}),
        }

class RegistroDesechosForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Semilla', 'Pulpa']

class RegistroBrixForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Valor_Primer_Brix', 'Hora_Primer_Brix', 'Valor_Brix_Final', 'Hora_Brix_Final']
        widgets = {
            'Hora_Primer_Brix': TimeInput(attrs={'type': 'time'}),
            'Hora_Brix_Final': TimeInput(attrs={'type': 'time'}),
        }

class RegistroEmpacadosForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['Producto_Terminado', 'Media_Libra', 'Libra', 'Bolsa_Seis_kg', 'Otro', 'Observaciones']
        widgets = {
            'Observaciones': forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }
        

class SeleccionarRegistrosForm(forms.Form):
    registros = forms.ModelMultipleChoiceField(queryset=Registro.objects.all())

class CompararRegistrosForm(forms.Form):
    registros = forms.ModelMultipleChoiceField(
        queryset=Registro.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

# Formulario para el registro de Usuarios.

class RegistrodeUsuarioForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma tu Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Formularios para el registro de la Fresa.

class RegistroFresaGeneralForm(forms.ModelForm):
    class Meta:
        model = RegistroFresa
        exclude = ['Usuario']
        fields = ['Canasta', 'Fecha']
        widgets = {
            'Fecha': DateInput(attrs={'type': 'date'})
        }

class RegistroFresaCanastaForm(forms.ModelForm):
    class Meta:
        model = RegistroFresa
        fields = ['Contenido_Total', 'Azucar', 'Limon', 'Producto_no_Conforme', 'Fruta_Seleccionada']

class RegistroFresaTiemposForm(forms.ModelForm):
    class Meta:
        model = RegistroFresa
        fields = ['Inicio_Jornada', 'Seleccion_del_Producto', 'Fresa_Entra_a_la_Olla', 'Hervor_Inicio', 'Introduccion_Azucar', 'Introduccion_Limon', 
                  'Hervor_Final', 'Hora_Licuado', 'Hora_Final_Fresa', 'Inicio_de_Empaque', 'Finalizacion_de_la_Canasta']
        
        widgets = {
            'Inicio_Jornada': TimeInput(attrs={'type': 'time'}),
            'Seleccion_del_Producto': TimeInput(attrs={'type': 'time'}),
            'Fresa_Entra_a_la_Olla': TimeInput(attrs={'type': 'time'}),
            'Hervor_Inicio': TimeInput(attrs={'type': 'time'}),
            'Introduccion_Azucar': TimeInput(attrs={'type': 'time'}),
            'Introduccion_Limon': TimeInput(attrs={'type': 'time'}),
            'Hervor_Final': TimeInput(attrs={'type': 'time'}),
            'Hora_Licuado': TimeInput(attrs={'type': 'time'}),
            'Hora_Final_Fresa' : TimeInput(attrs={'type': 'time'}),
            'Inicio_de_Empaque' : TimeInput(attrs={'type': 'time'}),
            'Finalizacion_de_la_Canasta' : TimeInput(attrs={'type': 'time'}),
        }

class RegistroFresaBrixForm(forms.ModelForm):
    class Meta:
        model = RegistroFresa
        fields = ['Valor_Primer_Brix', 'Hora_Primer_Brix', 'Valor_Brix_Final', 'Hora_Brix_Final']
        widgets = {
            'Hora_Primer_Brix': TimeInput(attrs={'type': 'time'}),
            'Hora_Brix_Final': TimeInput(attrs={'type': 'time'}),
        }

class RegistroFresaEmpacadosForm(forms.ModelForm):
    class Meta:
        model = RegistroFresa
        fields = ['Producto_Terminado', 'Media_Libra', 'Libra', 'Bolsa_Seis_kg', 'Otro', 'Observaciones']
        widgets = {
            'Observaciones': forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }

class SeleccionarRegistrosFresaForm(forms.Form):
    registros = forms.ModelMultipleChoiceField(queryset=RegistroFresa.objects.all())

class CompararRegistrosFresaForm(forms.Form):
    registrosfresa = forms.ModelMultipleChoiceField(
        queryset=RegistroFresa.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


# Formulario de seleccion de Registro.

class SeleccionTipoCanastaForm(forms.Form):
    TIPOS_CANASTA = (
        ('Mora', 'Canasta de Mora'),
        ('Fresa', 'Canasta de Fresa'),
    )
    tipo_canasta = forms.ChoiceField(label='Tipo de Canasta', choices=TIPOS_CANASTA)
