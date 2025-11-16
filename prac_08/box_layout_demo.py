from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

    def handle_greet(self):
        name = self.root.ids.input_name.text.strip()
        if name:
            self.root.ids.output_label.text = f"Hello, {name}!"
        else:
            self.root.ids.output_label.text = "Please enter a name."

BoxLayoutDemo().run()

