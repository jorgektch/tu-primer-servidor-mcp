/** Simulación educativa determinista; no usa MCP, red de modelos ni credenciales. */
export const TOOL_NAMES=['consultar_stock','consultar_precio','cotizar_producto'];
export const RESOURCE_URIS=['inventario://catalogo','inventario://producto/{producto}'];
export const PROMPT_NAMES=['guion_cotizacion'];
export const CASES=[
  {id:'discover',label:'Descubrir Tools',method:'tools/list',params:{}},
  {id:'quote',label:'Cotizar 2 bicicletas',method:'tools/call',params:{name:'cotizar_producto',arguments:{producto:'bicicletas',cantidad:2}}},
  {id:'empty',label:'Intentar cotizar casco sin stock',method:'tools/call',params:{name:'cotizar_producto',arguments:{producto:'casco',cantidad:1}}},
  {id:'invalid',label:'Rechazar cantidad inválida',method:'tools/call',params:{name:'cotizar_producto',arguments:{producto:'bicicleta',cantidad:0}}},
  {id:'resource',label:'Leer catálogo (Resource)',method:'resources/read',params:{uri:'inventario://catalogo'}},
  {id:'prompt',label:'Solicitar Prompt',method:'prompts/get',params:{name:'guion_cotizacion',arguments:{producto:'bicicleta',cantidad:'2'}}}
];
export function findProduct(catalog,name){
  if(typeof name!=='string'||name.length>70)return null;
  const clean=v=>String(v).normalize('NFD').replace(/[\u0300-\u036f]/g,'').trim().toLowerCase();
  return catalog.productos.find(p=>[p.id,...(p.alias||[])].some(x=>clean(x)===clean(name)))||null;
}
export function responseFor(test,catalog){
  if(!catalog||!Array.isArray(catalog.productos))throw new Error('Catálogo de ejemplo inválido');
  if(test.method==='tools/list')return {tools:TOOL_NAMES.map(name=>({name,description:'Herramienta de inventario ficticio',inputSchema:{type:'object'}}))};
  if(test.method==='resources/read')return {contents:[{uri:'inventario://catalogo',mimeType:'application/json',text:JSON.stringify(catalog)}]};
  if(test.method==='prompts/get')return {messages:[{role:'user',content:{type:'text',text:'Cotiza 2 bicicletas con datos del inventario ficticio; no realices compras ni cobros.'}}]};
  const {producto,cantidad}=test.params.arguments,p=findProduct(catalog,producto);
  if(!Number.isInteger(cantidad)||typeof cantidad==='boolean'||cantidad<1||cantidad>100)
    return {isError:false,structuredContent:{ok:false,codigo:'CANTIDAD_INVALIDA',mensaje:'Usa un entero entre 1 y 100.'}};
  if(!p)return {isError:false,structuredContent:{ok:false,codigo:'PRODUCTO_NO_ENCONTRADO'}};
  if(cantidad>p.stock)return {isError:false,structuredContent:{ok:false,codigo:'STOCK_INSUFICIENTE',disponibles:p.stock,solicitado:cantidad,venta_realizada:false}};
  const cents=cantidad*p.precio_centimos;
  return {isError:false,structuredContent:{ok:true,producto:p.id,cantidad,moneda:'PEN',total_centimos:cents,total:`S/ ${Math.floor(cents/100)}.${String(cents%100).padStart(2,'0')}`,venta_realizada:false}};
}
export function rpcView(test,catalog){
  return {request:{jsonrpc:'2.0',id:1,method:test.method,params:test.params},
    response:{jsonrpc:'2.0',id:1,result:responseFor(test,catalog)}};
}
