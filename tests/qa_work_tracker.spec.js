import { test, expect } from "@playwright/test";
import { DashboardPage } from "../pages/dashboard.js";
import { expectSignedIn, loginAsDefault } from "./utils/auth.js";

test.describe("Work Tracker", () => {
  test.beforeEach(async ({ page }) => {
    await loginAsDefault(page);
    await expectSignedIn(page);
  });

  test("TC-09 Work Tracker refresh and data sections", async ({ page }) => {
    const dashboard = new DashboardPage(page);

    await dashboard.workTrackerNav.click();
    await expect(page.getByRole("heading", { name: /Work Tracker/i })).toBeVisible();

    const dataSection = page.getByText(/Active Sessions|Downtime|Productive|Tasks/i).first();
    await expect(dataSection).toBeVisible();

    const refreshButton = page.getByRole("button", { name: /Refresh/i });
    if (await refreshButton.count()) {
      await refreshButton.click();
    }
  });
});
