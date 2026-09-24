-- setup_database.sql
-- Creates the BloodDonorDB database, Donor, Users, and Messages tables for ASP.NET Web Forms project

IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'BloodDonorDB')
BEGIN
    CREATE DATABASE BloodDonorDB;
END
GO

USE BloodDonorDB;
GO

-- 1. Create Donor Table
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Donor]') AND type in (N'U'))
BEGIN
    CREATE TABLE Donor (
        DonorID INT IDENTITY(1,1) PRIMARY KEY,
        Name VARCHAR(50) NOT NULL,
        Gender VARCHAR(10) NULL,
        Age INT NOT NULL,
        Email VARCHAR(100) NULL,
        Mobile VARCHAR(15) NOT NULL,
        City VARCHAR(50) NOT NULL,
        BloodGroup VARCHAR(5) NOT NULL,
        Weight INT NULL,
        LastDonationDate VARCHAR(20) NULL,
        MedicalConditions VARCHAR(255) NULL
    );
END
GO

-- 2. Alter table if missing new columns (separate batch)
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Donor]') AND type in (N'U'))
BEGIN
    IF NOT EXISTS (SELECT * FROM sys.columns WHERE object_id = OBJECT_ID(N'[dbo].[Donor]') AND name = 'Gender')
        ALTER TABLE Donor ADD Gender VARCHAR(20) NULL;
    IF NOT EXISTS (SELECT * FROM sys.columns WHERE object_id = OBJECT_ID(N'[dbo].[Donor]') AND name = 'Email')
        ALTER TABLE Donor ADD Email VARCHAR(100) NULL;
    IF NOT EXISTS (SELECT * FROM sys.columns WHERE object_id = OBJECT_ID(N'[dbo].[Donor]') AND name = 'Weight')
        ALTER TABLE Donor ADD Weight INT NULL;
    IF NOT EXISTS (SELECT * FROM sys.columns WHERE object_id = OBJECT_ID(N'[dbo].[Donor]') AND name = 'LastDonationDate')
        ALTER TABLE Donor ADD LastDonationDate VARCHAR(20) NULL;
    IF NOT EXISTS (SELECT * FROM sys.columns WHERE object_id = OBJECT_ID(N'[dbo].[Donor]') AND name = 'MedicalConditions')
        ALTER TABLE Donor ADD MedicalConditions VARCHAR(255) NULL;
END
GO

-- 3. Seed data / update existing records with default values if null
IF NOT EXISTS (SELECT * FROM Donor)
BEGIN
    INSERT INTO Donor (Name, Gender, Age, Email, Mobile, City, BloodGroup, Weight, LastDonationDate, MedicalConditions) VALUES
    ('Satyam Sharma', 'Male', 21, 'satyam@example.com', '9876543210', 'Rohtas', 'O+', 68, '2025-10-15', 'None'),
    ('Nency Rana', 'Female', 20, 'nency@example.com', '9876543211', 'Surat', 'A+', 55, 'Never', 'None'),
    ('Vaibhav Kumar', 'Male', 22, 'vaibhav@example.com', '9876543212', 'Dehri', 'B+', 72, '2025-12-01', 'None'),
    ('Chirag Darji', 'Male', 20, 'chirag@example.com', '9876543213', 'Okai', 'AB+', 60, 'Never', 'None'),
    ('Aditya Raj', 'Male', 21, 'aditya@example.com', '9876543214', 'Bihar', 'O-', 65, '2025-08-20', 'None');
END
ELSE
BEGIN
    ALTER TABLE Donor ALTER COLUMN Gender VARCHAR(20) NULL;
    UPDATE Donor SET Gender = 'Male' WHERE Gender IS NULL AND (Name LIKE '%Sharma%' OR Name LIKE '%Kumar%' OR Name LIKE '%Darji%' OR Name LIKE '%Raj%');
    UPDATE Donor SET Gender = 'Female' WHERE Gender IS NULL AND Name LIKE '%Rana%';
    UPDATE Donor SET Gender = 'Other' WHERE Gender IS NULL;
    UPDATE Donor SET Email = 'N/A' WHERE Email IS NULL;
    UPDATE Donor SET Weight = 60 WHERE Weight IS NULL;
    UPDATE Donor SET LastDonationDate = 'Never' WHERE LastDonationDate IS NULL;
    UPDATE Donor SET MedicalConditions = 'None' WHERE MedicalConditions IS NULL;
END
GO

-- 2. Create Users Table (for Authentication & Messaging)
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Users]') AND type in (N'U'))
BEGIN
    CREATE TABLE Users (
        UserID INT IDENTITY(1,1) PRIMARY KEY,
        FullName VARCHAR(100) NOT NULL,
        Email VARCHAR(100) NOT NULL UNIQUE,
        PasswordHash VARCHAR(256) NOT NULL,
        CreatedAt DATETIME DEFAULT GETDATE()
    );

    -- Insert sample user (Password is SHA256 of 'password123')
    -- 'password123' -> ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
    INSERT INTO Users (FullName, Email, PasswordHash) VALUES
    ('Demo User', 'demo@sharelife.net', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f');
END
GO

-- 3. Create Messages Table (for Contacting Donors)
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Messages]') AND type in (N'U'))
BEGIN
    CREATE TABLE Messages (
        MessageID INT IDENTITY(1,1) PRIMARY KEY,
        SenderUserID INT NOT NULL FOREIGN KEY REFERENCES Users(UserID),
        DonorID INT NOT NULL FOREIGN KEY REFERENCES Donor(DonorID),
        Subject VARCHAR(200) NOT NULL,
        Body NVARCHAR(MAX) NOT NULL,
        SentAt DATETIME DEFAULT GETDATE()
    );

    -- Insert sample message from Demo User (UserID=1) to Donor #1 (Satyam Sharma)
    INSERT INTO Messages (SenderUserID, DonorID, Subject, Body) VALUES
    (1, 1, 'Urgent O+ Blood Requirement for Surgery', 'Hello Satyam, we have an urgent requirement for 2 units of O+ blood at City Hospital tomorrow morning. Please let us know if you are available to donate.');
END
GO
