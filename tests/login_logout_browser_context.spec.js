import { test, expect } from "@playwright/test";
import { timeTrackerURL } from "../common.js";
import { chromium } from "playwright";

test("slow", async () => {
  const browser = await chromium.launch({
    headless: false,
    slowMo: 500,
  });

  const context = await browser.newContext({
    recordVideo: {
      dir: "videos/",
      size: { width: 800, height: 600 },
    },
  });

  const page = await context.newPage();

  await page.goto(timeTrackerURL());

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
  await expect(page.getByRole("button", { name: "Logout" })).toBeEnabled();

  // Perform logout
  await page.getByRole("button", { name: "Logout" }).click();
});
