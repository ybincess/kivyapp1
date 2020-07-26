from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

screen_helper= """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton: 
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'Profile'
    MDRectangleFlatButton: 
        text: 'Upload'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_press: root.manager.current = 'Upload'
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
    MDLabel:
        text: 'Please upload your pictures'
        halign: 'center'
    MDRectangleFlatButton: 
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'menu'

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


class ScreenerApp(MDApp):
    def build(sel):
        screen = Builder.load_string(screen_helper)
        return screen


ScreenerApp().run()