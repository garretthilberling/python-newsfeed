from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard') # every route will be prefixed with '/dashboard'

# user dashboard route
@bp.route('/')
def dash():
    return render_template('dashboard.html')

# edit post route
@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')