from flask import Flask
import threading
from tempmail import bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

def run_bot():
    bot.run()

# Start bot in background
threading.Thread(target=run_bot).start()
