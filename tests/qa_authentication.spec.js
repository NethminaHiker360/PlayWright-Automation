import { test, expect } from "@playwright/test";
import { LoginPage } from "../pages/login_page.js";
import { DashboardPage } from "../pages/dashboard.js";
import {
  expectSignedIn,
  expectSignedOut,
  gotoApp,
  loginAsDefault,
} from "./utils/auth.js";
import { testData } from "./utils/test-data.js";

const signInHeading = { name: /Sign In/i };
const dashboardHeading = { name: /Enter Employee Number/i };

test.describe("Authentication", () => {
  test("TC-01 User can log in with valid credentials", async ({ page }) => {
    await loginAsDefault(page);
    await expectSignedIn(page);
  });

  test("TC-02 Invalid login is rejected", async ({ page }) => {
    const loginPage = new LoginPage(page);
    await gotoApp(page);
    await loginPage.login(testData.username, testData.invalidPassword);

    await expect(page.getByRole("heading", signInHeading)).toBeVisible();
    await expect(page.getByRole("heading", dashboardHeading)).toBeHidden();
  });

  test("TC-03 Unauthenticated user is redirected to login", async ({ page }) => {
    await gotoApp(page);
    await expectSignedOut(page);
  });

  test("TC-11 Logout ends session", async ({ page }) => {
    const dashboard = new DashboardPage(page);
    await loginAsDefault(page);
    await expectSignedIn(page);

    await dashboard.logoutButton.click();
    await expectSignedOut(page);

    await gotoApp(page);
    await expectSignedOut(page);
  });
});
