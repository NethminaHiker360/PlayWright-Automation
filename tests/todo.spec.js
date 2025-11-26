import { test, expect } from '@playwright/test';

test('test @Sanity', async ({ page }) => {
  await page.goto('https://todomvc.com/examples/react/dist/');
  await page.getByTestId('text-input').click();
  await page.getByTestId('text-input').fill('Play Music');
  await page.getByTestId('text-input').press('Enter');
  await page.getByTestId('text-input').fill('Bike Ride');
  await page.getByTestId('text-input').press('Enter');
  await page.getByTestId('text-input').fill('Buy Foods');
  await page.getByTestId('text-input').press('Enter');
  await page.getByRole('listitem').filter({ hasText: 'Play Music' }).getByTestId('todo-item-toggle').check();
  await page.getByRole('link', { name: 'Active' }).click();
  await page.getByRole('link', { name: 'Completed' }).click();
  await page.getByRole('link', { name: 'All' }).click();
  await page.getByRole('listitem').filter({ hasText: 'Bike Ride' }).getByTestId('todo-item-toggle').check();
  await page.getByRole('button', { name: 'Clear completed' }).click();
  await expect(page.getByTestId('todo-item-label')).toBeVisible();
  await page.getByTestId('todo-item-label').click();
  await page.getByTestId('todo-item-toggle').check();
  await expect(page.getByTestId('todo-item-label')).toBeVisible();
});