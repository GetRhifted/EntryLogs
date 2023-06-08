from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, FormView, DeleteView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


from. forms import RegistroGeneralForm, RegistroCanastaForm, RegistroTiemposForm, RegistroDesechosForm, RegistroBrixForm, RegistroEmpacadosForm, CompararRegistrosForm, RegistrodeUsuarioForm, RegistroFresaGeneralForm, RegistroFresaCanastaForm, RegistroFresaTiemposForm, RegistroFresaBrixForm, RegistroFresaEmpacadosForm, CompararRegistrosFresaForm
from. models import Registro, RegistroFresa

from formtools.wizard.views import SessionWizardView

# Vista de Registro de Canasta de Mora.
class RegistroWizardView(SessionWizardView):
    template_name = 'registros/registro_mora.html'
    form_list = [RegistroGeneralForm, RegistroCanastaForm, RegistroTiemposForm, RegistroDesechosForm,
                 RegistroBrixForm, RegistroEmpacadosForm]

    def done(self, form_list, **kwargs):
        Usuario = self.request.user
        cleaned_data = self.get_all_cleaned_data()
        registro = Registro(Usuario=Usuario, **cleaned_data)
        registro.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('registros:registro_completado_mora')

# Vista Detalle del Registro de Canasta de Mora ingresado.    
class RegistroCompletadoView(TemplateView):
    model = Registro
    form_class = RegistroGeneralForm
    template_name = 'registros/registro_completado_mora.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registro'] = Registro.objects.last()
        return context

    def form_valid(self, form):
        # Guarda el registro y asigna la instancia del objeto a la variable 'registro'
        registro = form.save()
        # Agrega el objeto de registro al contexto de la plantilla
        return render(self.request, self.template_name, {'registro': registro})

# Vista de Creacion de Usuarios.    
class RegistroUsuarioView(SuccessMessageMixin, CreateView):
    template_name = 'registros/registro_usuario.html'
    form_class = RegistrodeUsuarioForm
    success_url = reverse_lazy('registros:home')
    success_message = "Usuario %(username)s creado"

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data['username']
        messages.success(self.request, self.success_message % {'username': username})
        return response
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for field in self.form_class.base_fields.values():
            field.help_text = ''

# Vista de Inicio de Sesion.
class LoginView(LoginView):
    template_name = 'registros/login.html'
    success_url = reverse_lazy('registros:home')

# Vista de Cierre de Sesion.
class MiLogoutView(LogoutView):
    next_page = reverse_lazy('registros:login')

# Vista de Pagina Principal.
class HomeView(ListView):
    template_name = 'registros/home.html'
    context_object_name = 'registros_mora'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registros_fresa'] = RegistroFresa.objects.all().order_by('-id')[:10]
        return context

    def get_queryset(self):
        return Registro.objects.all().order_by('-id')[:10]
    
# Vista para borrar Registros de Canastas de Mora.
class RegistroDeleteView(DeleteView):
    model = Registro
    template_name = 'registros/borrar_registro_mora.html'
    success_url = reverse_lazy('registros:home')

class RegistroUpdateView(LoginRequiredMixin, UpdateView):
     model = Registro
     form_class = RegistroGeneralForm
     template_name = 'registros/edicion_registro_mora.html'

     def dispatch(self, request, *args, **kwargs):
            obj = self.get_object()
            if obj.created_by != request.user:
                raise PermissionDenied
            return super().dispatch(request, *args, **kwargs)
     
     def get_success_url(self):
        return reverse_lazy('registros:home', kwargs={'pk': self.object.pk})
     
class RegistroDetalladoView(DetailView):
    model = Registro
    template_name = 'registros/registro_detallado_mora.html'