let cur = 1;
const total = 12;

function go(n) {
  const prev = document.getElementById('slide-' + cur);
  if (prev) prev.classList.remove('active');
  cur = Math.max(1, Math.min(n, total));
  const next = document.getElementById('slide-' + cur);
  if (next) next.classList.add('active');
  document.getElementById('nc').textContent = cur + ' / ' + total;
}

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown')  go(cur + 1);
  if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')    go(cur - 1);
  if (e.key === 'f' || e.key === 'F') toggleFs();
  if (e.key === 'n' || e.key === 'N') toggleNotes();
  if (e.key === 'Escape') { if (document.fullscreenElement) document.exitFullscreen(); }
});

function toggleFs() {
  if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {});
  else document.exitFullscreen();
}

function toggleNotes() {
  document.body.classList.toggle('show-notes');
}

document.addEventListener('DOMContentLoaded', () => go(1));
