using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Web.UI;

namespace ShareLife
{
    public partial class Search : Page
    {
        private readonly string connString = ConfigurationManager.ConnectionStrings["BloodDonorDBConnectionString"].ConnectionString;

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                lblSearchResult.Text = "Please select a blood group to search.";
            }
        }

        protected void btnSearch_Click(object sender, EventArgs e)
        {
            string selectedGroup = ddlSearchBloodGroup.SelectedValue;

            if (string.IsNullOrEmpty(selectedGroup))
            {
                lblSearchResult.Text = "Please select a valid blood group.";
                gvSearchDonors.DataSource = null;
                gvSearchDonors.DataBind();
                return;
            }

            SearchDonorsByBloodGroup(selectedGroup);
        }

        private void SearchDonorsByBloodGroup(string bloodGroup)
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(connString))
                {
                    string query = "SELECT DonorID, Name, ISNULL(Gender, 'N/A') AS Gender, Age, ISNULL(Email, 'N/A') AS Email, Mobile, City, BloodGroup, ISNULL(CAST(Weight AS VARCHAR), 'N/A') AS Weight, ISNULL(LastDonationDate, 'Never') AS LastDonationDate, ISNULL(MedicalConditions, 'None') AS MedicalConditions FROM Donor WHERE BloodGroup = @BloodGroup ORDER BY Name ASC";

                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        // Parameterized SQL query for safe filtering
                        cmd.Parameters.AddWithValue("@BloodGroup", bloodGroup);

                        using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))
                        {
                            DataTable dt = new DataTable();
                            adapter.Fill(dt);

                            gvSearchDonors.DataSource = dt;
                            gvSearchDonors.DataBind();

                            if (dt.Rows.Count > 0)
                            {
                                lblSearchResult.Text = string.Format("Found {0} registered donor(s) matching blood group '{1}':", dt.Rows.Count, bloodGroup);
                            }
                            else
                            {
                                lblSearchResult.Text = string.Format("No donors found matching blood group '{0}'.", bloodGroup);
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                lblSearchResult.Text = "Error fetching search results: " + ex.Message;
            }
        }
    }
}
