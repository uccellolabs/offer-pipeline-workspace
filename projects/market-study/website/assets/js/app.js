/* ── Active nav link ─────────────────────────────────────────── */
(function () {
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__links a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) {
      a.classList.add('active');
    }
  });
})();

/* ── Mobile nav toggle ───────────────────────────────────────── */
const toggle = document.querySelector('.nav__toggle');
const links  = document.querySelector('.nav__links');
if (toggle && links) {
  toggle.addEventListener('click', () => {
    links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', links.classList.contains('open'));
  });
}

/* ── Battlecard accordion ────────────────────────────────────── */
document.querySelectorAll('.battlecard__header').forEach(header => {
  header.addEventListener('click', () => {
    const body   = header.nextElementSibling;
    const chevron = header.querySelector('.battlecard__toggle');
    const isOpen  = body.classList.contains('open');
    body.classList.toggle('open', !isOpen);
    chevron && chevron.classList.toggle('open', !isOpen);
  });
});

/* ── Animated score bars ─────────────────────────────────────── */
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const fill = entry.target;
      const pct  = fill.dataset.pct || '0';
      fill.style.width = pct + '%';
      observer.unobserve(fill);
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll('.score-bar__fill').forEach(el => {
  el.style.width = '0%';
  observer.observe(el);
});

/* ── Gauge CSS custom property ───────────────────────────────── */
document.querySelectorAll('.gauge').forEach(g => {
  const val = parseFloat(g.dataset.score || 0);
  const max = parseFloat(g.dataset.max || 10);
  const pct = (val / max * 100).toFixed(1);
  g.style.setProperty('--pct', pct + '%');
  const bg = val >= 8 ? 'conic-gradient(#059669 ' + pct + '%, #e5e7eb 0%)'
           : val >= 6 ? 'conic-gradient(#d97706 ' + pct + '%, #e5e7eb 0%)'
           :             'conic-gradient(#dc2626 ' + pct + '%, #e5e7eb 0%)';
  g.style.background = bg;
});

/* ── Smooth fade-up on scroll ────────────────────────────────── */
const fadeObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.opacity = '1';
      e.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('[data-animate]').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(16px)';
  el.style.transition = 'opacity .5s ease, transform .5s ease';
  fadeObs.observe(el);
});
