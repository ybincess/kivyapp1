from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList, ThreeLineAvatarIconListItem, ThreeLineIconListItem, ThreeLineListItem, OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import username_helper

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette ="Green"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style='Dark'
        screen = Screen()
        # button_flat = MDRectangleFlatButton(text='Hello World', 
        # pos_hint={"center_x": 0.5, "center_y": 0.5})
        # icon_btn = MDIconButton(icon = 'android',
        #         pos_hint={"center_x": 0.5, "center_y": 0.5})
        # icon_btn = MDFloatingActionButton(icon = 'android',
        #         pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_login = MDRectangleFlatButton(text='Login', 
                pos_hint={"center_x": 0.5, "center_y": 0.4},
                on_release = self.show_data)

        # username = MDTextField(text = "Enter username",
        #         pos_hint={"center_x": 0.5, "center_y": 0.5},
        #         size_hint_x=None,width=300)

       
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(btn_login)
        return screen
    def show_data(self,obj):
        if self.username.text is "":
            check_string = "Please enter a username"
        else:
            check_string = self.username.text + 'does not exist'
        close_btn = MDRectangleFlatButton(text='Close', on_release=self.close_dlgbox)
        more_btn = MDRectangleFlatButton(text='More')

        self.showdialog = MDDialog(title = 'Username Check', text = check_string,
        size_hint = (0.5,1),
        buttons=[close_btn, more_btn])
        self.showdialog.open()     
    def close_dlgbox(self,obj):
        self.showdialog.dismiss()

DemoApp().run()