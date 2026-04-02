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
const themeToggleButtons = document.querySelectorAll('[data-theme-toggle]');

function syncThemeMetaColor(theme) {
  const themeMeta = document.querySelector('meta[name="theme-color"]');
  if (!themeMeta) {
    return;
  }
  themeMeta.setAttribute('content', theme === 'light' ? '#ffffff' : '#0a0a0a');
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  document.documentElement.classList.toggle('dark', theme === 'dark');
  localStorage.setItem('theme', theme);
  syncThemeMetaColor(theme);
  syncThemeToggleUI(theme);
}

function syncThemeToggleUI(theme) {
  themeToggleButtons.forEach((button) => {
    const sunIcon = button.querySelector('[data-theme-icon-sun]');
    const moonIcon = button.querySelector('[data-theme-icon-moon]');
    const label = button.querySelector('[data-theme-label]');

    if (sunIcon) {
      sunIcon.classList.toggle('hidden', theme !== 'light');
    }
    if (moonIcon) {
      moonIcon.classList.toggle('hidden', theme === 'light');
    }
    if (label) {
      label.textContent = theme === 'dark' ? 'LIGHT' : 'DARK';
    }
  });
}

if (themeToggleButtons.length > 0) {
  const currentTheme = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  syncThemeMetaColor(currentTheme);
  syncThemeToggleUI(currentTheme);

  themeToggleButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const activeTheme = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
      applyTheme(activeTheme === 'dark' ? 'light' : 'dark');
    });
  });
}

// Greeting Functions
const greetings = [
  'Hello!',
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
    // set first greeting before revealing bubble to avoid empty flash
    idx = 0;
    text.textContent = greetings[idx];
    bubble.style.opacity = '1';
    bubble.style.visibility = 'visible';
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

  return {
    start,
    stop,
    isActive() { return interval !== null; }
  };
}

// attach listeners on DOM ready so we don't rely on inline attributes
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.profile-wrapper').forEach(wrapper => {
    const controller = createGreetingController(wrapper);

    wrapper.addEventListener('mouseenter', controller.start);
    wrapper.addEventListener('mouseleave', controller.stop);

    // touch/click alternator for mobile/laptop;
    // use controller.isActive() to check running state
    wrapper.addEventListener('touchstart', e => {
      e.preventDefault();
      if (controller.isActive()) {
        controller.stop();
      } else {
        controller.start();
      }
    });
    wrapper.addEventListener('click', () => {
      if (controller.isActive()) {
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