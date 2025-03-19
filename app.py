from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Projet d'automatisation de la roue de la fortune !</h1>"

@app.route('/check')
def about():
    return "<h1>Verifier les logs du bots (WIP)</h1>"

@app.route('/aucasou')
def contact():
    return "<h1>Page de au cas ou</h1>"


if __name__ == "__main__":
    app.run(debug=True)
