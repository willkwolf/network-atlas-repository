# OpenWiki Repository Instructions: Network Atlas

## Objetivo y Filosofía
Network Atlas es el catálogo de referencia y sistema de decisión para personas y agentes que necesitan elegir, evaluar, implementar y desplegar herramientas, bibliotecas, datasets y algoritmos para el análisis y visualización de redes complejas.

Este wiki constituye la **fuente de verdad canónica** organizada bajo la especificación **OKF (Open Knowledge Format) v0.2**, diseñada para que cualquier agente de IA o desarrollador obtenga respuestas precisas en tiempo mínimo sin lecturas redundantes.

## Directrices de Documentación para Agentes
1. **Evidencia fundada (Grounded Claims):**
   - Toda afirmación sobre capacidades, compatibilidad o rendimiento debe estar respaldada por fuentes primarias (`data/resources.json`, documentación oficial, benchmarks reproducibles).
   - Utilizar identificadores de recursos en formato `repo://<ruta-relativa>#L<inicio>-L<fin>` cuando se citen archivos del repositorio.
2. **Distinción entre visualización y análisis:**
   - Nunca tratar la visualización como sustituto de métricas de centralidad, detección de comunidades fundamentada o inferencia causal.
3. **Manejo de Incertidumbre:**
   - Si una herramienta posee `verification_status: needs_link_resolution`, documentarla explícitamente como pendiente de confirmación.
4. **Taxonomía Canónica:**
   - Respetar las categorías primarias y dimensiones definidas en `data/domain-taxonomy.json`:
     - `desktop_exploration`
     - `web_hosted`
     - `python_analysis`
     - `web_visualization`
     - `r_analysis`
     - `scale_distributed`
     - `higher_order_temporal`
     - `research_layout_algorithms`
     - `datasets_benchmarks`
     - `graph_database_query`
5. **Idioma:**
   - El idioma principal del contenido de la base de conocimiento es español, manteniendo los identificadores técnicos, nombres de bibliotecas y tags en inglés para interoperabilidad.
