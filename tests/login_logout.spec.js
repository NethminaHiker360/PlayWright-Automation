import { test, expect } from "@playwright/test";
import { timeTrackerURL } from "../common.js";

test.describe("auth flows", () => {
  let context;
  let page;

  test.beforeAll(async ({ browser }) => {
    context = await browser.newContext();
    page = await context.newPage();
    await page.goto(timeTrackerURL());

    // Login once for all tests
    await expect(page.getByRole("heading", { name: "Sign In" })).toBeVisible();
    await page.getByRole("textbox", { name: "Username" }).fill("Administrator");
    await page.getByRole("textbox", { name: "Password" }).fill("123");
    await page.getByRole("button", { name: "Sign In" }).click();
    await expect(
      page.getByRole("heading", { name: "Enter Employee Number" })
    ).toBeVisible();
  });

  test.afterAll(async () => {
    await page.getByRole("button", { name: "Logout" }).click();
    await context.close();
  });

  test("login test", async () => {
    // Verify Time Tracker page is displayed after shared login
    await expect(
      page.getByRole("heading", { name: "Enter Employee Number" })
    ).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Clock In/Out" })
    ).toBeVisible();
  });

  test("Enter Employee Number", async () => {
    await page.getByRole("textbox", { name: "Enter ID" }).click();
    await page.getByRole("textbox", { name: "Enter ID" }).fill("12");
    await page
      .getByRole("button", { name: "Clock In Record your arrival" })
      .click();
    await page.getByRole("button", { name: "Clock Out Record your" }).click();
  });
});
