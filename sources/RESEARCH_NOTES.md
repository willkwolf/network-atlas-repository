# Notas de investigación externa

**Fecha de consulta exploratoria:** 2026-10-18. La consulta localizó páginas primarias y catálogos; no ejecutó benchmarks propios ni verificó todos los recursos del registro.

## Fuentes y hallazgos que motivan la estructura

- [Awesome Network Analysis](https://github.com/briatte/awesome-network-analysis): lista amplia de libros, cursos, datasets, software, métodos, papers y grupos; es la referencia externa más cercana.
- [NetworkX — Drawing](https://networkx.org/documentation/stable/reference/drawing.html): explica que el objetivo principal de NetworkX es análisis de grafos y recomienda herramientas dedicadas para visualización completa. Por eso se separan librerías analíticas y capas visuales.
- [Network Repository](https://networkrepository.com/network-data.php): se presenta como repositorio científico interactivo con datos de distintos tipos, incluidos temporales, espaciales y atribuidos.
- [OGDF docs](https://ogdf.github.io/doc/ogdf/index.html): referencia de framework C++ para algoritmos de grafos y dibujo/layouts; sustenta la categoría de investigación de layouts.
- [RAPIDS cuGraph docs](https://docs.rapids.ai/api/cugraph/stable/): documenta requisitos de hardware/software e instalación; el uso de GPU debe evaluarse como restricción arquitectónica.
- [GraphScope docs](https://graphscope.io/docs/): describe un sistema unificado de computación distribuida para workloads analíticos, interactivos y de aprendizaje de grafos; su rol difiere de una librería visual.
- [HyperNetX docs](https://hypernetx.readthedocs.io/en/develop/index.html): define hipergrafos para relaciones multi-entidad y expone análisis/visualización.
- [XGI docs](https://xgi-org.github.io/xgi/): incluye representación y visualización de hipergrafos, grafos dirigidos de orden superior y complejos simpliciales.
- [Cosmograph — comparison](https://cosmograph.app/docs-lib/comparison/): compara capacidades de visualización e interacción con otras bibliotecas; las cifras y características de versiones deben verificarse al seleccionar.
- [Grafana Node Graph](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/): muestra topologías/relaciones para infraestructura, jerarquías y diagramas; documenta una limitación de nodos visibles y estructuras de datos requeridas.
- [NetBox Visual Explorer](https://netboxlabs.com/docs/visual-explorer/): describe vistas topológicas a partir de inventario documentado en NetBox y aclara que no representa por sí solo el estado vivo del tráfico.
- [Grafana network-topology-exporter](https://github.com/grafana/network-topology-exporter): ofrece una ruta de descubrimiento/exportación de topología que puede alimentar la capa de observabilidad.
- [Awesome Dataviz: Graphs & Networks](https://awesomedataviz.com/topics/graphs-and-networks/): catálogo web adicional para descubrir herramientas de visualización; sus rankings no sustituyen pruebas propias.

## Límites de esta revisión

- Los enlaces de productos comerciales requieren comprobación de precios, ediciones, seguridad y términos en la fecha de adopción.
- Los enlaces de repositorios requieren revisar releases, issues, dependencias, licencia y actividad actual.
- La descripción de una capacidad en documentación no equivale a una prueba de desempeño con el dataset del usuario.
- Los recursos en investigación pueden cambiar de nombre o dejar de mantenerse. Los que llegaron por acortadores no resueltos se mantienen como pendientes.
