"""Soluciones orientativas sin SDK: incorpora las funciones en el servidor como retos."""
from catalogo import producto_por_nombre
def obtener_categoria(producto: str) -> dict:
    p=producto_por_nombre(producto)
    if p is None:return {'ok':False,'codigo':'PRODUCTO_NO_ENCONTRADO'}
    return {'ok':True,'producto':p['id'],'categoria':p['categoria']}

def texto_politicas() -> str:
    return 'Catálogo ficticio de uso educativo; no realiza compras, ventas ni pagos.'

def guion_consulta_stock(producto: str) -> str:
    return f'Consulta disponibilidad ficticia de {producto}; usa la herramienta MCP de stock.'
