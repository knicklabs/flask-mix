const mix = require('laravel-mix')

mix
    .postCss('css/app.css', '../static/css')
    .js('js/app.js', '../static/js')
    .version()
    .setPublicPath('../static')
