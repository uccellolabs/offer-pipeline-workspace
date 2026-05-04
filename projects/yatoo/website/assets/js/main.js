/* ─── YATOO — Site d'étude interne — main.js ─── */

/* ── Auth guard ────────────────────────────────────────────────── */
(function () {
  if (window.location.pathname.endsWith('login.html')) return;
  if (!sessionStorage.getItem('yatoo_auth')) {
    const dest = encodeURIComponent(window.location.pathname);
    window.location.href = '/login.html?r=' + dest;
  }
})();

/* ── Hamburger nav ─────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.querySelector('.nav__hamburger');
  const mobileMenu = document.querySelector('.nav__mobile');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      const open = mobileMenu.classList.toggle('open');
      hamburger.classList.toggle('open', open);
      hamburger.setAttribute('aria-expanded', open);
    });
    mobileMenu.querySelectorAll('.nav__link').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('open');
      });
    });
  }

  /* ── Active nav link ──────────────────────────────────────────── */
  var path = window.location.pathname;
  document.querySelectorAll('.nav__link').forEach(function (link) {
    var href = link.getAttribute('href');
    if (href && path.endsWith(href.replace(/^\//, '').replace(/^\.\.\//, ''))) {
      link.classList.add('nav__link--active');
    }
  });

  /* ── Accordions ───────────────────────────────────────────────── */
  document.querySelectorAll('.accordion__trigger').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var accordion = btn.closest('.accordion');
      var isOpen = accordion.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen);
    });
  });

  /* ── Battlecards ──────────────────────────────────────────────── */
  document.querySelectorAll('.battlecard__header').forEach(function (header) {
    header.addEventListener('click', function () {
      header.closest('.battlecard').classList.toggle('open');
    });
  });

  /* ── Score rings animation ────────────────────────────────────── */
  document.querySelectorAll('.score-ring').forEach(function (ring) {
    var fill = ring.querySelector('.score-ring__fill');
    if (!fill) return;
    var score = parseFloat(ring.dataset.score) || 0;
    var max   = parseFloat(ring.dataset.max) || 10;
    var r = 40;
    var circ = 2 * Math.PI * r;
    fill.setAttribute('stroke-dasharray', circ);
    fill.setAttribute('stroke-dashoffset', circ);
    setTimeout(function () {
      fill.style.strokeDashoffset = circ * (1 - score / max);
    }, 200);
  });

  /* ── Progress bars ────────────────────────────────────────────── */
  document.querySelectorAll('.progress-bar__fill').forEach(function (bar) {
    var target = bar.dataset.width || '0%';
    bar.style.width = '0%';
    setTimeout(function () { bar.style.width = target; }, 200);
  });

  /* ── Intersection observer for fade-in ───────────────────────── */
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.fade-in').forEach(function (el) {
      observer.observe(el);
    });
  } else {
    document.querySelectorAll('.fade-in').forEach(function (el) {
      el.classList.add('visible');
    });
  }
});

/* ── Login logic ────────────────────────────────────────────────── */
async function handleLogin(event) {
  event.preventDefault();
  var input = document.getElementById('password');
  var error = document.getElementById('login-error');
  if (!input) return;
  var pw = input.value;
  var hash = await sha256(pw);
  var stored = 'b37ec53b51e84407fdfb31f859b3d1fcae149bea5190f64fccb66d9b81b0210d';
  if (hash === stored) {
    sessionStorage.setItem('yatoo_auth', '1');
    var params = new URLSearchParams(window.location.search);
    var redirect = params.get('r') || '/index.html';
    window.location.href = redirect;
  } else {
    if (error) { error.classList.add('visible'); }
    input.value = '';
    input.focus();
    setTimeout(function () { if (error) error.classList.remove('visible'); }, 3000);
  }
}

async function sha256(message) {
  var msgBuffer = new TextEncoder().encode(message);
  var hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
  var hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(function (b) { return b.toString(16).padStart(2, '0'); }).join('');
}

/* ── fade-in CSS helper ─────────────────────────────────────────── */
(function () {
  var style = document.createElement('style');
  style.textContent = '.fade-in{opacity:0;transform:translateY(16px);transition:opacity 0.5s,transform 0.5s}.fade-in.visible{opacity:1;transform:none}';
  document.head.appendChild(style);
})();
