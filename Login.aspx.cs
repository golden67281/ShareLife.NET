using System;
using System.Configuration;
using System.Data.SqlClient;
using System.Security.Cryptography;
using System.Text;
using System.Web.UI;

namespace ShareLife
{
    public partial class Login : Page
    {
        private readonly string connString = ConfigurationManager.ConnectionStrings["BloodDonorDBConnectionString"].ConnectionString;

        protected void Page_Load(object sender, EventArgs e)
        {
            // If already logged in, redirect to Home
            if (!IsPostBack && Session["UserID"] != null)
            {
                Response.Redirect("~/Default.aspx");
            }
        }

        protected void btnLogin_Click(object sender, EventArgs e)
        {
            if (!Page.IsValid) return;

            string email = txtEmail.Text.Trim().ToLower();
            string password = txtPassword.Text.Trim();
            string hashedPassword = HashPassword(password);

            try
            {
                using (SqlConnection conn = new SqlConnection(connString))
                {
                    string query = "SELECT UserID, FullName, Email FROM Users WHERE Email = @Email AND PasswordHash = @PasswordHash";

                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        // Parameterized query to prevent SQL injection
                        cmd.Parameters.AddWithValue("@Email", email);
                        cmd.Parameters.AddWithValue("@PasswordHash", hashedPassword);

                        conn.Open();
                        SqlDataReader reader = cmd.ExecuteReader();

                        if (reader.Read())
                        {
                            // Store user info in Session
                            Session["UserID"] = reader["UserID"].ToString();
                            Session["FullName"] = reader["FullName"].ToString();
                            Session["Email"] = reader["Email"].ToString();

                            Response.Redirect("~/Default.aspx");
                        }
                        else
                        {
                            ShowError("Invalid email or password. Please try again.");
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                ShowError("An error occurred: " + ex.Message);
            }
        }

        private void ShowError(string message)
        {
            pnlError.Visible = true;
            lblError.Text = message;
        }

        /// <summary>
        /// Hashes the password using SHA-256 for secure storage and comparison.
        /// </summary>
        public static string HashPassword(string password)
        {
            using (SHA256 sha256 = SHA256.Create())
            {
                byte[] bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
                StringBuilder sb = new StringBuilder();
                foreach (byte b in bytes)
                    sb.Append(b.ToString("x2"));
                return sb.ToString();
            }
        }
    }
}
