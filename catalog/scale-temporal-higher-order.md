# Escala, redes temporales, multicapa y de orden superior

## Escala y procesamiento

| Recurso | Qué aporta | Antes de elegir |
|---|---|---|
| [RAPIDS cuGraph](https://docs.rapids.ai/api/cugraph/stable/) | Algoritmos de grafos acelerados por GPU | Confirmar GPU/CUDA/OS, transferencia de datos, algoritmos soportados y coste operativo. |
| [GraphScope](https://graphscope.io/docs/) | Plataforma de cálculo de grafos distribuido con interfaces para workloads distintos | Confirmar requisitos de despliegue, seguridad, equipo y partición de datos. |
| [Apache Spark GraphX](https://spark.apache.org/graphx/) | Procesamiento de grafos dentro de Spark | Tiene más sentido si ya existe infraestructura Spark adecuada. |
| [NetworKit](https://networkit.github.io/) | Analítica de redes eficiente | Medir con los algoritmos y distribución del grafo de destino. |
| [graph-tool](https://graph-tool.skewed.de/) | Análisis de rendimiento elevado para varios métodos | Evaluar entorno y disponibilidad de dependencias. |
| [OGDF](https://ogdf.net/) | Algoritmos y layouts para investigación de dibujo de grafos | Relevante para desarrollo de algoritmos y experimentos reproducibles. |
| [GraphBLAS](https://graphblas.org/) | Primitivas de álgebra lineal dispersa aplicables a grafos | Es una capa computacional; no una aplicación visual final. |

**No escalar antes de medir.** Una librería ligera puede ser suficiente; una stack distribuida introduce complejidad, coste y fallos operativos. Los números de rendimiento deben venir de un benchmark comparable y reproducible.

## Redes temporales, multicapa y de orden superior

| Recurso | Modelo principal | Pregunta que ayuda a resolver |
|---|---|---|
| [Raphtory](https://www.raphtory.com/) | Temporal/eventos | ¿Cómo cambian las relaciones y las métricas a lo largo del tiempo? |
| [pathpy](https://www.pathpy.net/) | Redes temporales y caminos de orden superior | ¿La secuencia de relaciones cambia los caminos o procesos? |
| [ndtv/statnet](https://statnet.org/) | Visualización/análisis de redes dinámicas en R | ¿Cómo comunicar cambios temporales en un flujo estadístico? |
| [MuxViz](http://muxviz.net/) | Multicapa/multiplex | ¿Qué estructura aparece entre capas y entrelazamientos? |
| [multinet](https://github.com/cran/multinet) | Multicapa en R | ¿Cómo se representa y analiza cada capa por separado y en conjunto? |
| [Py3Plex](https://github.com/SkBlaz/py3plex) | Multicapa en Python | ¿Cómo construir una representación multicapa compatible con un flujo Python? |
| [HyperNetX](https://hypernetx.readthedocs.io/) | Hipergrafos | ¿Una sola relación debe conectar tres o más entidades a la vez? |
| [XGI](https://xgi-org.github.io/xgi/) | Hipergrafos, complejos simpliciales e interacciones de orden superior | ¿Necesito generar, analizar y visualizar interacciones grupales? |

### Señales de que el grafo ordinario es insuficiente

- El orden temporal de los eventos afecta los caminos o la propagación.
- La misma entidad participa en varias capas con semánticas diferentes.
- Una colaboración, reunión, reacción o transacción relaciona simultáneamente a más de dos actores.
- Se requiere representar incertidumbre de las aristas o una distribución sobre grafos posibles.

En estos casos, convertir el conjunto a aristas por pares puede inducir relaciones que nunca existieron. Documentar el criterio de proyección o no proyectar.
