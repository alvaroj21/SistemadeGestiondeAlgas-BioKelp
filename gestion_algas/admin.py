"""
Configuración del panel de administración de Django
"""
from django.contrib import admin
from .models import Usuario, TipoAlga, RegistroProduccion, ControlAcceso, CapacidadProductiva, ConfiguracionReporte


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    """Administración de usuarios con rol personalizado"""
    list_display = ['username', 'email', 'telefono', 'rol']
    list_filter = ['rol']
    search_fields = ['username', 'email']
    ordering = ['username']
    
    fieldsets = (
        ('Credenciales', {
            'fields': ('username', 'password')
        }),
        ('Información Personal', {
            'fields': ('email', 'telefono')
        }),
        ('Permisos', {
            'fields': ('rol',)
        }),
    )
    
    add_fieldsets = (
        ('Credenciales', {
            'fields': ('username', 'password')
        }),
        ('Información Personal', {
            'fields': ('email', 'telefono')
        }),
        ('Permisos', {
            'fields': ('rol',)
        }),
    )


@admin.register(TipoAlga)
class TipoAlgaAdmin(admin.ModelAdmin):
    """Administración de tipos de algas"""
    list_display = ['nombre', 'factor_conversion', 'activo', 'fecha_creacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    ordering = ['nombre']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Configuración', {
            'fields': ('factor_conversion', 'activo')
        }),
    )


@admin.register(RegistroProduccion)
class RegistroProduccionAdmin(admin.ModelAdmin):
    """Administración de registros de producción"""
    list_display = ['fecha_registro', 'usuario', 'tipo_alga', 'cantidad_cosechada', 'sector']
    list_filter = ['fecha_registro', 'tipo_alga', 'usuario']
    search_fields = ['sector', 'observaciones', 'usuario__username', 'tipo_alga__nombre']
    date_hierarchy = 'fecha_registro'
    ordering = ['-fecha_registro']
    
    fieldsets = (
        ('Información del Registro', {
            'fields': ('usuario', 'tipo_alga', 'sector')
        }),
        ('Datos de Producción', {
            'fields': ('cantidad_cosechada', 'observaciones')
        }),
        ('Metadata', {
            'fields': ('fecha_registro', 'fecha_modificacion'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['fecha_registro', 'fecha_modificacion']


@admin.register(ControlAcceso)
class ControlAccesoAdmin(admin.ModelAdmin):
    """Administración de control de accesos"""
    list_display = ['fecha_acceso', 'usuario', 'tipo_acceso', 'ip_origen']
    list_filter = ['tipo_acceso', 'fecha_acceso']
    search_fields = ['usuario__username', 'ip_origen', 'detalles']
    date_hierarchy = 'fecha_acceso'
    ordering = ['-fecha_acceso']
    
    readonly_fields = ['usuario', 'ip_origen', 'tipo_acceso', 'fecha_acceso', 'detalles']
    
    def has_add_permission(self, request):
        """No permitir agregar accesos manualmente"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Solo superusuarios pueden eliminar"""
        return request.user.is_superuser


@admin.register(CapacidadProductiva)
class CapacidadProductivaAdmin(admin.ModelAdmin):
    """Administración de capacidad productiva"""
    list_display = ['mes', 'capacidad_mensual_maxima', 'volumen_producido', 'volumen_comprometido', 'disponibilidad_mensual', 'porcentaje_utilizado']
    list_filter = ['mes']
    search_fields = ['observaciones']
    ordering = ['-mes']
    
    fieldsets = (
        ('Período', {
            'fields': ('mes',)
        }),
        ('Capacidad', {
            'fields': ('capacidad_mensual_maxima', 'capacidad_anual_maxima')
        }),
        ('Producción', {
            'fields': ('volumen_producido', 'volumen_comprometido', 'observaciones')
        }),
        ('Metadata', {
            'fields': ('fecha_creacion', 'fecha_modificacion'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']
    
    def disponibilidad_mensual(self, obj):
        """Mostrar disponibilidad calculada"""
        return f"{obj.disponibilidad_mensual:.2f} kg"
    disponibilidad_mensual.short_description = 'Disponibilidad'
    
    def porcentaje_utilizado(self, obj):
        """Mostrar porcentaje utilizado"""
        return f"{obj.porcentaje_utilizado}%"
    porcentaje_utilizado.short_description = '% Utilizado'


@admin.register(ConfiguracionReporte)
class ConfiguracionReporteAdmin(admin.ModelAdmin):
    """Administración de configuraciones de reportes"""
    list_display = ['empresa', 'pais', 'email', 'unidad_medida', 'formato_preferido', 'activo', 'fecha_creacion']
    list_filter = ['activo', 'unidad_medida', 'formato_preferido', 'pais']
    search_fields = ['empresa', 'pais', 'contacto', 'email']
    ordering = ['-fecha_creacion']
    
    fieldsets = (
        ('Información del Cliente', {
            'fields': ('empresa', 'pais', 'contacto', 'email')
        }),
        ('Preferencias de Reporte', {
            'fields': ('unidad_medida', 'formato_preferido', 'periodo_historial_meses')
        }),
        ('Contenido del Reporte', {
            'fields': ('mostrar_capacidad_instalada', 'mostrar_disponibilidad', 'mostrar_historial_produccion')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
        ('Metadata', {
            'fields': ('fecha_creacion', 'fecha_modificacion'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']
