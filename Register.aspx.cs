using System;
using System.Configuration;
using System.Data.SqlClient;
using System.Web.UI;

namespace ShareLife
{
    public partial class Register : Page
    {
        private readonly string connString = ConfigurationManager.ConnectionStrings["BloodDonorDBConnectionString"].ConnectionString;

        protected void Page_Load(object sender, EventArgs e)
        {
        }

        protected void btnRegister_Click(object sender, EventArgs e)
        {
            if (!Page.IsValid)
            {
                return;
            }

            string name = txtName.Text.Trim();
            string gender = ddlGender.SelectedValue;
            int age = Convert.ToInt32(txtAge.Text.Trim());
            string email = string.IsNullOrWhiteSpace(txtEmail.Text) ? "N/A" : txtEmail.Text.Trim();
            string mobile = txtMobile.Text.Trim();
            string city = txtCity.Text.Trim();

            string bloodGroup = ddlBloodGroup.SelectedValue;
            int weight = Convert.ToInt32(txtWeight.Text.Trim());
            string lastDonationDate = string.IsNullOrWhiteSpace(txtLastDonationDate.Text) ? "Never / First Time" : txtLastDonationDate.Text.Trim();
            string medicalConditions = string.IsNullOrWhiteSpace(txtMedicalConditions.Text) ? "None" : txtMedicalConditions.Text.Trim();

            try
            {
                using (SqlConnection conn = new SqlConnection(connString))
                {
                    string query = @"INSERT INTO Donor (Name, Gender, Age, Email, Mobile, City, BloodGroup, Weight, LastDonationDate, MedicalConditions) 
                                    VALUES (@Name, @Gender, @Age, @Email, @Mobile, @City, @BloodGroup, @Weight, @LastDonationDate, @MedicalConditions)";

                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        // Parameterized SQL queries to prevent SQL Injection attacks
                        cmd.Parameters.AddWithValue("@Name", name);
                        cmd.Parameters.AddWithValue("@Gender", gender);
                        cmd.Parameters.AddWithValue("@Age", age);
                        cmd.Parameters.AddWithValue("@Email", email);
                        cmd.Parameters.AddWithValue("@Mobile", mobile);
                        cmd.Parameters.AddWithValue("@City", city);
                        cmd.Parameters.AddWithValue("@BloodGroup", bloodGroup);
                        cmd.Parameters.AddWithValue("@Weight", weight);
                        cmd.Parameters.AddWithValue("@LastDonationDate", lastDonationDate);
                        cmd.Parameters.AddWithValue("@MedicalConditions", medicalConditions);

                        conn.Open();
                        int rowsAffected = cmd.ExecuteNonQuery();

                        if (rowsAffected > 0)
                        {
                            ShowMessage("Donor registered successfully with Personal & Medical details! Thank you for volunteering to save lives.", false);
                            ClearFormFields();
                        }
                        else
                        {
                            ShowMessage("Failed to register donor. Please try again.", true);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                ShowMessage("Database Error: " + ex.Message, true);
            }
        }

        private void ClearFormFields()
        {
            txtName.Text = string.Empty;
            ddlGender.SelectedIndex = 0;
            txtAge.Text = string.Empty;
            txtEmail.Text = string.Empty;
            txtMobile.Text = string.Empty;
            txtCity.Text = string.Empty;
            ddlBloodGroup.SelectedIndex = 0;
            txtWeight.Text = string.Empty;
            txtLastDonationDate.Text = string.Empty;
            txtMedicalConditions.Text = string.Empty;
        }

        private void ShowMessage(string text, bool isError)
        {
            pnlMessage.Visible = true;
            lblMessage.Text = text;
            pnlMessage.CssClass = isError ? "alert-message alert-danger" : "alert-message alert-success";
        }
    }
}
