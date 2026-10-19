---
type: catalog
title: Datasets, Benchmarks y Repositorios de Redes
description: Colecciones públicas de grafos del mundo real, suites de evaluación estándar y generadores sintéticos.
tags: [datasets, benchmarks, snap, ogb, network-repository, openalex]
---

# Datasets, Benchmarks y Repositorios de Redes

Para validar algoritmos, probar rendimiento de layouts o entrenar modelos de aprendizaje sobre grafos, es indispensable contar con datos empíricos bien documentados.

## Repositorios Canónicos y Fuentes Abiertas

| Repositorio | Tipos de Grafos | Volumen / Escala | Enfoque Principal |
|---|---|---|---|
| **[Stanford SNAP Datasets](https://snap.stanford.edu/data/)** | Redes sociales, citas, web graphs, redes de colaboración | Miles a decenas de millones de nodos | Colección clásica de Stanford para investigación empírica en ciencia de redes. |
| **[Open Graph Benchmark (OGB)](https://ogb.stanford.edu/)** | Grafos moleculares, citas y conocimiento | Escala variable (nodo, arista, grafo completo) | Suite estandarizada para evaluar Graph Neural Networks (GNN) con particiones reproducibles de train/test. |
| **[Network Repository](https://networkrepository.com/)** | Redes biológicas, redes tecnológicas, grafos cerebrales, interacción social | Más de 5000 redes interactivas | El primer repositorio con visualizaciones interactivas y herramientas de comparación estadística directa. |
| **[OpenAlex](https://openalex.org/)** | Grafo bibliométrico y de literatura académica global | Cientos de millones de publicaciones, autores, instituciones y conceptos | Catálogo abierto que reemplaza fuentes propietarias para estudios de cienciometría y redes de coautoría. |

---

## Generadores Sintéticos de Grafos

- **Modelos de Grafo Aleatorio (Erdős–Rényi):** Útiles como baseline nulo, aunque carecen de clustering alto ni colas pesadas de grado.
- **Modelos de Pequeño Mundo (Watts–Strogatz):** Alto clustering y longitud de camino promedio corta.
- **Modelos de Conexión Preferencial (Barabási–Albert):** Distribución de grados libre de escala (scale-free power law).
- **Modelos de Bloques Estocásticos (SBM):** Grafos con estructura de comunidades explícita y controlada para evaluar algoritmos de clustering.

---

## Páginas Relacionadas
- [Evaluación y Benchmarking](../concepts/evaluation-and-benchmarking.md)
- [Análisis en Python](python-analysis.md)
- [Formatos e Interoperabilidad](formats-and-interoperability.md)
