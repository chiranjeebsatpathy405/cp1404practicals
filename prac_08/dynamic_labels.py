"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Lindsay Ward, first version: 11/07/2016
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that dynamically creates one Label per name."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # dictionary similar to dynamic_widgets demo
        self.people = {
            "Alice": "Friend",
            "Bob": "Colleague",
            "Charlie": "Neighbour",
            "Dora": "Cousin",
            "Eve": "Classmate",
        }

    def build(self):
        self.title = "Dynamic Labels"
        root = Builder.load_file("dynamic_labels.kv")

        # Create a Label for each name and add it to the BoxLayout with id "main"
        for name in self.people.keys():
            label = Label(text=name, font_size=40)
            root.ids.main.add_widget(label)

        return root


DynamicLabelsApp().run()
