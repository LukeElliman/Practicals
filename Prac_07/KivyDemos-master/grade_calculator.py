from kivy.app import App
from kivy.lang import Builder


class GradeCalculator(App):
    """App to calculate persons grades"""
    def build(self):
        self.title = "Grade Calculator"
        self.root = Builder.load_file('grade_calculator.kv')
        return self.root

    def handle_calculate(self):
        """Displays output box as grade"""
        number_grade = self.convert_to_float(self.root.ids.input_grade.text)
        if type(number_grade) == float and 0 <= number_grade <= 100:
            if 85 <= number_grade <= 100:
                self.root.ids.output_grade.text = "HD"
            elif 75 <= number_grade <= 84:
                self.root.ids.output_grade.text = "D"
            elif 65 <= number_grade <= 74:
                self.root.ids.output_grade.text = "C"
            elif 50 <= number_grade <= 64:
                self.root.ids.output_grade.text = "P"
            else:
                self.root.ids.output_grade.text = "N"
        else:
            self.root.ids.output_grade.text = "Grade must be between 0 and 100"

    def handle_clear(self):
        """Clear the input and output box"""
        self.root.ids.output_grade.text = "Enter your grade"
        self.root.ids.input_grade.text = ""

    def convert_to_float(self, text):
        """Convert text input in float"""
        try:
            return float(text)
        except ValueError:
            return None


GradeCalculator().run()