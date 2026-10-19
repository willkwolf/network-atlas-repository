---
type: catalog
title: Herramientas de Exploración Desktop y Aplicaciones GUI
description: Software de escritorio y plataformas interactivas para exploración visual, análisis exploratorio y bibliometría sin código.
tags: [desktop, gui, gephi, cytoscape, graphia, vosviewer, tulip]
---

# Herramientas de Exploración Desktop y Aplicaciones GUI

Herramientas para analistas, científicos e investigadores que necesitan cargar datos, ajustar layouts y explorar redes interactivamente sin construir una aplicación web.

## Comparativa de Herramientas Principales

| Herramienta | Dominio Principal | Motor / Layouts | Escala Típica | Cuándo Usarla | Precauciones |
|---|---|---|---|---|---|
| **[Gephi](https://gephi.org/)** | Propósito general | ForceAtlas2, OpenOrd, Yifan Hu | Hasta ~500k aristas | Primera exploración visual, filtrado por atributos y exportación de imágenes vectoriales. | El rendimiento decae severamente si no se asigna memoria JVM adecuada (`gephi.conf`). |
| **[Cytoscape](https://cytoscape.org/)** | Biología molecular y redes complejas | Prefuse, Spring-embedded, apps de terceros | Hasta ~200k aristas | Redes biomoleculares, integración con Gene Ontology, rutas metabólicas y plugins biológicos. | No confundir con Cytoscape.js (biblioteca web). Es pesado para análisis puramente estadísticos. |
| **[Graphia](https://graphia.app/)** | Redes científicas y 3D | Motor nativo acelerado por hardware | Hasta ~1M aristas | Visualización 2D/3D de datos de expresión génica, correlación y matrices densas. | Requiere GPU dedicada moderna para una experiencia fluida. |
| **[Tulip](https://tulip.labri.fr/)** | Investigación en visualización | C++ / OpenGL modular con scripting Python | Hasta ~1M aristas | Algoritmos a medida, manipulación jerárquica y clustering multinivel. | Curva de aprendizaje técnica más empinada que Gephi. |
| **[VOSviewer](https://www.vosviewer.com/)** | Bibliometría y cienciometría | VOS (Visualization of Similarities) | Hasta ~100k publicaciones | Mapeo de coautorías, cocitación y coocurrencia de palabras clave. | No es una herramienta para grafos de propósito general; asume matrices de proximidad bibliométrica. |
| **[NodeXL](https://nodexl.com/)** | Redes sociales en hojas de cálculo | Integración con Excel | Hasta ~50k aristas | Analistas de marketing y sociología habituados a Microsoft Excel. | Versión Basic muy limitada; versión Pro de pago. |
| **[Pajek](http://mrvar.fdv.uni-lj.si/pajek/)** | Redes sociales masivas | Algoritmos de optimización clásica en memoria | Hasta varios millones de aristas | Algoritmos tradicionales de SNA sobre redes grandes en Windows. | Interfaz de usuario obsoleta; formato de datos específico (`.net`). |

---

## Recursos con Verificación Pendiente
- **Gephisto:** Enlace pendiente de resolución en el catálogo original (`verification_status: needs_link_resolution`). No se debe recomendar para producción sin antes verificar su identidad y repositorio.
- **GraphInsight:** Enlace pendiente de resolución en el catálogo original.

---

## Páginas Relacionadas
- [Bibliotecas de Visualización Web](web-visualization.md)
- [Análisis en Python](python-analysis.md)
- [Framework de Decisión](../concepts/decision-framework.md)
