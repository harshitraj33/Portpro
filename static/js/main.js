// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

if (mobileMenuBtn && mobileMenu) {
  mobileMenuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
    const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
    mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
  });
}

// Theme Toggle Functionality
const themeToggleButton = document.getElementById('theme-toggle');
const sunIcon = document.getElementById('sun-icon');
const moonIcon = document.getElementById('moon-icon');

if (themeToggleButton) {
  if (
    localStorage.getItem('theme') === 'dark' ||
    (!('theme' in localStorage) &&
      window.matchMedia('(prefers-color-scheme: dark)').matches)
  ) {
    sunIcon.classList.remove('hidden');
    moonIcon.classList.add('hidden');
  } else {
    sunIcon.classList.add('hidden');
    moonIcon.classList.remove('hidden');
  }

  themeToggleButton.addEventListener('click', () => {
    sunIcon.classList.toggle('hidden');
    moonIcon.classList.toggle('hidden');

    if (document.documentElement.classList.contains('dark')) {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    } else {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
  });
}

// Greeting Functions
const greetings = [
  'नमस्ते',
  'Hola!',
  'Bonjour!',
  'Hallo!',
  'こんにちは',
  '你好',
  '안녕하세요'
];

// We'll track the interval per wrapper so multiple components won't interfere.
function createGreetingController(wrapper) {
  const bubble = wrapper.querySelector('.greeting-bubble');
  const text = wrapper.querySelector('.greeting-text');
  let idx = 0;
  let interval = null;

  function start() {
    if (interval) return;
    bubble.style.opacity = '1';
    bubble.style.visibility = 'visible';
    idx = 0;
    text.textContent = greetings[idx];
    interval = setInterval(() => {
      idx = (idx + 1) % greetings.length;
      text.textContent = greetings[idx];
    }, 2000);
  }

  function stop() {
    if (interval) {
      clearInterval(interval);
      interval = null;
    }
    bubble.style.opacity = '0';
    bubble.style.visibility = 'hidden';
    text.textContent = '';
  }

  return { start, stop };
}

// attach listeners on DOM ready so we don't rely on inline attributes
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.profile-wrapper').forEach(wrapper => {
    const controller = createGreetingController(wrapper);

    function enterHandler() {
      controller.start();
    }
    function leaveHandler() {
      controller.stop();
    }

    wrapper.addEventListener('mouseenter', enterHandler);
    wrapper.addEventListener('mouseleave', leaveHandler);

    // touch/click alternator for mobile/laptop
    wrapper.addEventListener('touchstart', e => {
      e.preventDefault();
      if (controller.interval) {
        controller.stop();
      } else {
        controller.start();
      }
    });
    wrapper.addEventListener('click', () => {
      if (controller.interval) {
        controller.stop();
      } else {
        controller.start();
      }
    });
  });
});

// keep globals for backwards compatibility (inline handlers still work)
window.startGreeting = function(event) {
  const wrapper = event.target.closest('.profile-wrapper');
  if (!wrapper) return;
  const { start } = createGreetingController(wrapper);
  start();
};
window.stopGreeting = function(event) {
  const wrapper = event.target.closest('.profile-wrapper');
  if (!wrapper) return;
  const { stop } = createGreetingController(wrapper);
  stop();
};