/** @type {import('prettier').Config} */
module.exports = {
  printWidth: 80,
  semi: false,
  singleQuote: true,
  trailingComma: 'all',

  pluginSearchDirs: false,
  plugins: [
    require('prettier-plugin-packagejson'),
    require('prettier-plugin-tailwindcss'),
  ],
}
