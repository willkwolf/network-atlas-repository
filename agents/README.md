# Uso del índice en un agente

No exige instalar una Skill: un agente puede leer `RESOURCE_ROUTING.md` y consultar `../data/resources.json`. La estructura está preparada para convertirse en Skill o herramienta más adelante, sin acoplarla ahora a un proveedor concreto.

Para una integración robusta, filtrar primero por `primary_category`, luego por etiquetas/atributos secundarios y restricciones duras. El texto de `notes` es orientativo; el agente debe abrir la URL primaria antes de tomar una decisión crítica.
