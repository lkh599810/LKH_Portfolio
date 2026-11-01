from pathlib import Path

from flask import Blueprint, abort, redirect, render_template, request, url_for

from ...projects import CATEGORIES, PROJECTS, PROJECTS_BY_SLUG, TAGS, category_counts, category_label

bp = Blueprint(name='project_view', url_prefix='/', import_name="project_view")

IMAGES_DIR = Path(__file__).resolve().parents[2] / 'static' / 'images'
# scripts/make_project_images.py가 만든 최적화본(opt/*.webp)과 카드 썸네일(thumbs/<slug>.webp)
OPTIMIZED = {f.name for f in (IMAGES_DIR / 'opt').glob('*.webp')}
THUMBS = {f.stem for f in (IMAGES_DIR / 'thumbs').glob('*.webp')}


@bp.app_template_global()
def img_url(name):
    webp = Path(name).with_suffix('.webp').name
    if '/' not in name and webp in OPTIMIZED:
        return '/static/images/opt/' + webp
    return '/static/images/' + name


@bp.app_template_global()
def full_img_url(name):
    return '/static/images/' + name


@bp.app_template_global()
def thumb_url(project):
    if not project.get('cover'):
        return None
    if project['slug'] in THUMBS:
        return '/static/images/thumbs/' + project['slug'] + '.webp'
    return img_url(project['cover'])


@bp.app_context_processor
def project_context():
    return {'CATEGORIES': CATEGORIES, 'TAGS': TAGS, 'category_label': category_label}


@bp.route('/')
def index_page():
    return render_template("index.html", projects=PROJECTS, counts=category_counts())


@bp.route('/projects')
def project_page():
    # 예전 단일 프로젝트 페이지 링크 호환: 메인 Projects 섹션으로 이동
    category = request.args.get('category')
    return redirect(url_for('project_view.index_page', category=category) + '#projects')


@bp.route('/projects/<slug>')
def project_detail_page(slug):
    project = PROJECTS_BY_SLUG.get(slug)
    if project is None:
        abort(404)
    index = PROJECTS.index(project)
    return render_template(
        "project_detail.html",
        project=project,
        prev_project=PROJECTS[index - 1] if index > 0 else None,
        next_project=PROJECTS[index + 1] if index + 1 < len(PROJECTS) else None,
    )


@bp.app_errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
