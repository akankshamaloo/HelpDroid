from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle
from connection import *
from sha256 import *
class ForgotPasswordPage(App):
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
        self.email_input = TextInput(hint_text='Enter your email', multiline=False, size_hint=(None, None), size=(200, 30))
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)

        # Create email input field
        password_label = Label(text='New Password:', halign='left', valign='center', size_hint=(None, None), size=(150, 30), color=(0, 0, 0, 1))
        self.password_input = TextInput(hint_text='Enter new password', multiline=False, size_hint=(None, None), size=(200, 30))
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)

        # Create password input field
        new_label = Label(text='Confirm Password:', halign='left', valign='center', size_hint=(None, None), size=(150, 30), color=(0, 0, 0, 1))
        self.new_input = TextInput(hint_text='Confirm password', password=True, multiline=False, size_hint=(None, None), size=(200, 30))
        layout.add_widget(new_label)
        layout.add_widget(self.new_input)

        # Create login button (smaller size)
        login_button = Button(text='Confirm', size_hint=(None, None), size=(100, 40))
        layout.add_widget(login_button)

        # Add space after the login button
        layout.add_widget(Label(size_hint=(None, None), height=20))

        # Bind an event handler to the login button
        login_button.bind(on_release=self.on_forgot_button_click)

        # Add the main layout (BoxLayout) to the root layout (RelativeLayout)
        root_layout.add_widget(layout)

        return root_layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def on_forgot_button_click(self, instance):
        #
        if(self.new_input.text == self.password_input.text):
            hash = sha256(self.password_input.text+""+self.email_input.text)    
            update(self.email_input.text,hash,)
            print('Password changed')
        else:
            print('Password does not match')
            self.new_input=''
            self.password_input=''

if __name__ == '__main__':
    ForgotPasswordPage().run()