```
import { test, expect } from '@playwright/test';

test('Navigate to rediffmail.com', async ({ page }) => {
  await page.goto('https://www.rediffmail.com/');
  await expect(page).toHaveURL('https://www.rediffmail.com/');
  await expect(page.locator('text=Rediffmail')).toBeVisible();
});
```