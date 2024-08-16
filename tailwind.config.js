/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './main/templates/**/*.html',
      './main/templates/forms.py',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    colors: {
      'main': {
        light: '#6F82B5',
        DEFAULT: '#4F669C',
        dark: '#3E517A',
      }},
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}