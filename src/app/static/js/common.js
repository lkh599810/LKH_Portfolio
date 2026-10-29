// index.html, projects.html 공통: 모바일 메뉴, data-target 스크롤 이동, 스크롤 진행 버튼
(function () {
    var HEADER_OFFSET = 72;
    var body = document.body;
    var toggle = document.querySelector('.menu-toggle');

    function setNavOpen(open) {
        body.classList.toggle('nav-open', open);
        if (toggle) {
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        }
    }

    if (toggle) {
        toggle.addEventListener('click', function () {
            setNavOpen(!body.classList.contains('nav-open'));
        });
    }

    document.querySelector('.nav-backdrop').addEventListener('click', function () {
        setNavOpen(false);
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            setNavOpen(false);
        }
    });

    document.addEventListener('click', function (event) {
        var trigger = event.target.closest('[data-target]');
        if (!trigger) {
            return;
        }
        var target = document.querySelector(trigger.getAttribute('data-target'));
        if (!target) {
            return;
        }
        setNavOpen(false);
        window.scrollTo({
            top: target.getBoundingClientRect().top + window.scrollY - HEADER_OFFSET,
            behavior: 'smooth'
        });
    });

    var topButton = document.querySelector('.scroll-top');
    var bar = topButton.querySelector('.scroll-top-bar');
    var length = 2 * Math.PI * bar.r.baseVal.value;
    bar.style.strokeDasharray = length;

    function updateProgress() {
        var max = document.documentElement.scrollHeight - window.innerHeight;
        var progress = max > 0 ? Math.min(window.scrollY / max, 1) : 0;
        bar.style.strokeDashoffset = length * (1 - progress);
        topButton.classList.toggle('visible', window.scrollY > 120);
    }

    window.addEventListener('scroll', updateProgress, {passive: true});
    window.addEventListener('resize', updateProgress);
    updateProgress();

    topButton.addEventListener('click', function () {
        window.scrollTo({top: 0, behavior: 'smooth'});
    });
})();
