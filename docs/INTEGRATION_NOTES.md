# Integración desde README to Slides

Base inspeccionada: `jorgektch/tu-primer-servidor-mcp`, rama `main`, commit `70b09cab07c02cdf5f33ba190fe26adb422b7725`.

## Archivos mantenidos idénticos a la plantilla vigente v1.5.1

- Todos los módulos `assets/js/*.mjs`.
- `assets/theme.css`.
- `engine-release.json` y su lista SHA-256 de archivos gestionados.
- `tools/update_engine.py`, `tools/build_engine_manifest.py` y `.github/workflows/engine-updates.yml`.
- Framework Reveal.js de `index.html`, con cambios solo de título y metadatos.

## Personalización del contenido

- `README.md` reemplazado por diapositivas y documentación del servidor MCP.
- `presentation.config.json` identifica el repositorio y al expositor.
- Nuevos archivos Python, JSON, notebook, demo, ejercicios, guías y pruebas.
- Workflow de calidad extiende la validación para incluir el SDK MCP real y conserva la suite del motor.

## Alcances

La demo web no tiene backend MCP. Las pruebas locales de dominio son independientes del SDK; las pruebas de `Client` y transportes requieren instalar el SDK v2. No se publican secrets ni se accede a recursos externos de producción. No se crea una release nueva del motor por añadir contenido educativo.
