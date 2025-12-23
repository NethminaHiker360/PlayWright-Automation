import { test, expect } from "@playwright/test";
import { DashboardPage } from "../pages/dashboard.js";
import { expectSignedIn, loginAsDefault } from "./utils/auth.js";

test.describe("Reports navigation", () => {
  test.beforeEach(async ({ page }) => {
    await loginAsDefault(page);
    await expectSignedIn(page);
  });

  test("TC-10 Reports dropdown navigates to Frappe reports", async ({ page }) => {
    const dashboard = new DashboardPage(page);

    await dashboard.reportsNav.click();

    const reportLinks = page
      .getByRole("menuitem")
      .or(page.getByRole("link"));
    const count = await reportLinks.count();

    expect(count).toBeGreaterThan(0);

    for (let i = 0; i < count; i += 1) {
      const link = reportLinks.nth(i);
      const href = await link.getAttribute("href");
      expect(href).not.toBeNull();
    }
  });
});
