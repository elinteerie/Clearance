/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors:{
        light_green:"#9FB59F",
        dark_green:"#0A270A",
        brown:"#7C4D4D",
        light_brown:"#F9ECEC"
      },
      // backgroundImage:{
      //   bg_img:'url(./public/assets/images/school_gate.png)'
      // }
    },
  },
  plugins: [],
}
