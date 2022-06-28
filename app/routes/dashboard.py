from flask import Blueprint, render_template, session

# every route will be prefixed with '/dashboard'
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# user dashboard route


@bp.route('/')
def dash():
    return render_template(
        'dashboard.html',
        loggedIn=session.get('loggedIn')
    )

# edit post route


@bp.route('/edit/<id>')
def edit(id):
    return render_template(
        'edit-post.html',
        loggedIn=session.get('loggedIn')
    )
