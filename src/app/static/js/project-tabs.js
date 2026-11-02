// 메인 All Projects: 카테고리 탭 필터. 선택 상태는 ?category= 로 URL에 남겨 상세 페이지에서 돌아와도 유지
(function () {
    var grid = document.getElementById('project-grid');
    if (!grid) {
        return;
    }
    var tabs = Array.prototype.slice.call(document.querySelectorAll('.project-tab'));
    var items = Array.prototype.slice.call(grid.querySelectorAll('.project-card-item'));
    var descs = Array.prototype.slice.call(document.querySelectorAll('[data-desc]'));

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
        items.forEach(function (item) {
            item.hidden = key !== 'all' && item.getAttribute('data-category') !== key;
        });
        descs.forEach(function (d) {
            d.hidden = d.getAttribute('data-desc') !== key;
        });
        // 카드 등장 애니메이션 재시작
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
            url.hash = 'all-projects';
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

    var initial = new URLSearchParams(window.location.search).get('category');
    select(initial || 'all', false);
    // 상세 페이지에서 카테고리를 지정해 돌아오면 필터 위치로 이동
    if (initial && window.location.hash === '#projects') {
        var target = document.getElementById('all-projects');
        requestAnimationFrame(function () {
            window.scrollTo(0, target.getBoundingClientRect().top + window.scrollY - 80);
        });
    }
})();
