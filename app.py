from flask import Flask, flash, redirect, session ,jsonify, request, url_for, abort
from flask import render_template
from flask import make_response
# from api.github import getRepoByName
from models.validation import is_logged_in
# import config

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
def main():
    return render_template('home.jinja')

@app.route("/dashboard")
def index():
    return render_template('dashboard.jinja')

@app.route("/login", methods=['GET', 'POST'])
def login():
    stored_pass = "12345"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if(password == stored_pass):
            session['username'] = username
            flash(' You are logged successfully ! ', 'success')
            return redirect(url_for('dashboard'))  
        else:
            error = 'Invalid login! please try again ! '
            return render_template('login.jinja', error=error)
    else:
        return render_template('login.jinja')

# @app.route('/logout')
# @is_logged_in
# def logout():
#     session.clear()
#     flash('Vous etes a présent déconnecter', 'success')
#     return redirect(url_for('login'))




# API ROUTES
@app.route("/api/languages")
def languages():
    return jsonify({'languages': langs})

@app.route("/api/repos")
def repo():
    # return jsonify({'repostories': getRepoByName()})
    return jsonify({'repo'})

@app.route('/api/language/<int:language_id>')
def language(language_id):
    language = [language for language in langs if language['id'] == language_id]
    if len(language) == 0:
        abort(404)
    return jsonify({'language': language[0]})



# Run App
if __name__ == '__main__':
    app.run()