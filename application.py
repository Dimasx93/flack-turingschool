import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def message(data):
    print("\n{data} \n")
    print(data["username"])
    print(data["msg"])
    send(data,broadcast=True)

@socketio.on("add username")
def add_username(data):
    username=""
    username= data["username"]
    print(username)
    emit("add username", {"username":username})
