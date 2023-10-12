from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
#:import CustomOverFlowMenu _main_.CustomOverFlowMenu
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: app.theme_cls.accent_color
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


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Welcome To HelpDroid"
                    elevation: 3
                    pos_hint: {"top": 1}
                    font_style: "H2"
                    specific_text_color: app.theme_cls.primary_color
                    md_bg_color: app.theme_cls.accent_color
                    use_overflow: True
                    overflow_cls: CustomOverFlowMenu()
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items:
                        [
                        ["home", lambda x: app.callback(x), "", "Home"],
                        ["logout", lambda x: app.callback(x), "", "Logout"],
                        ["account-edit-outline", lambda x: app.callback(x), "" , "Edit details"],
                        ]

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

                DrawerClickableItem:
                    icon: "medication"
                    text: "Medicine"

                DrawerClickableItem:
                    icon: "assistant"
                    text: "Assistance"

                DrawerClickableItem:
                    icon: "bell-ring"
                    text: "Notification"

                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "logout"
                    text: "Logout"
                
'''
class CustomOverFlowMenu(MDDropdownMenu):
    # In this class you can set custom properties for the overflow menu.
    pass

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.primary_hue = "900"
        return Builder.load_string(KV)


Example().run()