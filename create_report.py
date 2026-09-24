from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

# ─── Color Constants ─────────────────────────────────────────────────────────
RED        = RGBColor(0xC6, 0x28, 0x28)   # #C62828 Crimson Red
DARK_RED   = RGBColor(0x7B, 0x00, 0x00)   # #7B0000 Deep Red
LIGHT_GRAY = RGBColor(0xF5, 0xF5, 0xF5)   # #F5F5F5
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
BLACK      = RGBColor(0x1E, 0x1E, 0x1E)
GRAY_TEXT  = RGBColor(0x55, 0x55, 0x55)
HEADER_RED = RGBColor(0xD3, 0x2F, 0x2F)   # Table header red

# ─── Helpers ─────────────────────────────────────────────────────────────────
def set_cell_bg(cell, hex_color: str):
    """Set background color of a table cell."""
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement("w:shd")
    shd.set(qn("w:val"),   "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"),  hex_color)
    tcPr.append(shd)

def set_cell_border(cell, top=None, bottom=None, left=None, right=None):
    """Add borders to a cell."""
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for side, val in [("top", top), ("bottom", bottom), ("left", left), ("right", right)]:
        if val:
            el = OxmlElement(f"w:{side}")
            el.set(qn("w:val"),   val.get("val", "single"))
            el.set(qn("w:sz"),    val.get("sz",  "6"))
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), val.get("color", "C62828"))
            tcBorders.append(el)
    tcPr.append(tcBorders)

def add_horizontal_rule(doc, color="C62828", size=12):
    """Draw a thin colored horizontal rule paragraph."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(6)
    pPr  = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bot  = OxmlElement("w:bottom")
    bot.set(qn("w:val"),   "single")
    bot.set(qn("w:sz"),    str(size))
    bot.set(qn("w:space"), "1")
    bot.set(qn("w:color"), color)
    pBdr.append(bot)
    pPr.append(pBdr)
    return p

def add_heading(doc, text, level=1):
    """Add a styled section heading."""
    p    = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after  = Pt(4)
    run  = p.add_run(text)
    run.font.name  = "Calibri"
    run.font.bold  = True
    if level == 1:
        run.font.size  = Pt(16)
        run.font.color.rgb = RED
    elif level == 2:
        run.font.size  = Pt(13)
        run.font.color.rgb = DARK_RED
    else:
        run.font.size  = Pt(11)
        run.font.color.rgb = DARK_RED
        run.font.italic = True
    add_horizontal_rule(doc, "C62828" if level == 1 else "DDDDDD", 8 if level == 1 else 4)
    return p

def add_body(doc, text, bold=False, italic=False, color=None, size=11, space_after=6):
    """Add a styled body paragraph."""
    p   = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after  = Pt(space_after)
    run = p.add_run(text)
    run.font.name   = "Calibri"
    run.font.size   = Pt(size)
    run.font.bold   = bold
    run.font.italic = italic
    run.font.color.rgb = color if color else BLACK
    return p

def add_bullet(doc, text, level=0, check=False, color=None):
    """Add a bullet point paragraph."""
    p   = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after  = Pt(3)
    if level:
        p.paragraph_format.left_indent = Inches(0.25 * level)
    prefix = "✅  " if check else ""
    run = p.add_run(prefix + text)
    run.font.name = "Calibri"
    run.font.size = Pt(11)
    run.font.color.rgb = color if color else BLACK
    return p

def add_table(doc, headers, rows, col_widths=None, header_bg="C62828"):
    """Add a professional styled table."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style      = "Table Grid"
    table.alignment  = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    hdr_row = table.rows[0]
    for i, hdr in enumerate(headers):
        cell = hdr_row.cells[i]
        set_cell_bg(cell, header_bg)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p   = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(hdr)
        run.font.name  = "Calibri"
        run.font.bold  = True
        run.font.size  = Pt(10)
        run.font.color.rgb = WHITE

    # Data rows
    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
        bg  = "FFFFFF" if r_idx % 2 == 0 else "FFF5F5"
        for c_idx, cell_text in enumerate(row_data):
            cell = row.cells[c_idx]
            set_cell_bg(cell, bg)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p   = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(str(cell_text))
            run.font.name = "Calibri"
            run.font.size = Pt(10)
            run.font.color.rgb = BLACK

    # Set column widths
    if col_widths:
        for i, width in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Inches(width)
    doc.add_paragraph()
    return table

def add_code_block(doc, code_text):
    """Add a shaded code block paragraph."""
    p   = doc.add_paragraph()
    p.paragraph_format.left_indent  = Inches(0.4)
    p.paragraph_format.right_indent = Inches(0.4)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(8)
    # Light gray shading
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"),   "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"),  "F3F3F3")
    pPr.append(shd)
    run = p.add_run(code_text)
    run.font.name       = "Courier New"
    run.font.size       = Pt(9)
    run.font.color.rgb  = RGBColor(0x37, 0x00, 0x00)
    return p

def add_toc_line(doc, number, title):
    p   = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after  = Pt(1)
    num_run = p.add_run(f"  {number}.  ")
    num_run.font.name  = "Calibri"
    num_run.font.size  = Pt(11)
    num_run.font.bold  = True
    num_run.font.color.rgb = RED
    txt_run = p.add_run(title)
    txt_run.font.name  = "Calibri"
    txt_run.font.size  = Pt(11)
    txt_run.font.color.rgb = BLACK

# ─── Build Document ──────────────────────────────────────────────────────────
def build_report():
    doc = Document()

    # Page margins
    for section in doc.sections:
        section.top_margin    = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin   = Cm(3.0)
        section.right_margin  = Cm(2.5)

    # ── COVER PAGE ────────────────────────────────────────────────────────────
    doc.add_paragraph()
    doc.add_paragraph()

    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_r = title_p.add_run("ShareLife")
    title_r.font.name  = "Calibri"
    title_r.font.size  = Pt(40)
    title_r.font.bold  = True
    title_r.font.color.rgb = RED

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_r = sub_p.add_run("A Blood Donor Management System")
    sub_r.font.name  = "Calibri"
    sub_r.font.size  = Pt(20)
    sub_r.font.bold  = True
    sub_r.font.color.rgb = BLACK

    add_horizontal_rule(doc, "C62828", 16)

    tag_p = doc.add_paragraph()
    tag_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    tag_r = tag_p.add_run("Project Report")
    tag_r.font.name  = "Calibri"
    tag_r.font.size  = Pt(16)
    tag_r.font.italic = True
    tag_r.font.color.rgb = GRAY_TEXT

    doc.add_paragraph()
    doc.add_paragraph()

    # Meta info table on cover
    meta = doc.add_table(rows=5, cols=2)
    meta.style     = "Table Grid"
    meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Submitted By",   "Satyam Sharma"),
        ("Project Title",  "ShareLife — Blood Donor Management System"),
        ("Technology",     "ASP.NET Web Forms, C#, SQL Server"),
        ("GitHub",         "github.com/golden67281/ShareLife.NET"),
        ("Academic Year",  "2025 – 2026"),
    ]
    for i, (label, value) in enumerate(meta_data):
        lc = meta.rows[i].cells[0]
        vc = meta.rows[i].cells[1]
        set_cell_bg(lc, "C62828")
        set_cell_bg(vc, "FFF5F5")
        lc.width = Inches(2.0)
        vc.width = Inches(4.5)
        lr = lc.paragraphs[0].add_run(label)
        lr.font.name = "Calibri"; lr.font.bold = True
        lr.font.size = Pt(11);    lr.font.color.rgb = WHITE
        vr = vc.paragraphs[0].add_run(value)
        vr.font.name = "Calibri"; vr.font.size = Pt(11)
        vr.font.color.rgb = BLACK

    doc.add_page_break()

    # ── TABLE OF CONTENTS ─────────────────────────────────────────────────────
    add_heading(doc, "Table of Contents", 1)
    toc_items = [
        ("1",  "Abstract"),
        ("2",  "Introduction"),
        ("3",  "Problem Statement"),
        ("4",  "Objectives"),
        ("5",  "Technology Stack"),
        ("6",  "System Architecture"),
        ("7",  "Database Design"),
        ("8",  "Module Descriptions"),
        ("9",  "Security Features"),
        ("10", "System Flow"),
        ("11", "Project File Structure"),
        ("12", "Testing & Validation"),
        ("13", "Advantages & Limitations"),
        ("14", "Future Scope"),
        ("15", "Conclusion"),
        ("16", "References"),
    ]
    for num, title in toc_items:
        add_toc_line(doc, num, title)

    doc.add_page_break()

    # ── 1. ABSTRACT ───────────────────────────────────────────────────────────
    add_heading(doc, "1.  Abstract", 1)
    add_body(doc,
        "Blood donation is a vital healthcare need across the world. In emergency medical situations, the "
        "inability to quickly locate a compatible blood donor can cost lives. ShareLife is a web-based Blood "
        "Donor Management System developed using ASP.NET Web Forms (C#) and SQL Server, designed to address "
        "the challenge of connecting blood donors with recipients efficiently.")
    add_body(doc,
        "The system provides a centralized digital platform where voluntary donors can register with their "
        "personal and medical details, and requesters can search for donors by blood group. It further includes "
        "a user authentication system (sign-up/login), a direct donor messaging module, and an editable donor "
        "profile system — all protected with industry-standard security practices such as parameterized SQL "
        "queries and SHA-256 password hashing.")
    add_body(doc,
        "This project demonstrates how a lightweight yet feature-rich web application can solve a real-world "
        "medical infrastructure challenge using modern Microsoft .NET technologies.", space_after=12)

    # ── 2. INTRODUCTION ───────────────────────────────────────────────────────
    add_heading(doc, "2.  Introduction", 1)
    add_body(doc,
        "According to the World Health Organization (WHO), approximately 118.5 million blood donations are "
        "collected globally each year, yet there are persistent shortages in developing regions. A key cause "
        "of this shortage is not just lack of donors, but the inability to locate willing donors quickly during "
        "emergencies.")
    add_body(doc,
        "Traditional methods of blood donor management — phone directories, hospital notice boards, or paper "
        "registers — are slow, error-prone, and geographically limited. A digital, web-based system offers the "
        "following advantages:")
    for item in [
        "24/7 availability of donor records",
        "Instant search by blood group",
        "Direct contact with donors via messaging",
        "Secure and centralized data management",
    ]:
        add_bullet(doc, item)
    add_body(doc,
        "ShareLife was developed as a response to this need. Built on the ASP.NET Web Forms platform with a "
        "SQL Server backend, it provides a fully functional, responsive web application that streamlines blood "
        "donor management.", space_after=12)

    # ── 3. PROBLEM STATEMENT ──────────────────────────────────────────────────
    add_heading(doc, "3.  Problem Statement", 1)
    add_body(doc, "The current blood donor search process faces several key challenges:")
    add_table(doc,
        ["#", "Problem", "Impact"],
        [
            ["1", "Donor info stored in physical registers or spreadsheets", "Not easily searchable or scalable"],
            ["2", "No centralized platform connecting donors with patients",  "Delays during emergencies"],
            ["3", "Manual search for a blood group takes significant time",   "Wastes critical time"],
            ["4", "Donors cannot be contacted directly or quickly",           "Reduces donation rate"],
            ["5", "No mechanism for donors to update their own records",      "Outdated data, failed contacts"],
        ],
        col_widths=[0.4, 3.5, 2.5])

    # ── 4. OBJECTIVES ─────────────────────────────────────────────────────────
    add_heading(doc, "4.  Objectives", 1)
    add_body(doc, "The primary objectives of this project are:")
    objectives = [
        "Donor Registration — Allow voluntary donors to register with personal and medical information.",
        "Donor Search — Enable any user to search for available donors by blood group instantly.",
        "View Donor Directory — Display the complete list of all registered donors.",
        "User Authentication — Provide secure Sign Up and Login functionality for requesters.",
        "Donor Messaging — Allow logged-in users to send direct messages to donors.",
        "Donor Inbox — Allow donors to view messages they have received.",
        "Donor Profile Editing — Allow updates to donor records.",
        "Awareness — Provide educational content on blood donation eligibility and WHO statistics.",
        "Security — Ensure all data operations are protected against SQL Injection and XSS.",
    ]
    for obj in objectives:
        add_bullet(doc, obj, check=True)

    # ── 5. TECHNOLOGY STACK ───────────────────────────────────────────────────
    add_heading(doc, "5.  Technology Stack", 1)
    add_table(doc,
        ["Layer", "Technology", "Version / Details"],
        [
            ["Framework",     "ASP.NET Web Forms",    ".NET Framework 4.8"],
            ["Language",      "C#",                   "C# 7.3+"],
            ["Database",      "Microsoft SQL Server",  "MSSQLLocalDB via ADO.NET"],
            ["Data Access",   "ADO.NET",              "System.Data.SqlClient"],
            ["Frontend",      "HTML5 + Pure CSS3",    "Responsive, mobile-friendly"],
            ["IDE",           "Visual Studio",         "2022 Community Edition"],
            ["Web Server",    "IIS Express",           "Built-in development server"],
            ["Version Ctrl.", "Git + GitHub",          "github.com/golden67281/ShareLife.NET"],
        ],
        col_widths=[1.5, 2.2, 2.7])

    add_heading(doc, "5.1  Why ASP.NET Web Forms?", 2)
    for reason in [
        "Mature, server-side platform ideal for CRUD-heavy data applications.",
        "Built-in validation controls and state management (ViewState, Session).",
        "Seamless integration with SQL Server via ADO.NET.",
        "Code-behind pattern for clean separation of HTML (.aspx) and business logic (.aspx.cs).",
    ]:
        add_bullet(doc, reason)

    # ── 6. SYSTEM ARCHITECTURE ────────────────────────────────────────────────
    add_heading(doc, "6.  System Architecture", 1)
    add_body(doc, "ShareLife follows a 3-Tier Architecture:")
    add_code_block(doc,
        "┌─────────────────────────────────────────────────────┐\n"
        "│              PRESENTATION TIER                      │\n"
        "│  HTML5 + CSS3 Pages (.aspx) + Site.Master          │\n"
        "│  Responsive UI, ECG animations, card grids         │\n"
        "└────────────────────┬────────────────────────────────┘\n"
        "                     │  HTTP Request / Response\n"
        "┌────────────────────▼────────────────────────────────┐\n"
        "│              BUSINESS LOGIC TIER                    │\n"
        "│  C# Code-Behind files (.aspx.cs)                   │\n"
        "│  - Input validation (server + client)               │\n"
        "│  - Session management (UserID, FullName, Email)     │\n"
        "│  - SHA-256 password hashing                         │\n"
        "└────────────────────┬────────────────────────────────┘\n"
        "                     │  ADO.NET (SqlConnection, SqlCommand)\n"
        "┌────────────────────▼────────────────────────────────┐\n"
        "│                 DATA TIER                            │\n"
        "│  SQL Server / MSSQLLocalDB                          │\n"
        "│  Database: BloodDonorDB                             │\n"
        "│  Tables: Donor | Users | Messages                   │\n"
        "└──────────────────────────────────────────────────────┘")

    add_heading(doc, "6.1  Master Page Layout (Site.Master)", 2)
    for pt in [
        "Top navigation bar with dynamic login/logout links.",
        "Session-aware greeting (shows logged-in username).",
        "Shared CSS stylesheet (Style.css) for consistent design.",
        "Footer with project branding.",
    ]:
        add_bullet(doc, pt)

    # ── 7. DATABASE DESIGN ────────────────────────────────────────────────────
    add_heading(doc, "7.  Database Design", 1)
    add_body(doc, "Database Name: BloodDonorDB", bold=True, color=RED)
    add_body(doc, "The database consists of 3 tables with the following schema:")

    add_heading(doc, "7.1  Table: Donor", 2)
    add_body(doc, "Stores all registered blood donor records.")
    add_table(doc,
        ["Column", "Data Type", "Constraints", "Description"],
        [
            ["DonorID",          "INT",           "IDENTITY PK",   "Auto-generated unique donor ID"],
            ["Name",             "VARCHAR(50)",   "NOT NULL",       "Full name of the donor"],
            ["Gender",           "VARCHAR(20)",   "NULL",           "Male / Female / Other"],
            ["Age",              "INT",           "NOT NULL",       "Age of the donor"],
            ["Email",            "VARCHAR(100)",  "NULL",           "Email address"],
            ["Mobile",           "VARCHAR(15)",   "NOT NULL",       "Mobile contact number"],
            ["City",             "VARCHAR(50)",   "NOT NULL",       "City of residence"],
            ["BloodGroup",       "VARCHAR(5)",    "NOT NULL",       "A+, A-, B+, B-, O+, O-, AB+, AB-"],
            ["Weight",           "INT",           "NULL",           "Donor weight in kg"],
            ["LastDonationDate", "VARCHAR(20)",   "NULL",           "Date of last donation or Never"],
            ["MedicalConditions","VARCHAR(255)",  "NULL",           "Any medical conditions"],
        ],
        col_widths=[1.5, 1.3, 1.2, 2.4])

    add_heading(doc, "7.2  Table: Users", 2)
    add_body(doc, "Stores registered user accounts for authentication.")
    add_table(doc,
        ["Column", "Data Type", "Constraints", "Description"],
        [
            ["UserID",       "INT",          "IDENTITY PK",    "Auto-generated user ID"],
            ["FullName",     "VARCHAR(100)", "NOT NULL",        "User's full name"],
            ["Email",        "VARCHAR(100)", "NOT NULL UNIQUE", "Login email (unique)"],
            ["PasswordHash", "VARCHAR(256)", "NOT NULL",        "SHA-256 hashed password"],
            ["CreatedAt",    "DATETIME",     "DEFAULT GETDATE()","Account creation timestamp"],
        ],
        col_widths=[1.5, 1.3, 1.5, 2.1])

    add_heading(doc, "7.3  Table: Messages", 2)
    add_body(doc, "Stores messages sent from users to donors.")
    add_table(doc,
        ["Column", "Data Type", "Constraints", "Description"],
        [
            ["MessageID",    "INT",           "IDENTITY PK",           "Auto-generated message ID"],
            ["SenderUserID", "INT",           "NOT NULL FK → Users",   "ID of the sender user"],
            ["DonorID",      "INT",           "NOT NULL FK → Donor",   "ID of the recipient donor"],
            ["Subject",      "VARCHAR(200)",  "NOT NULL",               "Message subject"],
            ["Body",         "NVARCHAR(MAX)", "NOT NULL",               "Full message body"],
            ["SentAt",       "DATETIME",      "DEFAULT GETDATE()",      "Timestamp of message"],
        ],
        col_widths=[1.5, 1.4, 1.8, 1.7])

    add_heading(doc, "7.4  Entity Relationship Diagram (ERD)", 2)
    add_code_block(doc,
        "┌──────────────┐         ┌──────────────────┐         ┌─────────────┐\n"
        "│    Users     │         │     Messages      │         │    Donor    │\n"
        "├──────────────┤         ├──────────────────┤         ├─────────────┤\n"
        "│ UserID (PK)  │──1──┐   │ MessageID (PK)   │   ┌──1──│ DonorID(PK) │\n"
        "│ FullName     │     └──N│ SenderUserID (FK)│   │     │ Name        │\n"
        "│ Email        │         │ DonorID (FK)     │N──┘     │ BloodGroup  │\n"
        "│ PasswordHash │         │ Subject          │         │ Age / Gender│\n"
        "│ CreatedAt    │         │ Body / SentAt    │         │ City/Mobile │\n"
        "└──────────────┘         └──────────────────┘         └─────────────┘")

    # ── 8. MODULE DESCRIPTIONS ────────────────────────────────────────────────
    add_heading(doc, "8.  Module Descriptions", 1)

    modules = [
        ("8.1", "Home Page (Default.aspx)",
         "The landing page featuring a hero section with an animated ECG pulse SVG line, brand headline, "
         "and 'Be a Hero, Donate Blood' call-to-action. Below the hero, a 5-card features grid links "
         "directly to: Register Donor, Search Donor, View All Donors, Save Lives, and About Us pages."),
        ("8.2", "Donor Registration (Register.aspx)",
         "Allows new donors to register with personal details (Name, Gender, Age, Email, Mobile, City) "
         "and medical details (Blood Group, Weight, Last Donation Date, Medical Conditions). "
         "Includes client-side and server-side validation. All DB writes use parameterized SQL INSERT queries. "
         "On success, a confirmation message is shown and the form is automatically cleared."),
        ("8.3", "Donor Search (Search.aspx)",
         "Enables users to filter donors by blood group. Results are displayed in an ASP.NET GridView "
         "showing Name, Age, City, Blood Group, Mobile, and Last Donation Date. Result count is dynamically "
         "displayed. Contact buttons link to ContactDonor.aspx?id={DonorID}."),
        ("8.4", "View All Donors (ViewDonors.aspx)",
         "Displays the complete, unfiltered directory of all registered donors in a sortable GridView table "
         "with all columns including weight, email, and medical conditions."),
        ("8.5", "User Sign Up (SignUp.aspx)",
         "Allows new requesters to create an account. Validates email uniqueness, password minimum length "
         "(8 chars), and password confirmation matching. Password is stored as a SHA-256 hash — never plain text."),
        ("8.6", "User Login (Login.aspx)",
         "Authenticates registered users by hashing the entered password with SHA-256 and comparing it to the "
         "stored hash in the Users table. On success, stores UserID, FullName, and Email in ASP.NET session. "
         "Auto-redirects to home if the user is already logged in."),
        ("8.7", "Contact Donor (ContactDonor.aspx)",
         "Allows authenticated users to send a direct message to a specific donor. Shows the donor's profile "
         "card (Name, Age, Blood Group, City), message history, and a compose form. Login is required — "
         "non-authenticated users see a login prompt panel. On send, an INSERT is performed into the Messages table."),
        ("8.8", "Donor Messages / Inbox (DonorMessages.aspx)",
         "Displays all messages received by a specific donor, including sender name, subject, body, and timestamp."),
        ("8.9", "Edit Donor (EditDonor.aspx)",
         "Allows editing of an existing donor's details. Pre-loads all fields from the Donor table, "
         "validates changes, and performs a parameterized UPDATE query on save."),
        ("8.10", "About Page (About.aspx)",
         "Educational resource page covering: blood donation eligibility (age 18–65, weight ≥ 50 kg), "
         "blood type compatibility chart, health benefits of donation, and WHO statistics."),
    ]

    for num, title, desc in modules:
        add_heading(doc, f"{num}  {title}", 2)
        add_body(doc, desc)

    # Code samples
    add_heading(doc, "8.2  Sample Code — Parameterized INSERT (Register.aspx.cs)", 3)
    add_code_block(doc,
        'string query = @"INSERT INTO Donor\n'
        '    (Name, Gender, Age, Email, Mobile, City,\n'
        '     BloodGroup, Weight, LastDonationDate, MedicalConditions)\n'
        '    VALUES (@Name, @Gender, @Age, @Email, @Mobile, @City,\n'
        '            @BloodGroup, @Weight, @LastDonationDate, @MedicalConditions)";\n\n'
        'cmd.Parameters.AddWithValue("@Name",  name);\n'
        'cmd.Parameters.AddWithValue("@Age",   age);\n'
        '// ... all fields parameterized\n'
        'conn.Open();\n'
        'int rowsAffected = cmd.ExecuteNonQuery();')

    add_heading(doc, "8.6  Sample Code — SHA-256 Password Hashing (Login.aspx.cs)", 3)
    add_code_block(doc,
        'public static string HashPassword(string password)\n'
        '{\n'
        '    using (SHA256 sha256 = SHA256.Create())\n'
        '    {\n'
        '        byte[] bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));\n'
        '        StringBuilder sb = new StringBuilder();\n'
        '        foreach (byte b in bytes)\n'
        '            sb.Append(b.ToString("x2"));\n'
        '        return sb.ToString();\n'
        '    }\n'
        '}')

    # ── 9. SECURITY FEATURES ──────────────────────────────────────────────────
    add_heading(doc, "9.  Security Features", 1)
    add_table(doc,
        ["Security Measure", "Implementation", "Location"],
        [
            ["SQL Injection Prevention", "SqlCommand.Parameters.AddWithValue() — zero string concatenation", "All .aspx.cs files"],
            ["XSS Protection",           "Input encoded before rendering; Server.HtmlEncode()",             "Form output pages"],
            ["Password Hashing",         "SHA-256 via System.Security.Cryptography.SHA256",                 "Login.cs, SignUp.cs"],
            ["Session Management",       "UserID, FullName, Email stored in server-side ASP.NET sessions",  "Login.cs, Site.Master.cs"],
            ["Auth Guards",              "Protected pages check Session[\"UserID\"] != null",               "ContactDonor.cs"],
            ["Input Validation",         "RequiredFieldValidator, RangeValidator, RegularExpressionValidator", "All form pages"],
        ],
        col_widths=[2.0, 3.0, 1.5])

    # ── 10. SYSTEM FLOW ───────────────────────────────────────────────────────
    add_heading(doc, "10.  System Flow", 1)

    flows = [
        ("10.1  Donor Registration Flow",
         "Visit Register.aspx  →  Fill form (Name, Blood Group, Age, City, Mobile)  →\n"
         "Client-side validation passes  →  Server-side Page.IsValid check  →\n"
         "INSERT INTO Donor table (parameterized)  →  Success message shown  →  Form cleared"),
        ("10.2  Login Flow",
         "Visit Login.aspx  →  Enter Email + Password  →\n"
         "Server hashes password with SHA-256  →\n"
         "SELECT from Users WHERE Email = @Email AND PasswordHash = @Hash  →\n"
         "Match found  →  Store Session[UserID, FullName]  →  Redirect to Home"),
        ("10.3  Donor Search Flow",
         "Visit Search.aspx  →  Select blood group from dropdown  →  Click Search  →\n"
         "SELECT from Donor WHERE BloodGroup = @BloodGroup  →\n"
         "Display results in GridView  →  Click Contact  →  ContactDonor.aspx?id={DonorID}"),
        ("10.4  Messaging Flow",
         "Visit ContactDonor.aspx?id={DonorID}  →\n"
         "Check Session[UserID] — redirect if not logged in  →\n"
         "Load donor profile card from Donor table  →\n"
         "Load previous message history from Messages table  →\n"
         "Fill Subject + Body  →  Click Send  →\n"
         "INSERT INTO Messages (SenderUserID, DonorID, Subject, Body)  →  Confirmation shown"),
    ]
    for title, flow in flows:
        add_heading(doc, title, 2)
        add_code_block(doc, flow)

    # ── 11. FILE STRUCTURE ────────────────────────────────────────────────────
    add_heading(doc, "11.  Project File Structure", 1)
    add_code_block(doc,
        "ShareLife.net/\n"
        "│\n"
        "├── Site.Master / .cs          ← Master page (navigation, layout shell)\n"
        "├── Style.css                  ← Complete CSS design system (~700 lines)\n"
        "├── Web.config                 ← Connection string & app settings\n"
        "├── ShareLife.csproj           ← MSBuild project file (.NET 4.8)\n"
        "├── ShareLife.sln              ← Visual Studio solution file\n"
        "│\n"
        "├── Default.aspx / .cs         ← Home page (hero + features grid)\n"
        "├── Register.aspx / .cs        ← Donor registration form\n"
        "├── Search.aspx / .cs          ← Blood group donor search\n"
        "├── ViewDonors.aspx / .cs      ← All donors directory\n"
        "├── EditDonor.aspx / .cs       ← Edit donor record\n"
        "├── ContactDonor.aspx / .cs    ← Send message to donor\n"
        "├── DonorMessages.aspx / .cs   ← Donor message inbox\n"
        "├── Login.aspx / .cs           ← User login\n"
        "├── SignUp.aspx / .cs          ← User registration\n"
        "├── About.aspx / .cs           ← Awareness & education page\n"
        "│\n"
        "├── setup_database.sql         ← Full DB creation script (BloodDonorDB)\n"
        "├── create_presentation.py     ← Python PPT generator script\n"
        "├── ShareLife_Presentation.pptx← Project PowerPoint (10 slides)\n"
        "├── presentation.html          ← Interactive web slide deck\n"
        "└── blood_donation_hero.jpg    ← Hero section image")

    # ── 12. TESTING ───────────────────────────────────────────────────────────
    add_heading(doc, "12.  Testing & Validation", 1)
    add_heading(doc, "12.1  Form Validation Tests", 2)
    add_table(doc,
        ["Test Case", "Input", "Expected Output", "Result"],
        [
            ["Register — empty name",        "(blank)",      "Name is required error",             "✅ Pass"],
            ["Register — age < 18",          "Age = 15",     "Age must be 18–65 error",            "✅ Pass"],
            ["Register — invalid mobile",    'abc123',       "Regex validation error",             "✅ Pass"],
            ["Search — no blood group",      "(none)",       "Please select a blood group",        "✅ Pass"],
            ["Login — wrong password",       "Wrong pass",   "Invalid email or password",          "✅ Pass"],
            ["Login — correct credentials",  "Valid",        "Redirect to Home, session set",      "✅ Pass"],
            ["Contact donor — not logged in","No session",   "Login prompt panel shown",           "✅ Pass"],
            ["Send message — valid",         "Logged in",    "Message inserted, success shown",    "✅ Pass"],
        ],
        col_widths=[2.0, 1.4, 2.0, 1.0])

    add_heading(doc, "12.2  Security Tests", 2)
    add_table(doc,
        ["Test", "Method", "Result"],
        [
            ["SQL Injection in search", "' OR '1'='1 as blood group",  "✅ Blocked by parameterized query"],
            ["SQL Injection in login",  "admin'-- as email",           "✅ Blocked by parameterized query"],
            ["Plain-text password",     "Checked Users table in DB",   "✅ SHA-256 hash stored, not plain"],
            ["Unauthorized contact",    "Visit ContactDonor w/o login","✅ Login required panel shown"],
        ],
        col_widths=[1.8, 2.5, 2.1])

    add_heading(doc, "12.3  Browser Compatibility", 2)
    add_table(doc,
        ["Browser", "Tested", "Status"],
        [
            ["Google Chrome",   "✅", "Fully functional"],
            ["Microsoft Edge",  "✅", "Fully functional"],
            ["Mozilla Firefox", "✅", "Fully functional"],
        ],
        col_widths=[2.5, 1.0, 2.5])

    # ── 13. ADVANTAGES & LIMITATIONS ─────────────────────────────────────────
    add_heading(doc, "13.  Advantages & Limitations", 1)
    add_heading(doc, "13.1  Advantages", 2)
    for adv in [
        "Centralized Platform — All donor data stored in one database, accessible from any network node.",
        "Fast Search — Blood group filtering retrieves donors instantly from SQL Server.",
        "Secure — Parameterized queries, SHA-256 hashing, and session guards protect all data.",
        "User-Friendly — Modern UI with animations makes navigation intuitive for all user types.",
        "Direct Messaging — Eliminates intermediaries; requesters contact donors directly.",
        "Extensible — Modular page-based architecture makes it easy to add new features.",
        "Educational — About page spreads awareness on eligibility, compatibility, and donation.",
    ]:
        add_bullet(doc, adv, check=True)

    add_heading(doc, "13.2  Limitations", 2)
    for lim in [
        "No Email Notifications — Messages stored in DB but donors don't receive email alerts.",
        "No Real-Time Updates — Page must be manually refreshed; no WebSocket / SignalR messaging.",
        "LocalDB Dependency — Requires MSSQLLocalDB for development; not cloud-deployed.",
        "No Role-Based Access Control — Any user can view all donor records; no admin-only sections.",
        "No Donor Self-Login — Donors cannot log in as themselves; only requesters have accounts.",
    ]:
        add_bullet(doc, lim)

    # ── 14. FUTURE SCOPE ──────────────────────────────────────────────────────
    add_heading(doc, "14.  Future Scope", 1)
    add_table(doc,
        ["Enhancement", "Description"],
        [
            ["Email/SMS Notifications", "Notify donors via email or SMS when they receive a new message"],
            ["Location-Based Search",   "Filter donors by proximity using GPS/maps integration"],
            ["Mobile App",              "Companion Android/iOS app using Xamarin or .NET MAUI"],
            ["Donor Health Tracking",   "Allow donors to log donation history and health checkup records"],
            ["Donor Accounts",          "Allow donors to log in and manage their own profiles and inboxes"],
            ["Admin Dashboard",         "Admin panel for statistics, donor management, and moderation"],
            ["Cloud Deployment",        "Host on Azure App Service with Azure SQL Database"],
            ["Real-Time Alerts",        "Use SignalR for live message notifications"],
        ],
        col_widths=[2.5, 4.0])

    # ── 15. CONCLUSION ────────────────────────────────────────────────────────
    add_heading(doc, "15.  Conclusion", 1)
    add_body(doc,
        "ShareLife – A Blood Donor Management System is a fully functional, secure web application built on "
        "ASP.NET Web Forms (.NET Framework 4.8) with a SQL Server backend. The system successfully achieves "
        "its primary goal of connecting voluntary blood donors with people in urgent medical need through a "
        "centralized, efficient digital platform.")
    add_body(doc, "Key accomplishments of this project:")
    for acc in [
        "Built a complete CRUD application (Create, Read, Update, Delete) for donor records.",
        "Implemented user authentication with SHA-256 password security.",
        "Created a donor-requester messaging system with full message history.",
        "Applied industry best practices: parameterized SQL, input validation, session management.",
        "Designed a modern, responsive UI with crimson red medical theme.",
        "Developed and published a professional 10-slide project presentation deck.",
    ]:
        add_bullet(doc, acc, check=True)
    add_body(doc,
        "This project not only fulfills its academic objectives but also addresses a genuine social and medical "
        "need, making it a meaningful contribution to healthcare technology solutions.", space_after=12)

    # ── 16. REFERENCES ────────────────────────────────────────────────────────
    add_heading(doc, "16.  References", 1)
    refs = [
        "[1]  Microsoft Documentation — ASP.NET Web Forms Overview\n"
        "      https://docs.microsoft.com/en-us/aspnet/web-forms/",
        "[2]  Microsoft Documentation — ADO.NET with SQL Server\n"
        "      https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/",
        "[3]  World Health Organization (WHO) — Blood Safety and Availability\n"
        "      https://www.who.int/news-room/fact-sheets/detail/blood-safety-and-availability",
        "[4]  Microsoft SQL Server — T-SQL Reference\n"
        "      https://docs.microsoft.com/en-us/sql/t-sql/",
        "[5]  OWASP — SQL Injection Prevention Cheat Sheet\n"
        "      https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html",
        "[6]  NIST — Cryptographic Hash Standard (SHA-256)\n"
        "      https://csrc.nist.gov/publications/detail/fips/180/4/final",
    ]
    for ref in refs:
        add_body(doc, ref, color=GRAY_TEXT, size=10, space_after=8)

    add_horizontal_rule(doc, "C62828", 12)

    # Footer credit
    footer_p = doc.add_paragraph()
    footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = footer_p.add_run("© 2025–2026  Satyam Sharma  |  ShareLife – Blood Donor Management System")
    fr.font.name = "Calibri"
    fr.font.size = Pt(10)
    fr.font.italic = True
    fr.font.color.rgb = GRAY_TEXT

    out = r"d:\ShareLife.net\ShareLife_Project_Report.docx"
    doc.save(out)
    print(f"[OK] Report saved successfully:\n    {out}")

if __name__ == "__main__":
    build_report()
