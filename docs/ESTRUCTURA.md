# Estructura del repositorio

```text
tu-primer-servidor-mcp/
├── README.md                         # Misma fuente de documentación y diapositivas
├── index.html                        # Motor Reveal.js de README to Slides v1.5.1
├── presentation.config.json          # Personalización de la presentación
├── 01_python_sin_mcp.py              # Primer paso sin SDK
├── 02_probar_cliente_mcp.py          # Cliente MCP real por stdio
├── catalogo.py                       # Dominio y validaciones
├── servidor_mcp.py                   # SDK oficial v2; Tools, Resources y Prompt
├── cliente_mcp.py                    # Cliente stdio / HTTP real
├── data/inventario.json              # Datos 100% ficticios
├── demo/                             # Visualizador conceptual, NO conecta a MCP
├── notebooks/                        # Ejemplo autocontenido para Colab
├── ejercicios/                       # Retos y soluciones orientativas
├── docs/                             # Guías, conexión a hosts y documentación del motor
├── tests/                            # Pruebas del motor y del taller
├── tools/                            # Actualizador del motor, NO alterar
└── engine-release.json              # Manifiesto y hashes del motor intactos
```

## Relación con los demás talleres

- [Tu Primera Red Neuronal](https://github.com/jorgektch/tu-primera-red-neuronal): entrena un modelo desde cero.
- [Tu Primer Agente de IA](https://github.com/jorgektch/tu-primer-agente-ia): usa herramientas a través de un agente con LLM.
- [Tu Primer Servidor MCP](https://github.com/jorgektch/tu-primer-servidor-mcp): estandariza la publicación y el consumo de herramientas/contexto.
