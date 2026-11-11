import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {TOOL_NAMES,CASES,RESOURCE_URIS,PROMPT_NAMES,responseFor,findProduct,rpcView} from '../demo/protocol.mjs';
const catalog=JSON.parse(readFileSync(new URL('../data/inventario.json',import.meta.url),'utf8'));
test('inventory dataset is public, fictitious and shared',()=>{
  assert.equal(catalog.simulado,true);assert.equal(catalog.moneda,'PEN');assert.equal(catalog.productos.length,4);
});
test('all primitives have real workshop entries',()=>{
  assert.deepEqual(TOOL_NAMES,['consultar_stock','consultar_precio','cotizar_producto']);
  assert.equal(RESOURCE_URIS.length,2);assert.deepEqual(PROMPT_NAMES,['guion_cotizacion']);
});
test('alias and case-insensitive matching',()=>assert.equal(findProduct(catalog,'BÍCIs').id,'bicicleta'));
test('quote of two bicycles computes exact cents',()=>{
  const r=responseFor(CASES.find(x=>x.id==='quote'),catalog).structuredContent;
  assert.equal(r.total,'S/ 1700.00');assert.equal(r.total_centimos,170000);assert.equal(r.venta_realizada,false);
});
test('stock shortage yields an explicit domain failure',()=>assert.equal(responseFor(CASES.find(x=>x.id==='empty'),catalog).structuredContent.codigo,'STOCK_INSUFICIENTE'));
test('invalid quantities are rejected without side effects',()=>assert.equal(responseFor(CASES.find(x=>x.id==='invalid'),catalog).structuredContent.codigo,'CANTIDAD_INVALIDA'));
test('tool discovery includes exactly 3 tools',()=>assert.equal(responseFor(CASES.find(x=>x.id==='discover'),catalog).tools.length,3));
test('catalog resource returns full public data',()=>{
  const data=JSON.parse(responseFor(CASES.find(x=>x.id==='resource'),catalog).contents[0].text);
  assert.equal(data.productos.length,4);
});
test('prompt is an instruction and does not make a model call',()=>assert.match(responseFor(CASES.find(x=>x.id==='prompt'),catalog).messages[0].content.text,/simulado|ficticio/i));
test('illustrative JSON-RPC request never exposes a secret',()=>{
  const json=JSON.stringify(rpcView(CASES[1],catalog));
  assert.match(json,/tools\/call/);assert.doesNotMatch(json,/API[_-]?KEY|Bearer /i);
});
