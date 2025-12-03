"""
Modelos de la aplicación de gestión de algas
"""
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Usuario(models.Model):
    """
    Modelo de usuario del sistema con roles específicos
    
    ROLES Y PERMISOS:
    - Administrador: Acceso total al sistema
    - Trabajador: Gestión de producción y registros
    - Socio: Visualización de reportes y capacidad productiva
    """
    ROLES_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Trabajador', 'Trabajador'),
        ('Socio', 'Socio'),
    ]
    
    username = models.CharField(
        max_length=45,
        unique=True,
        verbose_name='Nombre de Usuario'
    )
    password = models.CharField(
        max_length=128,
        verbose_name='Contraseña'
    )
    email = models.EmailField(
        max_length=45,
        verbose_name='Correo Electrónico'
    )
    telefono = models.CharField(
        max_length=15,
        verbose_name='Teléfono'
    )
    rol = models.CharField(
        max_length=45,
        choices=ROLES_CHOICES,
        verbose_name='Rol'
    )
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']
    
    def __str__(self):
        return f"{self.username} - {self.rol}"
    
    def es_admin(self):
        return self.rol == 'Administrador'
    
    def es_trabajador(self):
        return self.rol == 'Trabajador'
    
    def es_socio(self):
        return self.rol == 'Socio'


class TipoAlga(models.Model):
    """
    Catálogo de tipos de algas disponibles en el sistema
    """
    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nombre'
    )
    factor_conversion = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('1.00'),
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Factor de Conversión',
        help_text='Factor para cálculos de conversión'
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descripción'
    )
    activo = models.BooleanField(
        default=True,
        verbose_name='Activo'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación'
    )
    
    class Meta:
        verbose_name = 'Tipo de Alga'
        verbose_name_plural = 'Tipos de Algas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class RegistroProduccion(models.Model):
    """
    Registro diario de producción de algas
    """
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='registros_produccion',
        verbose_name='Usuario'
    )
    tipo_alga = models.ForeignKey(
        TipoAlga,
        on_delete=models.PROTECT,
        related_name='registros',
        verbose_name='Tipo de Alga'
    )
    cantidad_cosechada = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Cantidad Cosechada (kg)',
        help_text='Cantidad en kilogramos'
    )
    sector = models.CharField(
        max_length=100,
        verbose_name='Sector de Cosecha'
    )
    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observaciones'
    )
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Registro'
    )
    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Modificación'
    )
    
    class Meta:
        verbose_name = 'Registro de Producción'
        verbose_name_plural = 'Registros de Producción'
        ordering = ['-fecha_registro']
        indexes = [
            models.Index(fields=['-fecha_registro']),
            models.Index(fields=['usuario', '-fecha_registro']),
            models.Index(fields=['tipo_alga', '-fecha_registro']),
        ]
    
    def __str__(self):
        return f"{self.tipo_alga} - {self.cantidad_cosechada}kg ({self.fecha_registro.strftime('%d/%m/%Y')})"
    
    @property
    def cantidad_con_factor(self):
        """Cantidad ajustada con el factor de conversión"""
        return self.cantidad_cosechada * self.tipo_alga.factor_conversion
    
    def get_info_completa(self):
        """Retorna información completa del registro (sin volumen_procesado)"""
        return {
            'id': self.id,
            'usuario': self.usuario.username,
            'tipo_alga': self.tipo_alga.nombre,
            'cantidad_cosechada': self.cantidad_cosechada,
            'sector': self.sector,
            'fecha_registro': self.fecha_registro,
            'observaciones': self.observaciones
        }


class CapacidadProductiva(models.Model):
    """
    Modelo para registrar la capacidad productiva instalada y disponibilidad
    """
    mes = models.DateField(
        verbose_name='Mes',
        help_text='Primer día del mes para el registro de capacidad'
    )
    capacidad_mensual_maxima = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name='Capacidad Mensual Máxima (kg)',
        help_text='Capacidad máxima de producción mensual en kilogramos'
    )
    capacidad_anual_maxima = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name='Capacidad Anual Máxima (kg)',
        help_text='Capacidad máxima de producción anual en kilogramos'
    )
    volumen_producido = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name='Volumen Producido (kg)',
        help_text='Volumen producido en el mes'
    )
    volumen_comprometido = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name='Volumen Comprometido (kg)',
        help_text='Volumen ya comprometido con clientes'
    )
    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observaciones'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación'
    )
    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Modificación'
    )
    
    class Meta:
        verbose_name = 'Capacidad Productiva'
        verbose_name_plural = 'Capacidades Productivas'
        ordering = ['-mes']
        unique_together = [['mes']]
        indexes = [
            models.Index(fields=['-mes']),
        ]
    
    def __str__(self):
        return f"Capacidad {self.mes.strftime('%m/%Y')} - {self.capacidad_mensual_maxima}kg"
    
    @property
    def disponibilidad_mensual(self):
        """Capacidad disponible no comprometida"""
        return self.capacidad_mensual_maxima - self.volumen_comprometido - self.volumen_producido
    
    @property
    def porcentaje_utilizado(self):
        """Porcentaje de capacidad utilizada"""
        if self.capacidad_mensual_maxima > 0:
            return round((self.volumen_producido / self.capacidad_mensual_maxima) * 100, 2)
        return Decimal('0.00')
    
    @property
    def porcentaje_disponible(self):
        """Porcentaje de capacidad disponible"""
        if self.capacidad_mensual_maxima > 0:
            return round((self.disponibilidad_mensual / self.capacidad_mensual_maxima) * 100, 2)
        return Decimal('0.00')


class ConfiguracionReporte(models.Model):
    """
    Configuración personalizada de reportes para clientes internacionales
    """
    UNIDADES_MEDIDA = [
        ('kg', 'Kilogramos (kg)'),
        ('ton', 'Toneladas (ton)'),
        ('lb', 'Libras (lb)'),
    ]
    
    FORMATOS_REPORTE = [
        ('pdf', 'PDF'),
        ('excel', 'Excel'),
        ('ambos', 'PDF y Excel'),
    ]
    
    empresa = models.CharField(
        max_length=200,
        verbose_name='Nombre de la Empresa',
        help_text='Nombre del cliente internacional'
    )
    pais = models.CharField(
        max_length=100,
        verbose_name='País',
        help_text='País del cliente'
    )
    contacto = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Persona de Contacto'
    )
    email = models.EmailField(
        verbose_name='Email de Contacto'
    )
    unidad_medida = models.CharField(
        max_length=10,
        choices=UNIDADES_MEDIDA,
        default='kg',
        verbose_name='Unidad de Medida Preferida'
    )
    formato_preferido = models.CharField(
        max_length=10,
        choices=FORMATOS_REPORTE,
        default='pdf',
        verbose_name='Formato de Reporte Preferido'
    )
    mostrar_capacidad_instalada = models.BooleanField(
        default=True,
        verbose_name='Mostrar Capacidad Instalada',
        help_text='Incluir información de capacidad productiva'
    )
    mostrar_disponibilidad = models.BooleanField(
        default=True,
        verbose_name='Mostrar Disponibilidad',
        help_text='Incluir información de disponibilidad mensual'
    )
    mostrar_historial_produccion = models.BooleanField(
        default=True,
        verbose_name='Mostrar Historial de Producción',
        help_text='Incluir historial de producción reciente'
    )
    periodo_historial_meses = models.IntegerField(
        default=6,
        validators=[MinValueValidator(1)],
        verbose_name='Período de Historial (meses)',
        help_text='Número de meses de historial a incluir'
    )
    # Filtros personalizables
    tipos_alga = models.ManyToManyField(
        TipoAlga,
        blank=True,
        verbose_name='Tipos de Alga',
        help_text='Selecciona tipos específicos (vacío = todos)'
    )
    sectores_especificos = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Sectores Específicos',
        help_text='Sectores separados por comas (vacío = todos)'
    )
    usar_fecha_personalizada = models.BooleanField(
        default=False,
        verbose_name='Usar Rango de Fecha Personalizado',
        help_text='Si está activo, ignora el período de historial'
    )
    fecha_desde = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha Desde',
        help_text='Fecha inicial del reporte personalizado'
    )
    fecha_hasta = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha Hasta',
        help_text='Fecha final del reporte personalizado'
    )
    # Opciones de visualización
    mostrar_graficos = models.BooleanField(
        default=True,
        verbose_name='Mostrar Gráficos',
        help_text='Incluir gráficos de tendencias y comparativas'
    )
    incluir_observaciones = models.BooleanField(
        default=False,
        verbose_name='Incluir Observaciones',
        help_text='Mostrar observaciones de cada registro'
    )
    activo = models.BooleanField(
        default=True,
        verbose_name='Configuración Activa'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación'
    )
    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Modificación'
    )
    
    class Meta:
        verbose_name = 'Configuración de Reporte'
        verbose_name_plural = 'Configuraciones de Reportes'
        ordering = ['-fecha_creacion']
        indexes = [
            models.Index(fields=['empresa']),
            models.Index(fields=['activo']),
        ]
    
    def __str__(self):
        return f"Reporte para {self.empresa} ({self.pais})"


class ControlAcceso(models.Model):
    """
    Registro de accesos al sistema para auditoría
    """
    TIPOS_ACCESO = [
        ('login_exitoso', 'Login Exitoso'),
        ('login_fallido', 'Login Fallido'),
        ('logout', 'Logout'),
        ('acceso_denegado', 'Acceso Denegado'),
    ]
    
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='accesos',
        verbose_name='Usuario'
    )
    ip_origen = models.GenericIPAddressField(
        verbose_name='IP de Origen'
    )
    tipo_acceso = models.CharField(
        max_length=50,
        choices=TIPOS_ACCESO,
        verbose_name='Tipo de Acceso'
    )
    fecha_acceso = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Acceso'
    )
    detalles = models.TextField(
        blank=True,
        null=True,
        verbose_name='Detalles'
    )
    
    class Meta:
        verbose_name = 'Control de Acceso'
        verbose_name_plural = 'Control de Accesos'
        ordering = ['-fecha_acceso']
        indexes = [
            models.Index(fields=['-fecha_acceso']),
            models.Index(fields=['usuario', '-fecha_acceso']),
        ]
    
    def __str__(self):
        return f"{self.get_tipo_acceso_display()} - {self.ip_origen} ({self.fecha_acceso.strftime('%d/%m/%Y %H:%M')})"
