from flask import Flask
import threading
import os
from tempmail import bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

def start_bot():
    print("Bot Started ✅")
    bot.run()

# 👇 bot हमेशा background में start होगा
threading.Thread(target=start_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
