from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.popup import Popup

Config.set('graphics', 'width',350)
Config.set('graphics', 'height',600)
Config.set('graphics', 'resizable',0)

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from plyer import sms, gps, email
from kivy.lang import Builder
from kivy_garden.mapview import MapView,MapMarker,MapMarkerPopup
from kivy.uix.camera import Camera

from kivy.properties import StringProperty,ListProperty,NumericProperty

#Builder.load_file("main.kv")
Builder.load_file("geodisplay.kv")
Builder.load_file("geomenu.kv")
Builder.load_file("geoadmin.kv")

class GeoScreenmanager(ScreenManager):

    # op te roepen Popup in de hele APP
    # call met:   self.manager.Popup_choose(alarmtype)
    # alarmtype om mee te geven: training, antwoord

    def Popup_Choose(self, alarmtype):
        self.PopupPressed = Popup(title="Warning",
                                  separator_color=[0, 1, 0, .6],
                                  content=Label(text=f"Please choose {alarmtype}", halign="center", font_size=13),
                                  size_hint=(None, None),
                                  size=(200, 100),
                                  pos_hint={"center_x": .5, "center_y": .5},
                                  background_color=[0, 0, 1, 1],
                                  auto_dismiss=True)
        self.PopupPressed.open()

class WaynApp(App):
    def build(self):
        return GeoScreenmanager()

if __name__== "__main__":
    WaynApp().run()
