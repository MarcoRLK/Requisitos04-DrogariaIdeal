var gulp = require('gulp');
var minifycss = require('gulp-clean-css');
var uglifyjs   = require('gulp-uglify')
var minifyimages = require('gulp-imagemin');
var htmlmin  = require('gulp-htmlmin');


gulp.task('minifycss', function() {
  return gulp.src('DrogariaIdeal/static/css/*.css')
    .pipe(minifycss())
    .pipe(gulp.dest('DrogariaIdeal/static/gulp'))
})

gulp.task('uglifyjs', function() {
  return gulp.src('DrogariaIdeal/static/js/*.js')
    .pipe(uglifyjs())
    .pipe(gulp.dest('DrogariaIdeal/static/gulp'))
})

gulp.task('minifyimages', function() {
  return gulp.src('DrogariaIdeal/static/*.png')
    .pipe(minifyimages())
    .pipe(gulp.dest('DrogariaIdeal/static/gulp'))
})

gulp.task('watch', function() {
  gulp.watch('DrogariaIdeal/static/css/*.css', ['minifycss'])
  gulp.watch('DrogariaIdeal/static/js/*.js', ['uglifyjs'])
  gulp.watch('DrogariaIdeal/static/*.png', ['minifyimages'])
})


gulp.task('default',['watch', 'minifycss', 'uglifyjs', 'minifyimages'] )
