import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QColor, QPalette


class AchievementWidget(QWidget):
    def __init__(self, achievement):
        super().__init__()
        self.achievement = achievement

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Name label
        name_label = QLabel(self.achievement["name"])
        layout.addWidget(name_label)

        # Description label
        desc_label = QLabel(self.achievement["desc"])
        layout.addWidget(desc_label)

        # Level label
        level_label = QLabel(f"Level: {self.achievement['lvl']}")
        layout.addWidget(level_label)

        # Image
        image_label = QLabel()
        image = QPixmap(self.achievement["img"])
        image_label.setPixmap(image)
        layout.addWidget(image_label)

        # Border
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor("blue"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self, achievements, obtained_achievements, potential_achievements, progress_value_1, progress_max_1, progress_value_2, progress_max_2):
        super().__init__()

        self.setWindowTitle("Achievements")

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Achievements grid
        achievements_layout = QHBoxLayout()
        for achievement in achievements:
            achievement_widget = AchievementWidget(achievement)
            achievements_layout.addWidget(achievement_widget)
        main_layout.addLayout(achievements_layout)

        # Obtained achievements
        obtained_layout = QVBoxLayout()
        obtained_layout.addWidget(QLabel("Obtained Achievements:"))
        for achievement in obtained_achievements:
            obtained_layout.addWidget(QLabel(f"{achievement['name']}: {achievement['xp']} XP"))
        main_layout.addLayout(obtained_layout)

        # Potential achievements
        potential_layout = QVBoxLayout()
        potential_layout.addWidget(QLabel("Potential Achievements:"))
        for achievement in potential_achievements:
            potential_layout.addWidget(QLabel(f"{achievement['name']}: {achievement['xp']} XP"))
        main_layout.addLayout(potential_layout)

        # Progress bars
        progress_layout = QVBoxLayout()
        progress_bar_1 = QProgressBar()
        progress_bar_1.setValue(progress_value_1)
        progress_bar_1.setMaximum(progress_max_1)
        progress_layout.addWidget(progress_bar_1)
        progress_bar_2 = QProgressBar()
        progress_bar_2.setValue(progress_value_2)
        progress_bar_2.setMaximum(progress_max_2)
        progress_layout.addWidget(progress_bar_2)
        main_layout.addLayout(progress_layout)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Sample data
    achievements = [
        {"name": "Achievement 1", "desc": "Description 1", "lvl": 1, "txp": 100, "img": "path/to/image1.png"},
        {"name": "Achievement 2", "desc": "Description 2", "lvl": 2, "txp": 200, "img": "path/to/image2.png"},
        # Add more achievements as needed
    ]

    obtained_achievements = [
        {"name": "Achievement 1", "xp": 50},
        # Add more obtained achievements as needed
    ]

    potential_achievements = [
        {"name": "Achievement 3", "xp": 150},
        # Add more potential achievements as needed
    ]

    progress_value_1 = 50
    progress_max_1 = 100

    progress_value_2 = 75
    progress_max_2 = 150

    window = MainWindow(achievements, obtained_achievements, potential_achievements,
                        progress_value_1, progress_max_1, progress_value_2, progress_max_2)
    window.show()

    sys.exit(app.exec())