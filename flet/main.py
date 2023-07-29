import os
import flet as ft
from loger import Logger
from time import time, sleep
from app import App
from time import time

start_time = time()

achivs = [{"name": "Рамка для A4", "img": "as.png", "desc": "Рамочка медная для листа A6", "lvl": 0, "progress": 0.1,
           "state": "10xp : 100xp"},
          {"name": "Фигурка Пегаса", "img": "as.png",
           "desc": "Пегас алюминиевого цвета с герба школы в 3D у вас на столе)", "lvl": 1, "progress": None,
           "state": "Ожидает получения"},
          {"name": "Грамота А4", "img": "as.png", "desc": "Грамота A3", "lvl": 2, "progress": 0.45,
           "state": "90xp : 200xp"},
          {"name": "Ручка гелевая", "img": "as.png", "desc": "Ручка золотая чёрная 0.5", "lvl": 3, "progress": 0.99,
           "state": "396xp : 400xp"},
          {"name": "Блокнот A5", "img": "as.png", "desc": "Блокнот A5 с секретным посланием", "lvl": 4,
           "progress": 0.79, "state": "395xp : 500xp"}]

# https://color.adobe.com/ru/create/color-wheel
lvl_colors = [{"bg": "#312D66", "txt": "#B1ADEA", "border": "#6E65E6", "clprogr": "#554FB3", "bgprogr": "#4D4B66"},
              {"bg": "#80715E", "txt": "#CCB497", "border": "#956F41", "clprogr": "#D1A56F", "bgprogr": "#4D4439"},
              {"bg": "#805E6C", "txt": "#CC97AD", "border": "#954164", "clprogr": "#C94F82", "bgprogr": "#4D3941"},
              {"bg": "#5E807B", "txt": "#97CCC4", "border": "#419588", "clprogr": "#4FC9B6", "bgprogr": "#394D4A"},
              {"bg": "#71805E", "txt": "#B4CC97", "border": "#6F9541", "clprogr": "#A9DD68", "bgprogr": "#444D39"}]

background = "#4D4B66"

loger = Logger(f"log/{time()}.log")

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def start(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()
    loger.info(f"Preload time: {time() - start_time}")
    app = App(loger, achivs, lvl_colors)
    content = app.build()
    print(content)
    page.add(content)
    page.update()



ft.app(target=start)

loger.info("Session stopped")
