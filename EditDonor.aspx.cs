using System;
using System.Configuration;
using System.Data.SqlClient;
using System.Web.UI;

namespace ShareLife
{
    public partial class EditDonor : Page
    {
        private readonly string connString = ConfigurationManager.ConnectionStrings["BloodDonorDBConnectionString"].ConnectionString;

        protected void Page_Load(object sender, EventArgs e)
        {
            // Step 1: Authorization check - User must be logged in to edit donor details
            if (Session["UserID"] == null)
            {
                pnlNotLoggedIn.Visible = true;
                pnlEditForm.Visible = false;
                pnlNotFound.Visible = false;
                return;
            }

            if (!IsPostBack)
            {
                int donorId = 0;
                if (int.TryParse(Request.QueryString["id"], out donorId) && donorId > 0)
                {
                    LoadDonorData(donorId);
                }
                else
                {
                    ShowNotFound();
                }
            }
        }

        private void LoadDonorData(int id)
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(connString))
                {
                    string query = @"SELECT DonorID, Name, Gender, Age, Email, Mobile, City, BloodGroup, Weight, LastDonationDate, MedicalConditions 
                                     FROM Donor WHERE DonorID = @DonorID";

                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        cmd.Parameters.AddWithValue("@DonorID", id);
                        conn.Open();

                        using (SqlDataReader reader = cmd.ExecuteReader())
                        {
                            if (reader.Read())
                            {
                                hfDonorID.Value = reader["DonorID"].ToString();
                                litDonorIDHeader.Text = reader["DonorID"].ToString();

                                txtName.Text = reader["Name"].ToString();
                                string gender = reader["Gender"] != DBNull.Value ? reader["Gender"].ToString() : "";
                                if (ddlGender.Items.FindByValue(gender) != null)
                                {
                                    ddlGender.SelectedValue = gender;
                                }

                                txtAge.Text = reader["Age"].ToString();
                                txtEmail.Text = reader["Email"] != DBNull.Value && reader["Email"].ToString() != "N/A" ? reader["Email"].ToString() : "";
                                txtMobile.Text = reader["Mobile"].ToString();
                                txtCity.Text = reader["City"].ToString();

                                string bloodGroup = reader["BloodGroup"].ToString();
                                if (ddlBloodGroup.Items.FindByValue(bloodGroup) != null)
                                {
                                    ddlBloodGroup.SelectedValue = bloodGroup;
                                }

                                txtWeight.Text = reader["Weight"] != DBNull.Value ? reader["Weight"].ToString() : "";

                                string lastDate = reader["LastDonationDate"] != DBNull.Value ? reader["LastDonationDate"].ToString() : "";
                                if (lastDate != "Never" && lastDate != "Never / First Time")
                                {
                                    txtLastDonationDate.Text = lastDate;
                                }

                                txtMedicalConditions.Text = reader["MedicalConditions"] != DBNull.Value && reader["MedicalConditions"].ToString() != "None" ? reader["MedicalConditions"].ToString() : "";

                                pnlEditForm.Visible = true;
                                pnlNotFound.Visible = false;
                            }
                            else
                            {
                                ShowNotFound();
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                ShowMessage("Error loading donor details: " + ex.Message, true);
            }
        }

        protected void btnUpdate_Click(object sender, EventArgs e)
        {
            if (Session["UserID"] == null)
            {
                pnlNotLoggedIn.Visible = true;
                pnlEditForm.Visible = false;
                return;
            }

            if (!Page.IsValid) return;

            int donorId = 0;
            if (!int.TryParse(hfDonorID.Value, out donorId) || donorId <= 0)
            {
                ShowMessage("Invalid donor ID.", true);
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
                    string query = @"UPDATE Donor SET 
                                     Name = @Name, 
                                     Gender = @Gender, 
                                     Age = @Age, 
                                     Email = @Email, 
                                     Mobile = @Mobile, 
                                     City = @City, 
                                     BloodGroup = @BloodGroup, 
                                     Weight = @Weight, 
                                     LastDonationDate = @LastDonationDate, 
                                     MedicalConditions = @MedicalConditions 
                                     WHERE DonorID = @DonorID";

                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
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
                        cmd.Parameters.AddWithValue("@DonorID", donorId);

                        conn.Open();
                        int rows = cmd.ExecuteNonQuery();

                        if (rows > 0)
                        {
                            ShowMessage("Donor details updated successfully! <a href='ViewDonors.aspx' style='color:var(--success-color); font-weight:bold; text-decoration:underline;'>View Directory</a>", false);
                        }
                        else
                        {
                            ShowMessage("Failed to update donor details. Please try again.", true);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                ShowMessage("Database Error: " + ex.Message, true);
            }
        }

        private void ShowNotFound()
        {
            pnlEditForm.Visible = false;
            pnlNotFound.Visible = true;
        }

        private void ShowMessage(string text, bool isError)
        {
            pnlMessage.Visible = true;
            lblMessage.Text = text;
            pnlMessage.CssClass = isError ? "alert-message alert-danger" : "alert-message alert-success";
        }
    }
}
