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

let greetingIntervals = {}; // Store intervals per profile wrapper
let activeGreeting = null; // Track currently active greeting wrapper

function startGreeting(event) {
  // Find the profile wrapper (parent of the hovered element)
  const target = event.target.closest('.profile-wrapper');
  if (!target) return;
  
  const wrapperId = target.dataset.wrapperId || 'default';
  
  // If this wrapper already has an active greeting, don't restart
  if (activeGreeting === wrapperId) return;
  
  // Stop any existing greeting first
  stopGreeting(event);
  
  const bubble = target.querySelector('.greeting-bubble');
  const text = target.querySelector('.greeting-text');
  
  if (bubble && text) {
    activeGreeting = wrapperId;
    
    // Show bubble
    bubble.style.opacity = '1';
    bubble.style.visibility = 'visible';
    
    // Start cycling greetings
    let index = 0;
    text.textContent = greetings[index];
    index = 1;
    
    greetingIntervals[wrapperId] = setInterval(function() {
      text.textContent = greetings[index];
      index = (index + 1) % greetings.length;
    }, 2000);
  }
}

function stopGreeting(event) {
  if (!activeGreeting) return;
  
  // Find the profile wrapper if event provided
  let target = null;
  if (event) {
    target = event.target.closest('.profile-wrapper');
  }
  
  // If no target from event, find the active one
  if (!target) {
    target = document.querySelector(`.profile-wrapper[data-wrapper-id="${activeGreeting}"]`);
  }
  
  if (target) {
    const wrapperId = target.dataset.wrapperId || 'default';
    const bubble = target.querySelector('.greeting-bubble');
    const text = target.querySelector('.greeting-text');
    
    // Clear interval
    if (greetingIntervals[wrapperId]) {
      clearInterval(greetingIntervals[wrapperId]);
      delete greetingIntervals[wrapperId];
    }
    
    // Hide bubble
    if (bubble) {
      bubble.style.opacity = '0';
      bubble.style.visibility = 'hidden';
    }
    
    // Reset text
    if (text) {
      text.textContent = '';
    }
  }
  
  activeGreeting = null;
}

// Expose functions globally for inline event handlers
window.startGreeting = startGreeting;
window.stopGreeting = stopGreeting;
