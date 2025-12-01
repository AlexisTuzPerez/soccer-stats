from flask import Flask
from flask_jwt_extended import JWTManager
import os


from routes.competiciones import competiciones_bp
from routes.equipos import equipos_bp
from routes.personas import personas_bp
from routes.usuarios import usuarios_bp
from routes.competiciones_favoritas import competiciones_favoritas_bp
from routes.equipos_favoritos import equipos_favoritos_bp
from routes.favoritos_personas import favoritos_personas_bp
from dotenv import load_dotenv


load_dotenv()




app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-string-here-change-in-production')
jwt = JWTManager(app)
app.register_blueprint(competiciones_bp)
app.register_blueprint(equipos_bp)
app.register_blueprint(personas_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(competiciones_favoritas_bp)
app.register_blueprint(equipos_favoritos_bp)
app.register_blueprint(favoritos_personas_bp)


@app.route('/')
def home():
    return 'Hello, Soccer Stats!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


# pipenv run python app.py