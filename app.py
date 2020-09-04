import aiml
from flask import Flask,render_template,request
from Semantic_Networks import Semantics

kernel = aiml.Kernel()
files = ["bike.aiml","goodbye.aiml", "into.aiml", "udc.aiml"]
for x in files:
    kernel.learn(x)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    Semantics(userText)
    return kernel.respond(userText)

if __name__ == "__main__":
    app.run()







