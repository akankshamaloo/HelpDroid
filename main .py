from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from otp_generate import *
from connection import *
from authentication import *

KV = '''
ScreenManager:
    id: screen_manager

    LoginPage:
        name: "login"
    WelcomePage:
        name: "welcome"
    RegistrationPage:
        name: "registration"
    ForgotPasswordPage:
        name: "forgot_password"
    LoginwithOTPPage:
        name: "loginwithotp"

<LoginPage>:
    FloatLayout:
        orientation: 'vertical'

        MDLabel:
            text: "HelpDroid"
            halign: 'center'
            font_style: "H2"
            size_hint_y: None
            height: self.texture_size[1]
            theme_text_color: "Custom"
            text_color: 0.070,0.16,0.30,1
            font_name: "Assets/Nunito/static/Nunito-Bold.ttf"  
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}

        FloatLayout:
            size_hint: None, None
            size: dp(300), dp(250)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDTextField:
                id: username
                hint_text: "Username"
                helper_text: "Enter your username"
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: dp(250)
                pos_hint: {'center_x': 0.5, 'center_y': 0.7}

            MDTextField:
                id: password
                hint_text: "Password"
                password: True
                helper_text: "Enter your password"
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: dp(250)
                pos_hint: {'center_x': 0.5, 'center_y': 0.48}

            MDRectangleFlatButton:
                text: "Login"
                size_hint: None, None
                size: dp(150), dp(50)
                pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                text_color: 0.070,0.16,0.30,1
                md_bg_color: 0.74,1.12,1,1  # Background color in rgba format
                ripple_behavior: "auto"
                on_release: app.login()
            
            MDRectangleFlatButton:
                text: "Register Here!"
                size_hint: None, None
                size: dp(150), dp(50)
                pos_hint: {'center_x': 0.5, 'center_y': -0.1}
                text_color: 0.070,0.16,0.30,1
                md_bg_color: 0.74,1.12,1,1  # Background color in rgba format
                ripple_behavior: "auto"
                on_release: app.root.current = "registration"

            MDLabel:
                text: "[ref=loginwithotp]Login with OTP[/ref]"
                on_ref_press: root.manager.current = 'loginwithotp'
                theme_text_color: "Secondary"
                halign: "center"
                markup: True
                size_hint_y: None
                height: dp(48)
                pos_hint: {'center_x': 0.75, 'center_y': 0.3}
    
            MDLabel:
                text: "[ref=forgot_password]Forgot Password!![/ref]"
                on_ref_press: root.manager.current = 'forgot_password'
                theme_text_color: "Error"
                halign: "center"
                markup: True
                size_hint_y: None
                height: dp(48)
                pos_hint: {'center_x': 0.3, 'center_y': 0.3}

<RegistrationPage>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(48)
            
            MDRectangleFlatButton:
                text: "Back"
                size_hint: None, None
                size: dp(80), dp(48)
                on_release: app.go_back()

            MDLabel:
                text: "Register here!!"
                halign: 'center'
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Custom"
                text_color: 0.070,0.16,0.30,1
                font_name: "Assets/Nunito/static/Nunito-Bold.ttf"
        
        FloatLayout:
            orientation: 'vertical'

            MDLabel:
                text: "Welcome OnBoard!!!"
                halign: 'center'
                font_style: "H2"
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Custom"
                text_color: 0.070,0.16,0.30,1
                font_name: "Assets/Nunito/static/Nunito-Bold.ttf"  
                pos_hint: {'center_x': 0.5, 'center_y': 0.9}

            FloatLayout:
                size_hint: None, None
                size: dp(300), dp(250)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                MDTextField:
                    id: MobileNo
                    hint_text: "MobileNo"
                    helper_text: "MobileNo"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.8}

                MDTextField:
                    id: Name
                    hint_text: "Name"
                    helper_text: "Enter Your Name"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 1}
                
                MDTextField:
                    id: Email
                    hint_text: "Email-id"
                    helper_text: "Enter Email-id"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                MDRectangleFlatButton:
                    text: "Verify"
                    size_hint: None, None
                    size: dp(150), dp(50)
                    pos_hint: {'center_x': 1.2, 'center_y': 0.6}
                    text_color: 0.070,0.16,0.30,1
                    md_bg_color: 0.74,1.12,1,1  # Background color in rgba format
                    ripple_behavior: "auto"
                    on_release: app.generateR()
                MDTextField:
                    id: OTP
                    hint_text: "OTP"
                    password: True
                    helper_text: "Enter Email OTP"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}

                MDTextField:
                    id: password
                    hint_text: "Password"
                    password: True
                    helper_text: "Enter New password"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.2}

                MDRectangleFlatButton:
                    text: "Submit"
                    size_hint: None, None
                    size: dp(150), dp(50)
                    pos_hint: {'center_x': 0.5, 'center_y': 0}
                    text_color: 0.070,0.16,0.30,1
                    md_bg_color: 0.74,1.12,1,1  # Background color in rgba format
                    ripple_behavior: "auto"
                    on_release: app.register()

<LoginwithOTPPage>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(48)
            
            MDRectangleFlatButton:
                text: "Back"
                size_hint: None, None
                size: dp(80), dp(48)
                on_release: app.go_back()

            MDLabel:
                text: "Login with OTP"
                halign: 'center'
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Custom"
                text_color: 0.070,0.16,0.30,1
                font_name: "Assets/Nunito/static/Nunito-Bold.ttf"

        FloatLayout:
            orientation: 'vertical'

            MDLabel:
                text: "Sign In"
                halign: 'center'
                font_style: "H2"
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Custom"
                text_color: 0.070,0.16,0.30,1
                font_name: "Assets/Nunito/static/Nunito-Bold.ttf"  
                pos_hint: {'center_x': 0.5, 'center_y': 0.9}

            FloatLayout:
                size_hint: None, None
                size: dp(300), dp(250)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                
                MDTextField:
                    id: Email
                    hint_text: "Email-id"
                    helper_text: "Enter Email-id"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}

                MDRectangleFlatButton:
                    text: "Verify"
                    size_hint: None, None
                    size: dp(150), dp(50)
                    pos_hint: {'center_x': 1.2, 'center_y': 0.6}
                    text_color: 0.070,0.16,0.30,1
                    md_bg_color: 0.74,1.12,1,1  # Background color in rgba format
                    ripple_behavior: "auto"
                    on_release: app.generateO()
                
                MDTextField:
                    id: OTP
                    hint_text: "OTP"
                    password: True
                    helper_text: "Enter Email OTP"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}

                MDRectangleFlatButton:
                    text: "Login"
                    size_hint: None, None
                    size: dp(150), dp(50)
                    pos_hint: {'center_x': 0.5, 'center_y': 0}
                    text_color: 0.070,0.16,0.30,1
                    md_bg_color: 0.74,1.12,1,1  # Background color in rgba format
                    ripple_behavior: "auto"
                    on_release: app.login_with_otp()

<ForgotPasswordPage>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(48)
            
            MDRectangleFlatButton:
                text: "Back"
                size_hint: None, None
                size: dp(80), dp(48)
                on_release: app.go_back()

            MDLabel:
                text: "Forgot Password!!"
                halign: 'center'
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Custom"
                text_color: 0.070,0.16,0.30,1
                font_name: "Assets/Nunito/static/Nunito-Bold.ttf"
        FloatLayout:
            orientation: 'vertical'

            MDLabel:
                text: "Verify E-mail"
                halign: 'center'
                font_style: "H2"
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Custom"
                text_color: 0.070,0.16,0.30,1
                font_name: "Assets/Nunito/static/Nunito-Bold.ttf"  
                pos_hint: {'center_x': 0.5, 'center_y': 0.9}

            FloatLayout:
                size_hint: None, None
                size: dp(300), dp(250)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                
                MDTextField:
                    id: Email
                    hint_text: "Email-id"
                    helper_text: "Enter Email-id"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}

                MDRectangleFlatButton:
                    text: "Verify"
                    size_hint: None, None
                    size: dp(150), dp(50)
                    pos_hint: {'center_x': 1.2, 'center_y': 0.6}
                    text_color: 0.070,0.16,0.30,1
                    md_bg_color: 0.74,1.12,1,1  # Background color in rgba format
                    ripple_behavior: "auto"
                    on_release: app.generateF()
                
                MDTextField:
                    id: OTP
                    hint_text: "OTP"
                    password: True
                    helper_text: "Enter Email OTP"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}

                MDTextField:
                    id: password
                    hint_text: "Password"
                    password: True
                    helper_text: "Enter New password"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.2}

                MDRectangleFlatButton:
                    text: "Submit"
                    size_hint: None, None
                    size: dp(150), dp(50)
                    pos_hint: {'center_x': 0.5, 'center_y': -0.1}
                    text_color: 0.070,0.16,0.30,1
                    md_bg_color: 0.74,1.12,1,1  # Background color in rgba format
                    ripple_behavior: "auto"
                    on_release: app.forgot_password()

<WelcomePage>:
    FloatLayout:
        orientation: 'vertical'
        
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(48)
            
            MDRectangleFlatButton:
                text: "Back"
                size_hint: None, None
                size: dp(80), dp(48)
                on_release: app.go_back()

            MDLabel:
                text: "Welcome to HelpDroid"
                halign: 'center'
                font_style: "H2"
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Custom"
                text_color: 0.070,0.16,0.30,1
                font_name: "Assets/Nunito/static/Nunito-Bold.ttf"  
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
'''

class LoginPage(MDScreen):
  pass

class RegistrationPage(MDScreen):
   pass

class ForgotPasswordPage(MDScreen):
    pass
class LoginwithOTPPage(MDScreen):
    pass
class WelcomePage(MDScreen):
    pass

class HelpDroid(MDApp):
    def build(self):
        login_page = LoginPage()
        self.registration_page = RegistrationPage()
        forgot_password_page = ForgotPasswordPage()
        login_with_otp = LoginwithOTPPage()
        welcome_page=WelcomePage()
        screen_manager = Builder.load_string(KV)
        screen_manager.add_widget(login_page)
        screen_manager.add_widget(welcome_page)
        screen_manager.add_widget(self.registration_page)
        screen_manager.add_widget(forgot_password_page)
        screen_manager.add_widget(login_with_otp)
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
    def go_back(self):
        self.root.current = "login"
        

if __name__ == "__main__":
    HelpDroid().run()
