import { test, expect } from "@playwright/test";

test("Alert Test", async ({ page }) => {
  await page.goto("https://www.selenium.dev/selenium/web/alerts.html#");
    page.on("dialog", async (dialog) => {
    console.log(`Dialog message: ${dialog.message()}`);
    await dialog.accept();
    await page.pause()
  });
});
