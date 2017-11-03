import logging.config

from flask import current_app
from flask import Flask

from .model import Teams
from .views import main as views_main

app = Flask(
    __name__,
    instance_relative_config=True,
)

app.config.from_pyfile('default_config.py', silent=False)
app.config.from_envvar('APP_CONFIG_FILE', silent=False)

app.register_blueprint(views_main)

# initialize the app
with app.app_context():
    data_dir = current_app.config.get('JSON_DATA_DIR')
    current_app.config['teams'] = Teams(data_dir)

    logging.config.dictConfig(current_app.config['LOG_CONFIG'])
