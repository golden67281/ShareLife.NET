# ShareLife.net - Blood Donor Management System

A web-based **Blood Donor Management System** built with **ASP.NET Web Forms (C#)** and **SQL Server (MSSQLLocalDB / T-SQL)**. This application connects volunteer blood donors with people in urgent medical need.

---

## 🌟 Key Features

1. **Active Donor Registry (`Register.aspx`)**:
   - Register volunteer blood donors with full name, age (18-65), blood group (A+, A-, B+, B-, O+, O-, AB+, AB-), mobile number, and city.
   - Comprehensive client-side and server-side validation.

2. **Rapid Donor Search (`Search.aspx`)**:
   - Filter active donors instantly by blood group.
   - View donor details with direct contact and inbox messaging actions.

3. **Complete Donor Directory (`ViewDonors.aspx`)**:
   - Browse all registered donors in a clean, responsive table grid.

4. **User Authentication (`Login.aspx` & `SignUp.aspx`)**:
   - Account creation and secure login for requesters and volunteers.
   - Passwords hashed using **SHA-256**.
   - Session-based state management with navigation bar state updates.

5. **Donor Contact & Messaging System (`ContactDonor.aspx` & `DonorMessages.aspx`)**:
   - Logged-in users can send direct messages with hospital details and urgency level to any donor.
   - Dedicated Donor Inbox page displaying received messages, sender information, and timestamp history.

6. **Educational & Awareness Resources (`About.aspx`)**:
   - Eligibility guidelines, donor health benefits, blood compatibility rules, and WHO facts.

---

## 🛠️ Technology Stack

- **Framework**: ASP.NET Web Forms (.NET Framework 4.8)
- **Language**: C# 7.3+
- **Database**: SQL Server / MSSQLLocalDB (`System.Data.SqlClient`)
- **Styling**: Pure CSS3 Design System (`Style.css`) — Mobile Responsive, Glassmorphic UI Tokens, Flexbox & Grid layouts.

---

## 🚀 Database Setup & Installation

### Step 1: Initialize Database
Run the [`setup_database.sql`](file:///d:/ShareLife.net/setup_database.sql) script in **SQL Server Management Studio (SSMS)** or Visual Studio **SQL Server Object Explorer**:

```sql
-- Executes setup_database.sql
-- Creates database BloodDonorDB and tables: Donor, Users, Messages
```

### Step 2: Connection String Configuration
Ensure your `Web.config` connection string matches your local SQL Server instance:

```xml
<connectionStrings>
  <add name="BloodDonorDBConnectionString" 
       connectionString="Data Source=(localdb)\MSSQLLocalDB;Initial Catalog=BloodDonorDB;Integrated Security=True;" 
       providerName="System.Data.SqlClient" />
</connectionStrings>
```

### Step 3: Default Credentials for Testing
A demo user account is pre-created in `setup_database.sql`:
- **Email**: `demo@sharelife.net`
- **Password**: `password123`

---

## 💻 Building & Running the Application

### Option A: Using MSBuild
From PowerShell / Developer Command Prompt:
```powershell
& "C:\Program Files\Microsoft Visual Studio\18\Community\MSBuild\Current\Bin\MSBuild.exe" ShareLife.csproj /t:Rebuild /p:Configuration=Debug
```

### Option B: Visual Studio
1. Open `ShareLife.sln` in Visual Studio.
2. Press `F5` or `Ctrl + F5` to run with IIS Express.


---

## 📊 Project Presentation & Slides

This project includes a complete **10-Slide Project Presentation Deck** designed in a modern Crimson Red Healthcare theme:

- **[ShareLife_Presentation.pptx](ShareLife_Presentation.pptx)**: 16:9 Widescreen PowerPoint presentation file ready for project defense / demonstration.
- **[presentation.html](presentation.html)**: Interactive web-based HTML slide deck to view and present directly in any web browser.
- **[create_presentation.py](create_presentation.py)**: Python script using `python-pptx` to generate and customize the slides.

---

## 🛡️ Security Features
- **SQL Injection Prevention**: All database commands utilize parameterized queries (`SqlCommand.Parameters`).
- **XSS Protection**: HTML outputs are escaped using `Server.HtmlEncode`.
- **Secure Credentials**: Password hashing via SHA-256 (`Login.HashPassword()`).
