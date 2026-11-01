// 메인 Projects 섹션: 카테고리 탭이 카드 그룹과 궤도(orbit) 강조를 함께 바꾼다.
// 선택 상태는 ?category= 로 URL에 남겨 상세 페이지에서 돌아와도 유지
(function () {
    var grid = document.getElementById('project-grid');
    if (!grid) {
        return;
    }
    var tabs = Array.prototype.slice.call(document.querySelectorAll('.project-tab'));
    var groups = Array.prototype.slice.call(grid.querySelectorAll('.project-group'));
    var orbit = document.querySelector('[data-orbit]');

    function select(key, updateUrl) {
        var tab = tabs.filter(function (t) { return t.getAttribute('data-category') === key; })[0];
        if (!tab) {
            tab = tabs[0];
            key = 'all';
        }
        tabs.forEach(function (t) {
            var active = t === tab;
            t.setAttribute('aria-selected', active ? 'true' : 'false');
            t.tabIndex = active ? 0 : -1;
        });
        grid.setAttribute('aria-labelledby', tab.id);
        groups.forEach(function (group) {
            group.hidden = key !== 'all' && group.getAttribute('data-category') !== key;
        });
        if (orbit) {
            orbit.setAttribute('data-active', key);
        }
        Array.prototype.forEach.call(document.querySelectorAll('.orbit-key'), function (button) {
            button.setAttribute('aria-pressed', button.getAttribute('data-select') === key ? 'true' : 'false');
        });
        // 애니메이션 재시작
        grid.classList.remove('is-switching');
        void grid.offsetWidth;
        grid.classList.add('is-switching');

        if (updateUrl) {
            var url = new URL(window.location.href);
            if (key === 'all') {
                url.searchParams.delete('category');
            } else {
                url.searchParams.set('category', key);
            }
            url.hash = 'projects';
            history.replaceState(null, '', url);
        }
        return tab;
    }

    tabs.forEach(function (tab, index) {
        tab.addEventListener('click', function () {
            select(tab.getAttribute('data-category'), true);
        });
        tab.addEventListener('keydown', function (event) {
            var next = null;
            if (event.key === 'ArrowRight') next = tabs[(index + 1) % tabs.length];
            if (event.key === 'ArrowLeft') next = tabs[(index - 1 + tabs.length) % tabs.length];
            if (event.key === 'Home') next = tabs[0];
            if (event.key === 'End') next = tabs[tabs.length - 1];
            if (!next) {
                return;
            }
            event.preventDefault();
            select(next.getAttribute('data-category'), true).focus();
        });
    });

    // 궤도 범례·태양을 누르면 같은 카테고리 탭을 고른다 (다시 누르면 전체)
    Array.prototype.forEach.call(document.querySelectorAll('[data-select]'), function (button) {
        button.addEventListener('click', function () {
            var key = button.getAttribute('data-select');
            var active = orbit ? orbit.getAttribute('data-active') : 'all';
            select(key === active ? 'all' : key, true);
        });
    });

    select(new URLSearchParams(window.location.search).get('category') || 'all', false);
})();
