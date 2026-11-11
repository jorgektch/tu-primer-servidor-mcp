"""Verificador estático de slides, rutas educativas y contrato del SDK."""
from pathlib import Path
import json,re,ast
ROOT=Path(__file__).resolve().parents[1]
md=(ROOT/'README.md').read_text(encoding='utf-8')
sections=re.split(r'\n---\n',md)
assert len(sections)>=40, f'Diapositivas insuficientes: {len(sections)}'
assert md.count('```mermaid')>=9
assert md.count('```')%2==0,'Código Markdown sin cerrar'
assert md.count('Note:')>=35
config=json.loads((ROOT/'presentation.config.json').read_text(encoding='utf-8'))
assert config['presentation']['repositoryUrl']=='https://github.com/jorgektch/tu-primer-servidor-mcp'
required=['servidor_mcp.py','cliente_mcp.py','catalogo.py','data/inventario.json',
          'demo/index.html','demo/protocol.mjs','notebooks/01_tu_primer_servidor_mcp.ipynb',
          'docs/GUIA_DEL_INSTRUCTOR.md','docs/REFERENCIAS.md','ejercicios/retos.md']
for rel in required: assert (ROOT/rel).is_file(),rel
for rel in ['servidor_mcp.py','cliente_mcp.py','catalogo.py','01_python_sin_mcp.py','02_probar_cliente_mcp.py']:
    ast.parse((ROOT/rel).read_text(encoding='utf-8'))
notebook=json.loads((ROOT/'notebooks/01_tu_primer_servidor_mcp.ipynb').read_text())
assert len(notebook['cells'])>=10
assert '@mcp.tool()' in (ROOT/'servidor_mcp.py').read_text()
print(f'OK: {len(sections)} slides, {md.count("```mermaid")} Mermaid, {len(notebook["cells"])} notebook cells')
