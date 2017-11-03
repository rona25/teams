from flask import Flask

from .views_admin import admin as views_admin

admin = Flask(
    __name__,
    instance_relative_config=True,
)

admin.config.from_pyfile('default_config.py', silent=False)
admin.config.from_envvar('APP_CONFIG_FILE', silent=False)

admin.register_blueprint(views_admin)
