// Hero 배포 파이프라인 패널: 단계를 누르면 내용을 펼친다.
// 화면에 보이는 동안 몇 초마다 다음 단계로 넘어가고, 사용자가 한 번이라도 조작하면 자동 진행을 멈춘다.
(function () {
    var panel = document.querySelector('[data-pipeline]');
    if (!panel) {
        return;
    }
    var steps = Array.prototype.slice.call(panel.querySelectorAll('.pipeline-step'));
    var current = 0;
    var timer = null;
    var stopped = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function open(index) {
        current = index;
        steps.forEach(function (step, i) {
            var active = i === index;
            step.classList.toggle('is-active', active);
            step.classList.toggle('is-done', i < index);
            step.querySelector('.pipeline-trigger').setAttribute('aria-expanded', active ? 'true' : 'false');
            step.querySelector('.step-detail').hidden = !active;
        });
    }

    function stop() {
        stopped = true;
        clearInterval(timer);
    }

    steps.forEach(function (step, i) {
        step.querySelector('.pipeline-trigger').addEventListener('click', function () {
            stop();
            open(i);
        });
    });
    panel.addEventListener('focusin', stop);

    function start() {
        if (stopped || timer) {
            return;
        }
        timer = setInterval(function () {
            open((current + 1) % steps.length);
        }, 3200);
    }

    function pause() {
        clearInterval(timer);
        timer = null;
    }

    panel.addEventListener('mouseenter', pause);
    panel.addEventListener('mouseleave', start);

    // 화면 밖에서는 돌리지 않음
    if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (entries) {
            if (entries[0].isIntersecting) {
                start();
            } else {
                pause();
            }
        }).observe(panel);
    } else {
        start();
    }
})();
