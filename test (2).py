from kivy.lang import *
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton


KV = '''
#:import CustomOverFlowMenu __main__.CustomOverFlowMenu
<DrawerClickableItem@MDNavigationDrawerItem>
    text_color: app.theme_cls.primary_color
    icon_color: app.theme_cls.primary_color
    ripple_color: "#c5bdd2"
    selected_color: app.theme_cls.accent_color


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: app.theme_cls.primary_color
    icon_color: app.theme_cls.primary_color
    focus_behavior: False
    selected_color: app.theme_cls.accent_color
    _no_ripple_effect: True

    
<CustomTopAppBar>:
    MDTopAppBar:
        title: "Welcome to Helpdroid"
        elevation: 3
        pos_hint: {"top": 1}
        font_style: "H2"
        specific_text_color: app.theme_cls.primary_color
        md_bg_color: app.theme_cls.accent_color
        use_overflow: True
        overflow_cls: CustomOverFlowMenu()
        left_action_items: [["menu", lambda x: app.root.ids.nav_drawer.set_state("open")]]
        right_action_items:
            [
            ["home", lambda x: app.on_home_button(x), "", "Home"],
            ["logout", lambda x: app.logout(), "", "Logout"],
            ["account-edit-outline", lambda x: app.callback(x), "" , "Edit details"],
            ]
MDScreen:

    MDNavigationLayout:
        
        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "dashboard"
                CustomTopAppBar:
                MDLabel:
                    text: "Welcome Onboard"
                    halign: "center"
            MDScreen:
                name: "doctor"

                CustomTopAppBar:
                MDLabel:
                    text: "Welcome Doctor"
                    halign: "center"
            
            MDScreen:
                name: "medication"
                CustomTopAppBar:
                FloatLayout:
                    size_hint: None, None
                    size: dp(300), dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDRaisedButton:
                        text: "Upload Prescription"
                        pos_hint: {'center_x': 0, 'center_y': 0.5}
                        md_bg_color: app.theme_cls.primary_color
                        on_release: app.generateO()
                    MDRaisedButton:
                        id: button
                        text: "View Uploaded Prescription"
                        pos_hint: {"center_x": 1, "center_y": .5}
                        on_release: app.menu_open()

               
            MDScreen:
                name: "arduino"
                CustomTopAppBar:
                MDLabel:
                    text: "Welcome Arduino"
                    halign: "center"

            MDScreen:
                name: "notification"
                CustomTopAppBar:
                MDLabel:
                    text: "Welcome Notification"
                    halign: "center"    
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title: "Menu"
                    title_color: app.theme_cls.primary_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
                    
                    
                DrawerClickableItem:
                    icon: "doctor"
                    text: "Doctor"
                    on_press:
                        app.root.ids.nav_drawer.set_state("close")
                        app.root.ids.screen_manager.current = "doctor"

                DrawerClickableItem:
                    icon: "medication"
                    text: "Medical Data"
                    on_press:
                        app.root.ids.nav_drawer.set_state("close")
                        app.root.ids.screen_manager.current = "medication"

                DrawerClickableItem:
                    icon: "heart-pulse"
                    text: "Arduino"
                    on_press:
                        app.root.ids.nav_drawer.set_state("close")
                        app.root.ids.screen_manager.current = "arduino"

                DrawerClickableItem:
                    icon: "bell-ring"
                    text: "Notification"
                    on_press:
                        app.root.ids.nav_drawer.set_state("close")
                        app.root.ids.screen_manager.current = "notification"

                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "logout"
                    text: "Logout"
                    on_press : app.logout()


            
                
'''
class CustomOverFlowMenu(MDDropdownMenu):
    # In this class you can set custom properties for the overflow menu.
    pass
class CustomTopAppBar(MDScreen):
    pass


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.primary_hue = "900"
        return Builder.load_string(KV)
    
    def menu_open(self):
        menu_items = [
            {
                "text": f"Item {i}",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        MDDropdownMenu(
            caller=self.root.ids.button, items=menu_items
        ).open()

    def on_home_button(self, instance):
        self.root.ids.screen_manager.current = "dashboard"

    #def logout(self):

Example().run()





MDNavigationLayout:

        MDScreenManager:

            MDScreen:
                name: "dashboard"
                MDTopAppBar:
                    title: "Welcome to Helpdroid"
                    elevation: 3
                    pos_hint: {"top": 1}
                    font_style: "H2"
                    specific_text_color: app.theme_cls.primary_color
                    md_bg_color: app.theme_cls.accent_color
                    left_action_items: [["menu", lambda x: app.root.ids.nav_drawer.set_state("open")]]
                    right_action_items:
                        [
                        ["home", lambda x: app.on_home_button(x), "", "Home"],
                        ["logout", lambda x: app.logout(), "", "Logout"],
                        ["account-edit-outline", lambda x: app.callback(x), "" , "Edit details"],
                        ]
                
                MDLabel:
                    text: "Welcome Onboard"
                    halign: "center"
            MDScreen:
                name: "doctor"
                MDTopAppBar:
                    title: "Welcome to Helpdroid"
                    elevation: 3
                    pos_hint: {"top": 1}
                    font_style: "H2"
                    specific_text_color: app.theme_cls.primary_color
                    md_bg_color: app.theme_cls.accent_color
                    left_action_items: [["menu", lambda x: app.root.ids.nav_drawer.set_state("open")]]
                    right_action_items:
                        [
                        ["home", lambda x: app.on_home_button(x), "", "Home"],
                        ["logout", lambda x: app.logout(), "", "Logout"],
                        ["account-edit-outline", lambda x: app.callback(x), "" , "Edit details"],
                        ]
                
                MDLabel:
                    text: "Welcome Doctor"
                    halign: "center"
            MDScreen:
                name: "medication"
                MDTopAppBar:
                    title: "Welcome to Helpdroid"
                    elevation: 3
                    pos_hint: {"top": 1}
                    font_style: "H2"
                    specific_text_color: app.theme_cls.primary_color
                    md_bg_color: app.theme_cls.accent_color
                    left_action_items: [["menu", lambda x: app.root.ids.nav_drawer.set_state("open")]]
                    right_action_items:
                        [
                        ["home", lambda x: app.on_home_button(x), "", "Home"],
                        ["logout", lambda x: app.logout(), "", "Logout"],
                        ["account-edit-outline", lambda x: app.callback(x), "" , "Edit details"],
                        ]
                
                FloatLayout:
                    size_hint: None, None
                    size: dp(300), dp(250)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDRaisedButton:
                        text: "Upload Prescription"
                        pos_hint: {'center_x': 0, 'center_y': 0.5}
                        md_bg_color: app.theme_cls.primary_color
                        on_release: app.generateO()
                    MDRaisedButton:
                        id: button
                        text: "View Uploaded Prescription"
                        pos_hint: {"center_x": 1, "center_y": .5}
                        on_release: app.menu_open()
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Menu"
                    title_color: app.theme_cls.primary_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
                    
                    
                DrawerClickableItem:
                    icon: "doctor"
                    text: "Doctor"
                    on_press:
                        app.root.ids.nav_drawer.set_state("close")
                        app.root.ids.screen_manager.current = "doctor"

                DrawerClickableItem:
                    icon: "medication"
                    text: "Medical Data"
                    on_press:
                        app.root.ids.nav_drawer.set_state("close")
                        app.root.ids.screen_manager.current = "medication"

                DrawerClickableItem:
                    icon: "heart-pulse"
                    text: "Arduino"
                    on_press:
                        app.root.ids.nav_drawer.set_state("close")
                        app.root.ids.screen_manager.current = "arduino"

                DrawerClickableItem:
                    icon: "bell-ring"
                    text: "Notification"
                    on_press:
                        app.root.ids.nav_drawer.set_state("close")
                        app.root.ids.screen_manager.current = "notification"

                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "logout"
                    text: "Logout"
                    on_press : app.logout()




MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Header title"
                    title_color: "#4a4939"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon: "gmail"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Inbox"

                DrawerClickableItem:
                    icon: "send"
                    text: "Outbox"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"