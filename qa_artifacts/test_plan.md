# Manual Test Plan

## Purpose
- Provide a manual test strategy for the Nexwave Clock In/Out dashboard that validates the critical employee time tracking user journeys before release.
- Ensure coverage of authentication, employee identification, activity selection, reporting shortcuts, and monitoring workflows visible in the front-end codebase.

## Scope
- In scope: Login, session handling, employee lookup, clock in/out, break handling, job/task selection, downtime/productive activity logging, work tracker monitoring, self-service modals (My Hours, My Smoko Times), report shortcuts, and logout.
- Out of scope: Backend calculation accuracy, third-party report rendering, performance/load testing, and non-web form factors.

## Test Approach
- Functional verification with positive and negative paths across high-priority user journeys.
- UI validation on supported desktop browsers, with focus on navigation flows defined in the React router.
- Session and access control checks to confirm redirect behaviors when authentication fails or expires.
- Data integrity spot checks against server responses for activity submissions and tracker refreshes.

## Test Environment
- Frontend: React + TypeScript + Vite dashboard running against the Nexwave Frappe backend endpoints invoked via hooks (e.g., timetracker handlers and worktracker APIs).
- Browsers: Latest Chrome/Edge; responsive layout sanity on standard desktop resolutions.
- Data: Test employee accounts with valid employee numbers, sample jobs/tasks, and seeded downtime/productive activities.

## Entry Criteria
- Deployable dashboard build is available and reachable.
- Test accounts and seed data (employees, jobs, tasks, activity types) exist.
- Backend APIs for login, activity submission, and reporting links are reachable.

## Exit Criteria
- All planned test cases executed with critical/blocker defects closed or workarounded.
- Regression of major flows (login, clock in/out, break handling, job selection, logout) passes.
- Open defects are documented with clear reproduction steps and severity.

## Risks & Mitigations
- Network/API instability may block submissions or tracker refreshes; capture timestamps and request payloads in defects.
- Seed data drift (missing activity types or jobs) could block selection; reset fixtures before execution.
- Report links may rely on external Frappe pages; verify redirects and surface errors clearly.

## Deliverables
- Executed test case results in Excel.
- Requirement Traceability Matrix (RTM).
- Defect reports logged in the agreed tracker with screenshots or console logs when relevant.
- Signed-off test summary referencing residual risks.

