from flask import Flask, jsonify

app = Flask(__name__)

movies = ["Inception", "Interstellar", "The Matrix"]

@app.route('/recommendations', methods=['GET'])
def recommend_movies():
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)
