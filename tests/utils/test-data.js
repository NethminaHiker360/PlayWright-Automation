export const testData = {
  username: process.env.PW_USERNAME ?? "Administrator",
  password: process.env.PW_PASSWORD ?? "123",
  invalidPassword: process.env.PW_INVALID_PASSWORD ?? "invalid-password",
  employeeId: process.env.PW_EMPLOYEE_ID ?? "12",
  jobName: process.env.PW_JOB_NAME ?? "Sample Job",
  taskName: process.env.PW_TASK_NAME ?? "Sample Task",
  productiveActivity: process.env.PW_PRODUCTIVE_ACTIVITY ?? "Productive",
  downtimeActivity: process.env.PW_DOWNTIME_ACTIVITY ?? "Downtime",
};
