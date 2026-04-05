from flask import Flask
import threading
from tempmail import bot  # Pyrogram client

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

def start_bot():
    bot.run()

# Start bot in separate thread
threading.Thread(target=start_bot).start()
