using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Web.UI;

namespace ShareLife
{
    public partial class ViewDonors : Page
    {
        private readonly string connString = ConfigurationManager.ConnectionStrings["BloodDonorDBConnectionString"].ConnectionString;

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                LoadAllDonors();
            }
        }

        private void LoadAllDonors()
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(connString))
                {
                    string query = "SELECT DonorID, Name, ISNULL(Gender, 'N/A') AS Gender, Age, ISNULL(Email, 'N/A') AS Email, Mobile, City, BloodGroup, ISNULL(CAST(Weight AS VARCHAR), 'N/A') AS Weight, ISNULL(LastDonationDate, 'Never') AS LastDonationDate, ISNULL(MedicalConditions, 'None') AS MedicalConditions FROM Donor ORDER BY DonorID ASC";

                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))
                        {
                            DataTable dt = new DataTable();
                            adapter.Fill(dt);

                            gvAllDonors.DataSource = dt;
                            gvAllDonors.DataBind();

                            lblStatus.Text = string.Format("Total Donors Registered: {0}", dt.Rows.Count);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                lblStatus.Text = "Error loading donors: " + ex.Message;
            }
        }
    }
}
