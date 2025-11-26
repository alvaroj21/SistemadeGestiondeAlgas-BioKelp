from django.core.management.base import BaseCommand
from gestion_algas.models import TipoAlga
from decimal import Decimal


class Command(BaseCommand):
    help = 'Agrega tipos de alga iniciales a la base de datos'

    def handle(self, *args, **options):
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

        self.stdout.write(self.style.SUCCESS('🌊 Agregando tipos de alga iniciales...'))
        self.stdout.write('-' * 50)

        created_count = 0
        existing_count = 0

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
                self.stdout.write(self.style.SUCCESS(f'✅ Creado: {tipo.nombre}'))
                created_count += 1
            else:
                self.stdout.write(self.style.WARNING(f'ℹ️  Ya existe: {tipo.nombre}'))
                existing_count += 1

        self.stdout.write('-' * 50)
        self.stdout.write(self.style.SUCCESS(f'📊 Creados: {created_count}'))
        self.stdout.write(self.style.WARNING(f'📊 Ya existían: {existing_count}'))
        self.stdout.write(self.style.SUCCESS(f'📊 Total en BD: {TipoAlga.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('✨ ¡Proceso completado!'))
