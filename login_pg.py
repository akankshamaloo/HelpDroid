from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle

class LoginPage(App):
    def build(self):
        # Create the root layout as a RelativeLayout
        root_layout = RelativeLayout()

        # Create the main layout (BoxLayout)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40, size_hint=(None, None), pos_hint={'x': 0, 'y': 0.5})

        # Set the background color to white for the entire screen (RelativeLayout)
        with root_layout.canvas.before:
            Color(1, 1, 1, 1)  # White color (RGBA)
            self.rect = Rectangle(pos=root_layout.pos, size=root_layout.size)

        # Bind the size and pos properties of the root layout to update the background size and position
        root_layout.bind(size=self._update_rect, pos=self._update_rect)

        # Create email input field
        email_label = Label(text='Email:', halign='left', valign='center', size_hint=(None, None), size=(150, 30), color=(0, 0, 0, 1))
        email_input = TextInput(hint_text='Enter your email', multiline=False, size_hint=(None, None), size=(200, 30))
        layout.add_widget(email_label)
        layout.add_widget(email_input)

        # Create password input field
        password_label = Label(text='Password:', halign='left', valign='center', size_hint=(None, None), size=(150, 30), color=(0, 0, 0, 1))
        password_input = TextInput(hint_text='Enter your password', password=True, multiline=False, size_hint=(None, None), size=(200, 30))
        layout.add_widget(password_label)
        layout.add_widget(password_input)

        # Create login button (smaller size)
        login_button = Button(text='Login', size_hint=(None, None), size=(100, 40))
        layout.add_widget(login_button)

        # Add space after the login button
        layout.add_widget(Label(size_hint=(None, None), height=20))

        # Create a grid layout for "Forgot Password" and "Login with OTP" options
        options_layout = GridLayout(cols=2, spacing=10, size_hint=(None, None), size=(300, 30))
        
        # Create "Forgot Password" text link
        forgot_password_label = Label(text='Forgot Password?', color=(0, 0, 1, 1), halign='left', valign='center', size_hint=(None, None), size=(150, 20))
        options_layout.add_widget(forgot_password_label)
        
        # Create "Login with OTP" text link
        login_with_otp_label = Label(text='Login with OTP', color=(0, 0, 1, 1), halign='left', valign='center', size_hint=(None, None), size=(150, 20))
        options_layout.add_widget(login_with_otp_label)

        layout.add_widget(options_layout)

        # Add the main layout (BoxLayout) to the root layout (RelativeLayout)
        root_layout.add_widget(layout)

        return root_layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    LoginPage().run()
