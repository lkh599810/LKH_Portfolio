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
    // 프로젝트 slug → 상세 주소 (open/cd 용)
    var projects = {};
    Array.prototype.forEach.call(templates.projects.content.querySelectorAll('a'), function (a) {
        projects[a.textContent.trim()] = a.getAttribute('href');
    });
    var aliases = { ls: 'projects', 'ls projects': 'projects', about: 'introduce', '?': 'help', 'cat introduce': 'introduce',
        'uname -a': 'uname', 'cat contact': 'contact', 'whoami --help': 'help' };
    var isEn = function () { return document.documentElement.lang === 'en'; };
    // template 없이 바로 처리하는 명령어. 문자열을 돌려주면 출력, null이면 출력 없음
    var builtins = {
        pwd: function () { return '/home/kanghyun'; },
        date: function () { return new Date().toLocaleString(isEn() ? 'en-US' : 'ko-KR'); },
        echo: function (arg) { return arg; },
        history: function () {
            return history.map(function (h, i) { return (i + 1) + '  ' + h; }).join('\n');
        },
        theme: function () {
            document.querySelector('.theme-toggle').click();
            return 'theme: ' + (document.body.classList.contains('dark-mode') ? 'dark' : 'light');
        },
        lang: function () {
            document.querySelector('.lang-toggle').click();
            return 'lang: ' + document.documentElement.lang;
        },
        open: function (arg) {
            if (!arg) {
                return isEn() ? 'usage: open <slug>  (see: projects)' : '사용법: open <slug>  (목록: projects)';
            }
            if (!projects[arg]) {
                return 'open: ' + arg + ': no such project';
            }
            window.location.href = projects[arg];
            return 'opening ' + arg + ' ...';
        },
        sudo: function () { return 'kanghyun is not in the sudoers file. This incident will be reported.'; },
        exit: function () { return isEn() ? 'There is no exit. Scroll down instead ↓' : '나가는 문은 없어요. 대신 아래로 스크롤해 보세요 ↓'; }
    };
    builtins.cd = function (arg) {
        if (!arg || arg === '~' || arg === '/') {
            return null;
        }
        return builtins.open(arg.replace(/\/$/, ''));
    };
    var names = Object.keys(templates).concat(['github', 'blog', 'clear'], Object.keys(builtins));
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
        var word = cmd.split(' ')[0];
        // echo는 대소문자 그대로 출력
        var arg = raw.trim().replace(/^\S+\s*/, '');
        if (word !== 'echo') {
            arg = arg.toLowerCase();
        }
        if (templates[cmd]) {
            out.appendChild(templates[cmd].content.cloneNode(true));
        } else if (builtins[word]) {
            var result = builtins[word](arg);
            if (result === null) {
                return;
            }
            out.classList.add('is-text');
            out.textContent = result;
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
            var typed = input.value.replace(/^\s+/, '').toLowerCase();
            // open/cd 뒤에서는 프로젝트 slug 자동완성
            var m = typed.match(/^(open|cd)\s+(.*)$/);
            var prefix = m ? m[1] + ' ' : '';
            var pool = m ? Object.keys(projects) : names;
            var hits = pool.filter(function (n) { return n.indexOf(m ? m[2] : typed) === 0; });
            if (hits.length) {
                event.preventDefault();
                // 후보들의 공통 앞부분까지 채우고, 여러 개면 목록도 보여줌
                var common = hits.reduce(function (a, b) {
                    var i = 0;
                    while (i < a.length && a[i] === b[i]) i++;
                    return a.slice(0, i);
                });
                input.value = prefix + common;
                if (hits.length > 1) {
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

    // 처음엔 help 결과를 미리 보여주고(기록에는 남기지 않음) 맨 위부터 보이게
    run('help');
    history = [];
    cursor = 0;
    log.scrollTop = 0;

    // 로그 빈 곳을 누르면 입력창으로 (링크·선택 중일 때는 제외)
    log.addEventListener('click', function (event) {
        if (!event.target.closest('a') && !String(window.getSelection())) {
            input.focus({ preventScroll: true });
        }
    });
})();
