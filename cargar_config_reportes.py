# Script para cargar configuraciones de reportes de ejemplo
# Ejecutar con: Get-Content cargar_config_reportes.py | python manage.py shell

from gestion_algas.models import ConfiguracionReporte, TipoAlga

# Obtener algunos tipos de alga para los filtros
algas = list(TipoAlga.objects.filter(activo=True))

# Configuraciones de reportes para diferentes clientes internacionales
configuraciones = [
    {
        'empresa': 'SeaFarm International Ltd.',
        'pais': 'Estados Unidos',
        'contacto': 'John Smith',
        'email': 'jsmith@seafarm.com',
        'unidad_medida': 'ton',
        'formato_preferido': 'pdf',
        'mostrar_capacidad_instalada': True,
        'mostrar_disponibilidad': True,
        'mostrar_historial_produccion': True,
        'periodo_historial_meses': 12,
        'mostrar_graficos': True,
        'incluir_observaciones': False,
        'activo': True,
    },
    {
        'empresa': 'AlgaeTech Europe',
        'pais': 'Alemania',
        'contacto': 'Hans Mueller',
        'email': 'h.mueller@algaetech.de',
        'unidad_medida': 'kg',
        'formato_preferido': 'excel',
        'mostrar_capacidad_instalada': True,
        'mostrar_disponibilidad': False,
        'mostrar_historial_produccion': True,
        'periodo_historial_meses': 6,
        'sectores_especificos': 'Sector A, Sector B',
        'mostrar_graficos': False,
        'incluir_observaciones': True,
        'activo': True,
    },
    {
        'empresa': 'BioMarine',
        'pais': 'Japón',
        'contacto': 'Yuki Tanaka',
        'email': 'y.tanaka@biomarine.jp',
        'unidad_medida': 'ton',
        'formato_preferido': 'ambos',
        'mostrar_capacidad_instalada': True,
        'mostrar_disponibilidad': True,
        'mostrar_historial_produccion': True,
        'periodo_historial_meses': 3,
        'mostrar_graficos': True,
        'incluir_observaciones': False,
        'activo': True,
    },
    {
        'empresa': 'Pacific Kelp Industries',
        'pais': 'Canadá',
        'contacto': 'Sarah Johnson',
        'email': 'sjohnson@pacifickelp.ca',
        'unidad_medida': 'lb',
        'formato_preferido': 'pdf',
        'mostrar_capacidad_instalada': False,
        'mostrar_disponibilidad': False,
        'mostrar_historial_produccion': True,
        'periodo_historial_meses': 6,
        'mostrar_graficos': True,
        'incluir_observaciones': False,
        'activo': True,
    },
    {
        'empresa': 'Harvest Solutions',
        'pais': 'Noruega',
        'contacto': 'Erik Hansen',
        'email': 'e.hansen@marineharvest.no',
        'unidad_medida': 'kg',
        'formato_preferido': 'excel',
        'mostrar_capacidad_instalada': True,
        'mostrar_disponibilidad': True,
        'mostrar_historial_produccion': True,
        'periodo_historial_meses': 24,
        'mostrar_graficos': False,
        'incluir_observaciones': True,
        'activo': True,
    },
]

print('Creando configuraciones de reportes...\n')
creados = 0

for config_data in configuraciones:
    config, created = ConfiguracionReporte.objects.get_or_create(
        empresa=config_data['empresa'],
        defaults=config_data
    )
    
    if created:
        # Si hay tipos de alga específicos para algunos clientes
        if config.empresa == 'AlgaeTech Europe GmbH' and len(algas) >= 2:
            # Solo Gracilaria y Lessonia para este cliente
            tipos_especificos = [a for a in algas if 'Gracilaria' in a.nombre or 'Lessonia' in a.nombre][:2]
            if tipos_especificos:
                config.tipos_alga.set(tipos_especificos)
        
        print(f'✓ Creado: {config.empresa} ({config.pais})')
        print(f'  - Formato: {config.get_formato_preferido_display()}')
        print(f'  - Unidad: {config.get_unidad_medida_display()}')
        print(f'  - Período: {config.periodo_historial_meses} meses')
        print(f'  - Gráficos: {"Sí" if config.mostrar_graficos else "No"}')
        print()
        creados += 1
    else:
        print(f'- Ya existe: {config.empresa}')

print(f'✅ Proceso completado!')
print(f'📋 Total de configuraciones creadas: {creados}')
print(f'📊 Total en sistema: {ConfiguracionReporte.objects.count()}')
