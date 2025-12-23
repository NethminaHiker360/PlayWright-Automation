import { expect } from "@playwright/test";
import { timeTrackerURL } from "../../common.js";
import { LoginPage } from "../../pages/login_page.js";
import { testData } from "./test-data.js";

export async function gotoApp(page) {
  await page.goto(timeTrackerURL());
}

export async function loginWithCredentials(page, username, password) {
  const loginPage = new LoginPage(page);
  await gotoApp(page);
  await loginPage.login(username, password);
}

export async function loginAsDefault(page) {
  await loginWithCredentials(page, testData.username, testData.password);
}

export async function expectSignedIn(page) {
  await expect(
    page.getByRole("heading", { name: /Enter Employee Number/i })
  ).toBeVisible();
}

export async function expectSignedOut(page) {
  await expect(page.getByRole("heading", { name: /Sign In/i })).toBeVisible();
}
