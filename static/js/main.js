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
  { text: 'Hello!', lang: 'English' },
  { text: 'नमस्ते', lang: 'Hindi' },
  { text: 'Hola!', lang: 'Spanish' },
  { text: 'Bonjour!', lang: 'French' },
  { text: 'Hallo!', lang: 'German' },
  { text: 'こんにちは', lang: 'Japanese' },
  { text: '你好', lang: 'Chinese' },
  { text: '안녕하세요', lang: 'Korean' }
];

let currentGreetingIndex = 0;
let greetingInterval = null;
let isHovering = false;

const avatarContainer = document.querySelector('.avatar-container');
const greetingText = document.getElementById('greeting-text');
const languageDots = document.querySelectorAll('.language-dots span');

function updateGreeting() {
  if (!greetingText) return;
  
  // Update greeting text with fade animation
  greetingText.style.opacity = '0';
  
  setTimeout(() => {
    greetingText.textContent = greetings[currentGreetingIndex].text;
    greetingText.style.opacity = '1';
    
    // Update language dots
    languageDots.forEach((dot, index) => {
      dot.classList.toggle('active', index === currentGreetingIndex);
    });
    
    // Move to next greeting
    currentGreetingIndex = (currentGreetingIndex + 1) % greetings.length;
  }, 200);
}

function startGreetingCycle() {
  if (!avatarContainer) return;
  
  isHovering = true;
  // Start cycling every 2 seconds
  greetingInterval = setInterval(updateGreeting, 2000);
}

function stopGreetingCycle() {
  isHovering = false;
  if (greetingInterval) {
    clearInterval(greetingInterval);
    greetingInterval = null;
  }
  // Reset to first greeting
  currentGreetingIndex = 0;
  if (greetingText) {
    greetingText.textContent = greetings[0].text;
  }
  // Reset dots
  languageDots.forEach((dot, index) => {
    dot.classList.toggle('active', index === 0);
  });
}

// Add event listeners
if (avatarContainer) {
  avatarContainer.addEventListener('mouseenter', startGreetingCycle);
  avatarContainer.addEventListener('mouseleave', stopGreetingCycle);
  
  // Also handle touch events for mobile
  avatarContainer.addEventListener('touchstart', () => {
    if (!isHovering) {
      startGreetingCycle();
    }
  });
}
