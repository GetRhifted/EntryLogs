from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from . import views 

app_name = 'registros'

urlpatterns = [
    
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('registro_mora/', login_required(views.RegistroWizardView.as_view()), name='registro_mora'),
    path('registro_fresa/', login_required(views.RegistroFresaWizardView.as_view()), name='registro_fresa'),
    path('registro_completado_mora/', login_required(views.RegistroCompletadoView.as_view()), name='registro_completado_mora'),
    path('registro_completado_fresa/', login_required(views.RegistroFresaCompletadoView.as_view()), name='registro_completado_fresa'),
    path('login/', LoginView.as_view(template_name='registros/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro_usuario/', views.RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('resultados_busqueda/', views.ResultadosBusquedaView.as_view(), name='resultados_busqueda'),
    path('editar_registro_mora/<int:pk>/', login_required(views.RegistroUpdateView.as_view()), name='editar_registro_mora'),
    path('editar_registro_mora2/<int:pk>/', login_required(views.RegistroUpdateView2.as_view()), name='editar_registro_mora2'),
    path('editar_registro_mora3/<int:pk>/', login_required(views.RegistroUpdateView3.as_view()), name='editar_registro_mora3'),
    path('editar_registro_mora4/<int:pk>/', login_required(views.RegistroUpdateView4.as_view()), name='editar_registro_mora4'),
    path('editar_registro_mora5/<int:pk>/', login_required(views.RegistroUpdateView5.as_view()), name='editar_registro_mora5'),
    path('editar_registro_mora6/<int:pk>/', login_required(views.RegistroUpdateView6.as_view()), name='editar_registro_mora6'),
    path('editar_registro_fresa/<int:pk>/', login_required(views.RegistroFresaUpdateView.as_view()), name='editar_registro_fresa'),
    path('editar_registro_fresa2/<int:pk>/', login_required(views.RegistroFresaUpdateView2.as_view()), name='editar_registro_fresa2'),
    path('editar_registro_fresa3/<int:pk>/', login_required(views.RegistroFresaUpdateView3.as_view()), name='editar_registro_fresa3'),
    path('editar_registro_fresa4/<int:pk>/', login_required(views.RegistroFresaUpdateView4.as_view()), name='editar_registro_fresa4'),
    path('editar_registro_fresa5/<int:pk>/', login_required(views.RegistroFresaUpdateView5.as_view()), name='editar_registro_fresa5'),
    path('comparar_registros/', login_required(views.CompararRegistrosView.as_view()), name='comparar_registros'),
    path('comparar_registros_fresa/', login_required(views.CompararRegistrosFresaView.as_view()), name='comparar_registros_fresa'),
    path('borrar_registro_mora/<int:pk>/', login_required(views.RegistroDeleteView.as_view()), name='borrar_registro_mora'),
    path('borrar_registro_fresa/<int:pk>/', login_required(views.RegistroFresaDeleteView.as_view()), name='borrar_registro_fresa'),
    path('registro_detallado_mora/<int:pk>/', login_required(views.RegistroDetalladoView.as_view()), name='registro_detallado_mora'),
    path('registro_detallado_fresa/<int:pk>/', login_required(views.RegistroFresaDetalladoView.as_view()), name='registro_detallado_fresa'),
    path('editar_usuario/', login_required(views.UserEditView.as_view()), name='editar_usuario'),

]