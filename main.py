from flask import Flask, render_template

app = Flask(__name__)

achievements = [
    {"name": "First Achievement", "desc": "This is the description of the first achievement", "lvl": 1, "txp": 50, "img": "static/test.jpg"},
    {"name": "Second Achievement", "desc": "This is the description of the second achievement", "lvl": 2, "txp": 100, "img": "static/test.jpg"},
    {"name": "Third Achievement", "desc": "This is the description of the third achievement", "lvl": 3, "txp": 150, "img": "static/test.jpg"},
    {"name": "Fourth Achievement", "desc": "This is the description of the fourth achievement", "lvl": 4, "txp": 200, "img": "static/test.jpg"},
    {"name": "Fifth Achievement", "desc": "This is the description of the fifth achievement", "lvl": 5, "txp": 500, "img": "static/test.jpg"}
]

achieved = [
    {"name": "First Achievement", "xp": 25},
    {"name": "Second Achievement", "xp": 76},
    {"name": "Third Achievement", "xp": 124},
]

not_achieved = [
    {"name": "Fourth Achievement", "xp": 230},
    {"name": "Fifth Achievement", "xp": 280},
]

#Глобал
current_xp = 350
max_xp = 5000

#До следуещей ачивки
next_lvl_xp = 500
current_lvl_xp = 250

@app.route("/")
def index():
    return render_template("index.html", achievements=achievements, achieved=achieved, not_achieved=not_achieved,
        current_xp=current_xp, next_lvl_xp=next_lvl_xp)

if __name__ == "__main__":
    app.run(debug=True)