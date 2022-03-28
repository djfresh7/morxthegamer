from flask import Flask
from threading import Thread

app = Flask("DJ-Fresh's Bot")

@app.route("/")
def home():
  with open("alive.html", "r") as h:
    return h.read()

def run():
  app.run(host="0.0.0.0", port=8000)

def alive():
  server = Thread(target=run)
  server.start()