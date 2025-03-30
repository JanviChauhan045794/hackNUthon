import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      animation: {
        aurora: "aurora 60s linear infinite",
      },
      keyframes: {
        aurora: {
          "0%": { backgroundPosition: "0% 50%, 0% 50%" },
          "50%": { backgroundPosition: "100% 50%, 100% 50%" },
          "100%": { backgroundPosition: "0% 50%, 0% 50%" },
        },
      },
    },
  },
  darkMode: "class",
  plugins: [],
};

export default config; 