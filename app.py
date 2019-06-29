from flask import Flask, flash, redirect, jsonify, request, url_for, abort
from flask import render_template
from flask import make_response

# implementation de l'application
app = Flask(__name__)

langs = [
    {
        'id': 1,
        'title': 'JavaScript',
        'resume': "Hello World",
        'stars': 3
    },
    {
        'id': 2,
        'title': 'Python 3',
        'resume': "Hello Python",
        'stars': 3
    }
]


# error format
@app.errorhandler(404)
def not_find(error):
    return make_response(jsonify({'error': 'Element pas trouvé ✖'}), 404)

# Application routes
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/home")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')


# API ROUTES

@app.route("/api/languages")
def languages():
    return jsonify({'languages': langs})


@app.route('/api/language/<int:language_id>')
def language(language_id):
    language = [language for language in langs if language['id'] == language_id]
    if len(language) == 0:
        abort(404)
    return jsonify({'language': language[0]})



# Run App
if __name__ == '__main__':
    app.run(debug=True)