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