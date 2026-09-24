<%@ Page Title="Login" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Login.aspx.cs" Inherits="ShareLife.Login" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <div class="auth-wrapper">
        <div class="auth-card">
            <div class="auth-logo">
                <div class="logo-icon-lg">&#10084;</div>
                <h2>Welcome Back</h2>
                <p>Sign in to contact blood donors and manage your profile.</p>
            </div>

            <asp:Panel ID="pnlError" runat="server" Visible="false">
                <div class="validation-summary">
                    <asp:Label ID="lblError" runat="server"></asp:Label>
                </div>
            </asp:Panel>

            <div class="form-group">
                <label for="<%= txtEmail.ClientID %>">Email Address</label>
                <asp:TextBox ID="txtEmail" runat="server" CssClass="form-control" TextMode="Email" placeholder="Enter your email"></asp:TextBox>
                <asp:RequiredFieldValidator ID="rfvEmail" runat="server" ControlToValidate="txtEmail"
                    ErrorMessage="Email is required." CssClass="validation-error" Display="Dynamic" />
            </div>

            <div class="form-group">
                <label for="<%= txtPassword.ClientID %>">Password</label>
                <asp:TextBox ID="txtPassword" runat="server" CssClass="form-control" TextMode="Password" placeholder="Enter your password"></asp:TextBox>
                <asp:RequiredFieldValidator ID="rfvPassword" runat="server" ControlToValidate="txtPassword"
                    ErrorMessage="Password is required." CssClass="validation-error" Display="Dynamic" />
            </div>

            <div style="margin-top: 1.5rem;">
                <asp:Button ID="btnLogin" runat="server" Text="Sign In" CssClass="btn-auth" OnClick="btnLogin_Click" />
            </div>

            <div class="auth-divider">
                Don't have an account? <a href="SignUp.aspx">Create one here</a>
            </div>
        </div>
    </div>
</asp:Content>
