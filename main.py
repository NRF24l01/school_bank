from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    achievements = [
        {'name': 'Achievement 1', 'desc': 'Description of achievement 1', 'level': 2, 'tonext': 100},
        {'name': 'Achievement 2', 'desc': 'Description of achievement 2', 'level': 3, 'tonext': 200},
        {'name': 'Achievement 3', 'desc': 'Description of achievement 3', 'level': 1, 'tonext': 50},
    ]
    goals = [
        {'name': 'Goal 1', 'xp': 50},
        {'name': 'Goal 2', 'xp': 100},
        {'name': 'Goal 3', 'xp': 150},
        {'name': 'Goal 4', 'xp': 200},
    ]
    current_xp = 120
    max_xp = 250
    return render_template('indexo.html', achievements=achievements, goals=goals, current_xp=current_xp, max_xp=max_xp)

if __name__ == '__main__':
    app.run(debug=True)