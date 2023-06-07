from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from . import views 

app_name = 'registros'

urlpatterns = [
    
    path('registro_mora/', views.RegistroWizardView.as_view(), name='registro_mora'),
    path('registro_completado_mora/', views.RegistroCompletadoView.as_view(), name='registro_completado_mora'),

]