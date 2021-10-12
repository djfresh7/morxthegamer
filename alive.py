from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def home():
  return "@DJ-Fresh Utilities Bot | Status: Alive"

def run():
  app.run(host="0.0.0.0", port=8000)

def alive():
  server = Thread(target=run)
  server.start()

# After you create these functions, import this file with the function (alive) into the main.py file.
# Then go to the website: uptimerobot.com & create a monitor (with the bot's site link) & host it 24/7.