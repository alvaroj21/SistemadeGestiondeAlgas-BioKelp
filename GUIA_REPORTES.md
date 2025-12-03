# Guía Rápida: Sistema de Reportes Personalizados

## ¿Qué puedes hacer?

El sistema de reportes te permite crear informes personalizados para clientes internacionales con:

✅ **Filtros avanzados** - Selecciona tipos de alga, sectores y rangos de fechas específicos  
✅ **Múltiples formatos** - Exporta en PDF, Excel o HTML  
✅ **Conversión de unidades** - Kilogramos, toneladas o libras  
✅ **Gráficos interactivos** - Tendencias mensuales y distribución por tipo  
✅ **Contenido personalizable** - Elige qué información incluir  

## Configurar un nuevo reporte

1. **Accede a "Configuración de Reportes"** desde el menú principal

2. **Completa la información del cliente:**
   - Nombre de empresa
   - País
   - Email de contacto
   - Persona de contacto (opcional)

3. **Selecciona las preferencias:**
   - **Unidad de medida**: kg, toneladas o libras
   - **Formato**: PDF, Excel o ambos
   - **Período**: Número de meses hacia atrás (1-24)

4. **Aplica filtros (opcional):**
   - **Tipos de alga**: Selecciona especies específicas (Ctrl+clic para múltiples)
   - **Sectores**: Escribe sectores separados por comas (ej: "Sector A, Sector B")
   - **Fecha personalizada**: Marca la casilla y elige rango exacto

5. **Elige qué mostrar:**
   - ☑ Capacidad instalada
   - ☑ Disponibilidad
   - ☑ Historial de producción
   - ☑ Gráficos
   - ☑ Observaciones detalladas

6. **Guarda la configuración**

## Generar el reporte

1. En la lista de configuraciones, haz clic en **"Generar"**
2. Según el formato seleccionado:
   - **PDF**: Se descargará automáticamente
   - **Excel**: Se descargará automáticamente  
   - **HTML**: Se mostrará en el navegador (puedes imprimirlo)

## Ejemplos prácticos

### Ejemplo 1: Reporte mensual completo

```
Cliente: SeaFarm International
Formato: PDF
Unidad: Toneladas
Período: 1 mes
Tipos de alga: Todos
Sectores: Todos
Incluir: Capacidad + Disponibilidad + Historial + Gráficos
```

### Ejemplo 2: Análisis de especies específicas

```
Cliente: AlgaeTech Europe
Formato: Excel
Unidad: Kilogramos
Fecha: 01/01/2024 - 30/06/2024
Tipos de alga: Gracilaria, Ulva
Sectores: Sector A
Incluir: Historial + Observaciones
```

### Ejemplo 3: Reporte ejecutivo trimestral

```
Cliente: BioMarine Corp
Formato: PDF y Excel
Unidad: Toneladas
Período: 3 meses
Tipos de alga: Todos
Incluir: Capacidad + Disponibilidad + Gráficos
```

## Instalación de formatos adicionales

Por defecto, los reportes se generan en **HTML** (siempre disponible).

### Para habilitar PDF:

```bash
pip install -r requirements-reportes.txt
```

O individualmente:

```bash
pip install weasyprint
```

### Para habilitar Excel:

```bash
pip install openpyxl
```

### Para ambos:

```bash
pip install weasyprint openpyxl
```

## Permisos por rol

| Acción | Administrador | Socio | Trabajador |
|--------|---------------|-------|------------|
| Ver configuraciones | ✅ | ✅ | ❌ |
| Generar reportes | ✅ | ✅ | ❌ |
| Crear configuraciones | ✅ | ❌ | ❌ |
| Editar configuraciones | ✅ | ❌ | ❌ |
| Eliminar configuraciones | ✅ | ❌ | ❌ |

## Preguntas frecuentes

**¿Puedo editar una configuración existente?**  
Sí, solo administradores. Haz clic en "Editar" junto a la configuración.

**¿Los reportes incluyen datos en tiempo real?**  
Sí, cada vez que generas un reporte se calculan los datos actuales según los filtros configurados.

**¿Puedo tener múltiples configuraciones para el mismo cliente?**  
Sí, puedes crear diferentes configuraciones con distintos filtros y preferencias.

**¿Qué pasa si no tengo WeasyPrint instalado?**  
El sistema mostrará un aviso y generará el reporte en formato HTML automáticamente.

**¿Los gráficos se incluyen en el PDF?**  
Sí, si tienes `mostrar_graficos` activado en la configuración.

**¿Cuántos registros detallados se muestran?**  
Hasta 50 registros más recientes (cuando `incluir_observaciones` está activo).

## Soporte

Para más detalles técnicos, consulta: `REPORTES_PERSONALIZADOS.md`

---

**BioKelp** - Sistema de Gestión de Algas  
Versión 1.0 - Diciembre 2024
