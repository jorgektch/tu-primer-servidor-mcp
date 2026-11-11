import {test,expect} from '@playwright/test';
test('MCP workshop renders slides and 10+ Mermaid diagrams',async ({page})=>{
  await page.goto('/',{waitUntil:'domcontentloaded'});
  await page.waitForFunction(()=>window.slideReady===true,{},{timeout:60000});
  expect(await page.evaluate(()=>Reveal.getSlides().length)).toBeGreaterThanOrEqual(40);
  const diag=await page.evaluate(()=>window.slideDiagnostics);
  expect(diag.errors).toEqual([]);expect(diag.rendered).toBe(diag.detected);
  expect(diag.detected).toBeGreaterThanOrEqual(9);
  await expect(page.locator('#nav-repository')).toHaveAttribute('href','https://github.com/jorgektch/tu-primer-servidor-mcp');
});
test('didactic simulator produces a quote and never claims to be live MCP',async ({page})=>{
  await page.goto('/demo/',{waitUntil:'domcontentloaded'});
  await expect(page.locator('#status')).toContainText('lista',{timeout:10000});
  await expect(page.locator('#response-json')).toContainText('1700.00');
  await expect(page.getByText('Simulación, no cliente MCP real.')).toBeVisible();
  await page.locator('#case-select').selectOption('empty');
  await expect(page.locator('#response-json')).toContainText('STOCK_INSUFICIENTE');
  await page.locator('#case-select').selectOption('resource');
  await expect(page.locator('#response-json')).toContainText('bicicleta');
});
