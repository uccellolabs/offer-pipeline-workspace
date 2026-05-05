// Hamburger menu
const nav = document.getElementById('nav');
const navMobile = document.getElementById('nav-mobile');
const hamburger = document.getElementById('hamburger');

function openMenu() {
  nav.classList.add('nav--open');
  navMobile.classList.add('nav--open');
  hamburger.setAttribute('aria-expanded', 'true');
  document.body.style.overflow = 'hidden';
}

function closeMenu() {
  nav.classList.remove('nav--open');
  navMobile.classList.remove('nav--open');
  hamburger.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
}

if (hamburger && nav && navMobile) {
  hamburger.addEventListener('click', () => {
    nav.classList.contains('nav--open') ? closeMenu() : openMenu();
  });

  document.querySelectorAll('.nav__mobile a').forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeMenu();
  });
}

// Generic accordion (.accordion)
document.querySelectorAll('.accordion__trigger').forEach(btn => {
  btn.addEventListener('click', () => {
    const acc = btn.closest('.accordion');
    const isOpen = acc.classList.contains('accordion--open');
    acc.classList.toggle('accordion--open', !isOpen);
    btn.setAttribute('aria-expanded', String(!isOpen));
    const icon = btn.querySelector('.accordion__icon');
    if (icon) icon.textContent = isOpen ? '+' : '−';
  });
});

// Battlecard toggle
document.querySelectorAll('.battlecard__header').forEach(header => {
  header.style.cursor = 'pointer';
  header.addEventListener('click', () => {
    header.closest('.battlecard').classList.toggle('battlecard--open');
  });
});

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
