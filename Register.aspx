<%@ Page Title="Register Donor" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Register.aspx.cs" Inherits="ShareLife.Register" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <div class="content-card">
        <h2 class="page-title">Donor Registration</h2>
        <p class="page-subtitle">Register to become an active blood donor and help save lives in your community.</p>

        <asp:Panel ID="pnlMessage" runat="server" Visible="false">
            <asp:Label ID="lblMessage" runat="server"></asp:Label>
        </asp:Panel>

        <!-- Section 1: Personal Details -->
        <div class="form-section">
            <h3 class="form-section-title"><span class="section-icon">&#128100;</span> Personal Details</h3>
            <div class="form-grid">
                <!-- Name -->
                <div class="form-group">
                    <label for="<%= txtName.ClientID %>">Full Name <span style="color:red;">*</span></label>
                    <asp:TextBox ID="txtName" runat="server" CssClass="form-control" placeholder="Enter your full name"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="rfvName" runat="server" ControlToValidate="txtName"
                        ErrorMessage="Full Name is required." CssClass="validation-error" Display="Dynamic" />
                </div>

                <!-- Gender -->
                <div class="form-group">
                    <label for="<%= ddlGender.ClientID %>">Gender <span style="color:red;">*</span></label>
                    <asp:DropDownList ID="ddlGender" runat="server" CssClass="form-control">
                        <asp:ListItem Text="-- Select Gender --" Value="" />
                        <asp:ListItem Text="Male" Value="Male" />
                        <asp:ListItem Text="Female" Value="Female" />
                        <asp:ListItem Text="Other" Value="Other" />
                    </asp:DropDownList>
                    <asp:RequiredFieldValidator ID="rfvGender" runat="server" ControlToValidate="ddlGender"
                        InitialValue="" ErrorMessage="Please select Gender." CssClass="validation-error" Display="Dynamic" />
                </div>

                <!-- Age -->
                <div class="form-group">
                    <label for="<%= txtAge.ClientID %>">Age (Years) <span style="color:red;">*</span></label>
                    <asp:TextBox ID="txtAge" runat="server" CssClass="form-control" TextMode="Number" placeholder="Enter age (18-65)"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="rfvAge" runat="server" ControlToValidate="txtAge"
                        ErrorMessage="Age is required." CssClass="validation-error" Display="Dynamic" />
                    <asp:RangeValidator ID="rvAge" runat="server" ControlToValidate="txtAge" MinimumValue="18" MaximumValue="65"
                        Type="Integer" ErrorMessage="Donor age must be between 18 and 65." CssClass="validation-error" Display="Dynamic" />
                </div>

                <!-- Email -->
                <div class="form-group">
                    <label for="<%= txtEmail.ClientID %>">Email Address</label>
                    <asp:TextBox ID="txtEmail" runat="server" CssClass="form-control" TextMode="Email" placeholder="e.g. donor@example.com"></asp:TextBox>
                    <asp:RegularExpressionValidator ID="revEmail" runat="server" ControlToValidate="txtEmail"
                        ValidationExpression="^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$" ErrorMessage="Please enter a valid email address."
                        CssClass="validation-error" Display="Dynamic" />
                </div>

                <!-- Mobile Number -->
                <div class="form-group">
                    <label for="<%= txtMobile.ClientID %>">Mobile Number <span style="color:red;">*</span></label>
                    <asp:TextBox ID="txtMobile" runat="server" CssClass="form-control" placeholder="10-digit mobile number"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="rfvMobile" runat="server" ControlToValidate="txtMobile"
                        ErrorMessage="Mobile number is required." CssClass="validation-error" Display="Dynamic" />
                    <asp:RegularExpressionValidator ID="revMobile" runat="server" ControlToValidate="txtMobile"
                        ValidationExpression="^\d{10}$" ErrorMessage="Please enter a valid 10-digit mobile number."
                        CssClass="validation-error" Display="Dynamic" />
                </div>

                <!-- City -->
                <div class="form-group">
                    <label for="<%= txtCity.ClientID %>">City / Location <span style="color:red;">*</span></label>
                    <asp:TextBox ID="txtCity" runat="server" CssClass="form-control" placeholder="Enter city name"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="rfvCity" runat="server" ControlToValidate="txtCity"
                        ErrorMessage="City is required." CssClass="validation-error" Display="Dynamic" />
                </div>
            </div>
        </div>

        <!-- Section 2: Medical Details -->
        <div class="form-section">
            <h3 class="form-section-title">Medical Details</h3>
            <div class="form-grid">
                <!-- Blood Group -->
                <div class="form-group">
                    <label for="<%= ddlBloodGroup.ClientID %>">Blood Group <span style="color:red;">*</span></label>
                    <asp:DropDownList ID="ddlBloodGroup" runat="server" CssClass="form-control">
                        <asp:ListItem Text="-- Select Blood Group --" Value="" />
                        <asp:ListItem Text="A+" Value="A+" />
                        <asp:ListItem Text="A-" Value="A-" />
                        <asp:ListItem Text="B+" Value="B+" />
                        <asp:ListItem Text="B-" Value="B-" />
                        <asp:ListItem Text="O+" Value="O+" />
                        <asp:ListItem Text="O-" Value="O-" />
                        <asp:ListItem Text="AB+" Value="AB+" />
                        <asp:ListItem Text="AB-" Value="AB-" />
                    </asp:DropDownList>
                    <asp:RequiredFieldValidator ID="rfvBloodGroup" runat="server" ControlToValidate="ddlBloodGroup"
                        InitialValue="" ErrorMessage="Please select a Blood Group." CssClass="validation-error" Display="Dynamic" />
                </div>

                <!-- Weight -->
                <div class="form-group">
                    <label for="<%= txtWeight.ClientID %>">Weight (kg) <span style="color:red;">*</span></label>
                    <asp:TextBox ID="txtWeight" runat="server" CssClass="form-control" TextMode="Number" placeholder="Min. 45 kg"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="rfvWeight" runat="server" ControlToValidate="txtWeight"
                        ErrorMessage="Weight is required." CssClass="validation-error" Display="Dynamic" />
                    <asp:RangeValidator ID="rvWeight" runat="server" ControlToValidate="txtWeight" MinimumValue="45" MaximumValue="150"
                        Type="Integer" ErrorMessage="Donor weight must be between 45 and 150 kg." CssClass="validation-error" Display="Dynamic" />
                </div>

                <!-- Last Donation Date -->
                <div class="form-group">
                    <label for="<%= txtLastDonationDate.ClientID %>">Last Donation Date</label>
                    <asp:TextBox ID="txtLastDonationDate" runat="server" CssClass="form-control" TextMode="Date" placeholder="Select date or leave blank if first-time"></asp:TextBox>
                </div>

                <!-- Medical Conditions -->
                <div class="form-group">
                    <label for="<%= txtMedicalConditions.ClientID %>">Medical Conditions / Health Status</label>
                    <asp:TextBox ID="txtMedicalConditions" runat="server" CssClass="form-control" placeholder="e.g. None, Hypertension, Diabetes (or None)"></asp:TextBox>
                </div>
            </div>
        </div>

        <div style="margin-top: 1.5rem;">
            <asp:Button ID="btnRegister" runat="server" Text="Register Donor" CssClass="btn-primary" OnClick="btnRegister_Click" />
        </div>
    </div>
</asp:Content>
