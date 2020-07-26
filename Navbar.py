from kivymd.app import MDApp
from kivy.lang import Builder


helper_nav ="""
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:  
                        title: 'Toolbar Demo'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 5
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image: 
                    source: 'Logo.png'
                MDLabel: 
                    text: ' Sujeet Singh'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel: 
                    text: '  Sujeet.Singh@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget: 
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-profile'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'                                
"""

class ToolbarApp(MDApp):
    def build(self):
        screen = Builder.load_string(helper_nav)
        return screen


ToolbarApp().run()
