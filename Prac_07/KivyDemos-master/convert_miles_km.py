from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


MILE_TO_KM_CONVERSION = 1.609

class MileToKmApp(App):
    """Kivy app to convert miles to km"""""

    output_km = StringProperty()

    def build(self):
        """Initializes kivy app from kv file"""
        self.title = "Mile to Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_press(self):
        miles = self.convert_to_float(self.root.ids.mile_input.text)
        self.output_km = str(miles * MILE_TO_KM_CONVERSION)

    def convert_to_float(self, text):
        try:
            return float(text)
        except ValueError:
            return 0.0





MileToKmApp().run()