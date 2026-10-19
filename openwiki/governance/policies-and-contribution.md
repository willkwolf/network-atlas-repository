---
type: governance
title: Gobernanza, Políticas y Directrices de Contribución
description: Criterios para proponer adiciones al catálogo, fichas de recursos y experimentos, y política de licencias.
tags: [governance, contributing, policies, license, resource-card]
---

# Gobernanza, Políticas y Directrices de Contribución

Network Atlas mantiene estándares rigurosos de curación para evitar que el catálogo se convierta en una lista inflada o desactualizada de enlaces.

## 1. Criterios para Incluir un Nuevo Recurso

Para que una biblioteca, herramienta o dataset sea aceptado en `data/resources.json`:

1. **Evidencia de Utilidad Real:** Debe resolver un problema técnico específico dentro del alcance (ciencia de redes, análisis de grafos, visualización interactiva, bibliometría, orden superior o bases de datos).
2. **Fuente Primaria Verificable:** Debe aportarse el enlace a la documentación oficial y al código fuente (GitHub/GitLab) o sitio web oficial. No se admiten enlaces acortados (`bit.ly`, `lnkd.in`) ni intermediarios no oficiales.
3. **Mantenimiento y Licencia:** Debe especificarse una licencia de software conocida (MIT, Apache-2.0, GPL, Propietaria con términos) y demostrarse actividad reciente o estabilidad probada.
4. **Cumplimiento del Esquema:** Todo nuevo recurso debe incluirse en `data/resources.json` y pasar `python scripts/validate_registry.py` sin errores.

---

## 2. Plantillas de Contribución

El repositorio incluye plantillas estandarizadas en `templates/`:
- **`templates/RESOURCE_CARD.md`**: Ficha detallada de un recurso, documentando modelo de datos, entorno, casos de uso óptimos, límites conocidos y prueba de 15 minutos.
- **`templates/EXPERIMENT_CARD.md`**: Ficha de validación empírica para registrar benchmarks de rendimiento (nodos, aristas, memoria pico, FPS, tiempo de cálculo).

---

## 3. Política de Licenciamiento

- **Scripts y Código Auxiliar (`scripts/`):** Diseñados para licenciamiento permisivo (ej. MIT o Apache-2.0).
- **Documentación y Wiki (`openwiki/`):** Curación y guías estructuradas bajo licenciamiento abierto (Creative Commons CC BY 4.0).
- **Recursos Externos:** Los enlaces a terceros pertenecen a sus respectivos autores; el repositorio no sublicencia ni garantiza software de terceros.

---

## Páginas Relacionadas
- [Arquitectura y Modelo de Datos](../concepts/architecture-and-data-model.md)
- [Framework de Decisión](../concepts/decision-framework.md)
- [Índice Maestro OpenWiki](../index.md)
