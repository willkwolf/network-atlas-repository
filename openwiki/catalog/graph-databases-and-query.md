---
type: catalog
title: Bases de Datos de Grafos y Motores de Consulta
description: Motores de persistencia de grafos de propiedades (LPG), bases RDF y tecnologías de consulta analítica.
tags: [graph-databases, neo4j, memgraph, kuzu, cypher, sparql]
---

# Bases de Datos de Grafos y Motores de Consulta

Una base de datos de grafos proporciona persistencia transaccional (ACID), indexación relacional y lenguajes declarativos de consulta (Cypher, GQL, SPARQL, Gremlin).

> [!NOTE]
> **Distinción Crítica:** Una base de datos almacena y recupera caminos eficientemente (punteros a memoria en tiempo constante \(O(1)\) por salto de arista). No está optimizada por defecto para algoritmos globales de ciencia de redes (como Betweenness sobre todo el grafo), a menos que incorpore extensiones especializadas (como Neo4j GDS).

## Motores Principales y Comparativa

| Motor | Tipo de Base | Lenguaje de Consulta | Arquitectura / Rendimiento | Casos de Uso Recomendados |
|---|---|---|---|---|
| **[Neo4j](https://neo4j.com/)** | Grafo de Propiedades (LPG) | Cypher / GQL | Motor nativo en disco con caché; ecosistema maduro (APOC, GDS, Bloom) | Aplicaciones empresariales, detección de fraude, grafos de conocimiento corporativo y gestión de identidades. |
| **[Memgraph](https://memgraph.com/)** | Grafo de Propiedades en memoria | Cypher | Motor en C++ 100% en memoria con persistencia en disco y soporte de streaming de eventos (Kafka) | Análisis y consultas en tiempo real con latencias de submilisegundos y transacciones de alta frecuencia. |
| **[Kùzu](https://kuzudb.com/)** | Grafo embebido (OLAP) | Cypher | Motor columnar embebido en C++ (el equivalente a DuckDB para grafos) | Analítica rápida de grafos local sin levantar servidores pesados; ideal para pipelines de Python con exportación directa a PyArrow/Pandas. |
| **[Apache AGE](https://age.apache.org/)** | Extensión multi-modelo | Cypher sobre PostgreSQL | Extensión relacional para bases de datos PostgreSQL | Equipos con infraestructura existente de Postgres que necesitan consultar relaciones en Cypher sin migrar de base de datos. |

---

## Visualizadores Comerciales y de Consulta sobre Bases de Datos

- **[Neo4j Bloom](https://neo4j.com/product/bloom/)**: Exploración visual orientada a usuarios de negocio sobre instancias de Neo4j.
- **[Linkurious](https://linkurious.com/)**: Plataforma de investigación empresarial y detección de anomalías para analistas de fraude e inteligencia.
- **[Graphistry](https://www.graphistry.com/)**: Visualización e investigación de grafos acelerada por GPU en la nube.

---

## Páginas Relacionadas
- [Computación a Escala](scale-gpu-distributed.md)
- [Formatos e Interoperabilidad](formats-and-interoperability.md)
- [Framework de Decisión](../concepts/decision-framework.md)
