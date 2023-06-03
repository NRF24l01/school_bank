from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    available_awards = [
        { 'name': 'Награда 1', 'desc': 'Описание награды 1', 'img': 'путь_к_изображению_1' },
        { 'name': 'Награда 2', 'desc': 'Описание награды 2', 'img': 'путь_к_изображению_2' },
        # Добавьте остальные награды в соответствии с вашими данными
    ]

    received_awards = [
        { 'name': 'Награда 3', 'desc': 'Описание награды 3', 'img': 'путь_к_изображению_3' },
        { 'name': 'Награда 4', 'desc': 'Описание награды 4', 'img': 'путь_к_изображению_4' },
        # Добавьте остальные награды в соответствии с вашими данными
    ]

    progress_bars = [
        { 'name': 'Прогресс 1', 'desc': 'Описание прогресса 1', 'max': 100, 'cur': 75 },
        { 'name': 'Прогресс 2', 'desc': 'Описание прогресса 2', 'max': 200, 'cur': 150 },
        # Добавьте остальные прогресс-бары в соответствии с вашими данными
    ]

    unclaimed_awards = [
        { 'name': 'Награда 5', 'desc': 'Описание награды 5' },
        { 'name': 'Награда 6', 'desc': 'Описание награды 6' },
        # Добавьте остальные награды, которые не получены
    ]

    return render_template('index.html', available_awards=available_awards, received_awards=received_awards, progress_bars=progress_bars, unclaimed_awards=unclaimed_awards)

if __name__ == '__main__':
    app.run()
