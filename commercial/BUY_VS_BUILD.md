# Decisión comercial: comprar, alojar, integrar o construir

## 1. Categorías de solución

- **Herramienta local de investigación:** instalación por investigador o equipo; mayor control local, pero la integración con usuarios/datos compartidos puede requerir desarrollo.
- **Biblioteca open source:** control de arquitectura y portabilidad; el equipo asume mantenimiento, UX, seguridad y operación.
- **Servicio web/SaaS:** menor fricción inicial y posible colaboración; aumenta la importancia de privacidad, residencia, roles, exportación y dependencia del proveedor.
- **Plataforma empresarial:** roles/auditoría/integración/soporte pueden ser centrales; confirmar qué forma parte de cada edición y qué requiere servicios adicionales.
- **Stack de infraestructura propia:** da control, pero añade coste de despliegue, observabilidad, actualizaciones y continuidad operativa.

## 2. Matriz de decisión

Puntuar cada criterio de 0 a 3 (0 = no cubierto; 1 = parcial o con trabajo importante; 2 = cubierto con limitaciones conocidas; 3 = cubierto y verificado en PoC). No sumar ciegamente: privacidad, seguridad y preservación semántica pueden ser criterios de veto.

| Criterio | Pregunta para la PoC |
|---|---|
| Ajuste al modelo | ¿Conserva dirección, pesos, tipos, timestamps, capas y relaciones grupales? |
| Calidad analítica | ¿Contiene los algoritmos necesarios y expone sus supuestos/parámetros? |
| Visualización/tareas | ¿Los usuarios realizan las tareas reales con menos errores y tiempo razonable? |
| Rendimiento | ¿Funciona con el dataset representativo y la carga prevista? |
| Integración | ¿API, formatos, autenticación, logs y exportación encajan con el stack existente? |
| Seguridad/gobierno | ¿Hay permisos, auditoría, cifrado, borrado, residencia y tratamiento claros? |
| Portabilidad | ¿Pueden extraerse datos, definiciones y resultados en formatos utilizables? |
| TCO a 12–36 meses | ¿Incluye licencias, infraestructura, almacenamiento, GPUs, soporte, ingeniería y migración? |
| Madurez | ¿Hay mantenimiento, roadmap, soporte, comunidad y compatibilidad claros? |
| Riesgo de proveedor | ¿Qué ocurre ante subida de precio, cambio de API o discontinuación? |

## 3. Coste total (TCO)

Calcular al menos:

`TCO = licencias + infraestructura + almacenamiento + transferencia + ingeniería + mantenimiento + soporte + seguridad/compliance + migración + coste esperado de interrupciones`

Estimar escenarios base, crecimiento y estrés. La edición gratuita no implica coste total bajo si requiere ingeniería y operación relevantes.

## 4. Gate de seguridad antes de probar SaaS

No cargar datos reales sensibles hasta confirmar: términos y privacidad, región/residencia, uso para entrenamiento, retención, borrado, subprocesadores, controles de acceso, SSO/MFA según el riesgo, auditoría, exportación, backups y respuesta a incidentes. Ejecutar inicialmente con datos sintéticos o anonimizados.

## 5. PoC acotada

1. Definir 3–5 tareas y criterios de aceptación.
2. Preparar un dataset anonimizado pero representativo y una verdad de referencia si existe.
3. Comparar una herramienta gratuita/local, una librería integrable y un producto comercial pertinente.
4. Medir funcionalidad, rendimiento, error de usuario, exportación, seguridad y coste.
5. Registrar decisión, evidencia, límites y condiciones que obligarían a reevaluar.

## 6. Señales de “no comprar todavía”

- No se conoce el esquema ni la semántica de nodos/aristas.
- Solo se ha mostrado un demo con datos del proveedor.
- La prueba no contiene el tamaño, densidad o tipos de relación reales.
- No se ha demostrado exportación preservando atributos.
- Los términos sobre datos no están aprobados.
- Se compara precio de licencia, pero no operación y coste de salida.
