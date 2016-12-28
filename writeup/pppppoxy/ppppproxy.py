from flask import Flask
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return '{"hash":"21232F297A57A5A743894A0E4A801FC3"}', 404

if __name__ == "__main__":
    app.run(port=8000)
