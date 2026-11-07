from flask import Flask, abort, request
from .controllers.view.general import bp as view_bp

server = Flask(__name__)
server.register_blueprint(view_bp)


@server.before_request
def block_direct_image_open():
    # 이미지 주소를 주소창/새 탭으로 직접 여는 요청(Sec-Fetch-Dest: document)만 차단.
    # 페이지 안 <img> 로드(dest=image)와 링크 미리보기 크롤러(헤더 없음)는 그대로 허용.
    # ponytail: 헤더를 안 보내는 클라이언트(curl 등)는 막지 못함 — 완전 차단은 불가능한 영역
    if request.path.startswith('/static/images/') and request.headers.get('Sec-Fetch-Dest') == 'document':
        abort(404)
