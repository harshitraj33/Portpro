// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

if (mobileMenuBtn && mobileMenu) {
  mobileMenuBtn.addEventListener('click', () => {
    // Toggle the hidden class to show/hide menu
    mobileMenu.classList.toggle('hidden');
    
    // Update aria-expanded attribute
    const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
    mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
  });
}

// Theme Toggle Functionality
const themeToggleButton = document.getElementById('theme-toggle');
const sunIcon = document.getElementById('sun-icon');
const moonIcon = document.getElementById('moon-icon');

// This script runs after the DOM is loaded.
// The initial theme is already set by the script in the <head> to prevent FOUC.

if (themeToggleButton) {
  // Set the initial state of the icon based on the current theme.
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
    // Toggle icons
    sunIcon.classList.toggle('hidden');
    moonIcon.classList.toggle('hidden');

    // Toggle theme and update localStorage
    if (document.documentElement.classList.contains('dark')) {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    } else {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
  });
}

// =========================================
// Avatar Multi-language Greeting
// =========================================

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

const avatarFrame = document.querySelector('.avatar-frame');
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
  if (!avatarFrame) return;
  
  // Start cycling every 1.5 seconds
  greetingInterval = setInterval(updateGreeting, 1500);
}

function stopGreetingCycle() {
  if (greetingInterval) {
    clearInterval(greetingInterval);
    greetingInterval = null;
  }
  // Reset to first greeting
  currentGreetingIndex = 0;
  if (greetingText) {
    greetingText.textContent = greetings[0];
  }
}

// Add event listeners
if (avatarFrame) {
  avatarFrame.addEventListener('mouseenter', startGreetingCycle);
  avatarFrame.addEventListener('mouseleave', stopGreetingCycle);
  
  // Touch support for mobile
  avatarFrame.addEventListener('touchstart', function() {
    if (!greetingInterval) {
      startGreetingCycle();
    }
  });
}
