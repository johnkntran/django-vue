import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    manifest: true,
    sourcemap: true,
    lib: {
      entry: path.resolve(__dirname, 'src/main.js'),
      name: 'viteLib',
      format: ['es', 'umd'],
      fileName: (format) => `vite-lib.${format}.js`,
    },
  },
});
