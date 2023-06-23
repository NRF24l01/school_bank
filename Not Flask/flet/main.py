import os
import flet as ft
import logging

achivs = [{"name": "blalala", "img": "as.png", "desc": "10eerwky! ыагывпаывпаываыав", "lvl": 0}]

#https://color.adobe.com/ru/create/color-wheel
lvl_colors = [{"bg":"#753926", "txt":"#FFB69E", "border":"#E88D48"}]


os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: ft.Page):
    r = ft.Row(wrap=True, scroll="always", expand=True)
    page.add(r)

    for i in achivs:
        logging.log(1, "рендер")
        r.controls.append(
            ft.Container(
                ft.Text(f"{i['name']}", color=lvl_colors[i["lvl"]]['txt'],top=True),
                width=100,
                height=100,
                bgcolor=lvl_colors[i["lvl"]]['bg'],
                border=ft.border.all(2, lvl_colors[i["lvl"]]['border']),
                border_radius=ft.border_radius.all(5),
            )
        )
    page.update()


ft.app(target=main)
