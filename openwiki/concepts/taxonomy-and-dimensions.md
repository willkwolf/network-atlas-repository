---
type: concept
title: Taxonomía y Dimensiones de Clasificación
description: Dimensiones ortogonales para categorizar recursos por modelo de red, categoría funcional, escala y entorno.
tags: [taxonomy, classification, network-types, scale-bands, environments]
---

# Taxonomía y Dimensiones de Clasificación

Network Atlas evita clasificar recursos únicamente por popularidad. Utiliza dimensiones ortogonales e independientes que permiten filtrar con precisión.

## 1. Categorías Primarias

Definidas canónicamente en `repo://data/domain-taxonomy.json`:

1. **`desktop_exploration` (Aplicaciones de exploración):** Herramientas GUI listas para instalar, importar datos y explorar interactivamente sin programar (ej. Gephi, Cytoscape, Graphia).
2. **`web_hosted` (Productos web o alojados):** Plataformas SaaS e interfaces en navegador para colaborar y compartir grafos sin gestión de infraestructura local.
3. **`python_analysis` (Análisis y herramientas Python):** Ecosistema de bibliotecas para modelar, manipular, calcular métricas y ejecutar algoritmos en Python (ej. NetworkX, igraph, NetworKit).
4. **`web_visualization` (Bibliotecas de visualización web):** SDKs y bibliotecas JavaScript/TypeScript para incrustar redes interactivas en aplicaciones web (ej. Sigma.js, Cytoscape.js, Cosmograph).
5. **`r_analysis` (Análisis y visualización en R):** Paquetes para investigación reproducible, bioestadística y modelos estocásticos (ej. igraph, tidygraph, ggraph).
6. **`scale_distributed` (Computación a escala y distribuida):** Aceleración por GPU y frameworks distribuidos para redes masivas (ej. cuGraph, GraphScope).
7. **`higher_order_temporal` (Temporal, multicapa y orden superior):** Modelos donde el tiempo, las capas interconectadas o las relaciones grupales (>2 entidades) son estructurales (ej. Raphtory, pathpy, XGI).
8. **`research_layout_algorithms` (Investigación de layouts y dibujo de grafos):** Algoritmos y frameworks formales de force-directed layout, reducción dimensional y dibujo ortogonal.
9. **`datasets_benchmarks` (Datasets y suites de prueba):** Colecciones públicas de redes reales y suites estandarizadas (ej. SNAP, OGB).
10. **`graph_database_query` (Bases de datos y analítica de grafos):** Motores de persistencia de grafos de propiedades y RDF con soporte de lenguajes de consulta (Cypher, GQL, SPARQL).

---

## 2. Modelos de Red (`network_types`)

- **`static`**: Red simple donde las aristas y nodos no cambian a lo largo del tiempo.
- **`directed` / `undirected`**: Aristas con o sin orientación de origen a destino.
- **`weighted`**: Relaciones con valores cuantitativos (fuerza, capacidad, distancia).
- **`bipartite` / `multipartite`**: Nodos divididos en dos o más conjuntos disjuntos donde sólo existen aristas entre conjuntos diferentes.
- **`multilayer`**: Redes compuestas por múltiples capas que representan diferentes tipos de interacciones sobre los mismos o distintos conjuntos de nodos.
- **`temporal`**: Redes con marcas de tiempo (marcas temporales discretas o continuas / streams de eventos).
- **`hypergraph`**: Estructuras donde una hiperarista puede conectar simultáneamente un número arbitrario de nodos.

---

## 3. Bandas de Escala (`scale_band`)

- **`small_in_memory`**: Hasta ~100.000 nodos/aristas. Ejecutable cómodamente en memoria en cualquier laptop común.
- **`medium_single_node`**: Desde 100.000 hasta ~5.000.000 aristas. Requiere bibliotecas optimizadas en C/C++ o Rust con bindings a Python/R.
- **`large_gpu_or_disk`**: Desde 5.000.000 hasta ~100.000.000 aristas. Requiere GPU con VRAM dedicada o motores de grafo orientados a memoria mapeada / disco.
- **`scale_distributed`**: Más de 100.000.000 aristas. Requiere clúster distribuido (Spark, GraphScope, ray).

---

## 4. Entornos de Ejecución (`environments`)

- `desktop_gui`: Software con interfaz gráfica de escritorio.
- `web`: Navegador cliente (HTML5 Canvas, WebGL, SVG).
- `python`: Intérprete Python y Jupyter Notebooks.
- `r`: Entorno R y RStudio.
- `cli`: Herramientas de línea de comandos.
- `gpu`: Aceleradores NVIDIA CUDA.
- `c_cpp`: Código compilado nativo de alto rendimiento.

---

## Páginas Relacionadas
- [Arquitectura y Modelo de Datos](architecture-and-data-model.md)
- [Framework de Decisión](decision-framework.md)
- [Índice Maestro OpenWiki](../index.md)
