/* ============================================================
   KIDS SURFACE — Interactions
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ─── Nav scroll shadow ─────────────────────────────────── */
  const nav = document.querySelector('.nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 16);
    }, { passive: true });
  }

  /* ─── Mobile nav toggle ─────────────────────────────────── */
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks  = document.querySelector('.nav-links');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });
    document.addEventListener('click', (e) => {
      if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {
        navLinks.classList.remove('open');
      }
    });
  }

  /* ─── Active nav link ───────────────────────────────────── */
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href && currentPath.endsWith(href.replace('../', '').replace('.html', ''))
        || (href === '../index.html' && (currentPath.endsWith('/') || currentPath.endsWith('index.html')))) {
      link.classList.add('active');
    }
  });

  /* ─── Battlecards accordion ─────────────────────────────── */
  document.querySelectorAll('.battlecard-header').forEach(header => {
    header.addEventListener('click', () => {
      const card = header.closest('.battlecard');
      const isOpen = card.classList.contains('open');
      document.querySelectorAll('.battlecard').forEach(c => c.classList.remove('open'));
      if (!isOpen) card.classList.add('open');
    });
  });

  /* ─── Tabs ──────────────────────────────────────────────── */
  document.querySelectorAll('.tabs').forEach(tabs => {
    const btns   = tabs.querySelectorAll('.tab-btn');
    const panels = tabs.querySelectorAll('.tab-panel');

    btns.forEach((btn, i) => {
      btn.addEventListener('click', () => {
        btns.forEach(b => b.classList.remove('active'));
        panels.forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        panels[i]?.classList.add('active');
      });
    });

    if (btns.length > 0) {
      btns[0].classList.add('active');
      panels[0]?.classList.add('active');
    }
  });

  /* ─── Score gauge animation ─────────────────────────────── */
  document.querySelectorAll('[data-score]').forEach(el => {
    const score    = parseFloat(el.dataset.score);
    const max      = parseFloat(el.dataset.max || 10);
    const pct      = score / max;
    const r        = 46;
    const circ     = 2 * Math.PI * r;
    const fill     = el.querySelector('.fill');
    if (!fill) return;

    const colors = pct >= 0.7 ? '#3D7A5E' : pct >= 0.5 ? '#D97706' : '#DC2626';
    fill.style.stroke = colors;
    fill.style.strokeDasharray = `${circ} ${circ}`;
    fill.style.strokeDashoffset = circ;

    const valueEl = el.querySelector('.gauge-value');
    if (valueEl) valueEl.style.color = colors;

    requestAnimationFrame(() => {
      setTimeout(() => {
        fill.style.strokeDashoffset = circ * (1 - pct);
      }, 200);
    });
  });

  /* ─── Fade-in on scroll ─────────────────────────────────── */
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.fade-in').forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(16px)';
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      observer.observe(el);
    });

    document.addEventListener('animationend', (e) => {
      if (e.target.classList.contains('fade-in')) {
        e.target.style.opacity = '1';
        e.target.style.transform = 'none';
      }
    });

    // Simplified: just add visible class
    document.querySelectorAll('.fade-in').forEach((el, i) => {
      observer.observe(el);
    });
  }

  /* Custom visible handler */
  const style = document.createElement('style');
  style.textContent = '.fade-in.visible { opacity: 1 !important; transform: none !important; }';
  document.head.appendChild(style);

});
