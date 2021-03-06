from flask import Flask

# importing blueprints from modules
from .module_ex_1.controllers import module_ex_1_bp
from .module_ex_2.controllers import module_ex_2_bp

# creating app
app = Flask(__name__)

# getting configurations
app.config.from_object('config')

# register blueprints
app.register_blueprint(module_ex_1_bp)
app.register_blueprint(module_ex_2_bp)

if __name__ == '__main__':
    app.run()