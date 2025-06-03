```
import { test, expect } from '@playwright/test;

test.describe('Rediff', () => {
  test('Navigate to Rediff.com', async ({ page }) => {
    await page.goto('https://www.rediff.com/');
    await expect(page).toHaveURL('https://www.rediff.com/');
  });
});
```