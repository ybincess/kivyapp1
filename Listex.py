from kivymd.app import MDApp
from kivymd.uix.list import MDList,OneLineListItem, ThreeLineListItem, ThreeLineIconListItem, ThreeLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget, IconRightWidget, ImageLeftWidget, ImageRightWidget
from kivymd.uix.screen import Screen
from kivy.uix.scrollview import ScrollView

class ListdemoApp(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)
        for i in range(10):
            # icon = IconLeftWidget(icon="android")
            img = ImageRightWidget(source='Logo.png')
            items = ThreeLineAvatarIconListItem( text ='Item' + str(i), secondary_text="2nd Text", tertiary_text="3rd text")
            items.add_widget(img)
            list_view.add_widget(items)
        screen.add_widget(scroll)

        return screen

ListdemoApp().run()