# Guía del instructor · Tu Primer Servidor MCP

**Público:** personas con fundamentos de Python. **Duración recomendada:** 120 minutos (ampliable). **Prerequisitos:** Python 3.11+, conocimientos básicos de funciones y JSON. Para Inspector se recomienda Node.js instalado. No requiere cuentas externas ni API keys.

| Minutos | Módulo | Actividad verificable |
|---|---|---|
| 0–15 | Fundamentos y arquitectura | Clasificar host / cliente / servidor |
| 15–30 | Catálogo Python puro | Ejecutar `01_python_sin_mcp.py` |
| 30–50 | Tools, Resources y Prompts | Revisar `servidor_mcp.py` |
| 50–70 | Cliente stdio | Ejecutar `02_probar_cliente_mcp.py` |
| 70–85 | Inspector / HTTP local | `mcp dev servidor_mcp.py` |
| 85–105 | Seguridad y pruebas | Verificar casos límite, SDK en proceso |
| 105–120 | Retos / evaluación | Añadir una capacidad con prueba |

## Preguntas detonantes

1. ¿Qué parte necesita un LLM? En este taller, ninguna.
2. ¿Qué controla el host y qué controla el servidor?
3. ¿Por qué `catalogo.py` no debe importar MCP?
4. ¿Por qué se usan céntimos enteros para dinero?
5. ¿Por qué la demo web muestra JSON ilustrativo y no conecta a un servidor Python?

## Preparación del docente

- Clonar o descargar el proyecto, activar `venv` y ejecutar `pip install -r requirements.txt`.
- Ejecutar previamente `python 02_probar_cliente_mcp.py` para verificar SDK y stdio.
- Verificar `mcp dev servidor_mcp.py` con la versión oficial v2 y las dependencias de Inspector.
    - Para alumnado avanzado, mostrar [CONEXION_HOSTS.md](CONEXION_HOSTS.md) sin activar un host externo por defecto.
- Servir el repositorio con `python -m http.server 8765`, comprobar presentación y demo.
- Tener un caso de reserva: `python 01_python_sin_mcp.py` funciona offline sin instalar MCP.

## Seguridad de la sesión

- Nunca pegar claves personales ni contraseñas.
- No ejecutar herramientas desconocidas de terceros con permisos amplios.
- No exponer el servidor HTTP del ejercicio a la red pública.
- Diferenciar errores de dominio (`ok:false`) y errores reales de `is_error` del SDK.

## Rúbrica rápida

| Criterio | Peso |
|---|---:|
| Explica host / cliente / servidor | 20 % |
| Implementa Tool con validación y docstring | 30 % |
| Descubre e invoca a través del cliente MCP | 25 % |
| Expone Resource o Prompt correctamente | 15 % |
| Explica los riesgos y límites del ejemplo | 10 % |

**Observación:** la ejecución del cliente con SDK debe verificarse en un entorno real después de instalar dependencias; la demo visual no acredita ese criterio.
