import {CASES,rpcView} from './protocol.mjs';
const $=id=>document.getElementById(id);
const controls=$('case-select');const request=$('request-json');const response=$('response-json');const label=$('case-title');
const status=$('status');
const render=(catalog)=>{
  const test=CASES.find(c=>c.id===controls.value)||CASES[0];
  label.textContent=test.label;
  const {request:req,response:res}=rpcView(test,catalog);
  request.textContent=JSON.stringify(req,null,2);
  response.textContent=JSON.stringify(res,null,2);
  $('case-description').textContent=test.method==='tools/call'?'Invocación simulada: el backend Python real se prueba desde cliente_mcp.py.':
    'Intercambio didáctico: no hay conexión a un servidor MCP desde esta página.';
};
async function start(){
  try {
    const response=await fetch('../data/inventario.json',{cache:'no-store'});
    if(!response.ok)throw new Error(`HTTP ${response.status}`);
    const data=await response.json();
    for(const c of CASES){const o=document.createElement('option');o.value=c.id;o.textContent=c.label;controls.append(o);}
    controls.value='quote';controls.addEventListener('change',()=>render(data));
    render(data);status.textContent='Catálogo ficticio cargado. Simulación offline lista.';
  }catch(e){status.textContent='Error al cargar el catálogo. Sirve la carpeta desde un servidor HTTP local.';status.setAttribute('role','alert');}
}
start();
