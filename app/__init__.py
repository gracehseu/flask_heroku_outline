from flask import Flask

# importing blueprints from modules
from .module_ex_1 import module_ex_1
from .module_ex_2 import module_ex_2

# creating app
app = Flask(__name__)

# getting configurations
app.config.from_object('config')

# register blueprints
app.register_blueprint(module_ex_1_bp)
app.register_blueprint(module_ex_2_bp)

if __name__ == '__main__':
    app.run()