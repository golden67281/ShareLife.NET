using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Web.UI;

namespace ShareLife
{
    public partial class DonorMessages : Page
    {
        private readonly string connString = ConfigurationManager.ConnectionStrings["BloodDonorDBConnectionString"].ConnectionString;

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                int donorId;
                if (!int.TryParse(Request.QueryString["id"], out donorId) || donorId <= 0)
                {
                    pnlNotFound.Visible = true;
                    pnlMain.Visible = false;
                    return;
                }

                LoadDonorProfile(donorId);
            }
        }

        private void LoadDonorProfile(int donorId)
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(connString))
                {
                    conn.Open();

                    // 1. Load donor info
                    string donorQuery = "SELECT DonorID, Name, Age, BloodGroup, Mobile, City FROM Donor WHERE DonorID = @DonorID";
                    using (SqlCommand cmd = new SqlCommand(donorQuery, conn))
                    {
                        cmd.Parameters.AddWithValue("@DonorID", donorId);
                        SqlDataReader reader = cmd.ExecuteReader();

                        if (!reader.Read())
                        {
                            pnlNotFound.Visible = true;
                            pnlMain.Visible = false;
                            return;
                        }

                        // Populate donor profile card literals
                        string name = reader["Name"].ToString();
                        litInitial.Text = name.Length > 0 ? name[0].ToString().ToUpper() : "D";
                        litName.Text = Server.HtmlEncode(name);
                        litAge.Text = reader["Age"].ToString();
                        litBloodGroup.Text = reader["BloodGroup"].ToString();
                        litMobile.Text = reader["Mobile"].ToString();
                        litCity.Text = Server.HtmlEncode(reader["City"].ToString());
                        litDonorId.Text = donorId.ToString();

                        lnkSendMsgHeader.HRef = "ContactDonor.aspx?id=" + donorId;
                        lnkSendMsgEmpty.HRef = "ContactDonor.aspx?id=" + donorId;

                        reader.Close();
                    }

                    // 2. Load all messages sent to this donor, joining with Users to get sender name
                    string msgQuery = @"
                        SELECT 
                            m.MessageID,
                            m.Subject,
                            m.Body,
                            m.SentAt,
                            u.FullName AS SenderName,
                            u.Email    AS SenderEmail
                        FROM Messages m
                        INNER JOIN Users u ON m.SenderUserID = u.UserID
                        WHERE m.DonorID = @DonorID
                        ORDER BY m.SentAt DESC";

                    using (SqlCommand cmd2 = new SqlCommand(msgQuery, conn))
                    {
                        cmd2.Parameters.AddWithValue("@DonorID", donorId);

                        using (SqlDataAdapter adapter = new SqlDataAdapter(cmd2))
                        {
                            DataTable dt = new DataTable();
                            adapter.Fill(dt);

                            pnlMain.Visible = true;

                            if (dt.Rows.Count == 0)
                            {
                                // No messages yet
                                litCount.Text = "0 messages received";
                                pnlEmpty.Visible = true;
                                pnlMessages.Visible = false;
                            }
                            else
                            {
                                string msgWord = dt.Rows.Count == 1 ? "message" : "messages";
                                litCount.Text = string.Format("{0} {1} received", dt.Rows.Count, msgWord);

                                rptMessages.DataSource = dt;
                                rptMessages.DataBind();

                                pnlMessages.Visible = true;
                                pnlEmpty.Visible = false;
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                pnlMain.Visible = true;
                litCount.Text = "Error: " + ex.Message;
            }
        }
    }
}
