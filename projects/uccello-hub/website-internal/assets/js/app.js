// Active nav link highlight
(function () {
  var links = document.querySelectorAll('.nav-links a');
  var current = window.location.pathname.split('/').pop() || 'index.html';
  links.forEach(function (a) {
    if (a.getAttribute('href') === current) a.classList.add('active');
  });
}());
