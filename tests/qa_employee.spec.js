import { test, expect } from "@playwright/test";
import { DashboardPage } from "../pages/dashboard.js";
import { expectSignedIn, loginAsDefault } from "./utils/auth.js";
import { testData } from "./utils/test-data.js";

test.describe("Employee identification", () => {
  test.beforeEach(async ({ page }) => {
    await loginAsDefault(page);
    await expectSignedIn(page);
  });

  test("TC-04 Employee number resolves to employee record", async ({ page }) => {
    const dashboard = new DashboardPage(page);
    await dashboard.enterEmployeeId(testData.employeeId);

    const actionButton = dashboard.clockInOutButton.or(dashboard.clockInButton);
    await expect(actionButton).toBeEnabled();
  });
});
