import os
import time

from kivy import platform
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy_garden.xcamera import XCamera

from test import LoadDialog

if platform == "android":
    from android.permissions import Permission, request_permissions


    def callback(permission, results):
        if all([res for res in results]):
            print("got all permissions xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        else:
            print("Error in Permissions xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE,
                         Permission.MANAGE_DOCUMENTS], callback)


class MainScreen(Screen):

    def capture(self):
        camera = self.ids["camera"]
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

    # Change Picturre in UploadScreen
    def selected_img_upload(self, filename):
        try:
            self.ids.input_img.source = filename[0]
            print("deploy to UploadScreen Worked")
        except:
            pass


class CameraScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class UploadScreen(Screen):
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load File", content=content, size_hint=(0.95, 0.95))
        self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def selected_file(self, filename):
        try:
            self.ids.dialog_prev.source = filename[0]
            print(filename[0])
        except:
            pass

    def img_send_to_main(self, filename):
        MainScreen.selected_img_upload(MainScreen, filename[0])
        print("Filename:")
        print(filename[0])
        self.cancel()


class mainApp(MDApp):
    def build(self):
        # Theme
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Red"

        # ScreenManager
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(MainScreen(name="main_screen"))
        self.sm.add_widget(CameraScreen(name="camera_screen"))
        self.sm.add_widget(HomeScreen(name="home_screen"))
        self.sm.add_widget(UploadScreen(name="upload_screen"))
        return self.sm

    def change_screen(self, screen):
        self.sm.current = screen

    def picture_taken(self):
        print("Foto wurde gemacht")
    # Get Pic for upload screen


mainApp().run()
