import { test, expect } from "@playwright/test";
import { timeTrackerURL } from "../common.js";

// Navigate to the app before each test so the page fixture is valid
test.beforeEach(async ({ page }) => {
  await page.goto(timeTrackerURL());
});

// After Each hooks
test.afterEach(async ({ page }) => {
  await page.getByRole('button', { name: 'Logout' }).click();
});

test("login test", async ({ page }) => {
  // Verify Sign In page is displayed
  await expect(page.getByRole("heading", { name: "Sign In" })).toBeVisible();

  // Perform login
  await page.getByRole("textbox", { name: "Username" }).click();
  await page.getByRole("textbox", { name: "Username" }).fill("Administrator");
  await page.getByRole("textbox", { name: "Password" }).click();
  await page.getByRole("textbox", { name: "Password" }).fill("123");
  await page.getByRole("button", { name: "Sign In" }).click();

  // Verify Time Tracker page is displayed
  await expect(
    page.getByRole("heading", { name: "Enter Employee Number" })
  ).toBeVisible();
  await expect(
    page.getByRole("button", { name: "Clock In/Out" })
  ).toBeVisible();
});
