from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
from kivy.metrics import dp
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



Window.size = (310, 580)

class ClickableImage(ButtonBehavior, FitImage):
    pass

class CustomTopAppBar(MDScreen):
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
        email = self.root.get_screen("registration").ids.Email.text
       
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
        email = self.root.get_screen("registration").ids.Email.text
        password = self.root.get_screen("registration").ids.password.text
        name = self.root.get_screen("registration").ids.Name.text
        mobile = self.root.get_screen("registration").ids.MobileNo.text
        otp = self.root.get_screen("registration").ids.OTP.text
        check=reg_auth(email,otp,password,name,mobile,self.temp_otp)
        if(check):
            print("signed in successful")
            exec(open("HelpDroid\test.py").read())
           # self.root.current="welcome"
            #new page call
        else:
            self.root.get_screen("registration").ids.Email.text = ''
            self.root.get_screen("registration").ids.password.text = ''
            self.root.get_screen("registration").ids.Name.text = ''
            self.root.get_screen("registration").ids.MobileNo.text = ''
            self.root.get_screen("registration").ids.OTP.text = ''
            print("signed in unsuccessful")
    def login(self):
        email = self.root.get_screen("login").ids.username.text
        password = self.root.get_screen("login").ids.password.text
        if(login_auth(email,password)):
            print("Login Successful")
            self.root.current="welcome"
        else:
            print("Login declined")
    def login_with_otp(self):
        email = self.root.get_screen("loginwithotp").ids.Email.text
        otp = self.root.get_screen("loginwithotp").ids.OTP.text
        if(otp==self.temp_otp):
            
            if(loginotpcheck(email)):
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
    def on_start(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )
        Window.bind(on_keyboard=self.events)  
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
        toast(path)
        encrypted(path)
        print(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
    # Running the app
    

    


    def viewmed(self):
        image_data = [
            {"path": "img1.jpeg", "subtitle": "Image 1"},
            {"path": "img2.jpeg", "subtitle": "Image 2"},
            {"path": "img3.jpeg", "subtitle": "Image 3 Subtitle"}
        ]

        my_screen = self.root.get_screen("viewmed")
        my_screen.ids.swiperitems.remove_widget()
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

    



if __name__ == "__main__":
    HelpDroid().run()