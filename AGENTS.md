# Network Atlas - Instrucciones para Agentes de IA

<!-- OPENWIKI:START -->

## OpenWiki

This repository has a generated `openwiki/` evidence index. It is optional just-in-time context, not required startup reading.

- Treat source code and tests as authoritative. A brief's unknowns and review items are verification gaps, not automatic requirements.
- Prefer the narrowest quiet validation that proves the changed behavior. Preserve complete failure output.

The scheduled OpenWiki GitHub Actions workflow refreshes the repository wiki. Do not hand-edit generated OpenWiki pages unless explicitly asked; prefer updating source code/docs and letting OpenWiki regenerate.

<!-- OPENWIKI:END -->

## Protocolo de Conexión y Consulta Rápida (Zero-Latency Agent Guide)

Cuando un agente se conecta a este repositorio, debe seguir este orden para acelerar la velocidad de consulta y evitar leer archivos innecesarios:

### 1. Dónde Buscar Primero (Fuentes de Verdad)
1. **Guía Rápida y Enrutamiento:** [`openwiki/quickstart.md`](openwiki/quickstart.md) - Mapa de decisiones y comandos directos.
2. **Índice Semántico Estructurado:** [`openwiki/index.md`](openwiki/index.md) - Mapa integral de conceptos, herramientas y sistemas bajo estándar OKF.
3. **Catálogo Canónico de Datos:** [`data/resources.json`](data/resources.json) o [`data/resources.csv`](data/resources.csv) - 97+ herramientas con taxonomía normalizada.
4. **Esquema de Validación de Recursos:** [`agents/resource.schema.json`](agents/resource.schema.json).
5. **Protocolo de Enrutamiento:** [`agents/RESOURCE_ROUTING.md`](agents/RESOURCE_ROUTING.md).

### 2. Consulta Programática sin dependencias (CLI)
No necesitas procesar texto en bruto si ejecutas el script CLI del repositorio:
```bash
# Filtrar por categoría principal:
python scripts/find_resources.py --category web_visualization

# Filtrar por modelo de red (ej. hipergrafos, multicapa):
python scripts/find_resources.py --network-type hypergraph --json

# Búsqueda textual por palabra clave:
python scripts/find_resources.py --text bibliometric
```

### 3. Validación y Mantenimiento del Repositorio
Para validar que el registro de recursos cumple con el esquema:
```bash
python scripts/validate_registry.py
```

### 4. Reglas Críticas para Agentes
- **No inventar capacidades ni enlaces:** Comprobar siempre `verification_status` en `data/resources.json`. Si es `needs_link_resolution`, declararlo con honestidad.
- **Distinguir visualización de análisis:** Una red visualmente atractiva no sustituye el cálculo de métricas estructurales o el modelado causal.
- **Respetar la taxonomía oficial:** Categorías primarias (`desktop_exploration`, `web_hosted`, `python_analysis`, `web_visualization`, `r_analysis`, `scale_distributed`, `higher_order_temporal`, `datasets_benchmarks`, `graph_database_query`, `research_layout_algorithms`).
