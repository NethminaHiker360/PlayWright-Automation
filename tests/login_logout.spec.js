import { test, expect } from '@playwright/test';
import { testURL } from '../common.js';

test('login test', async ({ page }) => {
  // Go to website
  await page.goto(testURL());

  // Verify Sign In page is displayed
  await expect(page.getByRole('heading', { name: 'Sign In' })).toBeVisible();

  // Perform login
  await page.getByRole('textbox', { name: 'Username' }).click();
  await page.getByRole('textbox', { name: 'Username' }).fill('Administrator');
  await page.getByRole('textbox', { name: 'Password' }).click();
  await page.getByRole('textbox', { name: 'Password' }).fill('123');
  await page.getByRole('button', { name: 'Sign In' }).click();

  // Verify Time Tracker page is displayed
  await expect(page.getByRole('heading', { name: 'Enter Employee Number' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Clock In/Out' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Logout' })).toBeEnabled();

  // Perform logout
  await page.getByRole('button', { name: 'Logout' }).click();
});