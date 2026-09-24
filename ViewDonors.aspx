<%@ Page Title="View All Donors" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="ViewDonors.aspx.cs" Inherits="ShareLife.ViewDonors" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <div class="content-card">
        <h2 class="page-title">Registered Donors Directory</h2>
        <p class="page-subtitle">Complete list of all registered blood donors in the system.</p>

        <asp:Label ID="lblStatus" runat="server" Font-Bold="true" ForeColor="#1f2937" Style="display:block; margin-bottom: 1rem;"></asp:Label>

        <div class="table-responsive">
            <asp:GridView ID="gvAllDonors" runat="server" AutoGenerateColumns="False" 
                CssClass="custom-gridview" GridLines="None" EmptyDataText="No donor records found in the database.">
                <Columns>
                    <asp:BoundField DataField="DonorID" HeaderText="ID" />
                    <asp:BoundField DataField="Name" HeaderText="Donor Name" />
                    <asp:BoundField DataField="Gender" HeaderText="Gender" />
                    <asp:BoundField DataField="Age" HeaderText="Age" />
                    <asp:TemplateField HeaderText="Blood Group">
                        <ItemTemplate>
                            <span class="blood-badge"><%# Eval("BloodGroup") %></span>
                        </ItemTemplate>
                    </asp:TemplateField>
                    <asp:BoundField DataField="Weight" HeaderText="Weight (kg)" />
                    <asp:BoundField DataField="LastDonationDate" HeaderText="Last Donation" />
                    <asp:BoundField DataField="MedicalConditions" HeaderText="Medical Status" />
                    <asp:BoundField DataField="Mobile" HeaderText="Mobile Number" />
                    <asp:BoundField DataField="City" HeaderText="City" />
                    <asp:TemplateField HeaderText="Actions">
                        <ItemTemplate>
                            <div style="display:flex; gap:0.4rem; flex-wrap:nowrap;">
                                <a href='EditDonor.aspx?id=<%# Eval("DonorID") %>' class="btn-edit">&#9998; Edit</a>
                                <a href='ContactDonor.aspx?id=<%# Eval("DonorID") %>' class="btn-contact">&#9993; Contact</a>
                                <a href='DonorMessages.aspx?id=<%# Eval("DonorID") %>' class="btn-inbox">&#128235; Inbox</a>
                            </div>
                        </ItemTemplate>
                    </asp:TemplateField>


                </Columns>
            </asp:GridView>
        </div>
    </div>
</asp:Content>
