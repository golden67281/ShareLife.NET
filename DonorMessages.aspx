<%@ Page Title="Donor Messages" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="DonorMessages.aspx.cs" Inherits="ShareLife.DonorMessages" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">

    <%-- Donor not found --%>
    <asp:Panel ID="pnlNotFound" runat="server" Visible="false">
        <div class="content-card" style="text-align:center; padding:3rem;">
            <div style="font-size:3rem; margin-bottom:1rem;">&#10060;</div>
            <h2 class="page-title">Donor Not Found</h2>
            <p class="page-subtitle">No donor exists with that ID.</p>
            <a href="ViewDonors.aspx" class="btn-primary">View All Donors</a>
        </div>
    </asp:Panel>

    <%-- Main messages panel --%>
    <asp:Panel ID="pnlMain" runat="server" Visible="false">

        <%-- Donor Profile Header Card --%>
        <div class="donor-profile-card" style="margin-bottom:1.5rem;">
            <div class="donor-avatar">
                <asp:Literal ID="litInitial" runat="server"></asp:Literal>
            </div>
            <div class="donor-info" style="flex:1;">
                <h3><asp:Literal ID="litName" runat="server"></asp:Literal></h3>
                <p>&#128205; <asp:Literal ID="litCity" runat="server"></asp:Literal> &nbsp;|&nbsp; &#128100; Age: <asp:Literal ID="litAge" runat="server"></asp:Literal></p>
                <p>&#128222; <asp:Literal ID="litMobile" runat="server"></asp:Literal></p>
                <div><span class="blood-badge-lg"><asp:Literal ID="litBloodGroup" runat="server"></asp:Literal></span></div>
            </div>
            <div style="text-align:right; flex-shrink:0;">
                <a id="lnkSendMsgHeader" runat="server" href="#" class="btn-contact" style="font-size:0.9rem; padding:0.5rem 1.1rem;">
                    &#9993; Send Message
                </a>
            </div>
        </div>

        <%-- Messages Section --%>
        <div class="content-card">
            <h2 class="page-title">Inbox for Donor #<asp:Literal ID="litDonorId" runat="server"></asp:Literal></h2>
            <p class="page-subtitle">All messages received by this donor from registered users.</p>

            <%-- Message count badge --%>
            <asp:Panel ID="pnlCount" runat="server">
                <div style="display:inline-flex; align-items:center; gap:0.5rem; background:#fee2e2; color:var(--primary-color); padding:0.4rem 1rem; border-radius:20px; font-weight:600; font-size:0.88rem; margin-bottom:1.5rem;">
                    &#9993; <asp:Literal ID="litCount" runat="server"></asp:Literal>
                </div>
            </asp:Panel>

            <%-- No messages state --%>
            <asp:Panel ID="pnlEmpty" runat="server" Visible="false">
                <div style="text-align:center; padding:3rem 1rem; color:var(--muted-text);">
                    <div style="font-size:3rem; margin-bottom:1rem; opacity:0.4;">&#128235;</div>
                    <p style="font-size:1.05rem; font-weight:500;">No messages yet for this donor.</p>
                    <p style="margin-top:0.5rem; font-size:0.9rem;">Be the first to reach out!</p>
                    <a id="lnkSendMsgEmpty" runat="server" href="#" class="btn-primary" style="display:inline-block; margin-top:1.2rem;">
                        Send a Message
                    </a>
                </div>
            </asp:Panel>

            <%-- Messages list via Repeater --%>
            <asp:Panel ID="pnlMessages" runat="server" Visible="false">
                <div class="message-list">
                    <asp:Repeater ID="rptMessages" runat="server">
                        <ItemTemplate>
                            <div class="message-item">
                                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.5rem;">
                                    <div class="msg-subject">&#9993; <%# Server.HtmlEncode(Eval("Subject").ToString()) %></div>
                                    <div class="msg-meta" style="white-space:nowrap;">
                                        <%# Eval("SentAt", "{0:ddd, dd MMM yyyy}") %> &nbsp;&#183;&nbsp; <%# Eval("SentAt", "{0:HH:mm}") %>
                                    </div>
                                </div>
                                <div class="msg-body"><%# Server.HtmlEncode(Eval("Body").ToString()) %></div>
                                <div class="msg-meta" style="margin-top:0.6rem; display:flex; align-items:center; gap:0.4rem;">
                                    <span style="display:inline-flex; align-items:center; justify-content:center; width:22px; height:22px; background:var(--primary-color); color:#fff; border-radius:50%; font-size:0.7rem; font-weight:700;">
                                        <%# Eval("SenderName").ToString().Length > 0 ? Eval("SenderName").ToString()[0].ToString().ToUpper() : "U" %>
                                    </span>
                                    <span>From: <strong><%# Server.HtmlEncode(Eval("SenderName").ToString()) %></strong></span>
                                </div>
                            </div>
                        </ItemTemplate>
                    </asp:Repeater>
                </div>
            </asp:Panel>
        </div>

    </asp:Panel>

</asp:Content>
