# Soluciones por dominio

## Redes sociales, organizacionales y de stakeholders

- **Gephi**: exploración general y exportación visual.
- **NodeXL / UCINET / SocNetV**: flujos clásicos de análisis de redes sociales.
- **Network Canvas**: recolección de datos de redes personales/egocéntricas en estudios con personas.
- **Kumu / Graph Commons**: mapas relacionales y comunicación colaborativa.

Comprobar definición de relación, muestreo, límites de la red, no respuesta y sesgo de selección. En estudios con personas, revisar consentimiento, minimización de datos, protección y aprobación ética aplicable.

## Bioinformática, sistemas biológicos y neurociencia

- **Cytoscape**: ecosistema extensible para redes biológicas e integración de anotaciones.
- **Graphia**: exploración de redes científicas/atribuidas.
- **igraph, graph-tool, NetworkX**: análisis reproducible con código.
- **HyperNetX / XGI**: si las interacciones grupales están modeladas como hipergrafos.

La red visual no reemplaza la evidencia experimental de cada interacción. Registrar procedencia, confianza, base de datos de origen y contexto de medición.

## Bibliometría, citas y ciencia

- **VOSviewer**: mapas bibliométricos especializados.
- **OpenAlex**: fuente de metadatos para construir redes de artículos, autores, instituciones y conceptos.
- **Gephi / igraph**: análisis adicionales y vistas diseñadas a medida.

Documentar normalización de nombres, identificadores, cobertura temporal, sesgos de indización y versión de los metadatos.

## Grafos de conocimiento y relaciones empresariales

- **SemSpect**, **Linkurious**, **Neo4j Bloom**: explorar datos semánticos o almacenados en ecosistemas específicos.
- **Graphistry**: investigación visual sobre grafos a escala, según despliegue.
- **Graph Commons / Kumu**: mapas de relaciones para análisis o comunicación, cuando el caso lo permita.

Separar almacenamiento, consultas, analítica y representación. Revisar permisos, auditoría, procedencia, explicación de relaciones inferidas, residencia de datos y salida a formatos comunes.

## Infraestructura y topología IT

Este dominio se enfoca en **qué está conectado con qué, cómo está documentado y cómo cambian las dependencias**; no sustituye herramientas de captura de paquetes ni observabilidad completa.

- [NetBox](https://netbox.readthedocs.io/): inventario/fuente de verdad para la infraestructura documentada.
- [NetBox Visual Explorer](https://netboxlabs.com/docs/visual-explorer/): vistas de racks, energía, cableado y topología WAN desde la información que mantiene NetBox.
- [Grafana Node Graph](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/visualizations/node-graph/): panel de relaciones para servicios, componentes e infraestructura dentro de dashboards.
- [Grafana network-topology-exporter](https://github.com/grafana/network-topology-exporter): componente de descubrimiento/exportación de topología para alimentar sistemas de métricas/observabilidad.
- **Graphviz**: diagramas de arquitectura reproducibles desde código.

Distinción operativa: un inventario describe el estado documentado; un exporter intenta observar/descubrir el estado; un dashboard muestra señales; un análisis de redes calcula propiedades. No asumir que una herramienta resuelve las cuatro funciones.

## Redes complejas, multilayer e interacciones superiores

- **MuxViz / multinet / Py3Plex**: redes multicapa/multiplex.
- **Raphtory / pathpy / ndtv**: redes temporales, eventos o secuencias.
- **HyperNetX / XGI**: hipergrafos y redes de orden superior.
- **GraphScope / cuGraph / Networkit**: candidatos de procesamiento a escala según operación y entorno.

El modelo matemático y la pregunta de investigación deben decidir la herramienta, no al revés.
