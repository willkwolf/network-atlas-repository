# Métodos, validez y evaluación de herramientas

## Separar cinco capas

1. **Modelo del fenómeno:** qué entidades y relaciones existen, cuál es su semántica y qué relaciones faltan.
2. **Datos observados:** cobertura, muestreo, atribución, duplicados, errores, fechas, sesgos y privacidad.
3. **Transformación/modelado:** proyecciones, filtros, inferencia, muestreo, agregaciones y supuestos.
4. **Análisis:** métricas, estimadores, algoritmos, parámetros, incertidumbre y pruebas de robustez.
5. **Visualización:** layout, codificaciones, interacción y comunicación.

Una imagen visible demuestra como máximo que un conjunto de datos se representó de una forma. No valida automáticamente las capas 1–4.

## Validez de una representación visual

- Declarar qué significan nodos, aristas, colores, tamaños, posiciones y grosores.
- Evitar usar la posición visual como distancia sustantiva a menos que el algoritmo y el diseño lo justifiquen.
- Si un layout es estocástico, guardar semilla y configuración cuando sea posible; informar estabilidad si la lectura depende de la posición.
- Reportar filtros, agregación, muestreo y nodos/aristas ocultos.
- Incluir tabla o vista alternativa para contrastar una lectura que dependa del gráfico.
- No equiparar “cluster visual” con comunidad estadísticamente validada.

## Validez analítica

Para cada métrica/método, documentar:

- definición matemática y pregunta que responde;
- supuestos sobre dirección, peso, multiaristas, conectividad y población observada;
- escala/unidad e interpretación permitida;
- parámetros, semillas, baseline y versión;
- análisis de sensibilidad y robustez;
- comparación con métodos alternativos cuando sea relevante;
- advertencias sobre datos faltantes, confusión, sesgos y causalidad.

## Evaluación de herramientas

### Evaluación funcional

Crear una matriz de requisitos verificables: importación/exportación, tipos de grafo, filtros, algoritmos, layouts, interacción, escalabilidad, API, notebook, colaboración y control de acceso. Evitar puntuaciones subjetivas sin evidencia.

### Benchmark de rendimiento

Separar medidas por operación y ejecutar al menos tres tamaños representativos cuando resulte viable. Publicar configuración completa; incluir resultados fallidos, no solo el mejor caso. Evitar comparar hardware, versiones o algoritmos diferentes sin reconocerlo.

### Evaluación de uso

Definir tareas, población, tiempo, tasa de error, calidad de conclusión, trazabilidad y accesibilidad. Un juicio estético puede formar parte del diseño, pero no sustituye la medida de desempeño.

### Evidencia mínima por recurso

- URL primaria y versión/fecha.
- Página oficial, documentación o repositorio que respalda la descripción.
- Licencia/precio/condiciones como campos separados, con fecha de comprobación.
- Requisitos técnicos y límites documentados.
- Un ejemplo de tarea en la que encaja y un límite conocido.
- Resultado de prueba propia, solo si el repositorio realmente la ejecutó.

## Niveles de evidencia recomendados

- **E0 — sin verificar:** enlace o nombre aportado; identidad/estado incierto.
- **E1 — fuente primaria localizada:** la documentación oficial define el proyecto/capacidad.
- **E2 — uso probado:** se completó una tarea con una versión registrada y un dataset concreto.
- **E3 — comparativa reproducible:** benchmark con baselines, métricas, datos y entorno registrables.
- **E4 — validación contextual:** usuarios o entorno de destino, restricciones de seguridad y resultados repetidos.

No asignar E2–E4 a una herramienta basándose únicamente en una lectura de documentación.
