import os
import flet as ft
from loger import EventLogger
from time import time, sleep
from render import render_people_data

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

glob = {"txt": "TEBE POPA TOCHNA",
        "max": 1500,
        "cur": 750,
        "bg": "",
        "bord": "",
        "txt_color": "",
        "pb_bg": "",
        "pb_cl": ""}

background = "#4D4B66"

loger = EventLogger()

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: ft.Page):
    loger.info(f"Preload time: {time() - start_time}")
    page = render_people_data(page, loger, background, achivs, lvl_colors, glob)
    page.update()



ft.app(target=main)

loger.info("Session stopped")
