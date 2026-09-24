using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ShareLife
{
    public partial class ContactDonor : Page
    {
        private readonly string connString = ConfigurationManager.ConnectionStrings["BloodDonorDBConnectionString"].ConnectionString;
        private int donorId = 0;

        protected void Page_Load(object sender, EventArgs e)
        {
            // Step 1: Must be logged in
            if (Session["UserID"] == null)
            {
                pnlNotLoggedIn.Visible = true;
                pnlContact.Visible = false;
                pnlNotFound.Visible = false;
                return;
            }

            // Step 2: Validate DonorID from query string
            if (!int.TryParse(Request.QueryString["id"], out donorId) || donorId <= 0)
            {
                pnlNotFound.Visible = true;
                pnlContact.Visible = false;
                return;
            }

            // Step 3: Load donor info on first visit
            if (!IsPostBack)
            {
                LoadDonorInfo(donorId);
                LoadMessageHistory(donorId);
            }
        }

        private void LoadDonorInfo(int id)
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(connString))
                {
                    string query = "SELECT DonorID, Name, Age, BloodGroup, City FROM Donor WHERE DonorID = @DonorID";
                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        cmd.Parameters.AddWithValue("@DonorID", id);
                        conn.Open();
                        SqlDataReader reader = cmd.ExecuteReader();

                        if (reader.Read())
                        {
                            // Populate donor profile card
                            string name = reader["Name"].ToString();
                            litDonorName.Text = name;
                            litDonorInitial.Text = name.Length > 0 ? name[0].ToString().ToUpper() : "D";
                            litDonorAge.Text = reader["Age"].ToString();
                            litDonorBloodGroup.Text = reader["BloodGroup"].ToString();
                            litDonorCity.Text = reader["City"].ToString();

                            pnlContact.Visible = true;
                            pnlNotFound.Visible = false;
                        }
                        else
                        {
                            pnlNotFound.Visible = true;
                            pnlContact.Visible = false;
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                pnlContact.Visible = true;
                ShowError("Error loading donor info: " + ex.Message);
            }
        }

        private void LoadMessageHistory(int id)
        {
            try
            {
                int userId = Convert.ToInt32(Session["UserID"]);

                using (SqlConnection conn = new SqlConnection(connString))
                {
                    string query = @"SELECT Subject, Body, SentAt 
                                     FROM Messages 
                                     WHERE SenderUserID = @UserID AND DonorID = @DonorID 
                                     ORDER BY SentAt DESC";

                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        cmd.Parameters.AddWithValue("@UserID", userId);
                        cmd.Parameters.AddWithValue("@DonorID", id);

                        using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))
                        {
                            DataTable dt = new DataTable();
                            adapter.Fill(dt);

                            if (dt.Rows.Count > 0)
                            {
                                rptMessages.DataSource = dt;
                                rptMessages.DataBind();
                                pnlHistory.Visible = true;
                            }
                        }
                    }
                }
            }
            catch
            {
                // Silently skip if message history fails to load
            }
        }

        protected void btnSend_Click(object sender, EventArgs e)
        {
            if (!Page.IsValid) return;

            // Re-parse donorId from query string on postback
            if (!int.TryParse(Request.QueryString["id"], out donorId) || donorId <= 0)
            {
                ShowError("Invalid donor. Please go back and try again.");
                return;
            }

            int userId = Convert.ToInt32(Session["UserID"]);
            string subject = txtSubject.Text.Trim();
            string body = txtMessage.Text.Trim();

            try
            {
                using (SqlConnection conn = new SqlConnection(connString))
                {
                    string query = @"INSERT INTO Messages (SenderUserID, DonorID, Subject, Body) 
                                     VALUES (@UserID, @DonorID, @Subject, @Body)";

                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        // Parameterized query to prevent SQL injection
                        cmd.Parameters.AddWithValue("@UserID", userId);
                        cmd.Parameters.AddWithValue("@DonorID", donorId);
                        cmd.Parameters.AddWithValue("@Subject", subject);
                        cmd.Parameters.AddWithValue("@Body", body);

                        conn.Open();
                        int rows = cmd.ExecuteNonQuery();

                        if (rows > 0)
                        {
                            // Clear form and show success message
                            txtSubject.Text = string.Empty;
                            txtMessage.Text = string.Empty;

                            pnlSuccess.Visible = true;
                            pnlError.Visible = false;
                            lblSuccess.Text = "Your message has been sent successfully! The donor can now view it in their inbox.";

                            // Set the "View Donor Inbox" link to go directly to this donor's messages page
                            lnkViewInbox.HRef = string.Format("DonorMessages.aspx?id={0}", donorId);

                            // Reload message history to include new message
                            LoadMessageHistory(donorId);
                        }

                    }
                }
            }
            catch (Exception ex)
            {
                ShowError("Failed to send message: " + ex.Message);
            }
        }

        private void ShowError(string message)
        {
            pnlError.Visible = true;
            lblError.Text = message;
            pnlSuccess.Visible = false;
        }
    }
}
