import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://offer-pipeline-internal.uccello.io',
  output: 'static',
  build: {
    format: 'directory',
  },
  compressHTML: true,
});
