# Script para cargar tipos de algas de la zona norte de Chile (Caldera)
# Ejecutar con: Get-Content cargar_algas_caldera.py | python manage.py shell

from gestion_algas.models import TipoAlga

# Tipos de algas comunes en la zona norte de Chile (Caldera)
algas_caldera = [
    {
        'nombre': 'Gracilaria chilensis (Pelillo)',
        'descripcion': 'Alga roja muy abundante en la zona norte, utilizada principalmente para la producción de agar-agar. Crece en zonas rocosas intermareales.',
        'factor_conversion': 1.0,
        'activo': True
    },
    {
        'nombre': 'Lessonia trabeculata (Huiro negro)',
        'descripcion': 'Alga parda de gran tamaño, característica de la zona norte. Importante recurso comercial para la producción de alginatos.',
        'factor_conversion': 1.0,
        'activo': True
    },
    {
        'nombre': 'Macrocystis pyrifera (Huiro)',
        'descripcion': 'Alga parda gigante que forma bosques submarinos. Utilizada para la extracción de alginatos y como alimento.',
        'factor_conversion': 1.0,
        'activo': True
    },
    {
        'nombre': 'Ulva lactuca (Lechuga de mar)',
        'descripcion': 'Alga verde comestible, rica en proteínas y minerales. Se encuentra en zonas intermareales rocosas.',
        'factor_conversion': 1.0,
        'activo': True
    },
    {
        'nombre': 'Durvillaea antarctica (Cochayuyo)',
        'descripcion': 'Alga parda de gran importancia económica y cultural. Utilizada en alimentación humana y producción de alginatos.',
        'factor_conversion': 1.0,
        'activo': True
    },
    {
        'nombre': 'Gelidium chilense (Chasca)',
        'descripcion': 'Alga roja utilizada para la producción de agar de alta calidad. Abundante en zonas rocosas expuestas.',
        'factor_conversion': 1.0,
        'activo': True
    },
    {
        'nombre': 'Chondracanthus chamissoi (Chicoria de mar)',
        'descripcion': 'Alga roja con alto contenido de carragenina. Importante recurso comercial en la zona norte.',
        'factor_conversion': 1.0,
        'activo': True
    },
    {
        'nombre': 'Pyropia columbina (Luche)',
        'descripcion': 'Alga roja comestible, consumida tradicionalmente en Chile. Rica en proteínas y vitaminas.',
        'factor_conversion': 1.0,
        'activo': True
    },
]

# Crear los tipos de algas
for alga_data in algas_caldera:
    alga, created = TipoAlga.objects.get_or_create(
        nombre=alga_data['nombre'],
        defaults={
            'descripcion': alga_data['descripcion'],
            'factor_conversion': alga_data['factor_conversion'],
            'activo': alga_data['activo']
        }
    )
    if created:
        print(f'✓ Creado: {alga.nombre}')
    else:
        print(f'- Ya existe: {alga.nombre}')

print(f'\n✅ Proceso completado. Total de tipos de algas: {TipoAlga.objects.count()}')
