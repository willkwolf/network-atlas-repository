# Protocolo de routing para agentes y humanos

Este archivo permite que un agente consulte el índice sin asumir que existe una Skill o API. El registro canónico se encuentra en `../data/resources.json`.

## Procedimiento

1. **Traducir intent a operación:** captura, limpieza, análisis, inferencia, visualización, exploración, consulta, publicación o topología/observabilidad.
2. **Identificar el modelo:** estático/temporal/multicapa/hipergrafo; dirigido o no; ponderado; atributos y tipos.
3. **Identificar el entorno:** no-code, Python, R, web app, notebook, SaaS, self-hosted, GPU o distribuido.
4. **Aplicar restricciones duras:** privacidad, licencia, sistema operativo, datos permitidos en nube, hardware, exportación y presupuesto.
5. **Seleccionar 2–4 candidatos:** justificar por tarea y límites; no recomendar por popularidad solamente.
6. **Declarar incertidumbre y prueba mínima:** qué se verificó y qué debe probarse con el dataset real.
7. **Citar fuentes primarias:** dar preferencia a documentación oficial y repositorios del proyecto; un índice de terceros sirve para descubrir, no para probar una capacidad crítica.

## Esquema de consulta sugerido

- `intent`: tarea concreta en lenguaje natural.
- `graph_model`: propiedades estructurales conocidas.
- `scale`: nodos/aristas/densidad, tasa de eventos y latencia, si se conoce.
- `environment`: lenguajes, notebook, navegador, desktop, cloud/on-prem.
- `constraints`: privacidad, licencia, coste, hardware, equipo, integración.
- `output`: imagen, explorador interactivo, métricas, API, dashboard, paper/reproducibilidad.
- `confidence_needed`: exploración rápida, investigación publicable, producción empresarial.

## Formato de respuesta esperado

Para cada candidato: **nombre + vínculo primario + por qué encaja + qué no resuelve + restricciones que deben verificarse + siguiente prueba de 15–30 minutos**. No afirmar rendimiento sin benchmark ni afirmar precio/licencia vigente sin fuente actual.

## Reglas de seguridad y validez

- No subir datos sensibles a un servicio hospedado sin aprobación.
- No convertir métricas/visualizaciones en afirmaciones causales sin diseño adecuado.
- No inferir que una herramienta está activa porque una página o lista la menciona.
- Si `verification_status` es `needs_link_resolution`, no recomendarla como opción viable.
- Antes de emitir una recomendación de producción, confirmar versión, licencia, mantenimiento, seguridad y posibilidad de exportar el grafo.
