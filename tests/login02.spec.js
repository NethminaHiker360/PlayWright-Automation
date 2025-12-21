import { test, expect } from "@playwright/test";
import { timeTrackerURL } from "../common.js";
import {LoginPage} from "../pages/login_page.js";
import { chromium } from "@playwright/test";


test('Login Test 02', async () => {

    // Launch browser and create a new page without using the fixture
    const browser = await chromium.launch({ headless: false });
    const context = await browser.newContext();
    const page = await context.newPage();

    const loginPage = new LoginPage(page);
    const timeTrackerUrl = timeTrackerURL();

    // Navigate to the Time Tracker URL
    await loginPage.goto(timeTrackerUrl);

    await page.pause();

    // Perform login
    await loginPage.login('Administrator', '123');

    
});
