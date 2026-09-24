using System;
using System.IO;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ShareLife
{
    public partial class SiteMaster : MasterPage
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                SetActiveNavLink();
                UpdateAuthPanel();
            }
        }

        private void SetActiveNavLink()
        {
            string currentPage = Path.GetFileName(Request.Url.AbsolutePath).ToLower();

            if (currentPage == "default.aspx" || currentPage == "")
                navHome.Attributes["class"] = "active";
            else if (currentPage == "register.aspx")
                navRegister.Attributes["class"] = "active";
            else if (currentPage == "search.aspx")
                navSearch.Attributes["class"] = "active";
            else if (currentPage == "viewdonors.aspx")
                navView.Attributes["class"] = "active";
            else if (currentPage == "about.aspx")
                navAbout.Attributes["class"] = "active";
        }

        private void UpdateAuthPanel()
        {
            // Check if user is logged in via Session
            if (Session["UserID"] != null)
            {
                pnlLoggedIn.Visible = true;
                pnlLoggedOut.Visible = false;
                litUsername.Text = Session["FullName"] != null ? Session["FullName"].ToString() : "User";
            }
            else
            {
                pnlLoggedIn.Visible = false;
                pnlLoggedOut.Visible = true;
            }
        }

        protected void btnLogout_Click(object sender, EventArgs e)
        {
            // Clear all session data and redirect to home
            Session.Clear();
            Session.Abandon();
            Response.Redirect("~/Default.aspx");
        }
    }
}
