import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    rollupOptions: {
      output: {
        assetFileNames: (assetInfo) => {
          // Garde les vidéos dans assets/videos/ avec leur nom original
          if (/\.(mp4|webm|ogg)$/.test(assetInfo.name)) {
            return 'assets/videos/[name][extname]'
          }
          // Autres assets avec hash pour cache-busting
          return 'assets/[name]-[hash][extname]'
        }
      }
    }
  },
  // Assure que les vidéos sont traitées comme des assets
  assetsInclude: ['**/*.mp4', '**/*.webm', '**/*.ogg'],
  // Public directory pour les fichiers statiques
  publicDir: 'public'
})
