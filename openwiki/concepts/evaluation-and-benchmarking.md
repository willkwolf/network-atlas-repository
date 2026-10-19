---
type: concept
title: Metodología de Evaluación y Benchmarking
description: Métricas formales para evaluar rendimiento, fidelidad topológica, latencia de renderizado y consumo de memoria.
tags: [evaluation, benchmarking, metrics, performance, memory]
---

# Metodología de Evaluación y Benchmarking

Nunca debe tomarse una decisión basada únicamente en cifras comerciales de "soporta millones de nodos". El rendimiento debe medirse en 4 capas independientes:

## 1. Las 4 Capas de Rendimiento

1. **Ingestión y Construcción del Grafo:**
   - Tiempo de parsing del archivo fuente (GraphML, CSV, JSON, Parquet).
   - Memoria pico durante la asignación de estructuras de datos (listas de adyacencia vs matrices CSR).
2. **Cómputo Algorítmico:**
   - Tiempo de ejecución de algoritmos estándar (PageRank, Betweenness Centrality, Louvain/Leiden, Componentes Conexas).
   - Escalabilidad con el número de hilos (multithreading en C++/OpenMP) o paralelismo en GPU.
3. **Cálculo de Layout Espacial:**
   - Convergencia del algoritmo de distribución espacial (ForceAtlas2, Fruchterman-Reingold, OpenOrd).
   - Reducción de solapamiento de aristas (*edge crossings*) y conservación de distancias geodésicas.
4. **Interacción y Renderizado:**
   - Tasa de cuadros por segundo (FPS) sostenida durante pan, zoom y selección.
   - Latencia de respuesta en eventos de hover y filtrado interactivo de subgrafos.

---

## 2. Protocolo de Prueba Mínima (PoC de 15 Minutos)

Para evitar inversiones fallidas en herramientas inadecuadas:

```
[Dataset Sintético o Muestra Real] 
       │
       ├──► 1. Medir memoria pico en reposo tras la carga
       ├──► 2. Ejecutar cálculo del algoritmo crítico
       ├──► 3. Medir FPS en navegación interactiva
       └──► 4. Exportar a formato estándar y comprobar pérdidas
```

### Registro de Métricas Obligatorio
- Nodos, aristas y densidad efectiva (\(2|E| / (|V|(|V|-1))\)).
- Hardware empleado (CPU, núcleos, RAM instalada, modelo de GPU y VRAM).
- Versión exacta del paquete o software.
- Tiempos medidos con cronómetro reproducible (`time`, `cProfile`, devtools de navegador).

---

## Páginas Relacionadas
- [Framework de Decisión](decision-framework.md)
- [Formatos e Interoperabilidad](../catalog/formats-and-interoperability.md)
- [Computación a Escala y GPU](../catalog/scale-gpu-distributed.md)
