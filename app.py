from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory storage)
users = [
    {'id': 1, 'name': 'John Doe'},
    {'id': 2, 'name': 'Jane Doe'}
]

# Home endpoint
@app.route('/', methods=['GET'])
def home():
    return "Welcome to our API!"

# GET endpoint to fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST endpoint to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()  # Get JSON data from the request
    new_user['id'] = len(users) + 1  # Auto-increment the user ID
    users.append(new_user)
    return jsonify(new_user), 201  # Return the new user and 201 Created status

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
  
