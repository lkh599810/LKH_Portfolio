"""projects.py가 참조하는 이미지로 카드 썸네일과 상세용 최적화 WebP를 만든다.

    python scripts/make_project_images.py

- thumbs/<slug>.webp : 카드용 800x500 (cover는 위쪽 기준 16:10 크롭, contain은 비율 유지)
- opt/<name>.webp    : 상세 페이지용, 긴 변 1600px. 원본보다 작을 때만 저장
원본 파일은 건드리지 않는다. 템플릿은 결과 파일이 있으면 쓰고 없으면 원본을 쓴다.
"""
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from app.projects import PROJECTS  # noqa: E402

IMAGES = ROOT / 'src' / 'app' / 'static' / 'images'
THUMB_SIZE = (800, 500)


def referenced(project):
    names = {project.get('cover'), project.get('hero')}

    def walk(blocks):
        for block in blocks:
            for f in block.get('figures', []):
                names.add(f['src'])
            if 'sub' in block:
                walk(block['sub']['blocks'])

    for section in project['sections']:
        walk(section['blocks'])
    return {n for n in names if n and '/' not in n and not n.endswith('.svg')}


def save_webp(image, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGBA' if 'A' in image.getbands() else 'RGB')
    image.save(path, 'WEBP', quality=82, method=6)


def make_thumb(project):
    src = IMAGES / project['cover']
    image = Image.open(src)
    if project.get('cover_fit') != 'contain':
        w, h = image.size
        target = THUMB_SIZE[0] / THUMB_SIZE[1]
        if w / h < target:
            image = image.crop((0, 0, w, round(w / target)))
        else:
            new_w = round(h * target)
            left = (w - new_w) // 2
            image = image.crop((left, 0, left + new_w, h))
        image = image.resize(THUMB_SIZE, Image.LANCZOS)
    else:
        image.thumbnail(THUMB_SIZE, Image.LANCZOS)
    save_webp(image, IMAGES / 'thumbs' / f"{project['slug']}.webp")


def make_optimized(name):
    src = IMAGES / name
    out = IMAGES / 'opt' / (Path(name).stem + '.webp')
    image = Image.open(src)
    image.thumbnail((1600, 1600), Image.LANCZOS)
    save_webp(image, out)
    if out.stat().st_size >= src.stat().st_size:
        out.unlink()


if __name__ == '__main__':
    names = set()
    for project in PROJECTS:
        cover = project.get('cover')
        if cover and not cover.endswith('.svg'):
            make_thumb(project)
        names |= referenced(project)
    for name in sorted(names):
        make_optimized(name)
    print(f'thumbs: {len(list((IMAGES / "thumbs").glob("*.webp")))}, optimized: {len(list((IMAGES / "opt").glob("*.webp")))}')
