# Referencias técnicas y bibliografía

## Fuentes primarias del protocolo (leer primero)

1. **Model Context Protocol.** *Documentación y especificaciones*. https://modelcontextprotocol.io/
2. **MCP Python SDK.** *Get started — First steps* (SDK v2). https://py.sdk.modelcontextprotocol.io/get-started/first-steps/
3. **MCP Python SDK.** *Running your server*. https://py.sdk.modelcontextprotocol.io/run/
4. **MCP Python SDK.** *The Client*. https://py.sdk.modelcontextprotocol.io/client/
5. **MCP Python SDK.** *Client transports*. https://py.sdk.modelcontextprotocol.io/client/transports/
6. **MCP Python SDK.** *Testing*. https://py.sdk.modelcontextprotocol.io/get-started/testing/
7. **MCP Python SDK.** *Migration Guide, v1 → v2*. https://py.sdk.modelcontextprotocol.io/migration/
8. **MCP maintainers.** *Security Best Practices*. https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices

## Investigación complementaria, no fundacional de MCP

- Yao, S., et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023. https://arxiv.org/abs/2210.03629
- Schick, T., et al. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. NeurIPS 2023. https://arxiv.org/abs/2302.04761

**Aclaración epistemológica:** los papers sobre agentes y uso de herramientas explican antecedentes de aplicaciones con LLM, **no** describen ni originan la especificación MCP. Los 14 diagramas Mermaid del README son ilustraciones didácticas originales, no reproducciones de las figuras oficiales.

## Versionado

Este taller fija el rango `mcp[cli]>=2.0,<3` por cambios incompatibles entre las líneas v1 y v2. La documentación enlazada corresponde a la API v2, con Python 3.11+. Comprueba las capacidades y transportes de cada host antes de integrarlo; una versión de un SDK no garantiza que todos los productos admitan la misma revisión del protocolo.
