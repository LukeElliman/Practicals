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

    def handle_increment(self, text, increment):
        """method to increment by -1 or +1 with up and down"""
        miles = self.convert_to_float(text) + increment
        self.root.ids.mile_input.text = str(miles)
        self.convert_mile_to_km()

    def convert_mile_to_km(self):
        """method to convert miles to km"""
        miles = self.convert_to_float(self.root.ids.mile_input.text)
        self.output_km = str(miles * MILE_TO_KM_CONVERSION)

    def convert_to_float(self, text):
        """method to convert the text input in float"""
        try:
            return float(text)
        except ValueError:
            return 0.0





MileToKmApp().run()