from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
notes = []

PAGE = """
<!doctype html>
<html>
<head>
    <title>Notes App</title>
    <style>
        body{ font-family: Arial, san-serif; max-width: 600px; margin: 40px auto;}
        input[type=text] {width: 70%; padding: 8px;}
        button {padding: 8px 14px;}
        li {margin: 6px 0;}
        footer {maring-top: 30px; color:gray; font-size: 14px;}
    </style>
</head>
<body>
    <h1>My Notes app</h1>
    <form method="post" action="/add">
        <input type="text" name="note" placeholder="Write a note..." required>
        <button type="submit">Add</button>
    </form>
    <h3>Notes ({{ notes|length}}) </h3>
    <ul>
        {% for n in notes %}
            <li>{{ n }} <a href="/delete/{{ loop.index0 }}">[delete]</a></li>
        {% else %}
            <li> No Notes Yet.</li>
        {% endfor %}
    </ul>
    <footer> CHUA WENG KIN - 106214072 - Running in Docker </footer>
</body>
</html> 
"""

@app.route("/")
def home():
    return render_template_string(PAGE, notes=notes)

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("note", "").strip()
    if text:
        notes.append(text)
    return redirect("/")

@app.route("/delete/<int:i>")
def delete(i):
    if 0 <= i <len(notes):
        notes.pop(i)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

