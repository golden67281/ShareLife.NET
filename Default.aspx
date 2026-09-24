<%@ Page Title="Home" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="ShareLife.Default" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <!-- Hero Section -->
    <div class="hero-custom-container">
        <div class="hero-content-row">
            <!-- Left Text Column -->
            <div class="hero-text-side">
                <span class="welcome-label">Welcome to</span>
                <h1 class="hero-brand-name">ShareLife</h1>
                <h2 class="hero-brand-tagline">A Blood Donor Management System</h2>

                <div class="ecg-divider-wrap">
                    <svg viewBox="0 0 280 20" class="ecg-svg" preserveAspectRatio="none">
                        <path d="M0 10h60l8-8 10 16 12-12 10 8h180" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/>
                    </svg>
                </div>

                <p class="hero-motto">
                    Share life, give life. Your one act of kindness can bring hope and save many lives.
                </p>

                <div class="hero-cta-wrap">
                    <a href="Register.aspx" class="btn-hero-donate">
                        <span class="cta-drop-symbol">&#129656;</span> BE A HERO, DONATE BLOOD
                    </a>
                </div>
            </div>

            <!-- Right Illustration Column -->
            <div class="hero-illustration-side">
                <div class="hero-image-wrapper">
                    <img src="blood_donation_hero.jpg" alt="ShareLife Blood Donation" class="hero-illustration-img" />
                </div>
            </div>
        </div>

        <!-- Red Wave Accent -->
        <div class="hero-bottom-wave">
            <svg viewBox="0 0 1440 100" preserveAspectRatio="none">
                <path d="M0,32L120,42.7C240,53,480,75,720,69.3C960,64,1200,32,1320,16L1440,0L1440,100L1320,100C1200,100,960,100,720,100C480,100,240,100,120,100L0,100Z" fill="#dc2626"></path>
            </svg>
        </div>
    </div>

    <!-- Our Features Section -->
    <div class="features-custom-section">
        <div class="features-header-title">
            <div class="title-line"></div>
            <div class="title-text-box">
                <span class="title-drop-icon">&#129656;</span>
                <h2>Our Features</h2>
            </div>
            <div class="title-line"></div>
        </div>

        <div class="features-cards-grid">
            <!-- Card 1: Register Donor -->
            <a href="Register.aspx" class="feature-box-card">
                <div class="icon-circle-bg">
                    <span class="box-icon">&#128100;<sup class="icon-plus">+</sup></span>
                </div>
                <h3>Register Donor</h3>
                <p>Register as a blood donor and save lives.</p>
            </a>

            <!-- Card 2: Search Donor -->
            <a href="Search.aspx" class="feature-box-card">
                <div class="icon-circle-bg">
                    <span class="box-icon">&#128065;</span>
                </div>
                <h3>Search Donor</h3>
                <p>Search donors by blood group.</p>
            </a>

            <!-- Card 3: View All Donors -->
            <a href="ViewDonors.aspx" class="feature-box-card">
                <div class="icon-circle-bg">
                    <span class="box-icon">&#128101;</span>
                </div>
                <h3>View All Donors</h3>
                <p>View the list of all registered donors.</p>
            </a>

            <!-- Card 4: Save Lives -->
            <a href="About.aspx" class="feature-box-card">
                <div class="icon-circle-bg">
                    <span class="box-icon">&#10084;</span>
                </div>
                <h3>Save Lives</h3>
                <p>Your one donation can save many lives.</p>
            </a>

            <!-- Card 5: About Us -->
            <a href="About.aspx" class="feature-box-card">
                <div class="icon-circle-bg">
                    <span class="box-icon">&#8505;</span>
                </div>
                <h3>About Us</h3>
                <p>Know more about blood donation.</p>
            </a>
        </div>
    </div>
</asp:Content>
