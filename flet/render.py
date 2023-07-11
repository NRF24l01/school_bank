import flet as ft
from time import time


def render_people_data(page: ft.Page, loger, background: str, achivs: list, lvl_colors: list, glob: dict) -> ft.Page:
    """

    :param page: flet page
    :param loger: my own loger class for logging
    :param background: color of background
    :param achivs: list with achives
    :param lvl_colors: list with achive colors
    :param glob: down progressbar data
    """
    loger.info("Start render people data page")
    st = time()
    page.bgcolor = background

    r = ft.Row(wrap=True, expand=True)
    page.add(r)
    for i in achivs:
        height = 150
        width = height * 3
        text_size = width - (height - 25) - 50
        r.controls.append(
            ft.Container(
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Image(src="static/zametki_site.png", width=(height - 5), height=(height - 5),
                                         fit=ft.ImageFit.NONE,
                                         repeat=ft.ImageRepeat.NO_REPEAT, border_radius=ft.border_radius.all(25))]
                        ),
                        ft.Column(
                            [ft.Text(f"{i['name']}", color=lvl_colors[i["lvl"]]['txt'], top=True, width=text_size,
                                     size=20, text_align=ft.TextAlign.CENTER),
                             ft.Text(f"{i['desc']}", color=lvl_colors[i["lvl"]]['txt'], top=True, width=text_size),
                             ft.Text(f"{i['state']}", color=lvl_colors[i["lvl"]]['txt'], top=True, width=text_size,
                                     text_align=ft.TextAlign.CENTER),
                             ft.ProgressBar(width=text_size, value=i["progress"], color=lvl_colors[i["lvl"]]['clprogr'],
                                            bgcolor=lvl_colors[i["lvl"]]['bgprogr'])]
                        )
                    ]),
                width=width, height=height, bgcolor=lvl_colors[i["lvl"]]['bg'],
                border=ft.border.all(2, lvl_colors[i["lvl"]]['border']), border_radius=10
            )
        )
        loger.info("Render element")

    try:
        progress = ft.Container(
            ft.Row(
                [
                    ft.Column(
                        [ft.Text(f"{glob['txt']}", color=glob["txt_color"], top=True),
                         ft.ProgressBar(width=1000, value=glob["max"]/glob["cur"], color=glob['pb_cl'],
                                        bgcolor=glob['pb_bg'])
                         ]
                    )
                ]
            ),
            bgcolor=glob['bg'], border=ft.border.all(2, glob['bord']), border_radius=10, height=200
        )
        page.add(progress)
        loger.info("Render progress")
    except Exception as e:
        loger.error(f"Render progress error, {e}")

    loger.info(f"Render people data page time: {time() - st}")
    return page
