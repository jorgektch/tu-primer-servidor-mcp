# Seguridad del servidor MCP educativo

Este laboratorio utiliza un inventario **ficticio**, no tiene autenticación porque solo se ejecuta localmente y no incluye operaciones de escritura. Estas decisiones **no** lo convierten automáticamente en un servidor apto para producción.

## Modelo de amenazas

| Riesgo | Mitigación en el taller | Requisito adicional para producción |
|---|---|---|
| Parámetros maliciosos | Validación de producto y cantidad | Validación de esquema y permisos por identidad |
| Fuga de datos | Inventario público simulado | Restricciones por usuario, minimización y auditoría |
| Ejecución arbitraria | Sin herramientas shell, URL ni archivos dinámicos | Aislamiento de procesos y allowlists |
| Credenciales | No se utilizan API keys | Gestión de secretos y rotación |
| Servidor remoto no autorizado | stdio local por defecto | Autenticación, autorización, TLS y control de origen |
| Prompt injection | El servidor no ejecuta instrucciones del catálogo | Tratar contenidos devueltos como no confiables |

## Reglas de operación

- Nunca incluyas secretos en JSON, README, commits, capturas ni la demo web.
- No abras `mcp run ... --transport streamable-http` a una IP pública sin controles adicionales.
- Un servidor MCP no debe aceptar tokens de audiencia ajena y pasarlos directamente a APIs posteriores (*token passthrough*).
- Si en un reto agregas escritura real, necesita confirmación, autorización y registro de acciones.
- Trata la salida de herramientas y recursos como **datos no confiables** desde el punto de vista del LLM.

**Fuentes primarias:** [Security Best Practices](https://modelcontextprotocol.io/specification/), [documentación de seguridad del protocolo](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices), [SDK Python](https://py.sdk.modelcontextprotocol.io/).
