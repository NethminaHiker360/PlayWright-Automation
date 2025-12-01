import { test, expect } from '@playwright/test';
import { testURL } from '../common.js';

test('login test', async ({ page }) => {
  await page.goto(testURL());
  await page.getByRole('textbox', { name: 'Username' }).click();
  await page.getByRole('textbox', { name: 'Username' }).fill('Administrator');
  await page.getByRole('textbox', { name: 'Password' }).click();
  await page.getByRole('textbox', { name: 'Password' }).fill('123');
  await page.getByRole('button', { name: 'Sign In' }).click();
  await page.getByRole('button', { name: 'Logout' }).click();
});