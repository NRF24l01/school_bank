from flet import border, Container, Column, TextAlign, Page, Text, Row, ImageFit, Image, ProgressBar, border_radius, \
    ImageRepeat, UserControl
from time import time
from loger import Logger


class App(UserControl):
    def __init__(self, loger: Logger, achivs: list, lvl_colors: list):
        """

                :param loger: my own loger class for logging
                :param achivs: list with achives
                :param lvl_colors: list with achive colors
                """
        super().__init__()
        self.logger = loger
        self.achivs = achivs
        self.lvl_colors = lvl_colors

    def build(self) -> Column:
        self.logger.info("Start render people data page")
        st = time()
        p = Row(wrap=True, expand=True)

        r = Row(wrap=True, expand=True)
        for i in self.achivs:
            height = 150
            width = height * 3
            text_size = width - (height - 25) - 50
            r.controls.append(
                Container(
                    Row(
                        [
                            Column(
                                [
                                    Image(src="static/zametki_site.png", width=(height - 5), height=(height - 5),
                                          fit=ImageFit.NONE,
                                          repeat=ImageRepeat.NO_REPEAT, border_radius=border_radius.all(25))]
                            ),
                            Column(
                                [Text(f"{i['name']}", color=self.lvl_colors[i["lvl"]]['txt'], top=True, width=text_size,
                                      size=20, text_align=TextAlign.CENTER),
                                 Text(f"{i['desc']}", color=self.lvl_colors[i["lvl"]]['txt'], top=True, width=text_size),
                                 Text(f"{i['state']}", color=self.lvl_colors[i["lvl"]]['txt'], top=True, width=text_size,
                                      text_align=TextAlign.CENTER),
                                 ProgressBar(width=text_size, value=i["progress"], color=self.lvl_colors[i["lvl"]]['clprogr'],
                                             bgcolor=self.lvl_colors[i["lvl"]]['bgprogr'])]
                            )
                        ]),
                    width=width, height=height, bgcolor=self.lvl_colors[i["lvl"]]['bg'],
                    border=border.all(2, self.lvl_colors[i["lvl"]]['border']), border_radius=10
                )
            )
            self.logger.info("Render element")

        self.logger.info(f"Render people data page time: {time() - st}")
        return r