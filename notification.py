from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class CalendarApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        auth_button = Button(text='Authenticate with Google')
        auth_button.bind(on_press=self.authenticate_google)
        layout.add_widget(auth_button)
        return layout

    def authenticate_google(self, instance):
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret_151690723541-2o01nir9ojvqf60vq1si0e667f09dd22.apps.googleusercontent.com.json',  # Replace with the path to your credentials file
            scopes=['https://www.googleapis.com/auth/calendar']
        )

        # Run the local server to authenticate
        flow.run_local_server(port=0)

        credentials = flow.credentials
        service = build('calendar', 'v3', credentials=credentials)
        # You can now use the 'service' object to make API calls
        print('Authentication successful!')

if __name__ == '__main__':
    CalendarApp().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class CalendarApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        auth_button = Button(text='Authenticate with Google')
        auth_button.bind(on_press=self.authenticate_google)
        layout.add_widget(auth_button)
        return layout

    def authenticate_google(self, instance):
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret_151690723541-2o01nir9ojvqf60vq1si0e667f09dd22.apps.googleusercontent.com.json',  # Replace with the path to your credentials file
            scopes=['https://www.googleapis.com/auth/calendar']
        )

        # Run the local server to authenticate
        flow.run_local_server(port=0)

        credentials = flow.credentials
        service = build('calendar', 'v3', credentials=credentials)
        # You can now use the 'service' object to make API calls
        print('Authentication successful!')

if __name__ == '__main__':
    CalendarApp().run()
