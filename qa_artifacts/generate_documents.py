from pathlib import Path
import zipfile
from xml.sax.saxutils import escape

BASE_DIR = Path(__file__).resolve().parent

# Data definitions
TEST_PLAN_SECTIONS = [
    (
        "Purpose",
        [
            "Provide a manual test strategy for the Nexwave Clock In/Out dashboard that validates the critical employee time tracking user journeys before release.",
            "Ensure coverage of authentication, employee identification, activity selection, reporting shortcuts, and monitoring workflows visible in the front-end codebase."
        ],
    ),
    (
        "Scope",
        [
            "In scope: Login, session handling, employee lookup, clock in/out, break handling, job/task selection, downtime/productive activity logging, work tracker monitoring, self-service modals (My Hours, My Smoko Times), report shortcuts, and logout.",
            "Out of scope: Backend calculation accuracy, third-party report rendering, performance/load testing, and non-web form factors."
        ],
    ),
    (
        "Test Approach",
        [
            "Functional verification with positive and negative paths across high-priority user journeys.",
            "UI validation on supported desktop browsers, with focus on navigation flows defined in the React router.",
            "Session and access control checks to confirm redirect behaviors when authentication fails or expires.",
            "Data integrity spot checks against server responses for activity submissions and tracker refreshes."
        ],
    ),
    (
        "Test Environment",
        [
            "Frontend: React + TypeScript + Vite dashboard running against the Nexwave Frappe backend endpoints invoked via hooks (e.g., timetracker handlers and worktracker APIs).",
            "Browsers: Latest Chrome/Edge; responsive layout sanity on standard desktop resolutions.",
            "Data: Test employee accounts with valid employee numbers, sample jobs/tasks, and seeded downtime/productive activities."
        ],
    ),
    (
        "Entry Criteria",
        [
            "Deployable dashboard build is available and reachable.",
            "Test accounts and seed data (employees, jobs, tasks, activity types) exist.",
            "Backend APIs for login, activity submission, and reporting links are reachable."
        ],
    ),
    (
        "Exit Criteria",
        [
            "All planned test cases executed with critical/blocker defects closed or workarounded.",
            "Regression of major flows (login, clock in/out, break handling, job selection, logout) passes.",
            "Open defects are documented with clear reproduction steps and severity."
        ],
    ),
    (
        "Risks & Mitigations",
        [
            "Network/API instability may block submissions or tracker refreshes; capture timestamps and request payloads in defects.",
            "Seed data drift (missing activity types or jobs) could block selection; reset fixtures before execution.",
            "Report links may rely on external Frappe pages; verify redirects and surface errors clearly."
        ],
    ),
    (
        "Deliverables",
        [
            "Executed test case results in Excel.",
            "Requirement Traceability Matrix (RTM).",
            "Defect reports logged in the agreed tracker with screenshots or console logs when relevant.",
            "Signed-off test summary referencing residual risks."
        ],
    ),
]

TEST_CASES = [
    {
        "id": "TC-01",
        "title": "User can log in with valid credentials",
        "preconditions": "Valid user exists; login API reachable.",
        "steps": "1. Open /login. 2. Enter valid username/password. 3. Submit.",
        "expected": "User is redirected to the dashboard home without errors.",
        "priority": "High",
        "type": "Positive",
        "status": "Planned",
    },
    {
        "id": "TC-02",
        "title": "Invalid login is rejected",
        "preconditions": "User is logged out.",
        "steps": "1. Open /login. 2. Enter wrong password. 3. Submit.",
        "expected": "Login fails and an error message is shown without navigation to home.",
        "priority": "High",
        "type": "Negative",
        "status": "Planned",
    },
    {
        "id": "TC-03",
        "title": "Unauthenticated user is redirected to login",
        "preconditions": "No active session.",
        "steps": "1. Open /. 2. Observe behavior.",
        "expected": "User is redirected to /login after session check fails.",
        "priority": "High",
        "type": "Negative",
        "status": "Planned",
    },
    {
        "id": "TC-04",
        "title": "Employee number resolves to employee record",
        "preconditions": "Employee list is available.",
        "steps": "1. Enter a known employee number. 2. Observe greeting and state.",
        "expected": "Employee name is displayed and activity buttons are enabled when applicable.",
        "priority": "High",
        "type": "Positive",
        "status": "Planned",
    },
    {
        "id": "TC-05",
        "title": "Clock in and clock out workflow",
        "preconditions": "Employee identified; backend accepts time logs.",
        "steps": "1. Enter employee number. 2. Tap Clock In. 3. Start a job. 4. Clock Out.",
        "expected": "Success toasts appear for each action and state resets per design.",
        "priority": "Critical",
        "type": "Positive",
        "status": "Planned",
    },
    {
        "id": "TC-06",
        "title": "Break and lunch handling",
        "preconditions": "Employee clocked in.",
        "steps": "1. Start Break. 2. Verify activity buttons disable. 3. End Break to resume last activity.",
        "expected": "Break status displays, actions are blocked appropriately, and resuming clears break state.",
        "priority": "High",
        "type": "Positive",
        "status": "Planned",
    },
    {
        "id": "TC-07",
        "title": "Select job or task and record productive/downtime activity",
        "preconditions": "Employee clocked in with available jobs/tasks and activity types.",
        "steps": "1. Choose Start Job and select a job/task. 2. Choose a productive activity. 3. Choose a downtime activity.",
        "expected": "Selections succeed with confirmations; downtime buttons are disabled when on break or before clock-in.",
        "priority": "High",
        "type": "Positive/Negative",
        "status": "Planned",
    },
    {
        "id": "TC-08",
        "title": "Self-service modals for My Hours and My Smoko Times",
        "preconditions": "Employee identified with historical data.",
        "steps": "1. Enter employee number. 2. Open My Hours. 3. Open My Smoko Times.",
        "expected": "Modals load without errors and display the employee-specific report data.",
        "priority": "Medium",
        "type": "Positive",
        "status": "Planned",
    },
    {
        "id": "TC-09",
        "title": "Work Tracker refresh and data sections",
        "preconditions": "Active sessions, downtime, productive activities, and tasks exist.",
        "steps": "1. Navigate to Work Tracker. 2. Observe active sessions and downtime lists. 3. Wait for auto-refresh or trigger manual refresh (if available).",
        "expected": "Data loads across all sections and refresh intervals update the last refreshed timestamp.",
        "priority": "Medium",
        "type": "Positive",
        "status": "Planned",
    },
    {
        "id": "TC-10",
        "title": "Reports dropdown navigates to Frappe reports",
        "preconditions": "Authenticated user on dashboard.",
        "steps": "1. Open Reports dropdown. 2. Select each report link.",
        "expected": "Browser navigates to the corresponding report URLs without blocking UI.",
        "priority": "Low",
        "type": "Positive",
        "status": "Planned",
    },
    {
        "id": "TC-11",
        "title": "Logout ends session",
        "preconditions": "User logged in.",
        "steps": "1. Click Logout. 2. Attempt to access home again.",
        "expected": "User is redirected to login and session endpoints clear credentials.",
        "priority": "High",
        "type": "Positive",
        "status": "Planned",
    },
]

REQUIREMENTS = [
    {"id": "R1", "description": "Users must authenticate with username/password to access the dashboard.", "tests": ["TC-01", "TC-02", "TC-03"]},
    {"id": "R2", "description": "Employee numbers resolve to employee records before allowing actions.", "tests": ["TC-04"]},
    {"id": "R3", "description": "Employees can clock in and clock out with backend confirmation.", "tests": ["TC-05"]},
    {"id": "R4", "description": "Breaks and lunches prevent conflicting activities until ended.", "tests": ["TC-06"]},
    {"id": "R5", "description": "Jobs or tasks can be selected prior to recording activities.", "tests": ["TC-07"]},
    {"id": "R6", "description": "Productive and downtime activities are logged with correct availability rules.", "tests": ["TC-07"]},
    {"id": "R7", "description": "Employees can view self-service My Hours and My Smoko Times details.", "tests": ["TC-08"]},
    {"id": "R8", "description": "Supervisors can monitor active work, downtime, and tasks in Work Tracker.", "tests": ["TC-09"]},
    {"id": "R9", "description": "Report shortcuts open the related Frappe reports.", "tests": ["TC-10"]},
    {"id": "R10", "description": "Logout clears the session and redirects to login.", "tests": ["TC-11"]},
]


def write_markdown():
    plan_path = BASE_DIR / "test_plan.md"
    with plan_path.open("w", encoding="utf-8") as fh:
        fh.write("# Manual Test Plan\n\n")
        for heading, paragraphs in TEST_PLAN_SECTIONS:
            fh.write(f"## {heading}\n")
            for paragraph in paragraphs:
                fh.write(f"- {paragraph}\n")
            fh.write("\n")

    cases_path = BASE_DIR / "test_cases.md"
    headers = ["Test ID", "Title", "Preconditions", "Steps", "Expected Result", "Priority", "Type", "Status"]
    with cases_path.open("w", encoding="utf-8") as fh:
        fh.write("# Test Cases\n\n")
        fh.write("| " + " | ".join(headers) + " |\n")
        fh.write("|" + " --- |" * len(headers) + "\n")
        for case in TEST_CASES:
            row = [
                case["id"],
                case["title"],
                case["preconditions"],
                case["steps"],
                case["expected"],
                case["priority"],
                case["type"],
                case["status"],
            ]
            fh.write("| " + " | ".join(row) + " |\n")

    rtm_path = BASE_DIR / "requirement_traceability_matrix.md"
    with rtm_path.open("w", encoding="utf-8") as fh:
        fh.write("# Requirement Traceability Matrix\n\n")
        fh.write("| Requirement ID | Description | Covered Test Cases |\n")
        fh.write("| --- | --- | --- |\n")
        for requirement in REQUIREMENTS:
            fh.write(
                f"| {requirement['id']} | {requirement['description']} | {', '.join(requirement['tests'])} |\n"
            )


def paragraph_xml(text: str, bold: bool = False) -> str:
    text_xml = escape(text)
    bold_xml = "<w:rPr><w:b/></w:rPr>" if bold else ""
    return f"<w:p><w:r>{bold_xml}<w:t xml:space=\"preserve\">{text_xml}</w:t></w:r></w:p>"


def build_docx(paragraphs):
    body_content = "".join(paragraph_xml(text, bold) for text, bold in paragraphs)
    document_xml = f"""<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<w:document xmlns:wpc=\"http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas\" xmlns:mc=\"http://schemas.openxmlformats.org/markup-compatibility/2006\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" xmlns:m=\"http://schemas.openxmlformats.org/officeDocument/2006/math\" xmlns:v=\"urn:schemas-microsoft-com:vml\" xmlns:wp14=\"http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing\" xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" xmlns:w10=\"urn:schemas-microsoft-com:office:word\" xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" xmlns:w14=\"http://schemas.microsoft.com/office/word/2010/wordml\" xmlns:wpg=\"http://schemas.microsoft.com/office/word/2010/wordprocessingGroup\" xmlns:wpi=\"http://schemas.microsoft.com/office/word/2010/wordprocessingInk\" xmlns:wne=\"http://schemas.microsoft.com/office/word/2006/wordml\" xmlns:wps=\"http://schemas.microsoft.com/office/word/2010/wordprocessingShape\" mc:Ignorable=\"w14 wp14\">
  <w:body>
    {body_content}
    <w:sectPr>
      <w:pgSz w:w=\"11906\" w:h=\"16838\"/>
      <w:pgMar w:top=\"1440\" w:right=\"1440\" w:bottom=\"1440\" w:left=\"1440\" w:header=\"708\" w:footer=\"708\" w:gutter=\"0\"/>
      <w:cols w:space=\"708\"/>
      <w:docGrid w:linePitch=\"360\"/>
    </w:sectPr>
  </w:body>
</w:document>
"""

    styles_xml = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<w:styles xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" xmlns:mc=\"http://schemas.openxmlformats.org/markup-compatibility/2006\" mc:Ignorable=\"w14 w15 w16se w16cid\">
  <w:style w:type=\"paragraph\" w:default=\"1\" w:styleId=\"Normal\">
    <w:name w:val=\"Normal\"/>
    <w:qFormat/>
  </w:style>
</w:styles>
"""

    rels_xml = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">
  <Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" Target=\"word/document.xml\"/>
</Relationships>
"""

    doc_rels_xml = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">
  <Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles\" Target=\"styles.xml\"/>
</Relationships>
"""

    content_types_xml = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">
  <Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>
  <Default Extension=\"xml\" ContentType=\"application/xml\"/>
  <Override PartName=\"/word/document.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml\"/>
  <Override PartName=\"/word/styles.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml\"/>
</Types>
"""

    return {
        "[Content_Types].xml": content_types_xml,
        "_rels/.rels": rels_xml,
        "word/document.xml": document_xml,
        "word/styles.xml": styles_xml,
        "word/_rels/document.xml.rels": doc_rels_xml,
    }


def save_docx(path: Path):
    paragraphs = [("Manual Test Plan", True)]
    for heading, paras in TEST_PLAN_SECTIONS:
        paragraphs.append((heading, True))
        for paragraph in paras:
            paragraphs.append((f"- {paragraph}", False))
        paragraphs.append(("", False))

    doc_parts = build_docx(paragraphs)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, content in doc_parts.items():
            zf.writestr(name, content)


def column_letter(index: int) -> str:
    result = ""
    while index > 0:
        index, remainder = divmod(index - 1, 26)
        result = chr(65 + remainder) + result
    return result


def build_xlsx(rows, sheet_name: str = "Sheet1"):
    shared_strings = []
    shared_index = {}

    def get_index(value: str) -> int:
        if value not in shared_index:
            shared_index[value] = len(shared_strings)
            shared_strings.append(value)
        return shared_index[value]

    sheet_rows = []
    for row_idx, row in enumerate(rows, start=1):
        cells_xml = []
        for col_idx, cell in enumerate(row, start=1):
            ref = f"{column_letter(col_idx)}{row_idx}"
            idx = get_index(cell)
            cells_xml.append(f"<c r=\"{ref}\" t=\"s\"><v>{idx}</v></c>")
        sheet_rows.append(f"<row r=\"{row_idx}\">{''.join(cells_xml)}</row>")

    sheet_xml = f"""<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<worksheet xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\" xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\">
  <sheetData>
    {''.join(sheet_rows)}
  </sheetData>
</worksheet>
"""

    shared_xml = [
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>",
        f"<sst xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\" count=\"{len(shared_strings)}\" uniqueCount=\"{len(shared_strings)}\">",
    ]
    for s in shared_strings:
        shared_xml.append(f"  <si><t>{escape(s)}</t></si>")
    shared_xml.append("</sst>")
    shared_xml_str = "\n".join(shared_xml)

    styles_xml = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<styleSheet xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\">
  <fonts count=\"1\"><font><sz val=\"11\"/><color theme=\"1\"/><name val=\"Calibri\"/><family val=\"2\"/></font></fonts>
  <fills count=\"2\"><fill><patternFill patternType=\"none\"/></fill><fill><patternFill patternType=\"gray125\"/></fill></fills>
  <borders count=\"1\"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
  <cellStyleXfs count=\"1\"><xf numFmtId=\"0\" fontId=\"0\" fillId=\"0\" borderId=\"0\"/></cellStyleXfs>
  <cellXfs count=\"1\"><xf numFmtId=\"0\" fontId=\"0\" fillId=\"0\" borderId=\"0\" xfId=\"0\"/></cellXfs>
  <cellStyles count=\"1\"><cellStyle name=\"Normal\" xfId=\"0\" builtinId=\"0\"/></cellStyles>
</styleSheet>
"""

    workbook_xml = f"""<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<workbook xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\" xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\">
  <sheets>
    <sheet name=\"{escape(sheet_name)}\" sheetId=\"1\" r:id=\"rId1\"/>
  </sheets>
</workbook>
"""

    workbook_rels = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<Relationships xmlns=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\">
  <Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet\" Target=\"worksheets/sheet1.xml\"/>
  <Relationship Id=\"rId2\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles\" Target=\"styles.xml\"/>
  <Relationship Id=\"rId3\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings\" Target=\"sharedStrings.xml\"/>
</Relationships>
"""

    rels_xml = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">
  <Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" Target=\"xl/workbook.xml\"/>
</Relationships>
"""

    content_types_xml = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">
  <Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>
  <Default Extension=\"xml\" ContentType=\"application/xml\"/>
  <Override PartName=\"/xl/workbook.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml\"/>
  <Override PartName=\"/xl/worksheets/sheet1.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml\"/>
  <Override PartName=\"/xl/sharedStrings.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml\"/>
  <Override PartName=\"/xl/styles.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml\"/>
</Types>
"""

    return {
        "[Content_Types].xml": content_types_xml,
        "_rels/.rels": rels_xml,
        "xl/workbook.xml": workbook_xml,
        "xl/_rels/workbook.xml.rels": workbook_rels,
        "xl/worksheets/sheet1.xml": sheet_xml,
        "xl/sharedStrings.xml": shared_xml_str,
        "xl/styles.xml": styles_xml,
    }


def save_xlsx(path: Path, rows, sheet_name: str):
    parts = build_xlsx(rows, sheet_name)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, content in parts.items():
            zf.writestr(name, content)


def main():
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    write_markdown()

    docx_path = BASE_DIR / "test_plan.docx"
    save_docx(docx_path)

    headers = ["Test ID", "Title", "Preconditions", "Steps", "Expected Result", "Priority", "Type", "Status"]
    case_rows = [headers]
    for case in TEST_CASES:
        case_rows.append([
            case["id"],
            case["title"],
            case["preconditions"],
            case["steps"],
            case["expected"],
            case["priority"],
            case["type"],
            case["status"],
        ])
    save_xlsx(BASE_DIR / "test_cases.xlsx", case_rows, "Test Cases")

    rtm_rows = [["Requirement ID", "Description", "Covered Test Cases"]]
    for req in REQUIREMENTS:
        rtm_rows.append([req["id"], req["description"], ", ".join(req["tests"])])
    save_xlsx(BASE_DIR / "requirement_traceability_matrix.xlsx", rtm_rows, "RTM")


if __name__ == "__main__":
    main()
