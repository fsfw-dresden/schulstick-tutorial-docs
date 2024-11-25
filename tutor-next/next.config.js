/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  distDir: 'export',
  images: {
    unoptimized: true
  },
  basePath: ''
}

module.exports = nextConfig
