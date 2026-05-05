/* e-novateur — Landing page script */

(function () {
  'use strict';

  /* ── Nav scroll shadow ─────────────────────────────── */
  const nav = document.getElementById('nav');
  if (nav) {
    const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 20);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ── Hamburger menu ────────────────────────────────── */
  const ham     = document.getElementById('ham');
  const mobMenu = document.getElementById('mob-menu');
  if (ham && mobMenu) {
    ham.addEventListener('click', () => {
      const isOpen = ham.classList.toggle('open');
      ham.setAttribute('aria-expanded', String(isOpen));
      mobMenu.classList.toggle('open', isOpen);
    });
    mobMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        ham.classList.remove('open');
        ham.setAttribute('aria-expanded', 'false');
        mobMenu.classList.remove('open');
      });
    });
  }

  /* ── FAQ accordion ─────────────────────────────────── */
  document.querySelectorAll('.faq-trigger').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const item   = trigger.closest('.faq-item');
      const isOpen = item.classList.contains('open');

      document.querySelectorAll('.faq-item.open').forEach(other => {
        if (other !== item) {
          other.classList.remove('open');
          other.querySelector('.faq-trigger').setAttribute('aria-expanded', 'false');
        }
      });

      item.classList.toggle('open', !isOpen);
      trigger.setAttribute('aria-expanded', String(!isOpen));
    });
  });

  /* ── Smooth scroll ─────────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const id = anchor.getAttribute('href');
      if (id === '#') return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const navH = nav ? nav.offsetHeight : 0;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - navH - 16, behavior: 'smooth' });
    });
  });

})();
