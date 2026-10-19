# Mapa de investigación de frontera

Este documento es un **mapa de temas para vigilar**, no una afirmación de que cada línea sea nueva ni de que un paquete concreto haya resuelto el problema. Las fronteras cambian; cada tema requiere una búsqueda bibliográfica y revisión de artículos recientes antes de iniciar un proyecto.

## 1. Representaciones que superan el grafo estático

- **Redes temporales y de eventos:** distinguir cuándo aparece una arista, duración, orden de eventos y ventanas temporales.
- **Redes multicapa/multiplex:** mantener capas semánticamente distintas y modelar interacciones entre ellas.
- **Hipergrafos, complejos simpliciales e interacciones de orden superior:** representar relaciones grupales sin convertirlas prematuramente en aristas por pares.
- **Redes heterogéneas y atribuidas:** tipos de nodos/aristas, atributos y fuentes distintas.
- **Redes dinámicas con incertidumbre:** distinguir arista observada, inferida, probable, simulada y desconocida.

Recursos de entrada: [Raphtory](https://www.raphtory.com/), [pathpy](https://www.pathpy.net/), [MuxViz](http://muxviz.net/), [XGI](https://xgi-org.github.io/xgi/), [HyperNetX](https://hypernetx.readthedocs.io/) y [graspologic](https://github.com/microsoft/graspologic).

## 2. Visual analytics y cognición

Preguntas abiertas/prácticas:

- ¿Qué tarea se mejora con layout libre frente a matrices de adyacencia, small multiples, mapas de calor, Sankey u otras codificaciones?
- ¿Cómo equilibrar overview, zoom, filtrado, detalle bajo demanda y trazabilidad de cada conclusión?
- ¿Cómo comunicar densidad, incertidumbre y relaciones ausentes sin implicar certeza visual excesiva?
- ¿Cuándo las vistas 3D aportan información útil frente a oclusión, perspectiva y carga cognitiva?
- ¿Qué controles y alternativas hacen una visualización accesible y reproducible?

Diseñar el estudio alrededor de tareas (comparar comunidades, rastrear caminos, localizar anomalías, contrastar hipótesis), no solo preferencia estética.

## 3. Algoritmos de layout, escala e interacción

- Layout determinista/reproducible frente a simulaciones estocásticas.
- Estabilidad de posiciones entre snapshots temporales.
- Layouts conscientes de atributos, semántica, jerarquía, restricciones y espacio geográfico.
- Agregación jerárquica, bundling, muestreo y vistas centradas en ego/red de interés.
- GPU, WebGL/WebGPU y renderizado progresivo para grafos densos o de gran tamaño.
- Medir por separado cálculo del layout, renderizado, hit-testing, memoria, interacción y comprensión de la tarea.

Puntos de partida: [OGDF](https://ogdf.net/), [Sigma.js](https://www.sigmajs.org/), [Cosmograph](https://cosmograph.app/), [cuGraph](https://docs.rapids.ai/api/cugraph/stable/) y [GraphScope](https://graphscope.io/docs/).

## 4. Aprendizaje automático sobre grafos

- Graph embeddings y GNN para nodos, enlaces, grafos y redes heterogéneas.
- Detección de anomalías, predicción de enlaces, clasificación y recomendación.
- Evaluación con leakage temporal, sesgo de muestreo, cambios de distribución y entidades frías.
- Interpretabilidad y explicaciones locales/estructurales que puedan comprobarse.
- Evaluación robusta frente a baselines simples, métodos clásicos y ablaciones.

Recursos: [OGB](https://ogb.stanford.edu/), [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/), [DGL](https://www.dgl.ai/), [Awesome Graph Classification](https://github.com/benedekrozemberczki/awesome-graph-classification) y [Awesome Community Detection](https://github.com/benedekrozemberczki/awesome-community-detection).

## 5. Inferencia, causalidad y dinámica de redes

No asumir que una asociación de red explica la causalidad. Distinguir homofilia, influencia, exposición compartida, selección, confusión, observación incompleta y cambios en la red. Para cada método, registrar supuestos identificadores, sensibilidad, diseño de identificación y límites.

Líneas útiles: modelos generativos de redes, ERGM y modelos estocásticos, difusión/contagio, intervención sobre redes, modelos de eventos, dinámica temporal y redes inferidas desde datos no relacionales.

## 6. Ingeniería, operación y gobernanza

- Pipelines reproducibles de limpieza, construcción, análisis y publicación.
- Auditoría de procedencia de nodos y aristas.
- Privacidad y reidentificación de grafos; los identificadores seudónimos no eliminan el riesgo relacional.
- Controles de acceso por nodo/relación, borrado y exportación en productos empresariales.
- Versionado de datasets y modelos, experimentos con parámetros y métricas de validez.
- Conversión entre bases de grafos, motores analíticos y capas visuales.

## Plantilla para promover una línea a “frontera verificada”

Exigir: pregunta precisa, búsqueda bibliográfica fechada, artículos primarios revisados, baselines, tareas y datasets, resultados reproducibles, limitaciones, licencia/código, estado de mantenimiento y nivel de evidencia. Un tema de moda o una página comercial no bastan.
