// Sources accordion
document.querySelectorAll('.sources-accordion__trigger').forEach(btn => {
  btn.addEventListener('click', () => {
    const acc = btn.closest('.sources-accordion');
    acc.classList.toggle('sources-accordion--open');
    btn.querySelector('.sources-accordion__icon').textContent =
      acc.classList.contains('sources-accordion--open') ? '▲' : '▼';
  });
});

// Score bar animation on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.score-grid__bar-fill').forEach(bar => {
        bar.style.width = bar.dataset.width;
      });
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll('.score-grid').forEach(el => {
  el.querySelectorAll('.score-grid__bar-fill').forEach(bar => {
    const w = bar.style.width;
    bar.dataset.width = w;
    bar.style.width = '0';
  });
  observer.observe(el);
});
