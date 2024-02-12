import os

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('web/index.html')

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 80)))
