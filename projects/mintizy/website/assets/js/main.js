/* Mintizy étude / interactions site interne */

(function () {
  'use strict';

  // Hamburger menu mobile
  const nav = document.querySelector('.nav');
  const hamburger = document.querySelector('.nav__hamburger');
  if (hamburger && nav) {
    hamburger.addEventListener('click', () => {
      nav.classList.toggle('menu-open');
      const expanded = nav.classList.contains('menu-open');
      hamburger.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
  }

  // Battlecards : clic sur le header pour déplier
  document.querySelectorAll('.battlecard__header').forEach(header => {
    header.addEventListener('click', () => {
      header.parentElement.classList.toggle('open');
    });
    header.setAttribute('role', 'button');
    header.setAttribute('tabindex', '0');
    header.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        header.click();
      }
    });
  });

  // Accordions génériques
  document.querySelectorAll('.accordion__trigger').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const expanded = trigger.getAttribute('aria-expanded') === 'true';
      trigger.setAttribute('aria-expanded', !expanded);
      const body = trigger.nextElementSibling;
      if (body && body.classList.contains('accordion__body')) {
        body.classList.toggle('open');
      }
    });
  });

  // Tabs (persona)
  document.querySelectorAll('[data-tabs]').forEach(group => {
    const buttons = group.querySelectorAll('.tabs__btn');
    const panels = group.querySelectorAll('.tab-panel');
    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.getAttribute('data-tab');
        buttons.forEach(b => b.classList.remove('tabs__btn--active'));
        panels.forEach(p => p.classList.remove('tab-panel--active'));
        btn.classList.add('tabs__btn--active');
        const targetPanel = group.querySelector(`#${target}`);
        if (targetPanel) targetPanel.classList.add('tab-panel--active');
      });
    });
  });

  // Smooth scroll pour les ancres
  document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
})();
