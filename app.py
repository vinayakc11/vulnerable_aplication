from flask import Flask, request
import os

app = Flask(__name__)

SECRET_KEY = "ABCDEF12345"

@app.route("/")
def home():
    return "Bug Application running"

@app.route("/exec")
def exec_cmd():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()  

@app.route("/xss")
def xss():
    q = request.args.get("q")
    return f"You entered: {q}"

if __name__ == "__main__":
    app.run(debug=True)