# Gestión de Tipos de Alga

## ¿Qué es?

El módulo de **Tipos de Alga** permite al administrador gestionar el catálogo de tipos de algas que se pueden registrar en el sistema de producción.

## ¿Por qué es importante?

Antes de poder registrar producción, **DEBES tener al menos un tipo de alga creado y activo** en el sistema. Sin tipos de alga, el formulario de registro de producción estará vacío.

## Acceso

- **Ruta:** `/tipos-alga/`
- **Menú:** Navegación → "Tipos de Alga" (solo visible para Administradores)
- **Permisos:** Solo los usuarios con rol **Administrador** pueden gestionar tipos de alga

## Funcionalidades

### 1. Crear Tipo de Alga

**Campos obligatorios:**
- **Nombre:** Nombre del tipo de alga (ej: Cochayuyo, Luche, Pelillo)
- **Factor de Conversión:** Número decimal para cálculos especiales (por defecto 1.00)

**Campos opcionales:**
- **Descripción:** Información adicional sobre el tipo de alga
- **Activo:** Marca si el tipo está activo o no (solo los activos aparecen en registro de producción)

**Cómo crear:**
1. Ir a "Tipos de Alga" en el menú
2. Llenar el formulario del lado izquierdo
3. Click en "➕ Crear Tipo de Alga"

### 2. Editar Tipo de Alga

**Cómo editar:**
1. En la tabla de tipos de alga, click en el botón ✏️ (editar)
2. Modificar los campos necesarios
3. Click en "💾 Actualizar Tipo de Alga"

### 3. Activar/Desactivar Tipo de Alga

**Cómo activar/desactivar:**
1. En la tabla, click en el botón 🔒/🔓
2. El estado cambiará automáticamente

**Importante:**
- Los tipos **inactivos NO aparecen** en el formulario de registro de producción
- Útil para tipos de alga que ya no se cosechan pero tienen registros históricos

### 4. Eliminar Tipo de Alga

**Cómo eliminar:**
1. En la tabla, click en el botón 🗑️
2. Confirmar la eliminación

**Importante:**
- **NO se puede eliminar** un tipo de alga que tenga registros de producción asociados
- En su lugar, puedes **desactivarlo**

## Tipos de Alga Iniciales

El sistema viene con 5 tipos de alga precargados (típicos de Chile):

1. **Cochayuyo** - Alga parda comestible
2. **Luche** - Alga roja comestible típica
3. **Pelillo** - Alga para extracción de carragenina
4. **Huiro** - Alga parda de gran tamaño
5. **Ulte** - Alga de uso gastronómico y medicinal

### Agregar tipos iniciales manualmente

Si necesitas volver a agregar los tipos iniciales, ejecuta:

```bash
python manage.py crear_tipos_alga
```

## Flujo de Trabajo Recomendado

### Primera vez usando el sistema:

1. ✅ **Paso 1:** Iniciar sesión como Administrador
2. ✅ **Paso 2:** Ir a "Tipos de Alga" y crear al menos un tipo
3. ✅ **Paso 3:** Ahora ya puedes ir a "Registrar Producción"

### Uso diario:

1. Los **Trabajadores** solo necesitan ir a "Registrar Producción"
2. El selector de "Tipo de Alga" mostrará todos los tipos activos
3. Si no aparece ningún tipo, contactar al Administrador

## Ejemplos de Uso

### Ejemplo 1: Agregar un nuevo tipo de alga

```
Nombre: Agar-agar
Factor de Conversión: 1.00
Descripción: Alga roja utilizada como gelificante natural en la industria alimentaria
Activo: ✓
```

### Ejemplo 2: Desactivar un tipo que ya no se cosecha

Si dejaste de cosechar "Pelillo" pero tienes registros históricos:

1. Click en 🔒 junto a "Pelillo"
2. El estado cambiará a "Inactivo"
3. Ya no aparecerá en el formulario de registro
4. Los registros históricos se mantienen intactos

## Tabla de Estados

| Badge | Estado | Visible en Registro | Se puede eliminar |
|-------|--------|---------------------|-------------------|
| 🟢 Activo | Activo | ✅ Sí | ❌ Solo si no tiene registros |
| ⚫ Inactivo | Inactivo | ❌ No | ❌ Solo si no tiene registros |

## Preguntas Frecuentes

### ❓ No puedo registrar producción, el selector está vacío

**Respuesta:** Necesitas crear al menos un tipo de alga activo. Solo los administradores pueden hacerlo.

**Solución:**
1. Iniciar sesión como Administrador
2. Ir a "Tipos de Alga"
3. Crear un tipo o activar uno existente

### ❓ ¿Por qué no puedo eliminar un tipo de alga?

**Respuesta:** El tipo tiene registros de producción asociados.

**Solución:** En lugar de eliminarlo, desactívalo para que no aparezca en nuevos registros.

### ❓ ¿Qué es el factor de conversión?

**Respuesta:** Es un número que se usa para cálculos especiales según el tipo de alga. Por defecto es 1.00.

**Ejemplo:** Si un alga tiene un factor de 1.5 y registras 100kg, el sistema calculará internamente 150kg para ciertos reportes.

### ❓ ¿Puedo tener tipos con el mismo nombre?

**Respuesta:** No, cada tipo de alga debe tener un nombre único.

## Permisos por Rol

| Acción | Administrador | Trabajador | Socio |
|--------|--------------|------------|-------|
| Ver tipos de alga | ✅ Sí | ❌ No | ❌ No |
| Crear tipo | ✅ Sí | ❌ No | ❌ No |
| Editar tipo | ✅ Sí | ❌ No | ❌ No |
| Activar/Desactivar | ✅ Sí | ❌ No | ❌ No |
| Eliminar tipo | ✅ Sí | ❌ No | ❌ No |
| Usar tipos en registro | ✅ Sí | ✅ Sí | ❌ No |

## Soporte

Si tienes problemas con los tipos de alga:

1. Verifica que tengas rol de **Administrador**
2. Verifica que el tipo esté **activo**
3. Ejecuta `python manage.py crear_tipos_alga` para agregar tipos iniciales
4. Contacta al equipo de desarrollo
