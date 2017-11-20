var gulp = require('gulp');
var minifycss = require('gulp-clean-css');
var uglifyjs   = require('gulp-uglify')
var minifyimages = require('gulp-imagemin');
var htmlmin  = require('gulp-htmlmin');


gulp.task('minifycss', function() {
  return gulp.src('./static/css/*.css')
    .pipe(minifycss())
    .pipe(gulp.dest('./static/gulp/'))
})

gulp.task('uglifyjs', function() {
  return gulp.src('./static/js/*.js')
    .pipe(uglifyjs())
    .pipe(gulp.dest('./static/gulp/'))
})

gulp.task('minifyimages', function() {
  return gulp.src('./static/*.png')
    .pipe(minifyimages())
    .pipe(gulp.dest('./static/gulp/'))
})

gulp.task('watch', function() {
  gulp.watch('./static/css/*.css', ['minifycss'])
  gulp.watch('./static/js/*.js', ['uglifyjs'])
  gulp.watch('./static/*.png', ['minifyimages'])
})


gulp.task('default',['watch', 'minifycss', 'uglifyjs', 'minifyimages'] )
