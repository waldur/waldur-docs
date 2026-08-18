import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [react()],
  // Relative base is mandatory: mike publishes the docs site under version
  // prefixes (/latest/, /8.0.5/, ...), so absolute asset paths would 404 on
  // every published version.
  base: './',
  build: {
    outDir: '../docs/developer-guide/oidc-explainer/app',
    emptyOutDir: true,
  },
});
