// Nav scroll behavior
(function () {
  var nav = document.querySelector('.nav');
  if (!nav) return;
  function onScroll() { nav.classList.toggle('scrolled', window.scrollY > 30); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}());

// FAQ accordion
document.querySelectorAll('.faq-q').forEach(function (q) {
  q.addEventListener('click', function () {
    this.closest('.faq-item').classList.toggle('open');
  });
});
