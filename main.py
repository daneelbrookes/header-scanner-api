from flask import Flask

app = Flask(__name__)

def main():
    
    from api import api

    app.register_blueprint(api, url_prefix='/api')

    app.run('0.0.0.0', 5000, debug=True)

if __name__ == "__main__":
    main()