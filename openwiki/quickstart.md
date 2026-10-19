---
type: guide
title: Guía Rápida y Enrutamiento de Tareas (Quickstart)
description: Punto de entrada rápido para que agentes y humanos resuelvan dudas sobre herramientas de redes en menos de 30 segundos.
tags: [quickstart, routing, agents, network-analysis, decision-matrix]
---

# Guía Rápida y Enrutamiento de Tareas

Esta guía permite a un agente o desarrollador pasar de un requerimiento a una recomendación justificada en segundos.

## 1. Atajos de Decisión en 30 Segundos

| Necesidad Primaria | Primera Opción | Alternativa Avanzada | Cuándo Descartar |
|---|---|---|---|
| **Exploración No-Code / GUI** | [Gephi](catalog/desktop-and-gui.md) | [Graphia](catalog/desktop-and-gui.md) / [Cytoscape](catalog/desktop-and-gui.md) | Datos mayores a memoria RAM o necesidad de automatización vía pipeline CI/CD. |
| **Análisis Estructural en Python** | [NetworkX](catalog/python-analysis.md) | [igraph](catalog/python-analysis.md) / [NetworKit](catalog/python-analysis.md) / [graph-tool](catalog/python-analysis.md) | Redes de >1M aristas con cálculos intensivos (centralidad de intermediación, etc.). |
| **Componente Visual en Web/Frontend** | [Sigma.js](catalog/web-visualization.md) | [Cytoscape.js](catalog/web-visualization.md) / [Cosmograph](catalog/web-visualization.md) | Redes que requieren layouts dinámicos en tiempo real con millones de nodos (usar WebGL/Cosmograph). |
| **Diagramación y Flujos** | [Graphviz](catalog/web-visualization.md) | [xyflow](catalog/web-visualization.md) | Redes densas sin orden jerárquico claro. |
| **Redes Temporales y Dinámicas** | [Raphtory](catalog/temporal-and-higher-order.md) | [pathpy](catalog/temporal-and-higher-order.md) / `ndtv` (R) | Cuando los datos no tienen marcas temporales ordenadas o sólo son agregaciones estáticas. |
| **Hipergrafos / Orden Superior (>2 entidades)** | [XGI](catalog/temporal-and-higher-order.md) | [HyperNetX](catalog/temporal-and-higher-order.md) | Cuando las relaciones son exclusivamente pares simples nodo-a-nodo. |
| **Cómputo a Escala / Aceleración GPU** | [cuGraph](catalog/scale-gpu-distributed.md) | [GraphScope](catalog/scale-gpu-distributed.md) | Cuando no se dispone de GPUs NVIDIA con memoria VRAM suficiente o los datos caben en CPU común. |
| **Base de Datos y Analítica de Grafos** | [Neo4j](catalog/graph-databases-and-query.md) | [Memgraph](catalog/graph-databases-and-query.md) / [Kùzu](catalog/graph-databases-and-query.md) | Necesidades analíticas puras sin persistencia transaccional ACID. |
| **Mapas Bibliométricos y de Literatura** | [VOSviewer](catalog/desktop-and-gui.md) | [Gephi](catalog/desktop-and-gui.md) + [OpenAlex](catalog/datasets-and-benchmarks.md) | Si la literatura no cuenta con identificadores DOI o citas normalizadas. |

---

## 2. Consulta Rápida por Terminal (Zero Latency)

El repositorio incluye un motor de búsqueda autónomo sin dependencias (`scripts/find_resources.py`):

```bash
# 1. Buscar herramientas web
python scripts/find_resources.py --category web_visualization

# 2. Filtrar por tipo de red (ej. hipergrafos) y volcar a JSON
python scripts/find_resources.py --network-type hypergraph --json

# 3. Buscar por texto libre
python scripts/find_resources.py --text "layout"
```

---

## 3. Formato Canónico de Recomendación para Agentes

Al responder a un usuario humano, todo agente debe seguir este formato estructurado:
1. **Herramienta recomendada:** Nombre y enlace primario.
2. **Por qué encaja:** Ajuste al modelo de datos, entorno y volumen.
3. **Qué NO resuelve:** Límites claros (memoria, formatos no soportados, curva de aprendizaje).
4. **Prueba de 15 minutos:** Comando, dataset de juguete o snippet para validar compatibilidad.

---

## Páginas Relacionadas
- [Índice Maestro OpenWiki](index.md)
- [Framework de Decisión y Criterios](concepts/decision-framework.md)
- [Taxonomía y Dimensiones](concepts/taxonomy-and-dimensions.md)
- [Arquitectura y Modelo de Datos](concepts/architecture-and-data-model.md)
