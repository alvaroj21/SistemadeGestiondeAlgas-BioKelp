# Sistema de Reportes Personalizados - BioKelp

## Descripción General

El sistema de reportes personalizados permite generar informes adaptados a las necesidades de cada cliente internacional, con opciones de filtrado avanzado, múltiples formatos de exportación y visualizaciones gráficas.

## Características Principales

### 1. **Configuración Personalizable**

Cada cliente puede tener una configuración única que incluye:

- **Información del Cliente**
  - Nombre de la empresa
  - País
  - Persona de contacto
  - Email de contacto

- **Preferencias de Formato**
  - Unidad de medida: Kilogramos, Toneladas o Libras
  - Formato de exportación: PDF, Excel o ambos
  - Período de historial: 1-24 meses

### 2. **Filtros Avanzados**

#### Filtros de Tiempo
- **Período Estándar**: Últimos X meses (configurable)
- **Rango Personalizado**: Selección de fechas específicas (desde/hasta)

#### Filtros de Datos
- **Tipos de Alga**: Seleccionar especies específicas o todas
- **Sectores**: Filtrar por sectores de producción específicos (separados por comas)

### 3. **Contenido del Reporte**

Opciones configurables de información a incluir:

- ✅ **Capacidad Instalada**
  - Capacidad mensual y anual máxima
  - Volumen producido
  - Porcentaje utilizado

- ✅ **Disponibilidad**
  - Volumen comprometido
  - Volumen disponible
  - Porcentaje disponible

- ✅ **Historial de Producción**
  - Totales por tipo de alga
  - Número de registros
  - Conversión automática a unidad preferida

- ✅ **Gráficos Interactivos** (Chart.js)
  - Tendencia de producción mensual
  - Distribución por tipo de alga

- ✅ **Registros Detallados**
  - Últimos 50 registros con observaciones
  - Fecha, tipo, cantidad, sector

## Formatos de Exportación

### PDF (WeasyPrint)
- Reporte profesional con estilos personalizados
- Listo para imprimir
- Incluye gráficos si está configurado
- Descarga automática con nombre: `reporte_[EMPRESA]_[FECHA].pdf`

**Requisito**: `pip install weasyprint`

### Excel (openpyxl)
- Formato tabular con estilos profesionales
- Encabezados resaltados
- Fácil de importar en otros sistemas
- Descarga automática con nombre: `reporte_[EMPRESA]_[FECHA].xlsx`

**Requisito**: `pip install openpyxl`

### HTML (Predeterminado)
- Vista web interactiva
- Gráficos dinámicos con Chart.js
- Opción de impresión desde navegador
- No requiere instalaciones adicionales

## Uso del Sistema

### Acceso por Roles

- **Administrador**: Crear, editar, eliminar configuraciones y generar reportes
- **Socio**: Ver configuraciones y generar reportes (solo lectura)
- **Trabajador**: Sin acceso a reportes personalizados

### Crear Nueva Configuración

1. Navegar a **Configuración de Reportes**
2. Completar información del cliente
3. Seleccionar preferencias de formato
4. Configurar filtros (opcional):
   - Seleccionar tipos de alga específicos (Ctrl+clic para múltiples)
   - Indicar sectores separados por comas
   - Activar fecha personalizada si es necesario
5. Elegir qué información incluir
6. Guardar configuración

### Generar Reporte

1. En la lista de configuraciones, hacer clic en **Generar**
2. El sistema aplicará todos los filtros configurados
3. Según el formato elegido:
   - **PDF**: Descarga automática del archivo
   - **Excel**: Descarga automática del archivo
   - **Ambos**: Generará PDF (también disponible en HTML)

## Ejemplos de Uso

### Caso 1: Cliente Internacional (Toneladas, 12 meses)

```
Empresa: SeaFarm International Ltd.
País: Estados Unidos
Email: reports@seafarm.com
Unidad: Toneladas
Formato: PDF y Excel
Período: 12 meses
Tipos de Alga: Todos
Mostrar: Capacidad, Disponibilidad, Historial, Gráficos
```

### Caso 2: Cliente con Filtro Específico

```
Empresa: AlgaeTech Europe
País: Alemania
Unidad: Kilogramos
Formato: Excel
Fecha Personalizada: 01/01/2024 - 30/06/2024
Tipos de Alga: Gracilaria, Ulva
Sectores: Sector A, Sector C
Mostrar: Historial, Observaciones
```

### Caso 3: Reporte Ejecutivo

```
Empresa: BioMarine Corp
País: Japón
Unidad: Toneladas
Formato: PDF
Período: 6 meses
Mostrar: Capacidad, Disponibilidad, Gráficos
Gráficos: Activado
```

## Conversiones de Unidades

El sistema realiza conversiones automáticas:

- **Kilogramos (kg)**: Factor 1.0 (base)
- **Toneladas (ton)**: Factor 0.001 (1 ton = 1000 kg)
- **Libras (lb)**: Factor 2.20462 (1 kg ≈ 2.2 lb)

## Visualizaciones con Chart.js

### Gráfico de Tendencia Mensual
- Tipo: Línea
- Muestra la evolución de la producción mes a mes
- Eje X: Meses
- Eje Y: Cantidad en unidad preferida

### Gráfico de Distribución
- Tipo: Barras
- Compara producción entre tipos de alga
- Colores diferenciados por especie
- Ordenado de mayor a menor producción

## Instalación de Dependencias

### Para generar PDFs:

```bash
pip install weasyprint
```

Dependencias del sistema (Windows):
- GTK3 Runtime (se instala automáticamente con weasyprint)

### Para generar Excel:

```bash
pip install openpyxl
```

### Ambos formatos:

```bash
pip install weasyprint openpyxl
```

## Notas Técnicas

- Los reportes HTML son siempre accesibles sin instalaciones adicionales
- Si WeasyPrint u openpyxl no están instalados, el sistema mostrará un mensaje y renderizará en HTML
- Los gráficos solo aparecen si `mostrar_graficos` está activado en la configuración
- Los registros detallados muestran un máximo de 50 entradas más recientes
- Las fechas se formatean según el estándar chileno: DD/MM/YYYY
- Los datos se filtran en tiempo real según la configuración activa

## Mantenimiento

### Editar Configuración
1. Clic en **Editar** junto a la configuración
2. Modificar campos necesarios
3. Guardar cambios

### Desactivar Configuración
- Desmarcar **Configuración Activa**
- La configuración se mantiene pero no aparece activa en listados

### Eliminar Configuración
- Solo disponible para Administradores
- Clic en **Eliminar** y confirmar
- **Precaución**: Esta acción es irreversible

## Solución de Problemas

### "WeasyPrint no está instalado"
- Ejecutar: `pip install weasyprint`
- Reiniciar el servidor Django

### "openpyxl no está instalado"
- Ejecutar: `pip install openpyxl`
- Reiniciar el servidor Django

### Los gráficos no aparecen
- Verificar que `mostrar_graficos` esté activado
- Verificar que existan datos de `produccion_por_mes`
- Revisar consola del navegador por errores de JavaScript

### El reporte está vacío
- Verificar que los filtros no sean demasiado restrictivos
- Comprobar que existan registros en el período seleccionado
- Revisar que los tipos de alga seleccionados tengan producción

## Mejoras Futuras

- [ ] Envío automático de reportes por email
- [ ] Programación de reportes periódicos
- [ ] Más tipos de gráficos (pastel, área, radar)
- [ ] Exportación a otros formatos (CSV, JSON)
- [ ] Comparativas entre períodos
- [ ] Proyecciones y tendencias con IA
- [ ] Reportes multiidioma
- [ ] Marca de agua personalizada por cliente

## Soporte

Para asistencia técnica o solicitudes de nuevas funcionalidades, contactar al equipo de desarrollo de BioKelp.

---

**Versión**: 1.0  
**Última actualización**: Diciembre 2024
