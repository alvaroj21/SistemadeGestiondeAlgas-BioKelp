# Capacidad Productiva - Documentación

## Cambios Realizados

Se ha actualizado la lógica de capacidad productiva para que funcione de manera automática y coherente con los registros de producción.

## Cómo Funciona Ahora

### 1. Registro de Capacidad Mensual
- El administrador puede establecer la **capacidad máxima mensual** para cada mes
- Solo necesita ingresar:
  - **Mes**: El mes al que corresponde la capacidad
  - **Capacidad Mensual Máxima (kg)**: La capacidad máxima que puede producir la empresa ese mes
  - **Capacidad Anual Máxima (kg)**: Referencia de capacidad anual
  - **Volumen Comprometido (kg)**: Volumen ya comprometido con clientes
  - **Observaciones**: Notas adicionales opcionales

### 2. Cálculo Automático del Volumen Producido
- El **volumen producido** ya NO se ingresa manualmente
- Se calcula automáticamente sumando todos los registros de producción del mes
- Cada vez que se registra una producción en el mes, el volumen producido se actualiza automáticamente

### 3. Visualización del Porcentaje Utilizado
- **% Utilizado** = (Volumen Producido / Capacidad Mensual Máxima) × 100
- Este porcentaje refleja exactamente cuánto de la capacidad mensual se ha utilizado
- Se actualiza automáticamente con cada registro de producción

## Ejemplo de Uso

### Paso 1: Configurar Capacidad del Mes
El administrador registra para enero 2024:
- Capacidad Mensual Máxima: 10,000 kg
- Volumen Comprometido: 2,000 kg

### Paso 2: Registrar Producciones
Durante enero se registran producciones:
- Día 5: 500 kg de alga tipo A
- Día 12: 800 kg de alga tipo B
- Día 20: 600 kg de alga tipo A

**Volumen Producido Total**: 1,900 kg (calculado automáticamente)

### Paso 3: Ver Resultados
En la pantalla de capacidad productiva se mostrará:
- Capacidad Mensual: 10,000 kg
- Volumen Producido: 1,900 kg (automático)
- Disponible: 6,100 kg (10,000 - 2,000 - 1,900)
- **% Utilizado: 19%** (1,900 / 10,000 × 100)

## Ventajas del Nuevo Sistema

1. **Automático**: No es necesario actualizar manualmente el volumen producido
2. **Coherente**: Siempre refleja los registros reales de producción
3. **Preciso**: Elimina errores humanos al ingresar datos manualmente
4. **Tiempo Real**: Se actualiza automáticamente con cada nuevo registro
5. **Simple**: El administrador solo configura la capacidad máxima una vez por mes

## Notas Técnicas

- El cálculo se realiza mediante una propiedad `@property` en el modelo
- Se utiliza `aggregate(Sum('cantidad_cosechada'))` para sumar las producciones
- El filtro de fecha considera todo el mes (del día 1 al último día)
- El campo `volumen_producido` se eliminó de la base de datos (migración 0006)
