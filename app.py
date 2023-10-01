from flask import Flask, request, jsonify

app = Flask(__name__)

user_data = [
    {
        'user_id': 1,
        'user_name': 'User1',
        'prompt': 'Please provide feedback on our new product design.'
    },
    {
        'user_id': 2,
        'user_name': 'User2',
        'prompt': 'Describe your favorite travel destination.'
    },
    {
        'user_id': 3,
        'user_name': 'User3',
        'prompt': 'Share your thoughts on the latest technology trends.'
    },
    {
        'user_id': 4,
        'user_name': 'User4',
        'prompt': 'Write a short story about a detective solving a mystery.'
    },
    {
        'user_id': 5,
        'user_name': 'User5',
        'prompt': 'Discuss the impact of climate change on global ecosystems.'
    }
]


@app.route("/", methods=["GET", "POST"])
def index(user, prompt):
    if request.method == "GET":
        if user_data > 0:
            return jsonify(user_data)
        else:
            return "There's no users, for now!", 404

    if request.method == "POST":
        

if __name__ == '__main__':
    app.run(debug=True)

