from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgets(App):
    def __init__(self):
        super().__init__()
        self.names = ["Alice", "Bob", "Claus"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            print(name)
            temp_label = Label(text=name)
            self.root.ids.name_labels.add_widget(temp_label)


DynamicWidgets().run()
