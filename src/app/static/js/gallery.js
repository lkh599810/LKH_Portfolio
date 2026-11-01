// 상세 페이지 이미지 슬라이더: 스와이프는 CSS scroll-snap이 처리하고, 여기서는 버튼·썸네일·방향키·전체 화면만 연결
(function () {
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    Array.prototype.forEach.call(document.querySelectorAll('[data-gallery]'), function (gallery) {
        var track = gallery.querySelector('.gallery-track');
        var thumbBar = gallery.querySelector('.gallery-thumbs');
        var thumbs = thumbBar.querySelectorAll('button');
        var bar = gallery.querySelector('.gallery-progress span');
        var full = gallery.querySelector('.gallery-full');
        var total = track.children.length;
        var current = 0;

        function go(index) {
            index = (index + total) % total;
            track.scrollTo({ left: index * track.clientWidth, behavior: reduceMotion ? 'auto' : 'smooth' });
        }

        function sync() {
            var index = Math.round(track.scrollLeft / track.clientWidth);
            if (index < 0 || index >= total) {
                return;
            }
            current = index;
            bar.style.width = ((index + 1) / total * 100) + '%';
            Array.prototype.forEach.call(thumbs, function (thumb, i) {
                if (i === index) {
                    thumb.setAttribute('aria-current', 'true');
                    // 페이지 전체가 아니라 썸네일 줄만 스크롤
                    thumbBar.scrollTo({
                        left: thumb.offsetLeft - (thumbBar.clientWidth - thumb.offsetWidth) / 2,
                        behavior: reduceMotion ? 'auto' : 'smooth'
                    });
                } else {
                    thumb.removeAttribute('aria-current');
                }
            });
        }

        var pending = false;
        track.addEventListener('scroll', function () {
            if (pending) {
                return;
            }
            pending = true;
            requestAnimationFrame(function () {
                pending = false;
                sync();
            });
        });

        gallery.querySelector('.gallery-prev').addEventListener('click', function () { go(current - 1); });
        gallery.querySelector('.gallery-next').addEventListener('click', function () { go(current + 1); });
        Array.prototype.forEach.call(thumbs, function (thumb, i) {
            thumb.addEventListener('click', function () { go(i); });
        });
        gallery.addEventListener('keydown', function (event) {
            if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
                event.preventDefault();
                go(current + (event.key === 'ArrowRight' ? 1 : -1));
            }
        });

        if (document.fullscreenEnabled && gallery.requestFullscreen) {
            full.hidden = false;
            full.addEventListener('click', function () {
                if (document.fullscreenElement) {
                    document.exitFullscreen();
                } else {
                    gallery.requestFullscreen();
                }
            });
            // 전체 화면 전환 후 너비가 바뀌어도 같은 장을 보여준다
            gallery.addEventListener('fullscreenchange', function () {
                var keep = current;
                requestAnimationFrame(function () { track.scrollLeft = keep * track.clientWidth; });
            });
        }

        sync();
    });
})();
