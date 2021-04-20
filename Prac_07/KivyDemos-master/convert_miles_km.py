from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MileToKmApp(App):
    """Kivy app to convert miles to km"""""
    def build(self):
        """Initializes kivy app from kv file"""
        Window.size = (400, 400)
        self.title = "Mile to Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


MileToKmApp().run()