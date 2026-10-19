# Datasets, fuentes y benchmarks

| Recurso | Utilidad | Riesgo/validación necesaria |
|---|---|---|
| [SNAP datasets](https://snap.stanford.edu/data/) | Redes reales y sintéticas ampliamente usadas en investigación | Verificar fuente primaria, versión, licencia, sesgo y unidad de observación. |
| [KONECT](http://konect.cc/) | Colección de datasets de redes | Confirmar metadatos, definición de aristas y términos por dataset. |
| [Network Repository](https://networkrepository.com/) | Catálogo científico con herramientas de análisis visual interactivo | Registrar identificador/versión exacta; la fuente informa diferentes tipos, incluidos temporal y espacial. |
| [ICON](https://icon.colorado.edu/) | Portal académico relacionado con datos de redes | Verificar la disponibilidad actual y el origen de cada colección. |
| [SuiteSparse Matrix Collection](https://sparse.tamu.edu/) | Benchmarks de matrices dispersas útiles en computación y problemas relacionados con grafos | Una matriz no siempre contiene semántica de red interpretable sin documentación. |
| [Open Graph Benchmark (OGB)](https://ogb.stanford.edu/) | Protocolos y datasets de evaluación para graph ML | Mantener split, métricas y protocolo prescritos; evitar leakage. |
| [XGI-DATA](https://github.com/xgi-org/xgi-data) | Datos para hipergrafos/redes de orden superior | Registrar la estructura de interacción grupal y su procedencia. |
| [OpenAlex](https://openalex.org/) | Metadatos de investigación para redes bibliométricas y científicas | Desambiguación de entidades, cobertura desigual y términos/API. |

## Protocolo para aceptar un dataset

- Identificador persistente, versión o fecha de descarga.
- Fuente primaria y licencia/condiciones verificadas.
- Unidad de observación y significado de nodo/arista documentados.
- Dirección, peso, tipo, tiempo y atributos explicados.
- Tratamiento de datos ausentes, duplicados, autoenlaces y entidades ambiguas.
- Limitaciones de representatividad, cobertura, sesgo, privacidad y ética.
- Hash del archivo o mecanismo equivalente para reproducir el mismo artefacto.

## Benchmarks de herramientas

Comparar con una carga relevante: distribución de grados, densidad, componentes, atributos, tipos de arista, temporalidad, tamaño del payload, hardware y operación evaluada. Reportar al menos:

- tiempo de ingestión y transformación;
- memoria máxima y almacenamiento;
- tiempo/resultado del algoritmo;
- tiempo de cálculo del layout y renderizado;
- latencia de interacción y de consultas;
- fidelidad al exportar/reimportar.

Los datasets sintéticos son útiles para aislamiento de variables; no demuestran que una herramienta funcione igual de bien con una red real.
