from flask import Flask, flash, redirect, jsonify, request, url_for, abort
from flask import render_template


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

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

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
    app.run(debug = True)