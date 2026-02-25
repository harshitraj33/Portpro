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

// Avatar Multi-language Greeting
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

let currentGreetingIndex = 0;
let greetingInterval = null;

const avatarContainer = document.querySelector('.avatar-container');
const greetingText = document.getElementById('avatar-greeting');

function updateGreeting() {
  if (!greetingText) return;
  
  greetingText.style.opacity = '0';
  
  setTimeout(() => {
    greetingText.textContent = greetings[currentGreetingIndex];
    greetingText.style.opacity = '1';
    currentGreetingIndex = (currentGreetingIndex + 1) % greetings.length;
  }, 150);
}

function startGreetingCycle() {
  if (!avatarContainer) return;
  greetingInterval = setInterval(updateGreeting, 2000);
}

function stopGreetingCycle() {
  if (greetingInterval) {
    clearInterval(greetingInterval);
    greetingInterval = null;
  }
  currentGreetingIndex = 0;
  if (greetingText) {
    greetingText.textContent = greetings[0];
  }
}

if (avatarContainer) {
  avatarContainer.addEventListener('mouseenter', startGreetingCycle);
  avatarContainer.addEventListener('mouseleave', stopGreetingCycle);
  
  avatarContainer.addEventListener('touchstart', function() {
    if (!greetingInterval) {
      startGreetingCycle();
    }
  });
}
