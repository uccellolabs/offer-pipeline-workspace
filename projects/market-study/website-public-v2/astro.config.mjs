import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://offer-pipeline.uccello.io',
  output: 'static',
  build: {
    format: 'directory',
  },
  compressHTML: true,
});
