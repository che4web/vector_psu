import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import pugPlugin from "vite-plugin-pug"
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),pugPlugin(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
    build:{
        assetsDir:'static'
    },
 
    server:{
   proxy: {
      "^/api": {
        "target": "http://127.0.0.1:8000",
        "ws": true,
        "changeOrigin": true
      },
      "^/admin": {
        "target": "http://127.0.0.1:8000",
        "ws": true,
        "changeOrigin": true
      },

      "^/media": {
        "target": "http://127.0.0.1:8000",
        "ws": true,
        "changeOrigin": true
      },
        }
    }
})
