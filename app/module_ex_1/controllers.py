from flask import Blueprint, render_template

module_ex_1_bp = Blueprint('module_ex_1', __name__)

@module_ex_1_bp("/module_ex_1_bp", methods=["GET", "POST"])
@module_ex_1_bp("/", methods=["GET", "POST"])
def main():
    print('in module_ex_1_bp')
    return render_template("module_ex_1/module.html")