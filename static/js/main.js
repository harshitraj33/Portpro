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