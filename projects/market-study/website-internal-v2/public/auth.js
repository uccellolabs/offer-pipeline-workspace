/**
 * Protection client-side simple par mot de passe.
 * SHA-256 du mot de passe stocké en clair dans le code (security through obscurity).
 *
 * Ce n'est PAS de la sécurité robuste — c'est un gate pour empêcher l'indexation
 * et les visites accidentelles. Pour une protection réelle, utiliser Cloudflare Access,
 * Netlify Identity, ou une auth serveur.
 *
 * Pour changer le mot de passe :
 *   1. Choisir un mot de passe (ex : "offerpipeline2026")
 *   2. Calculer le SHA-256 :
 *        echo -n "offerpipeline2026" | shasum -a 256
 *   3. Remplacer EXPECTED_HASH ci-dessous
 *
 * Mot de passe par défaut : "offerpipeline2026"
 */

const EXPECTED_HASH = 'a6c30c3de4dde658057bda5e2e6d6e4c0c9a72a9e6b34b97a0e7ef7e9a1b8b5e';
// ↑ placeholder à recalculer côté Jonathan une fois le vrai mot de passe choisi
//   (la valeur ci-dessus n'est pas valide — voir README pour la procédure)

const STORAGE_KEY = 'op-internal-auth';
const SESSION_DURATION_MS = 1000 * 60 * 60 * 12; // 12 heures

async function sha256(str) {
  const buf = new TextEncoder().encode(str);
  const hashBuf = await crypto.subtle.digest('SHA-256', buf);
  return Array.from(new Uint8Array(hashBuf))
    .map((b) => b.toString(16).padStart(2, '0'))
    .join('');
}

function isAuthenticated() {
  try {
    const raw = sessionStorage.getItem(STORAGE_KEY);
    if (!raw) return false;
    const { hash, exp } = JSON.parse(raw);
    if (Date.now() > exp) {
      sessionStorage.removeItem(STORAGE_KEY);
      return false;
    }
    return hash === EXPECTED_HASH;
  } catch {
    return false;
  }
}

function setAuthenticated() {
  sessionStorage.setItem(
    STORAGE_KEY,
    JSON.stringify({ hash: EXPECTED_HASH, exp: Date.now() + SESSION_DURATION_MS })
  );
}

function logout() {
  sessionStorage.removeItem(STORAGE_KEY);
  window.location.href = '/login/';
}

// Gate : si on n'est pas sur /login/ et pas authentifié → redirection
function gate() {
  const path = window.location.pathname;
  const onLogin = path === '/login' || path === '/login/' || path.endsWith('/login/index.html');
  if (!onLogin && !isAuthenticated()) {
    const next = encodeURIComponent(path + window.location.search);
    window.location.href = `/login/?next=${next}`;
  }
}

// Login form handler
async function handleLogin(e) {
  e.preventDefault();
  const form = e.target;
  const input = form.querySelector('input[name="password"]');
  const errEl = document.getElementById('login-error');
  if (errEl) errEl.textContent = '';
  const hash = await sha256(input.value);
  if (hash === EXPECTED_HASH) {
    setAuthenticated();
    const params = new URLSearchParams(window.location.search);
    const next = params.get('next') || '/';
    window.location.href = next;
  } else {
    if (errEl) errEl.textContent = 'Mot de passe incorrect.';
    input.value = '';
    input.focus();
  }
}

// Bind logout
function bindLogout() {
  document.querySelectorAll('[data-logout]').forEach((el) => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      logout();
    });
  });
}

// Init
if (typeof window !== 'undefined') {
  window.addEventListener('DOMContentLoaded', () => {
    gate();
    bindLogout();
    const form = document.getElementById('login-form');
    if (form) form.addEventListener('submit', handleLogin);
  });
}
