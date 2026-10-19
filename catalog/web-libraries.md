# Bibliotecas de visualización web

## Selección por necesidad

| Recurso | Punto fuerte | Mejor encaje | Riesgo de decisión |
|---|---|---|---|
| [Cytoscape.js](https://js.cytoscape.org/) | Interacción rica, ecosistema conocido | Aplicaciones web de redes y bioinformática | El tamaño y complejidad de interacción deben probarse con datos reales. |
| [Sigma.js](https://www.sigmajs.org/) | Renderizado especializado para grafos | Exploración web, redes grandes | Complementar con backend/modelo analítico. |
| [Graphology](https://graphology.github.io/) | Modelo/API de grafo en JavaScript | Manipulación del grafo en apps | No es un visualizador completo. |
| [D3-force](https://d3js.org/d3-force) | Primitivas de simulación por fuerzas | Visualizaciones personalizadas | Exige implementar el comportamiento, accesibilidad y UX. |
| [vis-network](https://visjs.github.io/vis-network/) | Red interactiva lista para web | Prototipos/aplicaciones de complejidad moderada | Evaluar límites, mantenimiento y diseño de interacción. |
| [react-force-graph](https://github.com/vasturiano/react-force-graph) | Componentes React 2D/3D/VR | Aplicaciones React que requieren varias vistas | 3D puede añadir ruido y degradar interpretación. |
| [3d-force-graph](https://github.com/vasturiano/3d-force-graph) | Vista 3D de grafos | Casos donde el espacio adicional aporta señal | Navegación y perspectiva pueden dificultar comparación. |
| [AntV G6](https://g6.antv.antgroup.com/) | Framework de grafos JS/TS | Aplicaciones interactivas ricas | Revisar la versión, ecosistema y requisitos antes de fijar arquitectura. |
| [xyflow](https://xyflow.com/) | Editores de nodos y flujos | Procesos, pipelines, workflow builders | Editor de flujo no equivale a motor general de ciencia de redes. |
| [Cosmograph library](https://cosmograph.app/docs-lib/) | Renderizado/exploración de grafos a escala | Casos web con muchos puntos y enlaces | Validar licenciamiento, API y benchmark actual. |

## Reglas de arquitectura

1. Separar **modelo y análisis** de **layout** y **renderizado**. La herramienta visual no debería ser la única copia de la verdad del grafo.
2. Definir contratos explícitos para nodos, aristas, atributos, timestamps, capas, IDs estables y valores ausentes.
3. Preferir agregación y filtros coordinados antes que renderizar todo por defecto.
4. Medir tiempo de carga, memoria, respuesta de búsqueda, fluidez, accesibilidad con teclado, lectura con lector de pantalla y comportamiento con datos parciales.
5. Usar una ruta de exportación (GraphML, CSV de nodos/aristas u otro formato común) para reducir lock-in.
6. Si hay información privada o sensible, verificar qué corre localmente y qué se sube a servicios externos.

## Conceptos próximos, pero diferentes

Las librerías de nodos visuales pueden apuntar a dos productos distintos:

- **Network graph:** entidades y relaciones para descubrir estructura o patrones.
- **Node-based editor:** interfaz en la que el usuario conecta bloques para definir una función o proceso.

Algunas librerías comparten una metáfora visual, pero sus modelos de interacción, accesibilidad y analítica son diferentes.
