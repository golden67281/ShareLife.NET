using System;
using System.Configuration;
using System.Data.SqlClient;
using System.Web.UI;

namespace ShareLife
{
    public partial class SignUp : Page
    {
        private readonly string connString = ConfigurationManager.ConnectionStrings["BloodDonorDBConnectionString"].ConnectionString;

        protected void Page_Load(object sender, EventArgs e)
        {
            // Redirect already-logged-in users
            if (!IsPostBack && Session["UserID"] != null)
            {
                Response.Redirect("~/Default.aspx");
            }
        }

        protected void btnSignUp_Click(object sender, EventArgs e)
        {
            if (!Page.IsValid) return;

            string fullName = txtFullName.Text.Trim();
            string email = txtEmail.Text.Trim().ToLower();
            string password = txtPassword.Text.Trim();

            // Hash password using SHA-256 (same method as Login page)
            string hashedPassword = Login.HashPassword(password);

            try
            {
                using (SqlConnection conn = new SqlConnection(connString))
                {
                    conn.Open();

                    // Check if email is already registered
                    string checkQuery = "SELECT COUNT(*) FROM Users WHERE Email = @Email";
                    using (SqlCommand checkCmd = new SqlCommand(checkQuery, conn))
                    {
                        checkCmd.Parameters.AddWithValue("@Email", email);
                        int count = (int)checkCmd.ExecuteScalar();

                        if (count > 0)
                        {
                            ShowMessage("This email address is already registered. Please <a href='Login.aspx'>login here</a>.", true);
                            return;
                        }
                    }

                    // Insert new user
                    string insertQuery = "INSERT INTO Users (FullName, Email, PasswordHash) VALUES (@FullName, @Email, @PasswordHash)";
                    using (SqlCommand insertCmd = new SqlCommand(insertQuery, conn))
                    {
                        insertCmd.Parameters.AddWithValue("@FullName", fullName);
                        insertCmd.Parameters.AddWithValue("@Email", email);
                        insertCmd.Parameters.AddWithValue("@PasswordHash", hashedPassword);

                        int rows = insertCmd.ExecuteNonQuery();

                        if (rows > 0)
                        {
                            // Automatically log in the new user
                            string idQuery = "SELECT UserID FROM Users WHERE Email = @Email";
                            using (SqlCommand idCmd = new SqlCommand(idQuery, conn))
                            {
                                idCmd.Parameters.AddWithValue("@Email", email);
                                object newUserId = idCmd.ExecuteScalar();

                                Session["UserID"] = newUserId.ToString();
                                Session["FullName"] = fullName;
                                Session["Email"] = email;
                            }
                            Response.Redirect("~/Default.aspx");
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                ShowMessage("Registration error: " + ex.Message, true);
            }
        }

        private void ShowMessage(string message, bool isError)
        {
            pnlMessage.Visible = true;
            lblMessage.Text = message;
            pnlMessage.CssClass = isError ? "validation-summary" : "alert-message alert-success";
        }
    }
}
