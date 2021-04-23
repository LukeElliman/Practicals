from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class GradeCalculator(App):
    output_fahrenheit = StringProperty()
    output_celsius = StringProperty()

    """App to convert f to c and c to f"""
    def build(self):
        self.title = "Temperature Calculator"
        self.root = Builder.load_file('temperature_calculator.kv')
        return self.root

    def fahrenheit_to_celsius(self):
        value = self.convert_to_float(self.root.ids.temp.text)
        fahrenheit = value * 9.0 / 5 + 32
        fahrenheit = round(fahrenheit, 2)
        self.output_fahrenheit = f"{self.root.ids.temp.text}C is {str(fahrenheit)}f"

    def celsius_to_fahrenheit(self):
        value = self.convert_to_float(self.root.ids.temp.text)
        celsius = 5 / 9 * (value - 32)
        celsius = round(celsius, 2)
        self.output_celsius = f"{self.root.ids.temp.text}f is {str(celsius)}C"

    def convert_to_float(self, text):
        try:
            return float(text)
        except:
            return 0.0

GradeCalculator().run()