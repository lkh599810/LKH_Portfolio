"""라우트·프로젝트 데이터 점검. `python tests/test_site.py` 또는 pytest로 실행."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))

from app import server  # noqa: E402
from app.projects import CATEGORIES, PROJECTS, TAGS  # noqa: E402

STATIC = ROOT / 'src' / 'app' / 'static'
client = server.test_client()


def test_data_is_consistent():
    slugs = [p['slug'] for p in PROJECTS]
    assert len(slugs) == len(set(slugs))
    keys = {c['key'] for c in CATEGORIES}
    for p in PROJECTS:
        assert p['category'] in keys - {'all'}, p['slug']
        assert set(p['tags']) <= set(TAGS), p['slug']
        assert re.fullmatch(r'[a-z0-9-]+', p['slug'])


def test_index_lists_every_project_once():
    html = client.get('/').get_data(as_text=True)
    for p in PROJECTS:
        assert html.count(f'class="project-card" href="/projects/{p["slug"]}"') == 1, p['slug']
    assert 'id="project-tab-all"' in html


def test_detail_pages_and_their_assets():
    for p in PROJECTS:
        res = client.get(f'/projects/{p["slug"]}')
        assert res.status_code == 200, p['slug']
        html = res.get_data(as_text=True)
        for src in set(re.findall(r'(?:src|href)="(/static/[^"]+)"', html)):
            assert (STATIC / src[len('/static/'):]).is_file(), (p['slug'], src)


def test_index_assets_exist():
    html = client.get('/').get_data(as_text=True)
    for src in set(re.findall(r'(?:src|href)="(/static/[^"]+)"', html)):
        assert (STATIC / src[len('/static/'):]).is_file(), src


def test_index_sections_and_featured():
    html = client.get('/').get_data(as_text=True)
    for anchor in ['id="projects"', 'id="experience"', 'id="skills"', 'id="archiving"', 'data-pipeline']:
        assert anchor in html, anchor
    assert html.count('class="featured-card') == 3
    assert 'class="orbit' not in html and 'resume-page' not in html


def test_multi_image_blocks_render_as_gallery():
    html = client.get('/projects/card24').get_data(as_text=True)
    assert 'data-gallery' in html and html.count('class="gallery-slide"') == 11


def test_unknown_project_and_legacy_url():
    assert client.get('/projects/nope').status_code == 404
    assert client.get('/no-such-page').status_code == 404
    res = client.get('/projects?category=ai')
    assert res.status_code == 302
    assert res.headers['Location'].endswith('/?category=ai#projects')


if __name__ == '__main__':
    for name, fn in list(globals().items()):
        if name.startswith('test_'):
            fn()
            print('ok', name)
