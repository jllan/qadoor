from flask import Blueprint
from flask import render_template

qa = Blueprint('qa', __name__, url_prefix='')

@qa.route('/<title>')
@qa.route('/', defaults={'title': None})
def index(title):
    return render_template('index.html', title=title, tem_str='Jlan')