from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "APP FOR PYTHON and FLASK"

if __name__ == '__main__':
    app.run()