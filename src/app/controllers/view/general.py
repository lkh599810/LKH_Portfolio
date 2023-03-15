from flask import Blueprint, render_template

bp = Blueprint(name='project_view', url_prefix='/', import_name="project_view")
@bp.route('/')
def index_page():
    return render_template("index.html")

@bp.route('/projects')
def project_page():
    return render_template("projects.html")
