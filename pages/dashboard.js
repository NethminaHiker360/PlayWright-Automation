exports.DashboardPage = class DashboardPage {
    constructor(page) {
        this.page = page;

        const employeeNamePattern = /Enter (Employee )?Number|Enter ID/i;
        this.employeeIdInput = page
            .getByRole("textbox", { name: employeeNamePattern })
            .or(page.getByPlaceholder(employeeNamePattern));

        this.dashboardHeading = page.getByRole("heading", { name: /Enter Employee Number/i });
        this.clockInOutButton = page.getByRole("button", { name: /Clock In\/?Out/i });
        this.clockInButton = page.getByRole("button", { name: /^Clock In$/i });
        this.clockOutButton = page.getByRole("button", { name: /^Clock Out$/i });
        this.startBreakButton = page.getByRole("button", { name: /Start Break|Break/i });
        this.endBreakButton = page.getByRole("button", { name: /End Break|Resume|End Lunch/i });
        this.startJobButton = page.getByRole("button", { name: /Start Job|Select Job|Start Task/i });
        this.productiveActivityButton = page.getByRole("button", { name: /Productive/i });
        this.downtimeActivityButton = page.getByRole("button", { name: /Downtime/i });
        this.myHoursButton = page.getByRole("button", { name: /My Hours/i });
        this.mySmokoTimesButton = page.getByRole("button", { name: /My Smoko Times/i });
        this.workTrackerNav = page
            .getByRole("link", { name: /Work Tracker/i })
            .or(page.getByRole("button", { name: /Work Tracker/i }));
        this.reportsNav = page
            .getByRole("button", { name: /Reports/i })
            .or(page.getByRole("link", { name: /Reports/i }));
        this.logoutButton = page.getByRole("button", { name: /Logout/i });
    }

    async enterEmployeeId(employeeId) {
        await this.employeeIdInput.fill(employeeId);
    }
};
