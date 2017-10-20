"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import random


class SquareNumberApp(App):
    """Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root
    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call),
        output result to label widget."""
        result = value ** 2
        self.root.ids.output_label.text = str(result)
        num1 = random.random()
        num2 = random.random()
        num3 = random.random()
        num4 = random.random()
        self.root.ids.output_label.color = num1, num2, num3, num4
        print(num1, num2, num3, num4)

SquareNumberApp().run()
