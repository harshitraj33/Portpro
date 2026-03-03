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

let greetingInterval = null;

function startGreeting(event) {
  const wrapper = event.target.closest('.profile-wrapper');
  if (!wrapper) return;

  const bubble = wrapper.querySelector('.greeting-bubble');
  const text = wrapper.querySelector('.greeting-text');

  if (greetingInterval) return;

  bubble.style.opacity = '1';
  bubble.style.visibility = 'visible';

  let index = 0;
  text.textContent = greetings[index];

  greetingInterval = setInterval(() => {
    index = (index + 1) % greetings.length;
    text.textContent = greetings[index];
  }, 2000);
}

function stopGreeting(event) {
  const wrapper = event.target.closest('.profile-wrapper');
  if (!wrapper) return;

  const bubble = wrapper.querySelector('.greeting-bubble');
  const text = wrapper.querySelector('.greeting-text');

  clearInterval(greetingInterval);
  greetingInterval = null;

  bubble.style.opacity = '0';
  bubble.style.visibility = 'hidden';
  text.textContent = '';
}

window.startGreeting = startGreeting;
window.stopGreeting = stopGreeting;