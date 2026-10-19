---
type: catalog
title: Análisis de Redes y Estadística en R
description: Ecosistema R para bioestadística, manipulación tidy de redes, modelado ERGM y publicaciones reproducibles.
tags: [r, tidygraph, ggraph, statnet, ergm, igraph-r]
---

# Análisis de Redes y Estadística en R

El ecosistema R destaca en la reproducibilidad académica, bioinformática y el modelado estadístico formal de redes sociales (ERGM / SAOM).

## Principales Paquetes y Enfoques

| Paquete | Paradigma | Propósito Principal | Cuándo Usarlo |
|---|---|---|---|
| **[igraph (R)](https://igraph.org/r/)** | Funcional / Matriz C | Cálculo algorítmico de alto rendimiento y métricas de red | Base computacional para la mayoría de análisis cuantitativos en R. |
| **[tidygraph](https://tidygraph.data-imaginist.com/)** | Tidyverse (`tbl_graph`) | Manipulación de nodos y aristas como data frames coordinados vía verbos de `dplyr` | Flujos de limpieza, filtrado relacional y análisis reproducible estructurado. |
| **[ggraph](https://ggraph.data-imaginist.com/)** | Gramática de Gráficos (`ggplot2`) | Visualización estática de alta calidad tipográfica para publicaciones científicas | Creación de figuras vectoriales (PDF/SVG) listas para artículos y libros. |
| **[statnet](https://statnet.org/)** | Modelado estocástico | Modelos de Grafos Aleatorios Exponenciales (ERGM) y redes de actores latentes | Pruebas de hipótesis sociológicas sobre mecanismos de formación de aristas (homofilia, transitividad). |
| **[visNetwork](https://datastorm-open.github.io/visNetwork/)** | HTMLWidgets | Visualizaciones interactivas incrustadas en informes R Markdown o Shiny | Dashboards web interactivos creados puramente en código R. |
| **[ndtv](https://cran.r-project.org/package=ndtv)** | Animación temporal | Animaciones de redes dinámicas y líneas de tiempo relacionales | Demostración visual de la evolución temporal de redes pequeñas y medianas. |

---

## Páginas Relacionadas
- [Análisis en Python](python-analysis.md)
- [Redes Temporales y Orden Superior](temporal-and-higher-order.md)
- [Framework de Decisión](../concepts/decision-framework.md)
