from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
import secrets
import os
import logging

def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)
    app.secret_key = secrets.token_hex(32)

    #Define Log dir and Log file
    LOG_DIR = "log"
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    LOG_FILE = os.path.join(LOG_DIR, 'flask.log')

    logging.basicConfig(
        #filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(), logging.FileHandler(LOG_FILE)] 
    )

    #Define file log handler
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    logger.info("Application Startup!!")

    # Import and register blueprints
    from .home import home_bp
    from .cookies import cookies_bp
    from .input import input_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(cookies_bp)
    app.register_blueprint(input_bp)
    
    return app