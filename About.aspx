<%@ Page Title="About Blood Donation" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="About.aspx.cs" Inherits="ShareLife.About" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <div class="content-card">
        <h2 class="page-title">About Blood Donation</h2>
        <p class="page-subtitle">Learn why donating blood saves lives, who is eligible, and how your contribution helps.</p>

        <div style="margin-bottom: 2rem;">
            <h3 style="color: var(--dark-bg); margin-bottom: 0.5rem;">Why Donate Blood?</h3>
            <p>
                Blood is an essential medical resource that cannot be artificially manufactured or synthetically synthesized. 
                Every day, thousands of patients require blood transfusions due to surgeries, traumatic injuries, cancer treatments, 
                and chronic illnesses like anemia or thalassemia. A single blood donation can save up to <strong>three lives</strong>.
            </p>
        </div>

        <div class="features-grid" style="margin-bottom: 2rem;">
            <div class="feature-card">
                <h3>Eligibility Criteria</h3>
                <ul style="padding-left: 1.2rem; color: var(--text-color);">
                    <li>Age between 18 and 65 years.</li>
                    <li>Minimum weight of 50 kg (110 lbs).</li>
                    <li>Normal blood pressure and hemoglobin level.</li>
                    <li>Good general health with no active infections.</li>
                </ul>
            </div>

            <div class="feature-card">
                <h3>Health Benefits</h3>
                <ul style="padding-left: 1.2rem; color: var(--text-color);">
                    <li>Stimulates new blood cell production.</li>
                    <li>Reduces harmful iron buildup in the body.</li>
                    <li>Includes a free mini-health screening.</li>
                    <li>Provides emotional satisfaction of saving lives.</li>
                </ul>
            </div>

            <div class="feature-card">
                <h3>Blood Compatibility</h3>
                <ul style="padding-left: 1.2rem; color: var(--text-color);">
                    <li><strong>O-</strong> is the Universal Red Blood Cell Donor.</li>
                    <li><strong>AB+</strong> is the Universal Plasma Recipient.</li>
                    <li>Blood can be donated safely every 56 days.</li>
                    <li>Donation process takes under 15 minutes.</li>
                </ul>
            </div>
        </div>

        <div style="background-color: #fee2e2; border-left: 4px solid var(--primary-color); padding: 1.2rem; border-radius: 6px;">
            <h4 style="color: var(--primary-color); margin-bottom: 0.3rem;">Did You Know?</h4>
            <p style="font-size: 0.95rem; color: #7f1d1d;">
                According to the World Health Organization (WHO), regular blood donation helps maintain adequate blood supplies in emergency rooms and intensive care units worldwide.
            </p>
        </div>
    </div>
</asp:Content>
