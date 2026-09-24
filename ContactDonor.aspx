<%@ Page Title="Contact Donor" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="ContactDonor.aspx.cs" Inherits="ShareLife.ContactDonor" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">

    <%-- Not logged in panel --%>
    <asp:Panel ID="pnlNotLoggedIn" runat="server" Visible="false">
        <div class="content-card" style="text-align:center; padding: 3rem;">
            <div style="font-size:3rem; margin-bottom:1rem;">&#128274;</div>
            <h2 class="page-title">Login Required</h2>
            <p class="page-subtitle" style="margin-top:0.5rem;">You must be logged in to contact a blood donor.</p>
            <a href="Login.aspx" class="btn-auth" style="display:inline-block; max-width:220px; margin: 0 auto;">Login to Continue</a>
            <div class="auth-divider" style="margin-top:1rem;">No account? <a href="SignUp.aspx">Create one here</a></div>
        </div>
    </asp:Panel>

    <%-- Donor not found panel --%>
    <asp:Panel ID="pnlNotFound" runat="server" Visible="false">
        <div class="content-card" style="text-align:center; padding: 3rem;">
            <div style="font-size:3rem; margin-bottom:1rem;">&#10060;</div>
            <h2 class="page-title">Donor Not Found</h2>
            <p class="page-subtitle">The donor you are trying to contact does not exist.</p>
            <a href="ViewDonors.aspx" class="btn-primary">View All Donors</a>
        </div>
    </asp:Panel>

    <%-- Main contact panel (shown when logged in and donor is found) --%>
    <asp:Panel ID="pnlContact" runat="server" Visible="false">
        <div class="content-card">
            <h2 class="page-title">Contact Donor</h2>
            <p class="page-subtitle">Send a message request to this registered donor.</p>

            <%-- Donor Profile Display --%>
            <div class="donor-profile-card">
                <div class="donor-avatar">
                    <asp:Literal ID="litDonorInitial" runat="server"></asp:Literal>
                </div>
                <div class="donor-info">
                    <h3><asp:Literal ID="litDonorName" runat="server"></asp:Literal></h3>
                    <p>&#128205; <asp:Literal ID="litDonorCity" runat="server"></asp:Literal></p>
                    <p>&#128100; Age: <asp:Literal ID="litDonorAge" runat="server"></asp:Literal> years</p>
                    <div><span class="blood-badge-lg"><asp:Literal ID="litDonorBloodGroup" runat="server"></asp:Literal></span></div>
                </div>
            </div>

            <%-- Message sent confirmation --%>
            <asp:Panel ID="pnlSuccess" runat="server" Visible="false">
                <div class="alert-message alert-success" style="margin-bottom: 1.5rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.8rem;">
                    <span><asp:Label ID="lblSuccess" runat="server"></asp:Label></span>
                    <a id="lnkViewInbox" runat="server" href="#" class="btn-inbox" style="font-size:0.85rem;">&#128235; View Donor Inbox</a>
                </div>
            </asp:Panel>


            <asp:Panel ID="pnlError" runat="server" Visible="false">
                <div class="validation-summary">
                    <asp:Label ID="lblError" runat="server"></asp:Label>
                </div>
            </asp:Panel>

            <%-- Contact Form --%>
            <asp:Panel ID="pnlForm" runat="server">
                <div class="contact-form">
                    <div class="form-group">
                        <label for="<%= txtSubject.ClientID %>">Subject <span style="color:red">*</span></label>
                        <asp:TextBox ID="txtSubject" runat="server" CssClass="form-control" placeholder="e.g. Urgent blood request for surgery"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="rfvSubject" runat="server" ControlToValidate="txtSubject"
                            ErrorMessage="Subject is required." CssClass="validation-error" Display="Dynamic" />
                    </div>

                    <div class="form-group">
                        <label for="<%= txtMessage.ClientID %>">Message <span style="color:red">*</span></label>
                        <asp:TextBox ID="txtMessage" runat="server" CssClass="form-control" TextMode="MultiLine"
                            placeholder="Write your message here. Include hospital name, contact number, and urgency details..." Rows="5"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="rfvMessage" runat="server" ControlToValidate="txtMessage"
                            ErrorMessage="Message body is required." CssClass="validation-error" Display="Dynamic" />
                    </div>

                    <div style="margin-top: 1rem; display: flex; gap: 1rem; align-items: center;">
                        <asp:Button ID="btnSend" runat="server" Text="Send Message" CssClass="btn-primary" OnClick="btnSend_Click" />
                        <a href="ViewDonors.aspx" style="color: var(--muted-text); text-decoration: none; font-size: 0.95rem;">&#8592; Back to All Donors</a>
                    </div>
                </div>
            </asp:Panel>
        </div>

        <%-- Past messages sent to this donor by the logged-in user --%>
        <asp:Panel ID="pnlHistory" runat="server" Visible="false">
            <div class="content-card">
                <h3 style="color: var(--dark-bg); margin-bottom:1rem; font-size:1.2rem; border-bottom: 2px solid var(--primary-color); display:inline-block; padding-bottom:0.3rem;">
                    Your Past Messages to This Donor
                </h3>
                <div class="message-list">
                    <asp:Repeater ID="rptMessages" runat="server">
                        <ItemTemplate>
                            <div class="message-item">
                                <div class="msg-subject">&#9993; <%# Eval("Subject") %></div>
                                <div class="msg-body"><%# Eval("Body") %></div>
                                <div class="msg-meta">Sent on <%# Eval("SentAt", "{0:ddd, dd MMM yyyy HH:mm}") %></div>
                            </div>
                        </ItemTemplate>
                    </asp:Repeater>
                </div>
            </div>
        </asp:Panel>
    </asp:Panel>

</asp:Content>
