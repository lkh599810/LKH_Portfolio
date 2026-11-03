// 히어로 미니 터미널: 입력한 명령어에 맞는 <template data-cmd> 내용을 로그에 출력한다.
(function () {
    var root = document.querySelector('[data-term]');
    if (!root) {
        return;
    }
    var log = root.querySelector('.term-log');
    var form = root.querySelector('.term-line');
    var input = form.querySelector('input');
    var templates = {};
    Array.prototype.forEach.call(root.querySelectorAll('template[data-cmd]'), function (t) {
        templates[t.getAttribute('data-cmd')] = t;
    });
    var links = {};
    Array.prototype.forEach.call(templates.contact.content.querySelectorAll('a[target]'), function (a) {
        links[a.textContent.indexOf('github') > -1 ? 'github' : 'blog'] = a.href;
    });
    var aliases = { ls: 'projects', about: 'introduce', '?': 'help', 'cat introduce': 'introduce' };
    var names = Object.keys(templates).concat(['github', 'blog', 'clear']);
    var history = [];
    var cursor = 0;

    function line(cls, text) {
        var p = document.createElement('p');
        p.className = cls;
        p.textContent = text;
        log.appendChild(p);
        return p;
    }

    function run(raw) {
        var cmd = raw.trim().toLowerCase().replace(/\s+/g, ' ');
        if (!cmd) {
            return;
        }
        history.push(cmd);
        cursor = history.length;
        cmd = aliases[cmd] || cmd;
        if (cmd === 'clear') {
            log.textContent = '';
            return;
        }
        line('term-echo', '$ ' + raw.trim());
        var out = document.createElement('div');
        out.className = 'term-out';
        if (templates[cmd]) {
            out.appendChild(templates[cmd].content.cloneNode(true));
        } else if (links[cmd]) {
            window.open(links[cmd], '_blank', 'noopener');
            out.textContent = 'opening ' + links[cmd] + ' ...';
        } else {
            out.classList.add('is-error');
            out.textContent = 'command not found: ' + cmd + ' — try help';
        }
        log.appendChild(out);
        // 페이지가 아니라 로그 영역만 스크롤
        log.scrollTop = log.scrollHeight;
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        run(input.value);
        input.value = '';
    });

    input.addEventListener('keydown', function (event) {
        if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {
            if (!history.length) {
                return;
            }
            event.preventDefault();
            cursor = Math.max(0, Math.min(history.length, cursor + (event.key === 'ArrowUp' ? -1 : 1)));
            input.value = history[cursor] || '';
        } else if (event.key === 'Tab' && input.value.trim()) {
            var hits = names.filter(function (n) { return n.indexOf(input.value.trim().toLowerCase()) === 0; });
            if (hits.length) {
                event.preventDefault();
                if (hits.length === 1) {
                    input.value = hits[0];
                } else {
                    line('term-muted', hits.join('  '));
                    log.scrollTop = log.scrollHeight;
                }
            }
        }
    });

    root.addEventListener('click', function (event) {
        var chip = event.target.closest('[data-run]');
        if (chip) {
            run(chip.getAttribute('data-run'));
        }
    });

    // 로그 빈 곳을 누르면 입력창으로 (링크·선택 중일 때는 제외)
    log.addEventListener('click', function (event) {
        if (!event.target.closest('a') && !String(window.getSelection())) {
            input.focus({ preventScroll: true });
        }
    });
})();
