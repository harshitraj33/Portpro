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

let greetingIndex = 0;
let greetingInterval = null;
let isGreetingActive = false;

function startGreeting() {
  const bubble = document.getElementById('greeting-bubble');
  const text = document.getElementById('greeting-text');
  
  if (bubble && text && !isGreetingActive) {
    isGreetingActive = true;
    // Clear any existing interval to prevent multiple intervals
    if (greetingInterval) {
      clearInterval(greetingInterval);
    }
    // Show bubble first
    bubble.style.opacity = '1';
    bubble.style.visibility = 'visible';
    // Immediately show first greeting and start cycling
    greetingIndex = 0;
    text.textContent = greetings[greetingIndex];
    greetingIndex = 1;
    greetingInterval = setInterval(function() {
      text.textContent = greetings[greetingIndex];
      greetingIndex = (greetingIndex + 1) % greetings.length;
    }, 2000);
  }
}

function stopGreeting() {
  const bubble = document.getElementById('greeting-bubble');
  const text = document.getElementById('greeting-text');
  
  isGreetingActive = false;
  
  if (greetingInterval) {
    clearInterval(greetingInterval);
    greetingInterval = null;
  }
  
  if (bubble) {
    bubble.style.opacity = '0';
    bubble.style.visibility = 'hidden';
  }
  
  greetingIndex = 0;
  if (text) {
    text.textContent = '';
  }
}

// Add event listeners for both hover and click (for better laptop support)
document.addEventListener('DOMContentLoaded', function() {
  const profileContainer = document.querySelector('.rounded-full.overflow-hidden');
  
  if (profileContainer) {
    // Mouse events for desktop
    profileContainer.addEventListener('mouseenter', startGreeting);
    profileContainer.addEventListener('mouseleave', stopGreeting);
    
    // Touch events for mobile
    profileContainer.addEventListener('touchstart', function(e) {
      e.preventDefault();
      if (isGreetingActive) {
        stopGreeting();
      } else {
        startGreeting();
      }
    });
    
    // Click fallback for laptops that might have issues with hover
    profileContainer.addEventListener('click', function() {
      if (isGreetingActive) {
        stopGreeting();
      } else {
        startGreeting();
      }
    });
  }
});

window.startGreeting = startGreeting;
window.stopGreeting = stopGreeting;
