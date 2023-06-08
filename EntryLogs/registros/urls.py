from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from . import views 

app_name = 'registros'

urlpatterns = [
    
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('registro_mora/', login_required(views.RegistroWizardView.as_view()), name='registro_mora'),
    path('registro_completado_mora/', login_required(views.RegistroCompletadoView.as_view()), name='registro_completado_mora'),
    path('login/', LoginView.as_view(template_name='registros/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro_usuario/', views.RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('editar_registro_mora/<int:pk>/', login_required(views.RegistroUpdateView.as_view()), name='editar_registro_mora'),
    path('borrar_registro_mora/<int:pk>/', login_required(views.RegistroDeleteView.as_view()), name='borrar_registro_mora'),
    path('registro_detallado_mora/<int:pk>/', login_required(views.RegistroDetalladoView.as_view()), name='registro_detallado_mora'),
    path('editar_usuario/', login_required(views.UserEditView.as_view()), name='editar_usuario'),

]