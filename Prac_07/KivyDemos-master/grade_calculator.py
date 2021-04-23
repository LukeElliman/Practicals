from kivy.app import App
from kivy.lang import Builder


class GradeCalculator(App):
    def build(self):
        self.title = "Grade Calculator"
        self.root = Builder.load_file('grade_calculator.kv')
        return self.root

    def handle_clear(self):
        """Clear the input and output box"""
        self.root.ids.output_grade.text = "Enter your grade"
        self.root.ids.input_grade.text = ""


GradeCalculator().run()