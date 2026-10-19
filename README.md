# Network Atlas: índice para visualizar y estudiar redes

**Propósito:** ayudar a personas y agentes a elegir herramientas, bibliotecas, datasets, estándares y métodos para representar, analizar, investigar, experimentar y desplegar sistemas de relaciones.

Este repositorio no intenta ser otra lista enciclopédica de enlaces. Su núcleo es un **sistema de decisión**: clasifica los recursos por función principal y añade dimensiones independientes para modelo de red, escala, entorno de ejecución, dominio y madurez.

## Empezar en 2 minutos

1. Abrir [`INDEX.md`](INDEX.md) para ver el mapa de contenidos.
2. Usar [`DECISION_GUIDE.md`](DECISION_GUIDE.md) para pasar de una necesidad a una shortlist.
3. Consultar [`data/resources.json`](data/resources.json) o [`data/resources.csv`](data/resources.csv) cuando se necesite filtrar programáticamente.
4. Revisar [`research/FRONTIER_MAP.md`](research/FRONTIER_MAP.md) para temas de frontera y [`commercial/BUY_VS_BUILD.md`](commercial/BUY_VS_BUILD.md) para decisiones de adopción comercial.

Buscar en el catálogo desde una terminal, sin dependencias externas:

```bash
python scripts/find_resources.py --category web_visualization
python scripts/find_resources.py --network-type hypergraph --json
python scripts/find_resources.py --text bibliometric
```

## Alcance

Incluye ciencia de redes, análisis de grafos, visualización interactiva, bibliometría, redes sociales, biología, grafos de conocimiento, redes temporales y de orden superior, sistemas de datos y algunos casos de topología de infraestructura.

**No trata la visualización de redes como sinónimo de análisis de redes.** Un layout atractivo no demuestra centralidad, causalidad, comunidades verdaderas ni importancia sustantiva. Los recursos de topología de infraestructura también se distinguen de herramientas de monitoreo de paquetes/tráfico.

## Estructura

| Ruta | Qué resuelve |
|---|---|
| `INDEX.md` | Índice principal y rutas de entrada por necesidad. |
| `TAXONOMY.md` | Modelo MECE práctico y dimensiones transversales. |
| `DECISION_GUIDE.md` | Árbol de decisión y shortlists iniciales. |
| `catalog/` | Catálogos por tipo de recurso y tarea principal. |
| `research/` | Frontera científica, evaluación y reproducibilidad. |
| `commercial/` | Criterios de compra, build-vs-buy y operación. |
| `agents/` | Protocolo de consulta y esquema de datos para agentes. |
| `data/resources.json` | Registro canónico legible por máquina. |
| `data/resources.csv` | Espejo tabular del registro para hojas de cálculo. |
| `templates/` | Plantillas para registrar herramientas y experimentos. |
| `sources/` | Procedencia de la lista inicial y notas de investigación. |

## Criterios de calidad

- Priorizar documentación primaria, repositorios oficiales y descripciones específicas de capacidades.
- No confundir compatibilidad con desempeño: la escala depende del dataset, algoritmo, hardware, memoria, layout y tarea.
- Separar proyectos de investigación, software estable, servicios alojados y ofertas comerciales.
- Registrar límites, requisitos, formatos y riesgo de lock-in, además de ventajas.
- Conservar procedencia, fecha de revisión y motivo de inclusión.
- Marcar explícitamente recursos con enlaces cortos o identidad todavía no verificada.

## Estado inicial

El registro inicial reúne herramientas aportadas por el usuario y recursos añadidos durante una búsqueda exploratoria. No representa una auditoría exhaustiva de licencias, seguridad, mantenimiento ni rendimiento. Antes de una adopción real, aplicar [`research/METHODS_AND_EVALUATION.md`](research/METHODS_AND_EVALUATION.md) y confirmar los términos vigentes.

## Recursos externos parecidos

El más cercano es [`briatte/awesome-network-analysis`](https://github.com/briatte/awesome-network-analysis), una lista amplia que incluye métodos, datos, cursos, software y artículos. Este repositorio **no la reemplaza ni la replica**: aporta clasificación orientada a decisiones, un registro estructurado, evaluación de evidencia, rutas de selección y una separación explícita entre investigación, uso comercial y visualización.

Véase [`catalog/existing-repositories.md`](catalog/existing-repositories.md).
