# Script para cargar datos de ejemplo de registros de producción
# Ejecutar con: Get-Content cargar_produccion_ejemplo.py | python manage.py shell

from gestion_algas.models import Usuario, TipoAlga, RegistroProduccion
from datetime import datetime, timedelta
from decimal import Decimal
import random

# Obtener usuario administrador
try:
    usuario = Usuario.objects.filter(rol='Administrador').first()
    if not usuario:
        print('❌ No se encontró un usuario administrador. Crear uno primero.')
        exit()
except Exception as e:
    print(f'❌ Error al obtener usuario: {e}')
    exit()

# Obtener tipos de algas
algas = list(TipoAlga.objects.filter(activo=True))
if not algas:
    print('❌ No hay tipos de algas registrados. Ejecutar cargar_algas_caldera.py primero.')
    exit()

# Sectores de producción
sectores = ['Sector A', 'Sector B', 'Sector C', 'Sector D']

# Observaciones de ejemplo
observaciones_ejemplos = [
    'Cosecha en óptimas condiciones',
    'Buena calidad del producto',
    'Alga en estado de madurez ideal',
    'Condiciones climáticas favorables',
    'Producción según lo planificado',
    'Excelente rendimiento',
    'Calidad superior',
    'Sin observaciones',
    'Cosecha matinal',
    'Producto de exportación',
]

# Generar registros de los últimos 6 meses
print('Generando registros de producción...\n')
registros_creados = 0
fecha_actual = datetime.now()

for dias_atras in range(180, 0, -5):  # Cada 5 días durante 6 meses
    fecha = fecha_actual - timedelta(days=dias_atras)
    
    # Generar 2-4 registros por día (diferentes tipos de alga)
    num_registros = random.randint(2, 4)
    algas_del_dia = random.sample(algas, min(num_registros, len(algas)))
    
    for alga in algas_del_dia:
        # Cantidad aleatoria según el tipo de alga
        if 'Huiro' in alga.nombre or 'Cochayuyo' in alga.nombre:
            cantidad = Decimal(str(random.uniform(500, 2000)))  # Algas grandes
        elif 'Pelillo' in alga.nombre or 'Chasca' in alga.nombre:
            cantidad = Decimal(str(random.uniform(200, 800)))   # Algas medianas
        else:
            cantidad = Decimal(str(random.uniform(100, 500)))   # Algas pequeñas
        
        sector = random.choice(sectores)
        observaciones = random.choice(observaciones_ejemplos)
        
        registro = RegistroProduccion.objects.create(
            usuario=usuario,
            tipo_alga=alga,
            cantidad_cosechada=cantidad,
            sector=sector,
            fecha_registro=fecha,
            observaciones=observaciones
        )
        
        registros_creados += 1
        if registros_creados % 10 == 0:
            print(f'✓ {registros_creados} registros creados...')

print(f'\n✅ Proceso completado!')
print(f'📊 Total de registros de producción creados: {registros_creados}')
print(f'📅 Período: {(fecha_actual - timedelta(days=180)).strftime("%d/%m/%Y")} - {fecha_actual.strftime("%d/%m/%Y")}')

# Estadísticas
total_kg = sum(r.cantidad_cosechada for r in RegistroProduccion.objects.all())
print(f'⚖️  Total producido: {total_kg:.2f} kg')
print(f'🌊 Tipos de alga con producción: {RegistroProduccion.objects.values("tipo_alga").distinct().count()}')
