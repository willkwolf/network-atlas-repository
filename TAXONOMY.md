# Taxonomía práctica: clasificación MECE

La clasificación primaria se basa en **la función principal para la que se adopta el recurso**, no en todas las cosas que puede hacer. Es una taxonomía operativa, no una ontología universal: varios productos cubren más de una función; el registro les asigna una sola categoría primaria y los indexa mediante etiquetas secundarias.

## 1. Categorías primarias

| ID | Categoría | Pregunta que responde | Incluye | No confundir con |
|---|---|---|---|---|
| `desktop_exploration` | Aplicaciones de exploración | ¿Quiero importar datos y explorar sin crear una app? | Gephi, Cytoscape desktop, Graphia, Tulip, VOSviewer, NodeXL | Una librería que exige código. |
| `web_hosted` | Productos web o alojados | ¿Quiero explorar, compartir o colaborar mediante una interfaz lista? | Kumu, Graphistry, Gephi Lite, Graph Commons, Linkurious | Que un producto alojado sea necesariamente gratuito o aceptable para datos privados. |
| `python_analysis` | Análisis y herramientas de notebooks Python | ¿Cómo construyo, transformo o analizo un grafo? | NetworkX, igraph, graph-tool, NetworKit, CDlib, ipysigma | Una librería analítica como motor de visualización final. |
| `web_visualization` | Bibliotecas de visualización web | ¿Cómo incorporo una red interactiva a mi propia aplicación? | Cytoscape.js, Sigma.js, D3-force, G6, vis-network, xyflow | Un framework de editores de nodos como si fuera necesariamente análisis de redes. |
| `r_analysis` | Análisis y visualización estadística en R | ¿Necesito análisis/figuras dentro de un flujo estadístico reproducible? | igraph, tidygraph, ggraph, visNetwork | Que un widget web garantice una aplicación de producción. |
| `scale_distributed` | Computación a escala | ¿Necesito aceleración GPU, procesamiento distribuido o grafos muy grandes? | cuGraph, GraphScope, Spark GraphX, GraphBLAS | Un benchmark sintético como garantía de rendimiento real. |
| `higher_order_temporal` | Modelos no estáticos o no diádicos | ¿El tiempo, las capas o relaciones grupales cambian el modelo? | Raphtory, pathpy, MuxViz, HyperNetX, XGI, ndtv | Un grafo estático construido desde una tabla sin semántica temporal. |
| `research_layout_algorithms` | Métodos de dibujo y layouts | ¿Investigo algoritmos de representación de grafos? | OGDF y recursos de dibujo | La visualización como medición directa de la estructura. |
| `datasets_benchmarks` | Datos y evaluación | ¿Necesito datos comparables, corpus o un benchmark? | SNAP datasets, KONECT, Network Repository, OGB | Asumir que todos los datasets tienen una misma licencia o calidad. |
| `graph_database_query` | Analítica ligada a bases de grafos | ¿Necesito consultar y analizar grafos persistidos? | Neo4j Graph Data Science, Neo4j Bloom | La base de datos, su motor analítico y el visualizador como un solo componente. |
| `infrastructure_topology` | Topología y sistemas IT | ¿Necesito representar inventario, dependencias o topología de infraestructura? | NetBox, Grafana Node Graph, exporters | Ciencia de redes sociales o monitorización de tráfico como tareas equivalentes. |
| `domain_data_sources` | Fuentes de datos de dominio | ¿Necesito construir redes desde datos de un dominio específico? | OpenAlex y otros corpus especializados | Confundir metadatos disponibles con datos completos o libres de sesgo. |
| `domain_solutions` | Flujos especializados de dominio | ¿Hay una herramienta cuyo flujo refleja mi tipo de estudio? | Network Canvas, Cytoscape bioinformático, VOSviewer | Que una herramienta de dominio sea apropiada para cualquier red. |
| `learning_research` | Aprendizaje y métodos de investigación | ¿Necesito aprender, consultar métodos o crear modelos ML sobre grafos? | Curso Network in Python, PyTorch Geometric, DGL | Tratar un curso o framework de ML como validación empírica de un método. |
| `existing_repositories` | Índices/repo de terceros | ¿Ya existe una colección curada que debo consultar? | Awesome Network Analysis y listas focalizadas | Copiar una lista externa sin revisar su alcance o licencia. |
| `needs_triage` | Pendientes de clasificación | ¿El recurso no puede categorizarse porque la identidad/enlace sigue sin verificarse? | Entradas recibidas por enlaces cortos no resueltos | Recomendar un recurso cuya identidad, función o destino aún no se confirma. |

## 2. Ejes transversales

Un recurso se filtra a lo largo de estas dimensiones independientemente de su categoría primaria:

- **Modelo de red:** simple/no dirigida, dirigida, ponderada, bipartita/multipartita, heterogénea/atribuida, temporal, multicapa/multiplex, hipergrafo, complejo/simplicial, espacial o probabilístico/inferido.
- **Trabajo:** captura; limpieza y transformación; análisis descriptivo; inferencia/modelado; layout y renderizado; exploración; comunicación; consultas; operación/observabilidad.
- **Entorno:** aplicación de escritorio, CLI, Python, R, JavaScript/TypeScript, notebook, navegador, SaaS, self-hosted, GPU, clúster/distribuido.
- **Escala:** no se etiqueta por una cifra universal. Registrar órdenes de magnitud orientativos y el dataset/operación que justifican la afirmación. Número de nodos renderizables no es igual a número de nodos analizables.
- **Madurez:** investigación, experimento/prototipo, proyecto OSS establecido, producto comercial, capacidad específica de un producto empresarial. No inferir madurez solo desde popularidad.
- **Restricciones:** privacidad, licencia, residencia de datos, coste, dependencias, hardware, accesibilidad, exportabilidad, reproducibilidad y bloqueo de proveedor.

## 3. Reglas anti-solapamiento

1. Asignar una categoría primaria por el uso más distintivo del recurso.
2. Los atributos secundarios deben ser etiquetas, no duplicados del recurso en nuevas categorías primarias.
3. Si se listan dos componentes de una misma familia (por ejemplo, Cytoscape desktop y Cytoscape.js), registrarlos por separado: resuelven problemas distintos.
4. Una página web que explica o agrega recursos se clasifica como índice, no como herramienta de análisis.
5. Mantener separados software, datasets, formatos, métodos, productos comerciales y publicaciones.
6. Si un recurso no tiene URL o identidad suficientemente confirmada, conservarlo como `needs_link_resolution`, no recomendarlo.

## 4. Qué significa “MECE” aquí

La dimensión primaria pretende ser mutuamente excluyente para facilitar clasificación y deduplicación; los ejes transversales permiten cubrir características que naturalmente se superponen. No es válido forzar dominios como “biológico”, “social” o “temporal” a una sola partición porque describen aspectos distintos de la misma red.
