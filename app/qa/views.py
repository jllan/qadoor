# encoding: utf-8

from flask import Blueprint, render_template
from flask_login import current_user
from ..user import User

qa = Blueprint('qa', __name__, url_prefix='')

@qa.route('/', methods=["GET"])
def index():
    return render_template('qa/index.html', current_user=current_user)