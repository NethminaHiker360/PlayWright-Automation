import { test, expect } from "@playwright/test";
import { DashboardPage } from "../pages/dashboard.js";
import { expectSignedIn, loginAsDefault } from "./utils/auth.js";
import { testData } from "./utils/test-data.js";

test.describe("Self-service modals", () => {
  test.beforeEach(async ({ page }) => {
    await loginAsDefault(page);
    await expectSignedIn(page);
  });

  test("TC-08 My Hours and My Smoko Times modals", async ({ page }) => {
    const dashboard = new DashboardPage(page);

    await dashboard.enterEmployeeId(testData.employeeId);

    await dashboard.myHoursButton.click();
    await expect(page.getByRole("heading", { name: /My Hours/i })).toBeVisible();
    await page.keyboard.press("Escape");

    await dashboard.mySmokoTimesButton.click();
    await expect(page.getByRole("heading", { name: /My Smoko Times/i })).toBeVisible();
    await page.keyboard.press("Escape");
  });
});
