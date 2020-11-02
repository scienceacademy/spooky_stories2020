from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = ["Walk the dog", "Do the dishes", "Finish homework"]

@app.route("/")
def index():
    return render_template("tasks.html", title="My Tasks", todos=todos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html", title="Add a task")
    else:
        task = request.form.get("task")
        if task != "":
            todos.append(task)
        return redirect("/")