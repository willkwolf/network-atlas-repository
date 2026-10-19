# Gobernanza, estados y mantenimiento

## Estados de verificación

- `needs_link_resolution`: enlace corto/identidad sin resolver; no usar como recomendación.
- `primary_url_selected`: URL primaria seleccionada, descripción inicial curada; revisar detalles antes de adoptar.
- `official_page_checked_YYYY-MM-DD`: página oficial consultada en la fecha indicada.
- `official_docs_checked_YYYY-MM-DD`: documentación oficial consultada en la fecha indicada.
- `web_search_checked_YYYY-MM-DD`: encontrado durante una búsqueda web; no equivale a benchmark ni auditoría.

## Niveles de evidencia

Consultar la escala E0–E4 en `research/METHODS_AND_EVALUATION.md`. El estado del enlace y el nivel de evidencia no son lo mismo: una URL oficial puede confirmar identidad, pero no rendimiento en el entorno del usuario.

## Cadencia sugerida

- Cada 3 meses: enlaces críticos, herramientas comerciales, releases y licencias.
- Cada 6 meses: revisión de recursos de investigación, métodos y listas externas.
- Antes de cada recomendación de producción: revisión ad hoc de compatibilidad, seguridad, licencia y mantenimiento.

## Estados de ciclo de vida

`candidate` → `verified` → `tested` → `recommended_for_context` o `archived`. No convertir una entrada en recomendada por su popularidad. Archivar no significa borrar: conservar razón, fecha y alternativa conocida.

## Neutralidad

No hay patrocinio implícito. La presencia en el registro no es una certificación, aval comercial ni validación de seguridad. Describir limitaciones y usos adecuados junto con fortalezas.
