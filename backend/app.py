import logging
from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.routes import initialize_routes
from resources.errors import errors
from database.db import initialize_db

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
CORS(app)
logging.basicConfig(filename='trainapp.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s')

api = Api(app, errors=errors)
ibcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
