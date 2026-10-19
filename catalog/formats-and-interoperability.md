# Formatos e interoperabilidad

Ningún formato resuelve todos los casos. Elegir el formato por estructura de red, preservación de atributos, escalabilidad, interoperabilidad y capacidad de reconstrucción.

| Formato / estándar | Forma típica | Usos y cautelas |
|---|---|---|
| CSV/TSV de aristas | `source,target` y columnas adicionales | Muy interoperable; documentar IDs, tipo, dirección, peso, timestamps y multiaristas. |
| CSV/TSV de nodos + aristas | Tabla separada de entidades y relaciones | Suele ser la mejor interfaz universal para integrar herramientas; preservar claves estables. |
| [GraphML](http://graphml.graphdrawing.org/) | XML para grafos con atributos | Formato útil para intercambio, pero comprobar las extensiones específicas soportadas. |
| [GEXF](https://gexf.net/) | XML para grafos, con atributos y extensiones temporales | Frecuente en flujos Gephi; comprobar conservación de los elementos avanzados. |
| [GML](https://en.wikipedia.org/wiki/Graph_Modelling_Language) | Formato textual de modelado de grafos | Variaciones en implementaciones; hacer test de ida/vuelta. |
| Pajek `.net` | Texto para redes y atributos | Conveniente en flujos que usan Pajek; validar el soporte del receptor. |
| DOT | Lenguaje de Graphviz | Ideal para diagramas reproducibles; no es un formato universal de datos semánticos. |
| JSON/JSON-LD | Estructuras JSON / datos vinculados | Adecuado para APIs/web y grafos semánticos, según contrato definido. |
| RDF / Turtle / N-Triples | Triples semánticos | Usar cuando los identificadores y relaciones tienen semántica formal; decidir si la visualización necesita una proyección. |
| Cypher | Lenguaje de consulta de grafos para Neo4j y ecosistemas compatibles | Es lenguaje de consulta, no formato de archivo por sí mismo. |
| GraphBLAS / matrices dispersas | Representación algebraica/computacional | Útil para computación eficiente; puede perder metadatos relacionales si no se guarda por separado. |
| Parquet/Arrow + tablas de nodos/aristas | Datos columnares con esquema | Útil para pipelines analíticos; acordar claves, tipos y cómo reconstruir el grafo. |

## Contrato mínimo de datos

- **Nodos:** `node_id` estable, `node_type`, atributos, fuente y fecha de observación.
- **Aristas:** `edge_id`, `source_id`, `target_id`, `relation_type`, `directed`, `weight`/unidad, fuente y confianza.
- **Tiempo:** separar `valid_from`, `valid_to` o `timestamp` del tiempo de ingesta; documentar zona horaria y semántica.
- **Capas:** registrar `layer_id` y qué representa cada capa.
- **Procedencia:** origen de la observación, método de inferencia, versión de extracción, licencia y transformaciones.

Los nombres son una recomendación de esquema, no un estándar impuesto. Adaptarlos sin perder semántica.

## Prueba de interoperabilidad

Para cada candidato, hacer una exportación e importación de ida y vuelta y comparar: cantidad de nodos/aristas, IDs, dirección, pesos, tipos, atributos nulos, multiaristas, timestamps, capas y codificación. Un fichero que abre sin errores puede haber perdido información.
