from flask import Flask
from flask_script import Manager
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
from flask_bootstrap import Bootstrap


print("start")

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    if request.cookies.get("name"):
        username = request.cookies.get("name")
        name = username

    if name == "Derek23":
        return redirect("http://www.derek23.ru/")
    
    response = make_response(render_template("user.html", name = name))
    response.set_cookie("name", name)
   
    return response 

@app.route("/nordic")
def nordic():
    return render_template("nordic.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

app.errorhandler(500)
def internet_server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)

print("Finish")
