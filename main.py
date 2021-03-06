from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.taptargetview import MDTapTargetView

KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "ContrastParentBackground"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        text_color: root.text_color

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "70dp", "70dp"
            source: "data/logo/Kaimak_logo_w.png"

    MDLabel:
        text: "Fast Management"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "kaimak_production@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



MDScreen: 
    
    MDBoxLayout:
        id:box
        orientation: "vertical"
    
    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

    MDFloatingActionButton:
        id: button
        icon: "plus"
        pos_hint: {"right":0.99, "top":0.111}
        on_release: app.tap_target_start()
'''


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Kaimak_Management(MDApp):
    title = "Kaimak Management"

    def build(self):
        screen = Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
            widget=screen.ids.button,
            title_text="Create New Projects",
            description_text="???????????????? ?????????? ????????????",
            widget_position="right_bottom",
        )
        screen.ids.box.add_widget(
                MDLabel(
                    text="??????????????????????",
                    halign="center",
                    theme_text_color="Secondary",
                )
            )
        return screen

    def on_start(self):
        icons_item = {
            "folder": "Projects",
            "account-multiple": "My Task",
            "star": "About Us",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()


Kaimak_Management().run()