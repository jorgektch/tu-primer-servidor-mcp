"""Inventario de demostración: lógica pura, sin MCP, red ni credenciales.

Los precios se guardan en céntimos para no redondear dinero con floats.
La fuente única de datos es data/inventario.json (compartida con la demo web).
"""
from __future__ import annotations
from functools import lru_cache
import json
from pathlib import Path
import unicodedata

DATA = Path(__file__).resolve().parent / 'data' / 'inventario.json'

@lru_cache(maxsize=1)
def inventario() -> dict:
    return json.loads(DATA.read_text(encoding='utf-8'))

def _normalizar(valor: str) -> str:
    if not isinstance(valor,str):
        return ''
    valor=unicodedata.normalize('NFKD',valor.strip().lower())
    return ''.join(c for c in valor if not unicodedata.combining(c))

def producto_por_nombre(nombre: str) -> dict | None:
    texto=_normalizar(nombre)
    if not texto or len(texto)>70:
        return None
    for p in inventario()['productos']:
        if texto in [_normalizar(p['id']), *[_normalizar(a) for a in p.get('alias',[])]]:
            return p
    return None

def precio_texto(centimos: int) -> str:
    return f'S/ {centimos // 100}.{centimos % 100:02d}'

def consultar_stock(producto: str) -> dict:
    p=producto_por_nombre(producto)
    if p is None:
        return {'ok':False,'codigo':'PRODUCTO_NO_ENCONTRADO','mensaje':'Producto no disponible en el catálogo de prueba.'}
    return {'ok':True,'producto':p['id'],'stock':p['stock'],'disponible':p['stock']>0}

def consultar_precio(producto: str) -> dict:
    p=producto_por_nombre(producto)
    if p is None:
        return {'ok':False,'codigo':'PRODUCTO_NO_ENCONTRADO','mensaje':'Producto no disponible en el catálogo de prueba.'}
    return {'ok':True,'producto':p['id'],'moneda':'PEN','precio_centimos':p['precio_centimos'],
            'precio':precio_texto(p['precio_centimos'])}

def cotizar_producto(producto: str, cantidad: int) -> dict:
    if type(cantidad) is not int or not 1<=cantidad<=100:
        return {'ok':False,'codigo':'CANTIDAD_INVALIDA','mensaje':'Usa un entero entre 1 y 100.'}
    p=producto_por_nombre(producto)
    if p is None:
        return {'ok':False,'codigo':'PRODUCTO_NO_ENCONTRADO','mensaje':'Producto no disponible en el catálogo de prueba.'}
    if cantidad>p['stock']:
        return {'ok':False,'codigo':'STOCK_INSUFICIENTE','producto':p['id'],
                'solicitado':cantidad,'disponibles':p['stock'],'venta_realizada':False}
    total=p['precio_centimos']*cantidad
    return {'ok':True,'producto':p['id'],'cantidad':cantidad,'moneda':'PEN',
            'precio_unitario_centimos':p['precio_centimos'],'total_centimos':total,
            'total':precio_texto(total),'venta_realizada':False}
