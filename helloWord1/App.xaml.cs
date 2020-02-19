using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace helloWord1
{
    public partial class App : Application
    {
        public static string DatabaseLocaltion = string.Empty;
        public App()
        {
            InitializeComponent();

            MainPage = new NavigationPage(new MainPage());
        }

        public App(string databaseLocaltion)
        {
            InitializeComponent();

            MainPage = new NavigationPage(new MainPage());

            DatabaseLocaltion = databaseLocaltion;
        }

        protected override void OnStart()
        {
        }

        protected override void OnSleep()
        {
        }

        protected override void OnResume()
        {
        }
    }
}
