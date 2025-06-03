const playwright = require('playwright');

(async () => {
  const browser = await playwright.chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://www.toysrus.com');

  await page.waitForLoadState('networkidle2');

  await expect(page).toHaveURL('https://www.toysrus.com/');

  await browser.close();
})();