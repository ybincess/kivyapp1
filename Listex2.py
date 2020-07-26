from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem, OneLineIconListItem
helper_list = """
Screen:
    ScrollView:
        MDList:
            id: container
"""


class ListexApp(MDApp):
    def build(self):
        screen = Builder.load_string(helper_list)
        return screen
    def on_start(self):
        for i in range(20):
            items = OneLineListItem(text='Item'+ str(i))
            self.root.ids.container.add_widget(items)


ListexApp().run()