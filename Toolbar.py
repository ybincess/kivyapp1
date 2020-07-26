from kivymd.app import MDApp
from kivy.lang import Builder


helper_screen ="""
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Toolbar Demo'
            left_action_items: [['menu',lambda x: app.navigation_draw()]]
            right_action_items: [['clock',lambda x: app.navigation_draw()]]
            elevation: 10

        MDLabel:
            text: 'Hello Tools'
            halign: 'center'

        MDBottomAppBar:
            MDToolbar:
                title: 'Help'
                left_action_items: [['coffee',lambda x: app.navigation_draw()]]
                right_action_items: [['clock',lambda x: app.navigation_draw()]]
                mode: 'end'
                icon: 'language-python'
                on_action_button: app.navigation_draw()
                elevation: 8

"""

class ToolbarApp(MDApp):
    def build(self):
        screen = Builder.load_string(helper_screen)
        return screen
    def navigation_draw(self):
        print('Navigation')
ToolbarApp().run()
