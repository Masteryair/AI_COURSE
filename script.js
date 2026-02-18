// Extra JS for accessibility and focus
// (Chart.js logic is inlined in index.html, but you can move it here if you want)
document.addEventListener('DOMContentLoaded', function() {
  // Focus first slider for accessibility
  var firstSlider = document.querySelector('.controls input[type="range"]');
  if(firstSlider) firstSlider.focus();
  // Keyboard shortcuts for reset buttons
  document.querySelectorAll('.controls button').forEach(btn => {
    btn.addEventListener('keyup', function(e) {
      if(e.key === 'Enter' || e.key === ' ') btn.click();
    });
  });
});
