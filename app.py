from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
DATA_FILE = "/data/tasks.txt"
BG_COLOR = os.getenv("APP_COLOR", "white")

@app.route('/')
def index():
    tasks = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            tasks = f.readlines()
    
    return render_template_string("""
        <body style="background-color: {{color}};">
            <h1>My Tasks</h1>
            <ul>
                {% for task in tasks %}<li>{{ task }}</li>{% endfor %}
            </ul>
            <form action="/add" method="post">
                <input type="text" name="task">
                <button type="submit">Add Task</button>
            </form>
        </body>
    """, color=BG_COLOR, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get("task")
    with open(DATA_FILE, "a") as f:
        f.write(task + "\\n")
    return "<script>window.location.href='/';</script>"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)