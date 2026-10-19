# Contribuir

## Qué contribuciones aceptar

- Herramientas, datasets, formatos, benchmarks, métodos o repositorios con función clara y vínculo primario.
- Comparaciones reproducibles que documenten versiones, hardware, datos y operación medida.
- Recursos de dominio que llenen un vacío real y no solo repitan otra lista.
- Correcciones de enlaces, mantenimiento, licencias, formatos, requisitos o advertencias.

## Requisitos para una nueva entrada

1. Abrir una ficha con `templates/RESOURCE_CARD.md`.
2. Añadir una entrada a `data/resources.json` con los campos del esquema.
3. Mantener el único `id` estable, kebab-case y sin duplicados.
4. Asignar una categoría primaria y etiquetas secundarias útiles.
5. Separar capacidades documentadas de resultados de pruebas propias.
6. Marcar como `needs_link_resolution` si el destino/identidad no está confirmado.
7. Añadir licencia/precio solo con fuente y fecha; en caso contrario usar `verify_current_terms`.
8. Ejecutar `python scripts/validate_registry.py`.

## No aceptar

- Recursos con links de afiliado como URL principal si existe la fuente original.
- Entradas sin función específica o que repiten una plataforma sin distinguir componentes.
- Cifras de rendimiento sin benchmark reproducible.
- Listas copiadas íntegramente de terceros sin revisar licencia, procedencia y duplicados.
- Afirmaciones de “mejor herramienta” sin criterios de tarea y restricciones.
- Contenido sensible, credenciales, datos privados o dumps de redes que no se puedan redistribuir.

## Proceso de actualización

Al modificar una entrada, conservar su `id`, actualizar la fecha/estado de revisión en la descripción o fuentes y explicar los cambios significativos en `CHANGELOG.md`.
