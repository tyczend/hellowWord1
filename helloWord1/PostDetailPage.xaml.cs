using helloWord1.Model;
using SQLite;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace helloWord1
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class PostDetailPage : ContentPage
    {
        private Post _selectedPost;

        public PostDetailPage(Post selectedPost)
        {
            InitializeComponent();

            _selectedPost = selectedPost;

            //! Dispaly
            exprienceEntry.Text = _selectedPost.Experience;
        }

        private void UpdateButton_Clicked(object sender, EventArgs e)
        {
            _selectedPost.Experience = exprienceEntry.Text;

            using (SQLiteConnection conn = new SQLiteConnection(App.DatabaseLocaltion))
            {
                conn.CreateTable<Post>();
                int rows = conn.Update(_selectedPost);

                if (rows > 0)
                {
                    DisplayAlert("Success", "Experience succesfully updated", "Ok");
                }
                else
                {
                    DisplayAlert("Failure", "Experience failed to be updated", "Ok");
                }
            }
        }

        private void DeleteButton_Clicked(object sender, EventArgs e)
        {
            using (SQLiteConnection conn = new SQLiteConnection(App.DatabaseLocaltion))
            {
                conn.CreateTable<Post>();
                int rows = conn.Delete(_selectedPost);

                if (rows > 0)
                {
                    DisplayAlert("Success", "Experience succesfully deleted", "Ok");
                }
                else
                {
                    DisplayAlert("Failure", "Experience failed to be deleted", "Ok");
                }
            }
        }
    }
}