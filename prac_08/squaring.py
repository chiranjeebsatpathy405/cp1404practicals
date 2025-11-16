"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    result_text = StringProperty("0.0")

    def build(self):
        self.title = "Square Number 2"
        return Builder.load_file("squaring.kv")

    def handle_square(self, text):
        """Square the number typed by the user."""
        try:
            value = float(text)
            self.result_text = str(value * value)
        except ValueError:
            self.result_text = "0.0"


SquareNumberApp().run()

