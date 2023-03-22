import argparse
import logging
from logging.config import fileConfig

import yaml
from flask import Flask
from flask_cors import CORS

from src.pciapi import api
from src.pciapi.auth import auth_setup
from src.util.conf import util_init_config


def create_app():
    app = Flask(__name__, static_folder='src/pciapi/static')
    _ = CORS(app, resources={r"/*": {"origins": "*"}},
             supports_credentials=True)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    auth_setup(app)
    app.register_blueprint(api.bp, url_prefix='/api')
    log_file = open('config/logger.yaml', 'r')
    logging.config.dictConfig(yaml.load(log_file, Loader=yaml.FullLoader))

    @app.errorhandler(AssertionError)
    def handle_custom_exception(error):
        logging.getLogger(__name__).exception(error)
        return {'text': str(error)}, 450

    @app.errorhandler(Exception)
    def handle_exceptions(error):
        logging.getLogger(__name__).exception(error)
        return {'text': str(error)}, 450

    return app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GFE Server.')
    parser.add_argument("--config", "-c", help="configuration file")
    args = parser.parse_args()
    cnf = util_init_config(args.config)
    create_app().run(debug=True)
