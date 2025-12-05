import { test, expect } from "@playwright/test";
import { timeTrackerURL } from "../common.js";
import {LoginPage} from "../pages/login_page.js";


test('Login Test', async ({ page }) => {
    const loginPage = new LoginPage(page);
    const timeTrackerUrl = timeTrackerURL();

    // Navigate to the Time Tracker URL
    await loginPage.goto(timeTrackerUrl);

    // Perform login
    await loginPage.login('Administrator', '123');

    await page.pause();
});
