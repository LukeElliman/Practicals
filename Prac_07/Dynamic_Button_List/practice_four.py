from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from Prac_07.Dynamic_Button_List.people import People


class DynamicNameButtons(App):
    status_text = StringProperty()
    """Create a list of buttons from a csv"""
    def __init__(self):
        super().__init__()
        in_file = open("practice_four_names.csv", 'r')
        self.list_of_names = create_list_of_lists(in_file)
        in_file.close()

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Buttons"
        self.root = Builder.load_file('practice_four.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Creates buttons based of csv"""
        for person_name in self.list_of_names:
            temp_button = Button(text=person_name.name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.name_button.add_widget(temp_button)

    def press_entry(self, instance):
        """Change label when button pressed"""
        name = instance.text
        for person in self.list_of_names:
            if person.name == name:
                self.status_text = "{}'s age is {}".format(name, person.age)




def create_list_of_lists(in_file):
    """Convert csv into a list of lists"""
    list_of_strings = in_file.readlines()  # List containing each row as one value
    list_of_lists = []  # List containing each row as a list of values
    for number, line in enumerate(list_of_strings):
        line_info_split_up = line.strip().split(",")
        name = line_info_split_up[0]
        age = line_info_split_up[1]
        person_to_add = People(name, age)
        list_of_lists.append(person_to_add)
    return list_of_lists


DynamicNameButtons().run()