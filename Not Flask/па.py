import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line

kivy.require('1.11.1')


class Separator(Widget):
    def __init__(self, color, **kwargs):
        super(Separator, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 2
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*color)  # Set the separator color here
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class BorderedBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(BorderedBoxLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set the border color here
            self.border = Line(width=2, rectangle=(self.x, self.y, self.width, self.height))

        self.bind(pos=self.update_border, size=self.update_border)

    def update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)


class MyInterface(BoxLayout):
    def __init__(self, elements, **kwargs):
        super(MyInterface, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10

        for element in elements:
            box = BorderedBoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=200)
            box.bind(minimum_height=box.setter('height'))
            self.add_widget(box)

            img_label = Label(text="Image: " + element["img"], size_hint=(None, 1), width=100)
            box.add_widget(img_label)

            element_box = BoxLayout(orientation='vertical', spacing=5)
            box.add_widget(element_box)

            title_label = Label(text="Title: " + element["title"], size_hint=(1, None), height=30)
            element_box.add_widget(title_label)

            desc_label = Label(text="Description: " + element["desc"], size_hint=(1, None), height=30)
            element_box.add_widget(desc_label)

            lvl_label = Label(text="Level: " + str(element["lvl"]), size_hint=(1, None), height=30)
            element_box.add_widget(lvl_label)

            progress = ProgressBar(max=element["max"], value=element["tek"], size_hint=(1, None), height=30)
            element_box.add_widget(progress)

            separator = Separator(color=(1, 1, 1, 1))
            box.add_widget(separator)


class MyApp(App):
    def build(self):
        # Пример списка элементов
        elements = [
            {
                "img": "path/to/image1.png",
                "title": "Элемент 1",
                "desc": "Описание элемента 1",
                "lvl": 1,
                "tek": 50,
                "max": 100
            },
            {
                "img": "path/to/image2.png",
                "title": "Элемент 2",
                "desc": "Описание элемента 2",
                "lvl": 2,
                "tek": 75,
                "max": 150
            },
            {
                "img": "path/to/image3.png",
                "title": "Элемент 3",
                "desc": "Описание элемента 3",
                "lvl": 3,
                "tek": 120,
                "max": 200
            }
        ]

        return MyInterface(elements)


if __name__ == '__main__':
    MyApp().run()
