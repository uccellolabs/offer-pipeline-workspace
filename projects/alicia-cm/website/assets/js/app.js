(function () {
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__links a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) a.classList.add('active');
  });
})();

const toggle = document.querySelector('.nav__toggle');
const links = document.querySelector('.nav__links');
if (toggle && links) {
  toggle.addEventListener('click', () => {
    links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', links.classList.contains('open'));
  });
}

document.querySelectorAll('.battlecard__header').forEach(header => {
  header.addEventListener('click', () => {
    const body = header.nextElementSibling;
    const ch = header.querySelector('.battlecard__toggle');
    const open = body.classList.contains('open');
    body.classList.toggle('open', !open);
    if (ch) ch.classList.toggle('open', !open);
  });
});

const fillObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const fill = entry.target;
      fill.style.width = (fill.dataset.pct || '0') + '%';
      fillObs.unobserve(fill);
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll('.score-bar__fill').forEach(el => {
  el.style.width = '0%';
  fillObs.observe(el);
});

document.querySelectorAll('.gauge').forEach(g => {
  const val = parseFloat(g.dataset.score || 0);
  const max = parseFloat(g.dataset.max || 10);
  const pct = (val / max * 100).toFixed(1);
  const c = val >= 8 ? '#059669' : val >= 6 ? '#d97706' : '#dc2626';
  g.style.background = 'conic-gradient(' + c + ' ' + pct + '%, #e2e8f0 0%)';
});
