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
  'Hello!',
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

function startGreeting() {
  const bubble = document.getElementById('greeting-bubble');
  const text = document.getElementById('greeting-text');
  
  if (bubble && text) {
    bubble.style.opacity = '1';
    greetingInterval = setInterval(function() {
      text.textContent = greetings[greetingIndex];
      greetingIndex = (greetingIndex + 1) % greetings.length;
    }, 2000);
  }
}

function stopGreeting() {
  const bubble = document.getElementById('greeting-bubble');
  const text = document.getElementById('greeting-text');
  
  if (greetingInterval) {
    clearInterval(greetingInterval);
    greetingInterval = null;
  }
  
  if (bubble) {
    bubble.style.opacity = '0';
  }
  
  greetingIndex = 0;
  if (text) {
    text.textContent = 'Hello!';
  }
}

window.startGreeting = startGreeting;
window.stopGreeting = stopGreeting;

import { SpeedInsights } from '@vercel/speed-insights/next';
export default function RootLayout({
  children,
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <SpeedInsights />
      </body>
    </html>
  );
}