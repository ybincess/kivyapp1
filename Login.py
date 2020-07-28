from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import requests, json
from  kivy.network.urlrequest import UrlRequest
from authdata import url, headers
screen_helper= """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name: 'menu'
    MDCard:
        size_hint: None, None
        size: "280dp", "180dp"
        orientation: 'vertical'
        padding: "8dp"
        spacing: "8dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        MDLabel:
            text: "Please Login"
            theme_text_color: "Secondary"
            size_hint_y: None
            bold: True
            height: self.texture_size[1]
        MDSeparator: 
            height: "1dp"

        MDTextFieldRound:
            id: username
            hint_text: "Username "
            helper_text_mode: "on_focus"
            size_hint_y: None
            size_hint_x: 0.6
            pos_hint: {"center_x": .5, "center_y": .5}

        MDTextFieldRound:
            id: password
            hint_text: "Password "
            helper_text_mode: "on_focus"
            password: True  
            size_hint_y: None
            size_hint_x: 0.6
            pos_hint: {"center_x": .5, "center_y": .5}
        MDSeparator: 
            height: "1dp"
        MDRoundFlatButton: 
            text: 'Submit'
            md_bg_color: 0, 0, 1, 1
            bold: True
            on_press: app.pressed1(username.text, password.text)
            pos_hint: {"center_x": .5, "center_y": .5}

<ProfileScreen>:
    name: 'Profile'
    MDLabel:
        text: 'Welcome Sujeet'
        halign: 'center'
    MDRectangleFlatButton: 
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'


<UploadScreen>:
    name: 'Upload'

"""
class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class UploadScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='Profile'))
sm.add_widget(UploadScreen(name='Upload'))


class LoginApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def authenticate_user(username, password):
        r=requests.get("http://www.google.com")
        print(r)

    def pressed1(self, logintext, pwdtext):
        url = 'https://reqres.in/api/login'
        myobj = {
            "emal": logintext,
            "password": pwdtext
        }
        myobj1 ={}
        myobj1['email'] =logintext
        myobj1['password'] = pwdtext
        json.dumps(myobj1)
        x = requests.post(url, data = myobj1)
        print(x.text)
        print(x.status_code)
        if (x.status_code == 200):  
            self.root.current="Profile"
LoginApp().run()
