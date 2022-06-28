from flask import Blueprint,render_template

bp = Blueprint('home', __name__, url_prefix='/')

# homepage route
@bp.route('/')
def index():
    return render_template('homepage.html')

# user login route
@bp.route('/login')
def login():
    return render_template('login.html')

# single post route
@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')