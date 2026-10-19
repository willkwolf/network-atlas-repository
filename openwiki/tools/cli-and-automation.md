---
type: tool
title: Herramientas CLI y Scripts de Automatización
description: Manual operativo de los scripts de búsqueda, validación de integridad y comandos del CLI de OpenWiki.
tags: [cli, scripts, find-resources, validate-registry, openwiki-cli]
---

# Herramientas CLI y Scripts de Automatización

Este repositorio incluye herramientas autónomas en Python y Node.js para que tanto agentes como humanos interactúen con el catálogo sin overhead de dependencias externas.

## 1. Buscador Rápido de Recursos (`scripts/find_resources.py`)

Script escrito en Python estándar (sin requerir paquetes externos) para filtrar el catálogo canónico (`data/resources.json`):

```bash
# Mostrar ayuda con todos los parámetros disponibles:
python scripts/find_resources.py --help

# 1. Filtrar por categoría primaria:
python scripts/find_resources.py --category web_visualization

# 2. Filtrar por modelo de red:
python scripts/find_resources.py --network-type hypergraph

# 3. Filtrar por entorno de ejecución:
python scripts/find_resources.py --environment python

# 4. Búsqueda por texto libre en nombre y descripción:
python scripts/find_resources.py --text "community detection"

# 5. Salida en formato JSON limpio (para agentes o scripts):
python scripts/find_resources.py --category desktop_exploration --json
```

---

## 2. Validador de Integridad del Catálogo (`scripts/validate_registry.py`)

Verifica que el archivo `data/resources.json` cumpla las restricciones del esquema:
- Valida la unicidad de identificadores (`id`).
- Valida que todos los recursos posean campos requeridos (`id`, `name`, `primary_category`, `network_types`, `scale_band`, `environments`, `description`, `primary_url`, `verification_status`).
- Verifica que `primary_category` pertenezca al vocabulario controlado de `data/domain-taxonomy.json`.
- Detecta recursos con enlaces pendientes (`needs_link_resolution`).

```bash
python scripts/validate_registry.py
```

---

## 3. Comandos del CLI de OpenWiki

Al tener `openwiki` instalado en el entorno:

- **Visualizador Web Interactivo:**
  Inicia un servidor local con grafo de nodos y lector interactivo de la base de conocimiento:
  ```bash
  openwiki visualize openwiki --port 4321
  ```
- **Exportación estática para hosting web:**
  ```bash
  openwiki visualize openwiki --export docs/openwiki-visualizer --no-open
  ```
- **Actualización incremental basada en Git Diffs:**
  ```bash
  openwiki code --update --print
  ```

---

## Páginas Relacionadas
- [Arquitectura y Modelo de Datos](../concepts/architecture-and-data-model.md)
- [Guía Rápida y Enrutamiento](../quickstart.md)
- [Índice Maestro OpenWiki](../index.md)
