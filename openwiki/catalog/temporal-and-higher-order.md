---
type: catalog
title: Redes Temporales, Multicapa y de Orden Superior
description: Bibliotecas para modelar sistemas donde el tiempo, las múltiples capas de interacción o las relaciones grupales (>2 nodos) son fundamentales.
tags: [temporal, higher-order, hypergraphs, multilayer, raphtory, xgi, hypernetx]
---

# Redes Temporales, Multicapa y de Orden Superior

Muchas redes del mundo real no pueden ser reducidas a pares estáticos de nodos sin perder información crítica sobre causalidad o cooperación grupal.

## 1. Redes Temporales y de Eventos

| Biblioteca | Modelo Temporal | Características Clave |
|---|---|---|
| **[Raphtory](https://www.raphtory.com/)** | Grafos dinámicos en streaming (Rust + Python) | Mantiene el grafo como un flujo continuo de eventos temporales; permite consultas sobre ventanas de tiempo deslizantes, vistas históricas en cualquier timestamp y cálculo de métricas temporales escalables. |
| **[pathpy](https://www.pathpy.net/)** | Caminos de orden superior (Higher-Order Paths) | Modela la dinámica causal en secuencias temporales para evitar la falacia de asumir que las aristas adyacentes son transitivas en el tiempo. |
| **[ndtv](https://cran.r-project.org/package=ndtv)** (R) | Snapshots y animaciones discretas | Visualización pedagógica de cambios estructurales paso a paso a lo largo del tiempo. |

---

## 2. Hipergrafos y Complejos Simpliciales (Relaciones > 2 Entidades)

Cuando una relación involucra a 3 o más entidades simultáneamente (ej. coautoría de un artículo entre 5 investigadores, reacciones químicas entre reactivos y catalizadores, grupos de chat), proyectar el hipergrafo a aristas binarias genera *cliques* artificiales que distorsionan la densidad y las métricas de clustering.

| Biblioteca | Enfoque | Cuándo Usarla |
|---|---|---|
| **[XGI](https://github.com/xgi-org/xgi)** | Hipergrafos y complejos simpliciales en Python | Modelado de orden superior con API inspirada en NetworkX, cálculo de centralidades de hipergrafo, clustering de orden superior y dibujo de hipergrafos. |
| **[HyperNetX](https://github.com/pnnl/hypernetx)** (PNNL) | Hipergrafos generales y visualizaciones Euler/Venn | Visualización interactiva y análisis de hipergrafos mediante diagramas bipartitos o representaciones de conjuntos. |

---

## 3. Redes Multicapa (Multilayer Networks)

- **[Py3Plex](https://github.com/SkBlaz/py3plex)**: Redes heterogéneas multicapa y multiplex en Python.
- **[multinet](https://github.com/cran/multinet)**: Análisis de redes multicapa en R, evaluando overlap entre capas y coeficientes de clustering intercapa.

---

## Páginas Relacionadas
- [Taxonomía y Dimensiones](../concepts/taxonomy-and-dimensions.md)
- [Análisis en Python](python-analysis.md)
- [Framework de Decisión](../concepts/decision-framework.md)
