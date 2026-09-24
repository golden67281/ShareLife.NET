# ShareLife – A Blood Donor Management System
### Project Report

---

> **Submitted by:** Satyam Sharma
> **Project Title:** ShareLife — A Blood Donor Management System
> **Technology:** ASP.NET Web Forms (C#), SQL Server, HTML, CSS
> **GitHub Repository:** [https://github.com/golden67281/ShareLife.NET](https://github.com/golden67281/ShareLife.NET)
> **Academic Year:** 2025–2026

---

## Table of Contents

1. [Abstract](#1-abstract)
2. [Introduction](#2-introduction)
3. [Problem Statement](#3-problem-statement)
4. [Objectives](#4-objectives)
5. [Technology Stack](#5-technology-stack)
6. [System Architecture](#6-system-architecture)
7. [Database Design](#7-database-design)
8. [Module Descriptions](#8-module-descriptions)
9. [Security Features](#9-security-features)
10. [System Flow](#10-system-flow)
11. [Project File Structure](#11-project-file-structure)
12. [Testing & Validation](#12-testing--validation)
13. [Advantages & Limitations](#13-advantages--limitations)
14. [Future Scope](#14-future-scope)
15. [Conclusion](#15-conclusion)
16. [References](#16-references)

---

## 1. Abstract

Blood donation is a vital healthcare need across the world. In emergency medical situations, the inability to quickly locate a compatible blood donor can cost lives. **ShareLife** is a web-based Blood Donor Management System developed using **ASP.NET Web Forms (C#)** and **SQL Server**, designed to address the challenge of connecting blood donors with recipients efficiently.

The system provides a centralized digital platform where voluntary donors can register with their personal and medical details, and requesters can search for donors by blood group. It further includes a user authentication system (sign-up/login), a direct donor messaging module, and an editable donor profile system — all protected with industry-standard security practices such as parameterized SQL queries and SHA-256 password hashing.

This project demonstrates how a lightweight yet feature-rich web application can solve a real-world medical infrastructure challenge using modern Microsoft .NET technologies.

---

## 2. Introduction

According to the **World Health Organization (WHO)**, approximately **118.5 million blood donations** are collected globally each year, yet there are persistent shortages in developing regions. A key cause of this shortage is not just lack of donors, but the **inability to locate willing donors quickly** during emergencies.

Traditional methods of blood donor management — phone directories, hospital notice boards, or paper registers — are slow, error-prone, and geographically limited. A digital, web-based system offers the following advantages:

- **24/7 availability** of donor records
- **Instant search** by blood group
- **Direct contact** with donors via messaging
- **Secure and centralized** data management

**ShareLife** was developed as a response to this need. Built on the **ASP.NET Web Forms** platform with a **SQL Server** backend, it provides a fully functional, responsive web application that streamlines blood donor management.

---

## 3. Problem Statement

The current blood donor search process faces several key challenges:

| # | Problem | Impact |
|---|---------|--------|
| 1 | Blood donor information is stored in physical registers or spreadsheets | Data is not easily searchable or scalable |
| 2 | There is no centralized platform connecting donors with patients | Delays in finding matched donors during emergencies |
| 3 | Manual search for a specific blood group takes significant time | Wastes critical time in life-or-death situations |
| 4 | Donors cannot be contacted directly or quickly | Communication bottlenecks reduce donation rate |
| 5 | No mechanism for donors to update or manage their own records | Outdated data leads to failed contact attempts |

**ShareLife** was designed specifically to solve all of the above problems through a structured, user-friendly web application.

---

## 4. Objectives

The primary objectives of this project are:

- ✅ **Donor Registration** — Allow voluntary donors to register with personal information (name, age, gender, city) and medical information (blood group, weight, medical conditions, last donation date).
- ✅ **Donor Search** — Enable any user to search for available donors by blood group instantly.
- ✅ **View Donor Directory** — Display the complete list of all registered donors.
- ✅ **User Authentication** — Provide secure Sign Up and Login functionality for requesters.
- ✅ **Donor Messaging** — Allow logged-in users to send direct messages to donors with hospital details and urgency level.
- ✅ **Donor Inbox** — Allow donors to view messages they have received.
- ✅ **Donor Profile Editing** — Allow updates to donor records (admin or self-managed).
- ✅ **Awareness** — Provide educational content on blood donation eligibility, compatibility, and WHO statistics.
- ✅ **Security** — Ensure all data operations are protected against SQL Injection and XSS attacks.

---

## 5. Technology Stack

| Layer | Technology | Version / Details |
|-------|-----------|-------------------|
| **Framework** | ASP.NET Web Forms | .NET Framework 4.8 |
| **Language** | C# | C# 7.3+ |
| **Database** | Microsoft SQL Server | MSSQLLocalDB (via ADO.NET) |
| **Data Access** | ADO.NET | `System.Data.SqlClient` |
| **Frontend** | HTML5 + Pure CSS3 | Responsive, mobile-friendly |
| **IDE** | Visual Studio | 2022 Community Edition |
| **Web Server** | IIS Express | Built-in development server |
| **Version Control** | Git + GitHub | [github.com/golden67281/ShareLife.NET](https://github.com/golden67281/ShareLife.NET) |

### Why ASP.NET Web Forms?

ASP.NET Web Forms was chosen because:
- It is a mature, server-side platform ideal for **CRUD-heavy data applications**
- It provides built-in **validation controls** and **state management** (ViewState, Session)
- It integrates seamlessly with **SQL Server via ADO.NET**
- It uses the **code-behind pattern** for clean separation of HTML (`.aspx`) and business logic (`.aspx.cs`)

---

## 6. System Architecture

ShareLife follows a **3-Tier Architecture**:

```
┌─────────────────────────────────────────────────────────────┐
│                   PRESENTATION TIER                         │
│   HTML5 + CSS3 Pages (.aspx) + Site.Master (Master Page)   │
│   Mobile-responsive UI, ECG animated hero, card grids      │
└─────────────────────────┬───────────────────────────────────┘
                          │  HTTP Request / Response
┌─────────────────────────▼───────────────────────────────────┐
│                   BUSINESS LOGIC TIER                       │
│   C# Code-Behind files (.aspx.cs)                          │
│   - User input validation (server-side + client-side)       │
│   - Session management (UserID, FullName, Email)            │
│   - SHA-256 password hashing                                │
│   - Business rules (eligibility, authorization checks)      │
└─────────────────────────┬───────────────────────────────────┘
                          │  ADO.NET (SqlConnection, SqlCommand)
┌─────────────────────────▼───────────────────────────────────┐
│                     DATA TIER                               │
│   SQL Server / MSSQLLocalDB                                 │
│   Database: BloodDonorDB                                    │
│   Tables: Donor | Users | Messages                          │
└─────────────────────────────────────────────────────────────┘
```

### Master Page Layout (`Site.Master`)

The application uses a **Master Page** to ensure a consistent layout across all pages:
- Top navigation bar with dynamic login/logout links
- Session-aware greeting (shows logged-in username)
- Shared CSS stylesheet (`Style.css`)
- Footer with project branding

---

## 7. Database Design

**Database Name:** `BloodDonorDB`

The database consists of **3 tables** with the following schema:

### 7.1 — Table: `Donor`

Stores all registered blood donor records.

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| `DonorID` | `INT` | `IDENTITY(1,1) PRIMARY KEY` | Auto-generated unique donor ID |
| `Name` | `VARCHAR(50)` | `NOT NULL` | Full name of the donor |
| `Gender` | `VARCHAR(20)` | `NULL` | Gender (Male / Female / Other) |
| `Age` | `INT` | `NOT NULL` | Age of the donor |
| `Email` | `VARCHAR(100)` | `NULL` | Email address |
| `Mobile` | `VARCHAR(15)` | `NOT NULL` | Mobile contact number |
| `City` | `VARCHAR(50)` | `NOT NULL` | City of residence |
| `BloodGroup` | `VARCHAR(5)` | `NOT NULL` | Blood group (A+, A-, B+, B-, O+, O-, AB+, AB-) |
| `Weight` | `INT` | `NULL` | Donor weight in kg |
| `LastDonationDate` | `VARCHAR(20)` | `NULL` | Date of last donation or "Never" |
| `MedicalConditions` | `VARCHAR(255)` | `NULL` | Any medical conditions |

### 7.2 — Table: `Users`

Stores registered user accounts for authentication.

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| `UserID` | `INT` | `IDENTITY(1,1) PRIMARY KEY` | Auto-generated user ID |
| `FullName` | `VARCHAR(100)` | `NOT NULL` | User's full name |
| `Email` | `VARCHAR(100)` | `NOT NULL UNIQUE` | Login email (unique) |
| `PasswordHash` | `VARCHAR(256)` | `NOT NULL` | SHA-256 hashed password |
| `CreatedAt` | `DATETIME` | `DEFAULT GETDATE()` | Account creation timestamp |

### 7.3 — Table: `Messages`

Stores messages sent from users to donors.

| Column | Data Type | Constraints | Description |
|--------|-----------|-------------|-------------|
| `MessageID` | `INT` | `IDENTITY(1,1) PRIMARY KEY` | Auto-generated message ID |
| `SenderUserID` | `INT` | `NOT NULL FK → Users(UserID)` | ID of the sender user |
| `DonorID` | `INT` | `NOT NULL FK → Donor(DonorID)` | ID of the recipient donor |
| `Subject` | `VARCHAR(200)` | `NOT NULL` | Message subject |
| `Body` | `NVARCHAR(MAX)` | `NOT NULL` | Full message body |
| `SentAt` | `DATETIME` | `DEFAULT GETDATE()` | Timestamp of message |

### Entity Relationship Diagram (ERD)

```
┌─────────────┐        ┌──────────────┐        ┌─────────────┐
│   Users     │        │   Messages   │        │    Donor    │
├─────────────┤        ├──────────────┤        ├─────────────┤
│ UserID (PK) │──1──┐  │ MessageID(PK)│  ┌──1──│ DonorID(PK) │
│ FullName    │     └─N│ SenderUserID │  │     │ Name        │
│ Email       │        │ DonorID      │N─┘     │ BloodGroup  │
│ PasswordHash│        │ Subject      │        │ Age / Gender│
│ CreatedAt   │        │ Body         │        │ City / Email│
└─────────────┘        │ SentAt       │        │ Mobile      │
                       └──────────────┘        └─────────────┘
```

---

## 8. Module Descriptions

### 8.1 — Home Page (`Default.aspx`)

The landing page of ShareLife featuring:
- **Hero Section**: Animated ECG pulse SVG line, brand headline, and "Be a Hero, Donate Blood" call-to-action button
- **Features Grid**: 5 feature cards linking to: Register Donor, Search Donor, View All Donors, Save Lives, About Us
- **Design**: Crimson Red (#dc2626) color theme with wave SVG animations

**Key UI elements:**
```
• Hero CTA → Register.aspx
• Feature cards → Register / Search / ViewDonors / About pages
• ECG SVG animation divider
• Responsive two-column layout
```

---

### 8.2 — Donor Registration (`Register.aspx` + `Register.aspx.cs`)

Allows new donors to register their details in the system.

**Form Fields Collected:**
- Personal: Name, Gender, Age, Email, Mobile, City
- Medical: Blood Group (dropdown), Weight, Last Donation Date, Medical Conditions

**Validation:**
- Required field validators (client + server side)
- Age range: 18–65 years (enforced via `RangeValidator`)
- Mobile: 10-digit numeric validation

**Code Logic (`Register.aspx.cs`):**
```csharp
// Parameterized INSERT query to prevent SQL injection
string query = @"INSERT INTO Donor (Name, Gender, Age, Email, Mobile, City, 
                 BloodGroup, Weight, LastDonationDate, MedicalConditions) 
                 VALUES (@Name, @Gender, @Age, @Email, @Mobile, @City, 
                 @BloodGroup, @Weight, @LastDonationDate, @MedicalConditions)";
cmd.Parameters.AddWithValue("@Name", name);
// ... all fields parameterized
```

**Post-registration:** Success message displayed, form fields cleared automatically.

---

### 8.3 — Donor Search (`Search.aspx` + `Search.aspx.cs`)

Enables users to find available blood donors by blood group.

**Functionality:**
- Dropdown to select blood group: A+, A-, B+, B-, O+, O-, AB+, AB-
- Results displayed in an ASP.NET `GridView` showing: Name, Gender, Age, City, Blood Group, Mobile, Last Donation Date
- Result count shown (e.g., *"Found 3 registered donor(s) matching blood group 'O+'"*)
- Contact & Message buttons linked to `ContactDonor.aspx`

**SQL Query:**
```sql
SELECT DonorID, Name, ISNULL(Gender,'N/A') AS Gender, Age, Mobile, City, 
       BloodGroup, ISNULL(LastDonationDate,'Never') AS LastDonationDate 
FROM Donor 
WHERE BloodGroup = @BloodGroup 
ORDER BY Name ASC
```

---

### 8.4 — View All Donors (`ViewDonors.aspx`)

Displays the complete, unfiltered list of all registered donors in a sortable `GridView` table.

**Columns displayed:** DonorID, Name, Blood Group, Age, Gender, City, Mobile, Email, Weight, Last Donation Date

---

### 8.5 — User Sign Up (`SignUp.aspx` + `SignUp.aspx.cs`)

Allows new users (blood requesters) to create an account.

**Fields:** Full Name, Email, Password, Confirm Password

**Security measures:**
- Email uniqueness validation (checked against `Users` table)
- Password strength: minimum 8 characters
- Password confirmation matching validator
- Password stored as **SHA-256 hash** (never plain text)

---

### 8.6 — User Login (`Login.aspx` + `Login.aspx.cs`)

Authenticates registered users to access protected features.

**Authentication logic:**
```csharp
// Hash entered password and compare with stored hash
string hashedPassword = HashPassword(password);
string query = "SELECT UserID, FullName, Email FROM Users 
                WHERE Email = @Email AND PasswordHash = @PasswordHash";
// On success: store user info in Session
Session["UserID"] = reader["UserID"].ToString();
Session["FullName"] = reader["FullName"].ToString();
```

**SHA-256 Password Hashing Implementation:**
```csharp
public static string HashPassword(string password)
{
    using (SHA256 sha256 = SHA256.Create())
    {
        byte[] bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
        StringBuilder sb = new StringBuilder();
        foreach (byte b in bytes)
            sb.Append(b.ToString("x2"));
        return sb.ToString();
    }
}
```

**Session Variables stored:** `UserID`, `FullName`, `Email`

**Auto-redirect:** If already logged in, redirects directly to `Default.aspx`.

---

### 8.7 — Contact Donor (`ContactDonor.aspx` + `ContactDonor.aspx.cs`)

Allows authenticated users to send a direct message to a specific donor.

**Access control:** Login required — non-authenticated users are redirected to a login prompt panel.

**Features:**
- Donor profile card displayed (Name, Age, Blood Group, City)
- Message form: Subject line + Message Body
- Message history panel (shows previous messages to same donor)
- On success: confirmation message + "View Donor Inbox" link

**Data flow:**
```
User selects donor → ContactDonor.aspx?id={DonorID}
  → LoadDonorInfo(donorId)      → SELECT from Donor table
  → LoadMessageHistory(donorId) → SELECT from Messages table
  → btnSend_Click()             → INSERT INTO Messages table
```

---

### 8.8 — Donor Messages / Inbox (`DonorMessages.aspx`)

Displays all messages received by a specific donor.

**Shown:** Sender name, message subject, body, and timestamp
**Access:** Viewable via `DonorMessages.aspx?id={DonorID}`

---

### 8.9 — Edit Donor (`EditDonor.aspx` + `EditDonor.aspx.cs`)

Allows editing of an existing donor's registration details.

**Functionality:**
- Pre-loads existing donor data into form fields
- Validates and saves changes back to the `Donor` table
- Supports update of all fields including medical details

---

### 8.10 — About Page (`About.aspx`)

Educational resource page covering:
- Blood donation eligibility criteria (age 18–65, minimum weight 50 kg, health conditions)
- Blood type compatibility chart (universal donor O-, universal recipient AB+)
- Health benefits of donating blood for the donor
- WHO blood donation statistics and guidelines

---

## 9. Security Features

| Security Measure | Implementation | Location |
|-----------------|----------------|----------|
| **SQL Injection Prevention** | All database queries use `SqlCommand.Parameters.AddWithValue()` — no string concatenation | All `.aspx.cs` files |
| **XSS Protection** | User input is never rendered directly to HTML without encoding | `Server.HtmlEncode()` where applicable |
| **Password Hashing** | SHA-256 one-way hashing via `System.Security.Cryptography.SHA256` | `Login.aspx.cs`, `SignUp.aspx.cs` |
| **Session Management** | Login state stored securely in server-side ASP.NET sessions | `Login.aspx.cs`, `Site.Master.cs` |
| **Authentication Guards** | Protected pages check `Session["UserID"] != null` before displaying content | `ContactDonor.aspx.cs` |
| **Input Validation** | Both client-side (`RequiredFieldValidator`, `RangeValidator`, `RegularExpressionValidator`) and server-side validation | All form pages |

---

## 10. System Flow

### User Registration Flow (Donor)
```
Visit Register.aspx
    → Fill form (Name, Blood Group, Age, City, Mobile, etc.)
    → Client-side validation passes
    → Server-side: Page.IsValid check
    → INSERT INTO Donor table (parameterized)
    → Success message shown → Form cleared
```

### Login Flow
```
Visit Login.aspx
    → Enter Email + Password
    → Server hashes password with SHA-256
    → SELECT from Users WHERE Email = @Email AND PasswordHash = @Hash
    → Match found → Store Session["UserID"], Session["FullName"]
    → Redirect to Default.aspx (Home)
```

### Donor Search Flow
```
Visit Search.aspx
    → Select blood group from dropdown
    → Click "Search" button
    → SELECT from Donor WHERE BloodGroup = @BloodGroup
    → Display results in GridView
    → Click "Contact" → ContactDonor.aspx?id={DonorID}
```

### Messaging Flow
```
Visit ContactDonor.aspx?id={DonorID}
    → Check Session["UserID"] — redirect if not logged in
    → Load donor profile card from Donor table
    → Load previous message history from Messages table
    → Fill Subject + Body → Click Send
    → INSERT INTO Messages (SenderUserID, DonorID, Subject, Body)
    → Success confirmation shown
```

---

## 11. Project File Structure

```
ShareLife.net/
│
├── 📄 Site.Master              ← Master page (navigation bar, layout shell)
├── 📄 Site.Master.cs           ← Master page code-behind (session nav updates)
├── 📄 Style.css                ← Complete CSS design system (~700 lines)
├── 📄 Web.config               ← Connection string & app settings
├── 📄 ShareLife.csproj         ← MSBuild project file
├── 📄 ShareLife.sln            ← Visual Studio solution file
│
├── 🏠 Default.aspx/.cs         ← Home page (hero + features grid)
├── 📝 Register.aspx/.cs        ← Donor registration form
├── 🔍 Search.aspx/.cs          ← Blood group search
├── 👥 ViewDonors.aspx/.cs      ← All donors directory
├── ✏️  EditDonor.aspx/.cs       ← Edit donor record
├── 📩 ContactDonor.aspx/.cs    ← Send message to donor
├── 📬 DonorMessages.aspx/.cs   ← Donor message inbox
├── 🔑 Login.aspx/.cs           ← User login
├── 📋 SignUp.aspx/.cs          ← User registration
├── ℹ️  About.aspx/.cs           ← Awareness & education page
│
├── 🗄️  setup_database.sql       ← Full DB creation script (BloodDonorDB)
├── 🐍 create_presentation.py   ← Python PPT generator script
├── 📊 ShareLife_Presentation.pptx ← Project PowerPoint (10 slides)
├── 🌐 presentation.html        ← Interactive web slide deck
└── 🖼️  blood_donation_hero.jpg  ← Hero section image
```

---

## 12. Testing & Validation

### 12.1 Form Validation Testing

| Test Case | Input | Expected Output | Result |
|-----------|-------|-----------------|--------|
| Register with empty name | (blank) | "Name is required" error | ✅ Pass |
| Register with age < 18 | Age = 15 | "Age must be between 18 and 65" | ✅ Pass |
| Register with invalid mobile | "abc123" | Regex validation error | ✅ Pass |
| Search with no blood group selected | (none) | "Please select a valid blood group" | ✅ Pass |
| Login with wrong password | Wrong pass | "Invalid email or password" error | ✅ Pass |
| Login with correct credentials | Valid | Redirect to Home, session set | ✅ Pass |
| Contact donor without login | No session | Login prompt panel shown | ✅ Pass |
| Send message to donor | Logged in, valid form | Message inserted, success shown | ✅ Pass |

### 12.2 Security Testing

| Test | Method | Result |
|------|--------|--------|
| SQL Injection in search field | `' OR '1'='1` as blood group | Blocked by parameterized query | ✅ Safe |
| SQL Injection in login email | `admin'--` | Blocked by parameterized query | ✅ Safe |
| Plain text password storage | Checked DB `Users` table | SHA-256 hash stored, not plaintext | ✅ Safe |
| Unauthorized contact attempt | Visit `ContactDonor.aspx` without login | Login required panel shown | ✅ Safe |

### 12.3 Browser Compatibility

| Browser | Tested | Status |
|---------|--------|--------|
| Google Chrome | ✅ | Fully functional |
| Microsoft Edge | ✅ | Fully functional |
| Mozilla Firefox | ✅ | Fully functional |

---

## 13. Advantages & Limitations

### ✅ Advantages

1. **Centralized Platform** — All donor data is stored in one database, accessible from anywhere on the network.
2. **Fast Search** — Blood group-based filtering retrieves donors instantly from SQL Server.
3. **Secure** — Parameterized queries, SHA-256 hashing, and session guards ensure data integrity and user privacy.
4. **User-Friendly** — Clean, modern UI with animated elements makes navigation intuitive for all users.
5. **Direct Messaging** — Eliminates the need for intermediaries; requesters contact donors directly.
6. **Extensible** — Modular ASP.NET page-based architecture makes it easy to add new pages/features.
7. **Educational** — The About page spreads awareness about eligibility, compatibility, and donation importance.

### ⚠️ Limitations

1. **No Email Notifications** — Messages are stored in the database but donors do not receive email alerts.
2. **No Real-Time Updates** — Page must be manually refreshed; no WebSocket or SignalR real-time messaging.
3. **LocalDB Dependency** — Requires MSSQLLocalDB for local development; not cloud-deployed.
4. **No Role-Based Access Control** — Any user can view all donor records; no admin-only sections.
5. **No Donor Self-Login** — Donors cannot currently log in as themselves; only requesters have accounts.

---

## 14. Future Scope

The following enhancements are planned for future versions of ShareLife:

| Enhancement | Description |
|-------------|-------------|
| 📧 **Email/SMS Notifications** | Notify donors via email or SMS when they receive a new message request |
| 🗺️ **Location-Based Search** | Filter donors by proximity using GPS/maps integration |
| 📱 **Mobile App** | Build a companion Android/iOS app using Xamarin or .NET MAUI |
| 🩺 **Donor Health Tracking** | Allow donors to log donation history and health checkup records |
| 🔐 **Donor Accounts** | Allow donors to log in and manage their own profiles and inboxes |
| 📊 **Admin Dashboard** | Admin panel for statistics, donor management, and moderation |
| ☁️ **Cloud Deployment** | Host on Azure App Service with Azure SQL Database |
| 🔔 **Real-Time Alerts** | Use SignalR for live message notifications |

---

## 15. Conclusion

**ShareLife – A Blood Donor Management System** is a fully functional, secure web application built on **ASP.NET Web Forms (.NET Framework 4.8)** with a **SQL Server** backend. The system successfully achieves its primary goal of connecting voluntary blood donors with people in urgent medical need through a centralized, efficient digital platform.

Key accomplishments of this project:
- ✅ Built a complete CRUD application (Create, Read, Update, Delete) for donor records
- ✅ Implemented user authentication with SHA-256 password security
- ✅ Created a donor-requester messaging system with message history
- ✅ Applied industry best practices (parameterized SQL, input validation, session management)
- ✅ Designed a modern, responsive UI with crimson red medical theme
- ✅ Developed and published a professional 10-slide project presentation

This project not only fulfills its academic objectives but also addresses a genuine **social and medical need**, making it a meaningful contribution to healthcare technology solutions.

---

## 16. References

1. **Microsoft Documentation** — ASP.NET Web Forms Overview  
   https://docs.microsoft.com/en-us/aspnet/web-forms/

2. **Microsoft Documentation** — ADO.NET with SQL Server  
   https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/

3. **World Health Organization (WHO)** — Blood Safety and Availability  
   https://www.who.int/news-room/fact-sheets/detail/blood-safety-and-availability

4. **Microsoft SQL Server Documentation** — T-SQL Reference  
   https://docs.microsoft.com/en-us/sql/t-sql/

5. **OWASP** — SQL Injection Prevention Cheat Sheet  
   https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

6. **NIST** — Cryptographic Hash Standard (SHA-256)  
   https://csrc.nist.gov/publications/detail/fips/180/4/final

---

*© 2025–2026 Satyam Sharma — ShareLife Blood Donor Management System*  
*GitHub: [https://github.com/golden67281/ShareLife.NET](https://github.com/golden67281/ShareLife.NET)*
