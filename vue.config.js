module.exports = {
  publicPath: 'http://localhost:8000/', // Change this to match your host name
  outputDir: './stocks/static', // This is the default, app-level static folder
  filenameHashing: false,
  chainWebpack: (config) => {
    // Use a webpack.config.js to determine what keys to delete
    config.plugins.delete('prefetch');
    config.plugins.delete('splitVendor');
    config.optimization.delete('splitChunks');
  },
  configureWebpack: {
    entry: {
      app: './stocks/src/main.js',
    },
    optimization: {
      splitChunks: false,
    },
  },
};
