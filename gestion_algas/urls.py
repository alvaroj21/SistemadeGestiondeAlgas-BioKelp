# -*- coding: utf-8 -*-
"""
URLs de la aplicación de gestión de algas
"""
from django.urls import path
from . import views

urlpatterns = [
    # Autenticación
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Producción
    path('registro/', views.registro_produccion, name='registro_produccion'),
    path('registro/eliminar/<int:registro_id>/', views.eliminar_registro, name='eliminar_registro'),
    
    # Reportes
    path('reportes/', views.reportes, name='reportes'),
    path('reportes/pdf-semanal/', views.generar_pdf_semanal, name='generar_pdf_semanal'),
    
    # Usuarios
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    
    # Perfil de Usuario
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    
    # Tipos de Alga
    path('tipos-alga/', views.tipos_alga, name='tipos_alga'),
    path('tipos-alga/editar/<int:tipo_id>/', views.editar_tipo_alga, name='editar_tipo_alga'),
    path('tipos-alga/eliminar/<int:tipo_id>/', views.eliminar_tipo_alga, name='eliminar_tipo_alga'),
    path('tipos-alga/toggle/<int:tipo_id>/', views.toggle_tipo_alga, name='toggle_tipo_alga'),
    
    # Capacidad Productiva
    path('capacidad/', views.capacidad_productiva, name='capacidad_productiva'),
    path('capacidad/editar/<int:capacidad_id>/', views.editar_capacidad, name='editar_capacidad'),
    path('capacidad/eliminar/<int:capacidad_id>/', views.eliminar_capacidad, name='eliminar_capacidad'),
    
    # Configuración de Reportes
    path('configuracion-reportes/', views.configuracion_reportes, name='configuracion_reportes'),
    path('configuracion-reportes/editar/<int:config_id>/', views.editar_configuracion, name='editar_configuracion'),
    path('configuracion-reportes/eliminar/<int:config_id>/', views.eliminar_configuracion, name='eliminar_configuracion'),
    path('reportes/personalizado/<int:config_id>/', views.generar_reporte_personalizado, name='generar_reporte_personalizado'),
    
    # API
    path('api/produccion-semanal/', views.api_produccion_semanal, name='api_produccion_semanal'),
]
