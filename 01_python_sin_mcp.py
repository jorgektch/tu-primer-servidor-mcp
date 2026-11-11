"""Paso 1: misma lógica de negocio en Python puro, antes de añadir MCP."""
import json
from catalogo import consultar_stock,consultar_precio,cotizar_producto

if __name__=='__main__':
    for respuesta in [consultar_stock('bicicleta'),consultar_precio('casco'),
                      cotizar_producto('bicicletas',2),cotizar_producto('casco',1)]:
        print(json.dumps(respuesta,ensure_ascii=False,indent=2))
    print('Estas funciones no son un servidor. El siguiente paso las expondrá como tools MCP.')
