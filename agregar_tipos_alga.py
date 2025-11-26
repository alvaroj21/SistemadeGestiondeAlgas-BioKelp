# Script para agregar tipos de alga iniciales
# Ejecutar con: python manage.py shell < agregar_tipos_alga.py

from gestion_algas.models import TipoAlga
from decimal import Decimal

# Tipos de alga comunes en Chile
tipos_iniciales = [
    {
        'nombre': 'Cochayuyo',
        'factor_conversion': Decimal('1.00'),
        'descripcion': 'Alga parda comestible, muy común en Chile. Se usa en gastronomía.',
        'activo': True
    },
    {
        'nombre': 'Luche',
        'factor_conversion': Decimal('1.00'),
        'descripcion': 'Alga roja comestible típica de Chile, popular en preparaciones tradicionales.',
        'activo': True
    },
    {
        'nombre': 'Pelillo',
        'factor_conversion': Decimal('1.00'),
        'descripcion': 'Alga utilizada principalmente para extracción de carragenina.',
        'activo': True
    },
    {
        'nombre': 'Huiro',
        'factor_conversion': Decimal('1.00'),
        'descripcion': 'Alga parda de gran tamaño, usada en alimentación y procesos industriales.',
        'activo': True
    },
    {
        'nombre': 'Ulte',
        'factor_conversion': Decimal('1.00'),
        'descripcion': 'Alga de uso gastronómico y medicinal.',
        'activo': True
    },
]

print("🌊 Agregando tipos de alga iniciales...")
print("-" * 50)

for tipo_data in tipos_iniciales:
    tipo, created = TipoAlga.objects.get_or_create(
        nombre=tipo_data['nombre'],
        defaults={
            'factor_conversion': tipo_data['factor_conversion'],
            'descripcion': tipo_data['descripcion'],
            'activo': tipo_data['activo']
        }
    )
    
    if created:
        print(f"✅ Creado: {tipo.nombre}")
    else:
        print(f"ℹ️  Ya existe: {tipo.nombre}")

print("-" * 50)
print(f"📊 Total de tipos de alga en BD: {TipoAlga.objects.count()}")
print("✨ ¡Proceso completado!")
