import flowbitePlugin from 'flowbite/plugin'
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}', './node_modules/flowbite/**/*.js'],
  theme: {
    extend: {
      colors: {
        brand: {
          softer: '#EBF5FF',
          strong: '#1E429F',
          100: '#979dac', // Gri-albăstrui deschis
          200: '#7d8597', // Gri-albăstrui mediu
          300: '#5c677d', // Gri-albăstrui mai închis
          400: '#33415c', // Gri-albăstrui spre bleumarin
          500: '#0466c8', // Albastrul vibrant (Culoarea principală/de bază)
          600: '#0353a4', // Albastru închis
          700: '#023e7d', // Albastru marin
          800: '#002855', // Bleumarin închis
          900: '#001845', // Cel mai închis bleumarin
        },
      },
    },
  },
  plugins: [flowbitePlugin],
}
