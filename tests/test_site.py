"""라우트·프로젝트 데이터 점검. `python tests/test_site.py` 또는 pytest로 실행."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))

from app import server  # noqa: E402
from app.projects import CATEGORIES, CHILDREN, PROJECTS, PROJECTS_BY_SLUG, TAGS, TOP_PROJECTS  # noqa: E402

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


def test_projects_page_lists_every_project_once():
    html = client.get('/projects').get_data(as_text=True)
    for p in TOP_PROJECTS:
        assert html.count(f'class="project-card" href="/projects/{p["slug"]}"') == 1, p['slug']
    # 하위 프로젝트는 상위 카드 안의 목록으로만 나온다
    for children in CHILDREN.values():
        for c in children:
            assert html.count(f'href="/projects/{c["slug"]}"') == 1, c['slug']
    assert 'id="project-tab-all"' in html
    assert 'id="project-tab-ai"' not in html
    assert client.get('/projects?category=research').status_code == 200


def test_index_links_to_projects_page():
    html = client.get('/').get_data(as_text=True)
    assert 'class="all-projects-link" href="/projects"' in html
    assert 'id="project-grid"' not in html


def test_sub_projects_are_linked_both_ways():
    lab = client.get('/projects/tosel-lab').get_data(as_text=True)
    assert 'id="sub-projects"' in lab
    for c in CHILDREN['tosel-lab']:
        assert f'href="/projects/{c["slug"]}"' in lab
        child = client.get(f'/projects/{c["slug"]}').get_data(as_text=True)
        assert 'class="detail-parent" href="/projects/tosel-lab"' in child


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
    # 히어로 터미널: 칩으로 노출한 명령어마다 출력 template이 있어야 함
    for cmd in ['help', 'introduce', 'whoami', 'projects', 'experience', 'skills', 'contact', 'what_is_positive_algorithm']:
        assert f'<template data-cmd="{cmd}">' in html, cmd
    assert "{'ko'" not in html
    # 카톡 등 링크 미리보기: 프로필 사진 대신 KH 로고, 절대 https 주소
    assert 'og:image" content="https://introduce.leekanghyun.co.kr/static/images/og-image.png"' in html
    assert (ROOT / 'src/app/static/images/og-image.png').exists()


def test_multi_image_blocks_render_as_gallery():
    html = client.get('/projects/card24').get_data(as_text=True)
    assert 'data-gallery' in html and html.count('class="gallery-slide"') == 11


def test_unknown_project():
    assert client.get('/projects/nope').status_code == 404
    assert client.get('/no-such-page').status_code == 404


if __name__ == '__main__':
    for name, fn in list(globals().items()):
        if name.startswith('test_'):
            fn()
            print('ok', name)
