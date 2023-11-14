from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
from kivy.metrics import dp
import re
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image as KivyImage
from kivy.uix.scatter import Scatter
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.button import MDIconButton
from kivy.uix.label import Label
from kivymd.uix.floatlayout import MDFloatLayout
import json
from kivy.uix.popup import Popup
from kivy.uix.image import Image as KivyImage
from kivymd.uix.fitimage import FitImage
from PIL import Image
from kivymd.toast import toast
import os
from otp_generate import *
from connection import *
from authentication import *
from triple_des import *
from kivy.core.image import Image as CoreImage
from io import BytesIO
from knn_predict import *


Window.size = (310, 580)

class ClickableImage(ButtonBehavior, FitImage):
    pass

class CustomTopAppBar(MDScreen):
    pass
class ClickableImage(ButtonBehavior, FitImage):
    pass
class HelpDroid(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        screen_manager=ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login_pg.kv"))
        screen_manager.add_widget(Builder.load_file("loginotp_pg.kv"))
        screen_manager.add_widget(Builder.load_file("registration_pg.kv"))
        screen_manager.add_widget(Builder.load_file("forgot_pg.kv"))
        screen_manager.add_widget(Builder.load_file("welcome.kv"))
        screen_manager.add_widget(Builder.load_file("edit_details_pg.kv"))
        screen_manager.add_widget(Builder.load_file("viewmed_pg.kv"))
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.primary_hue = "900"
        return screen_manager
    
    def generateR(self):
        self.temp_otp =  generate_otp()
        email = self.root.get_screen("register").ids.Email.text
       
        send_mail(email,self.temp_otp)
    def generateF(self):
        self.temp_otp =  generate_otp()
        email = self.root.get_screen("forgot_password").ids.Email.text
       
        send_mail(email,self.temp_otp)
    def generateO(self):
        self.temp_otp =  generate_otp()
        email = self.root.get_screen("loginwithotp").ids.Email.text
       
        send_mail(email,self.temp_otp)
    
    def register(self):
        email = self.root.get_screen("register").ids.Email.text
        password = self.root.get_screen("register").ids.password.text
        name = self.root.get_screen("register").ids.Name.text
        mobile = self.root.get_screen("register").ids.MobileNo.text
        otp = self.root.get_screen("register").ids.OTP.text
        check=reg_auth(email,otp,password,name,mobile,self.temp_otp)
        if(check):
            print("signed in successful")
            self.save_session(email)
            self.root.current="welcome"
            #new page call
        else:
            self.root.get_screen("register").ids.Email.text = ''
            self.root.get_screen("register").ids.password.text = ''
            self.root.get_screen("register").ids.Name.text = ''
            self.root.get_screen("register").ids.MobileNo.text = ''
            self.root.get_screen("register").ids.OTP.text = ''
            print("signed in unsuccessful")
    def login(self):
        email = self.root.get_screen("login").ids.username.text
        password = self.root.get_screen("login").ids.password.text

        if(login_auth(email,password)):
            print("Login Successful")
            #session management
            self.save_session(email)
            self.root.get_screen("login").ids.username.text = ''
            self.root.get_screen("login").ids.password.text = ''
            self.root.current="welcome"
        else:
            print("Login declined")
    def login_with_otp(self):
        email = self.root.get_screen("loginwithotp").ids.Email.text
        otp = self.root.get_screen("loginwithotp").ids.OTP.text
        if(otp==self.temp_otp):
            
            if(loginotpcheck(email)):
                self.save_session(email)
                self.root.current="welcome"
                print("Login Successful")

            else:
                self.root.get_screen("loginwithotp").ids.Email.text = ''
                self.root.get_screen("loginwithotp").ids.OTP.text = ''
                print("Login Failed")
            #
        else:
            self.root.get_screen("loginwithotp").ids.Email.text = ''
            self.root.get_screen("loginwithotp").ids.OTP.text = ''
            print("otp wrong")
    def forgot_password(self):
        email = self.root.get_screen("forgot_password").ids.Email.text
        otp = self.root.get_screen("forgot_password").ids.OTP.text
        password = self.root.get_screen("forgot_password").ids.password.text
        if(otp==self.temp_otp):
            hash = sha256(password+""+email)    
            update(email,hash)
            self.root.current="login"
            print('Password changed')
        else:
            self.root.get_screen("forgot_password").ids.OTP.text = ''
            self.root.get_screen("forgot_password").ids.password.text = ''
            self.root.get_screen("forgot_password").ids.Email.text = ''
            print("otp wrong")
    def editdetails(self):
        self.root.current="editdetails"
        
    def logout(self):
        self.root.current="login"
        self.clear_session()
    def save_session(self, email):
        session_data = {
            'user_email': email
        }
        with open('session.json', 'w') as session_file:
            json.dump(session_data, session_file)

    def clear_session(self):
        if os.path.exists('session.json'):
            os.remove('session.json')
    def on_start(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )
        Window.bind(on_keyboard=self.events)  
        self.load_session()
    def load_session(self):
        if os.path.exists('session.json'):
            with open('session.json', 'r') as session_file:
                session_data = json.load(session_file)
                email = session_data.get('user_email')
                if email and login_auth(email, None):  # You need to modify login_auth to support session check without password
                    self.root.current = "welcome"
                else:
                    self.root.current = "login"
        

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        ) 

    def uploadmed(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True
        
    def select_path(self, path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        '''
        
        self.exit_manager()

        # Get the size of the file in kilobytes (KB)
        file_size_kb = os.path.getsize(path) / 1024

        # Check if the file size is less than or equal to 300 KB
        if file_size_kb <= 300:
            toast(f"File selected: {path}")
            
            append_encrypted_image_to_prescription(path)  # Call the encryption function

            print(f"File path: {path} (Size: {file_size_kb:.2f} KB)")
        else:
            # File is too large, notify the user
            toast("Choose a file within 300 KB")


    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return 
    flag=0
    def viewmed(self):
       
        if(self.flag==0):
            self.flag=1
            image_data = fetch_and_decrypt_prescription_images()
            my_screen = self.root.get_screen("viewmed")
            
            for data in image_data:
                my_screen.ids.swiperitems.add_widget(
                    MDSwiperItem(
                        MDCard(
                            ClickableImage(
                                source=data["path"],
                                size_hint=(1, 0.8),
                                radius=(10, 10, 0, 0),
                                on_release=lambda x, path=data["path"]: self.viewImage(path,data["subtitle"]),
                            ),
                            MDLabel(
                                text=data["subtitle"],
                                halign="center",
                                size_hint_y= None,  # add this line
                            ),
                            orientation='vertical',
                            size_hint=(0.8, 0.8),
                        )
                    )
                )
        
        self.root.current = "viewmed"

    def viewImage(self, path, subtitle):
        
        image = KivyImage(source=path, size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        popup = Popup(title=subtitle, content=image, size_hint=(1, .8))
        popup.open()

    def get_contact(self, contact):
        self.check_heath(4)
        print(contact)
        pattern = re.compile(r"^\+?[0-9]{10,15}$")
        
        if(pattern.match(contact)):
            insert_contact("user",contact)
            print("Contact number:", contact)  # You can replace this with any action you want
            toast("Contact number added successfully")
            self.root.get_screen("editdetails").ids.econtact.text = ''
        else:
            toast("Invalid contact number")
    def send_message(self,contact_info):
        phoneNumber = contact_info["phone"]
        name=contact_info["name"]
        message = "Hi "+name+" I am in serious health issue please help me"
        
        print(contact_info)
        pass
    def check_heath(self,score):
        print("Health checked")
        # score = get_score()
        print(score)
        if(score == 0):
            toast("You are healthy")
        elif(score==1):
            toast("Please take care of your health, You have mild health issues")
        elif(score == 2):
            toast("Please take care of your health, You have moderate health issues")
        else:
            contacts= fetch_contacts()
            for contact in contacts:
                self.send_message(contact)
                
        

            


if __name__ == "__main__":
    HelpDroid().run()
