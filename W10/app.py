from flask import Flask, request, render_template_string

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "pass123"

login_page = """
<h2>Dummy Login</h2>
<form method="POST">
  Username: <input name="username"><br>
  Password: <input name="password" type="password"><br>
  <input type="submit" value="Login">
</form>
<p>{{ message }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            message = "Login successful"
        else:
            message = "Invalid credentials"
    return render_template_string(login_page, message=message)

app.run(debug=True)
