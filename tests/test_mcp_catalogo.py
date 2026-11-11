"""Pruebas 100% offline; usan únicamente la biblioteca estándar."""
import unittest
import catalogo
class CatalogoTests(unittest.TestCase):
    def test_catalogo_four_products(self):
        self.assertEqual(len(catalogo.inventario()['productos']),4)
        self.assertTrue(catalogo.inventario()['simulado'])
    def test_alias_accents(self):
        self.assertEqual(catalogo.producto_por_nombre('BÍCIS')['id'],'bicicleta')
    def test_stock(self):
        self.assertEqual(catalogo.consultar_stock('casco')['stock'],0)
    def test_cotizacion(self):
        r=catalogo.cotizar_producto('bicicletas',2)
        self.assertTrue(r['ok']);self.assertEqual(r['total_centimos'],170000);self.assertFalse(r['venta_realizada'])
    def test_sin_stock(self):
        self.assertEqual(catalogo.cotizar_producto('casco',1)['codigo'],'STOCK_INSUFICIENTE')
    def test_producto_no_existe(self):
        self.assertEqual(catalogo.consultar_precio('patineta')['codigo'],'PRODUCTO_NO_ENCONTRADO')
    def test_cantidad_no_valida(self):
        for x in [0,-1,101,True,False,2.0,'2']:
            with self.subTest(x=x):self.assertEqual(catalogo.cotizar_producto('bicicleta',x)['codigo'],'CANTIDAD_INVALIDA')
    def test_money_exact(self):
        self.assertEqual(catalogo.cotizar_producto('candado',3)['total'],'S/ 135.00')
    def test_malicious_name_not_interpreted(self):
        self.assertIsNone(catalogo.producto_por_nombre('../etc/passwd'))
    def test_no_state_changes(self):
        before=dict(catalogo.producto_por_nombre('bicicleta'))
        catalogo.cotizar_producto('bicicleta',1)
        self.assertEqual(before,catalogo.producto_por_nombre('bicicleta'))
if __name__=='__main__':unittest.main()
