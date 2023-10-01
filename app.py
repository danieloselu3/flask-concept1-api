from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(user, prompt):
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass

if __name__ == '__main__':
    app.run(debug=True)

