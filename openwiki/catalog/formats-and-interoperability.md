---
type: catalog
title: Formatos de Archivo e Interoperabilidad de Grafos
description: Estándares de serialización, conversión entre herramientas y preservación de atributos tipados y temporales.
tags: [formats, interoperability, graphml, gexf, parquet, json, csv]
---

# Formatos de Archivo e Interoperabilidad de Grafos

La elección del formato de intercambio determina si los atributos de nodos, las coordenadas visuales y las marcas temporales se preservan o se pierden al transferir datos entre herramientas.

## Comparativa de Formatos de Red

| Formato | Estructura Base | Soporte de Atributos Tipados | Soporte Temporal | Eficiencia / Tamaño | Herramientas Principales |
|---|---|:---:|:---:|---|---|
| **GraphML** (`.graphml`) | XML formal | Sí (enteros, floats, strings, booleanos declarados en header) | Limitado (como atributos personalizados) | Media (verboso por etiquetas XML) | NetworkX, igraph, Gephi, Cytoscape, Tulip. Formato estándar universal más confiable. |
| **GEXF** (`.gexf`) | XML jerárquico | Sí | Nativo (soporta intervalos temporales dinámicos y evolución de atributos) | Media | Gephi, Sigma.js, Graphology. Excelente para redes que cambian en el tiempo. |
| **CSV / TSV** (Pares) | Texto plano tabular | No en archivo único (requiere archivo separado de nodos y otro de aristas) | Posible si se agrega columna de timestamp | Alta (fácil de comprimir en gzip/zip) | Pandas, Excel, R, bases de datos SQL. Ideal para pipelines ETL. |
| **JSON-Graph / Node-Link JSON** | JSON | Sí | Posible | Baja a media para redes grandes | D3.js, Cytoscape.js, APIs web. Fácil de consumir en JavaScript. |
| **Parquet / Arrow** | Columnar binario | Sí (esquema estricto y compresión eficiente) | Sí | Muy alta (10x-50x más rápido que texto) | Kùzu, cuGraph, DuckDB, Spark. Formato recomendado para redes de >5M aristas. |
| **Pajek** (`.net`) | Texto plano posicional | Muy limitado | No | Alta | Pajek, programas clásicos de SNA. |
| **DOT** (`.dot`, `.gv`) | Lenguaje de definición Graphviz | Enfocado en atributos de renderizado gráfico | No | Media | Graphviz, pydot, Doxygen. Ideal para diagramas jerárquicos. |

---

## Directrices de Interoperabilidad

1. **Evitar CSV sin esquema para atributos complejos:** Al compartir datos relacionales con atributos heterogéneos, preferir `GraphML` para garantizar que los tipos de datos no se conviertan todos en texto.
2. **Para redes temporales continuas:** Usar `GEXF` si el destino es exploración visual en Gephi, o tablas `Parquet` con columnas `source`, `target`, `timestamp` para pipelines analíticos de Python.

---

## Páginas Relacionadas
- [Herramientas Desktop y GUI](desktop-and-gui.md)
- [Visualización Web](web-visualization.md)
- [Arquitectura y Modelo de Datos](../concepts/architecture-and-data-model.md)
