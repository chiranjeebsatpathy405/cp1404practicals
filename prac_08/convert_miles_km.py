"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

# CONSTANT conversion factor
MILES_TO_KM = 1.6


class ConvertMilesKmApp(App):
    # StringProperty so the label auto-updates
    result_text = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file("convert_miles_km.kv")

    # --- core logic -------------------------------------------------
    def convert(self, miles_text: str) -> None:
        """Convert miles in the TextInput to km and update result_text."""
        miles = self._get_miles_value(miles_text)
        km = miles * MILES_TO_KM
        self.result_text = f"{km:.5f}"

    def handle_increment(self, miles_text: str, amount: int) -> None:
        """
        Increase/decrease the value of miles by 'amount'
        """
        miles = self._get_miles_value(miles_text)
        miles += amount
        # update TextInput; its on_text will call convert()
        self.root.ids.input_miles.text = str(miles)

    # --- helpers ----------------------------------------------------
    @staticmethod
    def _get_miles_value(text: str) -> float:
        try:
            return float(text)
        except (ValueError, TypeError):
            return 0.0



ConvertMilesKmApp().run()
