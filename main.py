from kivy.config import Config
Config.set('graphics', 'width', '310')
Config.set('graphics', 'height', '580')
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
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
from kivymd.uix.button import MDFlatButton
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
from prediction import *
from otp_generate import *
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDTimePicker
from kivy.clock import Clock
from kivy.utils import platform
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import IconRightWidget
from kivymd.uix.list import IconLeftWidget
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from sms import *
from location import *
Window.size = (310, 580)



class ClickableImage(ButtonBehavior, FitImage):
    pass
class CustomTopAppBar(MDScreen):
    pass
class ClickableImage(ButtonBehavior, FitImage):
    pass

class MyCompleteListener:
    def onComplete(self, task):
        if task.isSuccessful():
            token = task.getResult()
            print("Device Token:", token)
        else:
            print("Failed to get token")

class HelpDroid(MDApp):
    
    def build(self):
        if os.path.exists("session.json"):
            send_notification()
            self.bind_global_events()
            self.reset_inactivity_timer()
            
            
        # FirebaseMessaging = autoclass('com.google.firebase.messaging.FirebaseMessaging')
        # FirebaseMessaging.getInstance().getToken().addOnCompleteListener(MyCompleteListener())
      
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        screen_manager=ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login_pg.kv"))
        screen_manager.add_widget(Builder.load_file("loginotp_pg.kv"))
        screen_manager.add_widget(Builder.load_file("registration_pg.kv"))
        screen_manager.add_widget(Builder.load_file("forgot_pg.kv"))
        screen_manager.add_widget(Builder.load_file("welcome.kv"))
        screen_manager.add_widget(Builder.load_file("welcomeD.kv"))
        screen_manager.add_widget(Builder.load_file("notification.kv"))
        screen_manager.add_widget(Builder.load_file("viewmed_pg.kv"))
        screen_manager.add_widget(Builder.load_file("editcontacts.kv"))
        screen_manager.add_widget(Builder.load_file("editmed.kv")) 
        screen_manager.add_widget(Builder.load_file("deletemed.kv"))
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
        email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")   
        password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        mobile_pattern = re.compile(r'^[6789]\d{9}$')

        if(not email_pattern.match(email)):
            toast("Invalid email")
        elif(not password_pattern.match(password)):
            toast("Password should have at least 8 characters, one uppercase letter, one lowercase letter, one number, and one special character")
        elif(not name):
            toast("Please enter name")
        elif(not mobile_pattern.match(mobile)):
            toast("Invalid mobile number")
        else:
            check=reg_auth(email,otp,password,name,mobile,self.temp_otp,self.role)
            if(check):
                print("signed in successful")
                self.save_session(email)
                self.root.get_screen("register").ids.Email.text = ''
                self.root.get_screen("register").ids.password.text = ''
                self.root.get_screen("register").ids.Name.text = ''
                self.root.get_screen("register").ids.MobileNo.text = ''
                self.root.get_screen("register").ids.OTP.text = ''
                if(self.role):
                    self.root.current="welcomeD"
                else:
                    self.root.current="welcome"
            else:
                self.root.get_screen("register").ids.OTP.text = ''
                print("signed in unsuccessful")
    role= False
    def checkdoctor(self, switch_instance):
        if switch_instance.active:
            self.role = True
            print('The checkbox is active')
        else:
            self.role=False
            print('The checkbox is inactive')

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
                self.root.get_screen("loginwithotp").ids.Email.text = ''
                self.root.get_screen("loginwithotp").ids.OTP.text = ''
                self.root.current="welcome"
                print("Login Successful")

            else:
                self.root.get_screen("loginwithotp").ids.Email.text = ''
                self.root.get_screen("loginwithotp").ids.OTP.text = ''
                print("Login Failed")
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
            self.root.get_screen("forgot_password").ids.OTP.text = ''
            self.root.get_screen("forgot_password").ids.password.text = ''
            self.root.get_screen("forgot_password").ids.Email.text = ''
            self.root.current="login"
            print('Password changed')
        else:
            self.root.get_screen("forgot_password").ids.OTP.text = ''
            self.root.get_screen("forgot_password").ids.password.text = ''
            self.root.get_screen("forgot_password").ids.Email.text = ''
            print("otp wrong")

    def notification(self):
        self.root.transition.direction="left"
        self.root.current="notification"

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()
        #print(time_dialog.hour, time_dialog.minute)
        
    def get_time(self, instance, time):
        '''
        The method returns the set time.
        :type instance: <kivymd.uix.picker.MDTimePicker object>
        :type time: <class 'datetime.time'>
        '''
        formatted_hour = str(time.hour).zfill(2)
        formatted_minute = str(time.minute).zfill(2)
        formatted_time = f"{formatted_hour}:{formatted_minute}"

        self.root.get_screen("editmed").ids.time_label.text = formatted_time
        return time

    def logout(self):
        self.root.current="login"
        self.clear_session()
        self.cancel_inactivity_timer()
        self.unbind_global_events()

    def cancel_inactivity_timer(self):
        if self.inactivity_timer is not None:
            self.inactivity_timer.cancel()
        self.inactivity_timer = None

    def logoutAgain(self, instance):
        print("Logging out.")
        instance.parent.parent.dismiss()
        self.logout()

    def save_session(self, email):
        session_data ={
            'user_email': email
        }
        self.bind_global_events()
        self.reset_inactivity_timer()

        with open('session.json', 'w') as session_file:
            json.dump(session_data, session_file)

    def clear_session(self):
        if os.path.exists('session.json'):
            os.remove('session.json')


    def refresh_data_from_mongodb(self, dt):
        # TODO: Fetch new data from MongoDB and update your UI components
        # This is a placeholder function. You need to implement the actual data fetching
        # and updating logic based on your application's requirements.
        pass
    
    def on_start(self):
        Clock.schedule_interval(self.refresh_data_from_mongodb, 10)
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
        self.inactivity_timer = None
        self.timeout_duration =300
       
    

    def emergency(self):        
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(
                text="Emergency button pressed\nInformed your contacts",
                buttons=[
                    MDFlatButton(
                        text="OKAY",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss(),
                    ),
                ],
            )
        self.dialog.open()
        details= user_details()
        for contact in details.get("contacts", []):
            response=get_location('223.191.62.144')
            message="Your closed one have severe health issues please check .\nUser Details:\n Name:"+(details.get("name"))+"\n Mobile "+(details.get("mobile"))+"\n Email:"+(details.get("email"))+ "\nLocation: "+"\nCountry: "+response.get("country_name")+"\nState: "+response.get("region")+"\nCity: "+response.get("city")+"\nLatitude: "+str(response.get("latitude"))+"\nLongitude: "+str(response.get("longitude"))    
            if contact.get("email"):
                #print(contact.get("email"))
                #print(message)
                send_mail(contact.get("email"),message,"Emergency from HelpDroid")
                toast("Please take care of your health, You have severe health issues, Informed your contacts")
            if contact.get("mobile"):
                #send_sms(contact.get("mobile"),message)
                toast("Please take care of your health, You have severe health issues, Informed your contacts")

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
        self.root.transition.direction="left"
        self.root.current = "viewmed"

    def viewImage(self, path, subtitle):       
        image = KivyImage(source=path, size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        popup = Popup(title=subtitle, content=image, size_hint=(1, .8))
        popup.open()

    def get_contact(self,name,contact,phn):
        #print(name,contact)
        email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")  
        mobile_pattern = re.compile(r'^[6789]\d{9}$')     
        print(contact,phn) 
        if(email_pattern.match(contact)) :
            if(mobile_pattern.match(phn)):
                if(insert_contact(name,contact,phn)):
                    #print("Contact number:", contact)  # You can replace this with any action you want
                    toast("Contact  added successfully")
                    self.root.get_screen("editcontacts").ids.econtact.text = ''
                else:
                    print("Error occured while inserting")
            else:
                toast("Invalid mobile number")
        else:
            toast("Invalid email ")
    dialog = None
    def check_heath(self):
        print("Health checked")
        txt=""
        score,p = get_score()
        print(score)
        if(score == 0):
            toast("You are healthy")
            txt="Condition: Normal"            
        elif(score==1):
            toast("Please take care of your health, You have mild health issues")
            txt="Condition: Mild"
        elif(score == 2):
            toast("Please take care of your health, You have moderate health issues")
            txt="Condition: Moderate"
        else:
            txt="Condition: Severe"
            details= user_details()
            for contact in details.get("contacts", []):
                response=get_location('223.191.62.144')
                message="Your closed one have severe health issues please check .\nUser Details:\n Name:"+(details.get("name"))+"\n Mobile "+(details.get("mobile"))+"\n Email:"+(details.get("email"))+ "\nLocation: "+"\nCountry: "+response.get("country_name")+"\nState: "+response.get("region")+"\nCity: "+response.get("city")+"\nLatitude: "+str(response.get("latitude"))+"\nLongitude: "+str(response.get("longitude"))    
                if contact.get("email"):
                    #print(contact.get("email"))                    
                    #print(message)
                    send_mail(contact.get("email"),message,"Emergency from HelpDroid")
                    toast("Please take care of your health, You have severe health issues, Informed your contacts")
                if contact.get("mobile"):
                    #send_sms(contact.get("mobile"),message)
                    toast("Please take care of your health, You have severe health issues, Informed your contacts") 
        txt = txt + "\nPulse: "+str(p[0])+"\nOxygen Level: "+str(p[1])

        #print(txt)
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(
                text=txt,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss(),
                    ),
                ],
            )
        self.dialog.open()

    def get_medication(self, med_name):
        med_time = self.root.get_screen("editmed").ids.time_label.text
        #print(med_name,med_time)
        if(insert_medication(med_name,med_time)):
            print("Medication inserted successfully")
            toast("Medication added successfully")
            self.root.get_screen("editmed").ids.medname.text = ''
            self.root.get_screen("editmed").ids.time_label.text = ''

    def remove_item(self, instance):
        my_screen = self.root.get_screen("deletemed")
        my_screen.ids.md_list.remove_widget(instance.parent.parent)
        print(instance.parent.parent.text)
        print(instance.parent.parent.secondary_text)
        if(delete_medication(instance.parent.parent.text,instance.parent.parent.secondary_text)):
            toast("Medication deleted successfully")
        else:
            toast("Error occured while deleting")

    def delete_med(self):
        medications = get_medications_details()
        my_screen = self.root.get_screen("deletemed")
        my_screen.ids.md_list.clear_widgets()
        for med in medications:
            item = TwoLineAvatarIconListItem(
                IconRightWidget(
                    on_release=self.remove_item,
                    icon="trash-can"
                ),
                IconLeftWidget(
                    icon="medication-outline"
                ),
                text=f"{med['name']}",
                secondary_text=f"{med['time']}"
            )
            my_screen.ids.md_list.add_widget(item)

    def reset_inactivity_timer(self):
        if self.inactivity_timer is not None:
            self.inactivity_timer.cancel()
        self.inactivity_timer = Clock.schedule_once(self.on_timeout, self.timeout_duration)

    def on_timeout(self, *args):
        self.show_timeout_modal()

    def show_timeout_modal(self):
        self.dialog = MDDialog(
        title="Session Timeout",
        text="Please Login again to continue.",
        buttons=[
            MDFlatButton(
            text="Close",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color,
            on_release=lambda x: (self.logout(), self.dialog.dismiss()),
)         
        ],
    )
        self.dialog.open()
    def bind_global_events(self):
        Window.bind(on_motion=self.on_any_event)
        Window.bind(on_key_down=self.on_any_event)
        Window.bind(on_key_up=self.on_any_event)
        Window.bind(mouse_pos=self.on_any_event)

    def unbind_global_events(self):
        Window.unbind(on_key_down=self.on_any_event)
        Window.unbind(on_key_up=self.on_any_event)
        Window.unbind(on_motion=self.on_any_event)
        Window.unbind(mouse_pos=self.on_any_event)

    def on_any_event(self, *args):
        self.reset_inactivity_timer()
    

if __name__ == "__main__":
    HelpDroid().run()
