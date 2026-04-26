(function () {
  var slides  = Array.from(document.querySelectorAll('.slide'));
  var count   = document.querySelector('.nav-count');
  var prevBtn = document.querySelector('.nav-prev');
  var nextBtn = document.querySelector('.nav-next');
  var fsBtn   = document.querySelector('.nav-fs');
  var cur     = 0;
  var total   = slides.length;

  function go(n) {
    slides[cur].classList.remove('active');
    cur = Math.max(0, Math.min(n, total - 1));
    slides[cur].classList.add('active');
    count.textContent   = (cur + 1) + ' / ' + total;
    prevBtn.disabled    = cur === 0;
    nextBtn.disabled    = cur === total - 1;
  }

  prevBtn.addEventListener('click', function () { go(cur - 1); });
  nextBtn.addEventListener('click', function () { go(cur + 1); });

  fsBtn.addEventListener('click', function () {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(function () {});
    } else {
      document.exitFullscreen();
    }
  });

  document.addEventListener('keydown', function (e) {
    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case ' ':
        e.preventDefault();
        go(cur + 1);
        break;
      case 'ArrowLeft':
      case 'ArrowUp':
        e.preventDefault();
        go(cur - 1);
        break;
      case 'f':
      case 'F':
        if (!document.fullscreenElement) {
          document.documentElement.requestFullscreen().catch(function () {});
        } else {
          document.exitFullscreen();
        }
        break;
    }
  });

  go(0);
}());
