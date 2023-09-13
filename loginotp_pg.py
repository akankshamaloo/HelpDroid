from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle
from otp_generate import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle
from connection import *
from kivy.utils import platform
class LoginOTPPage(App):
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
        
        # Create "Generate OTP" text link
        generate_otp_label = Label(text='Generate OTP', color=(0, 0, 1, 1), halign='left', valign='center', size_hint=(None, None), size=(150, 20))
        generate_otp_label.bind(on_touch_down=self.generate_otp)
        layout.add_widget(generate_otp_label)

        # Create otp input field
        otp_label = Label(text='Enter the OTP:', halign='left', valign='center', size_hint=(None, None), size=(150, 30), color=(0, 0, 0, 1))
        self.otp_input = TextInput(hint_text='Enter your OTP', multiline=False, size_hint=(None, None), size=(200, 30))
        layout.add_widget(otp_label)
        layout.add_widget(self.otp_input)
        
        # Create login button (smaller size)
        login_button = Button(text='Login', size_hint=(None, None), size=(100, 40))
        layout.add_widget(login_button)

        # Add space after the login button
        layout.add_widget(Label(size_hint=(None, None), height=20))
        login_button.bind(on_release=self.on_confirm_button_click)
        

        # Add the main layout (BoxLayout) to the root layout (RelativeLayout)
        root_layout.add_widget(layout)

        return root_layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def generate_otp(self, instance, touch):
        print("hello")
        if instance.collide_point(*touch.pos):
            # When the "Generate OTP" label is clicked, open otp_generator.py
            print(platform)
            if platform == 'win':
                # Windows (or non-Android) behavior
                '''import os
                os.system('start otp.py')  # Opens the file using the default program
                try:
                    subprocess.run(["python", "otp.py"], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error running otp.py: {e}")'''
                print("on the way to sent")
                self.otp_sent=generate_otp()
                email=self.email_input.text
                send_mail(email,self.otp_sent)
                print("sent")
                
    
    def on_confirm_button_click(self, instance):
        
        if(self.otp_sent==self.otp_input.text):
            
            if(loginotpcheck(self.email_input.text)):
                print("Login Successful")
            else:
                print("Login Failed")
            #
        else:
            print("otp wrong")


if __name__ == '__main__':
    LoginOTPPage().run()