module.exports = {
  publicPath: 'http://localhost:8000/', // Change this to match your host name
  outputDir: './stocks/static', // This is the default, app-level static folder
  filenameHashing: false,
  configureWebpack: {
    entry: {
      app: './stocks/src/main.js',
    },
  },
};
