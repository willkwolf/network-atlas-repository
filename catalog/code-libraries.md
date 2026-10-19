# Bibliotecas de análisis, modelado y notebooks

## Python: análisis general

| Recurso | Foco | Decisión rápida |
|---|---|---|
| [NetworkX](https://networkx.org/) | Construcción y análisis general | Mejor punto de inicio para prototipos y claridad del modelo. |
| [igraph](https://igraph.org/) | Análisis eficiente, múltiples lenguajes | Comparar cuando rendimiento o métricas importan. |
| [graph-tool](https://graph-tool.skewed.de/) | Análisis de alto rendimiento | Evaluar si las dependencias y el entorno de instalación son viables. |
| [NetworKit](https://networkit.github.io/) | Análisis eficiente/paralelo | Considerar para redes grandes y algoritmos disponibles. |
| [SNAP](https://snap.stanford.edu/) | Algoritmos, herramientas y datos | Distinguir librería y corpus de datos. |
| [scikit-network](https://scikit-network.readthedocs.io/) | Análisis con interfaz Python científica | Comparar métodos/formatos frente a igraph y NetworkX. |
| [rustworkx](https://www.rustworkx.org/) | Grafos de alto rendimiento en Rust/Python | Útil si su modelo y algoritmos cubren la necesidad. |
| [graspologic](https://github.com/microsoft/graspologic) | Estadística, modelos y redes múltiples | Para preguntas de inferencia/modelado, no solo dibujo. |
| [CDlib](https://cdlib.readthedocs.io/) | Detección/evaluación de comunidades | Comparar varios algoritmos y reportar estabilidad. |
| [python-louvain](https://python-louvain.readthedocs.io/) | Louvain | Componente especializado, no stack completo. |
| [PyGSP](https://pygsp.readthedocs.io/) | Señales sobre grafos | Cuando las señales, filtros u operadores espectrales son centrales. |
| [Py3Plex](https://github.com/SkBlaz/py3plex) | Redes multicapa | Verificar mantenimiento y modelo multicapa antes de usar. |

## Python: visualización/automatización en notebooks

| Recurso | Foco | Límite a considerar |
|---|---|---|
| [PyVis](https://pyvis.readthedocs.io/) | Redes HTML interactivas desde Python | Probar rendimiento y seguridad de las salidas generadas. |
| [ipysigma](https://github.com/medialab/ipysigma) | Sigma.js dentro de Jupyter | No es un backend de análisis por sí mismo. |
| [ipycytoscape](https://github.com/cytoscape/ipycytoscape) | Cytoscape.js en Jupyter | Enfoque de notebook; producto multiusuario requiere arquitectura extra. |
| [py4cytoscape](https://py4cytoscape.readthedocs.io/) | Automatizar Cytoscape con Python | Depende de la integración y versiones del entorno Cytoscape. |
| [netwulf](https://github.com/benmaier/netwulf) | Refinamiento visual interactivo desde Python | Especializado en flujo ligero de visualización. |
| [nxviz](https://github.com/ericmjl/nxviz) | Diseños alternativos sobre NetworkX | Verificar estado de mantenimiento y compatibilidad. |
| [pydot](https://github.com/pydot/pydot) / [PyGraphviz](https://pygraphviz.github.io/) | Puente Python–Graphviz/DOT | No confundir integración de renderizado con analítica. |
| [ipyvolume](https://ipyvolume.readthedocs.io/) | Visualización 3D de notebooks | Adyacente, no una solución específica para redes. |
| [ipydagred3](https://github.com/timkpaine/ipydagred3) | Grafos dirigidos/diagramas en notebook | Validar actividad y compatibilidad antes de adoptarlo. |

## R

| Recurso | Foco | Uso típico |
|---|---|---|
| [igraph for R](https://igraph.org/r/) | Análisis de grafos | Métricas y análisis reproducible. |
| [tidygraph](https://tidygraph.data-imaginist.com/) | Manipulación de redes en un flujo tidy | Transformación y composición de análisis. |
| [ggraph](https://ggraph.data-imaginist.com/) | Visualización estática con gramática gráfica | Figuras y publicaciones reproducibles. |
| [visNetwork](https://datastorm-open.github.io/visNetwork/) | Visualización interactiva | Informes y aplicaciones R. |
| [networkD3](https://christophergandrud.github.io/networkD3/) | Redes D3 desde R | Prototipos HTML interactivos; validar mantenimiento. |
| [statnet](https://statnet.org/) | Modelado estadístico de redes | ERGM y métodos estadísticos sociales, según paquetes. |
| [multinet](https://github.com/cran/multinet) | Redes multicapa | Requiere definir capas e interacciones con precisión. |

## Aprendizaje sobre grafos no es visualización

- [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/) y [DGL](https://www.dgl.ai/) sirven para modelos de aprendizaje profundo sobre grafos, incluyendo GNN.
- Elegirlos exige una pregunta de ML, particiones de datos, función de pérdida, baseline y protocolo de evaluación.
- Un embedding o una predicción de enlace no sustituye a la visualización exploratoria ni demuestra causalidad.
