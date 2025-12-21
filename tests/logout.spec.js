import { test, expect } from "@playwright/test";
import { chromium } from "@playwright/test";
import { timeTrackerURL } from "../common.js";

test("Todo Test", async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  const page = await context.newPage();

  page.goto(timeTrackerURL());
  await page.getByRole("textbox", { name: "Username" }).click();
  await page.getByRole("textbox", { name: "Username" }).fill("Administrator");
  await page.getByRole("textbox", { name: "Password" }).click();
  await page.getByRole("textbox", { name: "Password" }).fill("123");
  await page.getByRole("button", { name: "Sign In" }).click();
  await page.getByRole("textbox", { name: "Enter ID" }).fill("12");


  // Open a new tab in the same context --> same session new tab
  const newPage01 = await context.newPage();
  await newPage01.goto(timeTrackerURL());

  // Open a new window with a new context --> incognito window
  const newContext = await browser.newContext();
  const newPage02 = await newContext.newPage();
  await newPage02.goto(timeTrackerURL());
  await newPage02.pause();
});
