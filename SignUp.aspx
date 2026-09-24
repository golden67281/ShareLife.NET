<%@ Page Title="Sign Up" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="SignUp.aspx.cs" Inherits="ShareLife.SignUp" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <div class="auth-wrapper">
        <div class="auth-card">
            <div class="auth-logo">
                <div class="logo-icon-lg">&#43;</div>
                <h2>Create Account</h2>
                <p>Join our network to search and contact blood donors quickly.</p>
            </div>

            <asp:Panel ID="pnlMessage" runat="server" Visible="false">
                <asp:Label ID="lblMessage" runat="server"></asp:Label>
            </asp:Panel>

            <div class="form-group">
                <label for="<%= txtFullName.ClientID %>">Full Name <span style="color:red">*</span></label>
                <asp:TextBox ID="txtFullName" runat="server" CssClass="form-control" placeholder="Enter your full name"></asp:TextBox>
                <asp:RequiredFieldValidator ID="rfvFullName" runat="server" ControlToValidate="txtFullName"
                    ErrorMessage="Full Name is required." CssClass="validation-error" Display="Dynamic" />
            </div>

            <div class="form-group">
                <label for="<%= txtEmail.ClientID %>">Email Address <span style="color:red">*</span></label>
                <asp:TextBox ID="txtEmail" runat="server" CssClass="form-control" TextMode="Email" placeholder="Enter your email"></asp:TextBox>
                <asp:RequiredFieldValidator ID="rfvEmail" runat="server" ControlToValidate="txtEmail"
                    ErrorMessage="Email is required." CssClass="validation-error" Display="Dynamic" />
                <asp:RegularExpressionValidator ID="revEmail" runat="server" ControlToValidate="txtEmail"
                    ValidationExpression="^[^@\s]+@[^@\s]+\.[^@\s]+$"
                    ErrorMessage="Please enter a valid email address." CssClass="validation-error" Display="Dynamic" />
            </div>

            <div class="form-group">
                <label for="<%= txtPassword.ClientID %>">Password <span style="color:red">*</span></label>
                <asp:TextBox ID="txtPassword" runat="server" CssClass="form-control" TextMode="Password" placeholder="Create a password"></asp:TextBox>
                <asp:RequiredFieldValidator ID="rfvPassword" runat="server" ControlToValidate="txtPassword"
                    ErrorMessage="Password is required." CssClass="validation-error" Display="Dynamic" />
                <asp:RegularExpressionValidator ID="revPassword" runat="server" ControlToValidate="txtPassword"
                    ValidationExpression="^.{6,}$"
                    ErrorMessage="Password must be at least 6 characters." CssClass="validation-error" Display="Dynamic" />
                <span class="password-hint">Minimum 6 characters.</span>
            </div>

            <div class="form-group">
                <label for="<%= txtConfirmPassword.ClientID %>">Confirm Password <span style="color:red">*</span></label>
                <asp:TextBox ID="txtConfirmPassword" runat="server" CssClass="form-control" TextMode="Password" placeholder="Repeat your password"></asp:TextBox>
                <asp:RequiredFieldValidator ID="rfvConfirm" runat="server" ControlToValidate="txtConfirmPassword"
                    ErrorMessage="Please confirm your password." CssClass="validation-error" Display="Dynamic" />
                <asp:CompareValidator ID="cvPassword" runat="server" ControlToValidate="txtConfirmPassword"
                    ControlToCompare="txtPassword" ErrorMessage="Passwords do not match."
                    CssClass="validation-error" Display="Dynamic" />
            </div>

            <div style="margin-top: 1.5rem;">
                <asp:Button ID="btnSignUp" runat="server" Text="Create Account" CssClass="btn-auth" OnClick="btnSignUp_Click" />
            </div>

            <div class="auth-divider">
                Already have an account? <a href="Login.aspx">Sign in here</a>
            </div>
        </div>
    </div>
</asp:Content>
