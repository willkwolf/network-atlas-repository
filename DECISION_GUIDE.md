# Guía de decisión: de la pregunta a la herramienta

## Árbol mínimo

### 1. ¿Cuál es el resultado que necesita el usuario?

- **Explorar una red existente rápidamente:** empezar con Gephi, Cytoscape, Graphia o un producto web según dominio, escala y colaboración.
- **Analizar estructura y métricas con código:** empezar por NetworkX para prototipar; comparar igraph, graph-tool o NetworKit cuando el tamaño/algoritmo lo exijan.
- **Construir una visualización en una app web:** elegir Sigma.js, Cytoscape.js, G6 o Cosmograph según interacción, tamaño y control de diseño.
- **Dibujar diagramas reproducibles:** Graphviz; para editores interactivos de nodos/flujos, xyflow.
- **Visualizar series de tiempo/redes cambiantes:** evaluar Raphtory, pathpy y herramientas de redes dinámicas en el ecosistema R.
- **Analizar relaciones de más de dos entidades:** evaluar XGI o HyperNetX para hipergrafos y redes de orden superior.
- **Procesar a escala o aprovechar GPU:** evaluar cuGraph, GraphScope o un entorno distribuido existente. No introducir infraestructura distribuida sin prueba de necesidad.
- **Explorar datos persistidos en una graph database:** evaluar el motor y el visualizador adecuados juntos (por ejemplo, Neo4j Graph Data Science y Bloom, con sus roles separados).
- **Representar infraestructura IT/topología:** partir de la fuente de verdad y observabilidad existentes; revisar NetBox Visual Explorer, Grafana Node Graph y el exporter de topología de Grafana.
- **Mapear literatura científica:** VOSviewer y OpenAlex son rutas de entrada; la limpieza bibliográfica es parte sustancial del trabajo.

### 2. Comprobar la forma del dato

Antes de elegir, responder:

1. ¿Qué representa un nodo? ¿Qué cuenta como relación real?
2. ¿Hay dirección, peso, tipo, atributos, capas o marca temporal?
3. ¿Es una relación por pares o conecta grupos de tres o más entidades?
4. ¿Necesito la red observada, inferida, simulada o normativa?
5. ¿Qué información se pierde si reduzco, agrego o muestreo la red?

Si la respuesta a 2–3 cambia el modelo, no decidir solo por la apariencia de la herramienta.

### 3. Probar escala con una muestra representativa

Usar datos anonimizados que conserven densidad, distribución de grados, heterogeneidad, cantidad de atributos y patrón temporal. Registrar:

- nodos, aristas y densidad;
- formato y coste de carga/limpieza;
- memoria pico y tiempo de importación;
- tiempo del algoritmo o layout;
- FPS/latencia de interacción y límites de navegador;
- tiempo de exportación y pérdida de atributos;
- hardware, sistema operativo, versiones y parámetros.

No utilizar una cifra publicitaria de “millones de nodos” como prueba suficiente: renderizado, layout, análisis y consulta son operaciones distintas.

## Shortlist de partida por escenario

| Escenario | Primera prueba | Alternativa o siguiente nivel | Señal para descartar |
|---|---|---|---|
| Exploración general no-code | Gephi | Graphia o Tulip | El importador no conserva atributos/relaciones o el layout confunde más de lo que aclara. |
| Bioinformática | Cytoscape | Graphia, igraph | No hay acceso a los atributos/anotaciones biológicas requeridas. |
| Ciencia de redes desde Python | NetworkX | igraph / graph-tool / NetworKit | La memoria o runtime no sirve; comparar por algoritmo concreto. |
| App web propia | Sigma.js | Cytoscape.js, G6, Cosmograph | Se requiere analítica avanzada que la capa visual no aporta o accesibilidad insuficiente. |
| Mapas bibliométricos | VOSviewer | Gephi + datos de OpenAlex | Desambiguación y procedencia de datos insuficientes. |
| Red temporal/eventos | Raphtory o pathpy | ndtv/R y herramientas del estudio | El modelo solo conserva snapshots y pierde orden/eventos. |
| Hipergrafo/orden superior | XGI | HyperNetX | Solo existe representación de aristas binarias que destruye relaciones grupales. |
| Cómputo en GPU | cuGraph | stack distribuido existente | No hay GPU compatible, transferencia de datos costosa o no existe algoritmo requerido. |
| Topología IT | NetBox / Grafana según función | exporter de topología | Se usa visualización estática como sustituto del monitoreo live, o viceversa. |
| Investigación comercial | prueba de concepto con criterios | build vs buy | Sin benchmark de carga real, revisión de seguridad ni TCO. |

## Preguntas de selección obligatorias

- **Función:** ¿analizar, inferir, explorar, comunicar, operar o hacer consultas?
- **Fidelidad:** ¿el producto conserva datos, metadatos, dirección, multiaristas, tiempo y semántica?
- **Escala:** ¿el límite relevante es carga, cálculo, layout, render, consulta o colaboración?
- **Integración:** ¿qué formatos/APIs y lenguajes admite y qué se pierde en la conversión?
- **Gobierno:** ¿SaaS o self-hosted? ¿Qué datos saldrán del perímetro? ¿Hay controles, auditoría y borrado?
- **Viabilidad:** ¿licencia, coste total, mantenimiento, skills del equipo y exportación permiten migrar luego?

## Anti-patterns

- Elegir un producto solo por una imagen de ejemplo o por estrellas en GitHub.
- Leer el layout de fuerza como si fuera geografía o evidencia causal.
- Calcular centralidad en una red con relaciones no comparables sin justificar la semántica del peso/dirección.
- Reducir red temporal, multicapa o de orden superior a un grafo estático binario antes de evaluar la pérdida.
- Evaluar una herramienta únicamente con un dataset de juguete.
- Producir una “hairball” con todas las aristas cuando la pregunta exige ego-red, rutas, comunidades contrastables o agregación.
