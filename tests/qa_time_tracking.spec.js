import { test, expect } from "@playwright/test";
import { DashboardPage } from "../pages/dashboard.js";
import { expectSignedIn, loginAsDefault } from "./utils/auth.js";
import { testData } from "./utils/test-data.js";

async function selectOption(page, namePattern, options = {}) {
  const { optional = false } = options;
  const candidates = [
    page.getByRole("option", { name: namePattern }),
    page.getByRole("menuitem", { name: namePattern }),
    page.getByRole("button", { name: namePattern }),
    page.getByRole("listitem", { name: namePattern }),
  ];

  for (const candidate of candidates) {
    if (await candidate.count()) {
      await candidate.first().click();
      return true;
    }
  }

  if (optional) {
    return false;
  }

  throw new Error(`No selectable option found for: ${namePattern}`);
}

async function clockIn(dashboard) {
  await dashboard.enterEmployeeId(testData.employeeId);
  const clockInButton = dashboard.clockInButton.or(dashboard.clockInOutButton);
  await clockInButton.click();
}

test.describe("Time tracking", () => {
  test.beforeEach(async ({ page }) => {
    await loginAsDefault(page);
    await expectSignedIn(page);
  });

  test("TC-05 Clock in and clock out workflow", async ({ page }) => {
    const dashboard = new DashboardPage(page);

    await clockIn(dashboard);
    await dashboard.startJobButton.click();
    await selectOption(page, new RegExp(testData.jobName, "i"));

    const clockOutButton = dashboard.clockOutButton.or(dashboard.clockInOutButton);
    await clockOutButton.click();
  });

  test("TC-06 Break and lunch handling", async ({ page }) => {
    const dashboard = new DashboardPage(page);

    await clockIn(dashboard);
    await dashboard.startBreakButton.click();

    if (await dashboard.productiveActivityButton.count()) {
      await expect(dashboard.productiveActivityButton).toBeDisabled();
    }

    if (await dashboard.downtimeActivityButton.count()) {
      await expect(dashboard.downtimeActivityButton).toBeDisabled();
    }

    await dashboard.endBreakButton.click();
  });

  test("TC-07 Select job/task and record productive/downtime activity", async ({ page }) => {
    const dashboard = new DashboardPage(page);

    await clockIn(dashboard);
    await dashboard.startJobButton.click();
    await selectOption(page, new RegExp(testData.jobName, "i"));
    await selectOption(page, new RegExp(testData.taskName, "i"), { optional: true });

    await dashboard.productiveActivityButton.click();
    await dashboard.downtimeActivityButton.click();
  });
});
