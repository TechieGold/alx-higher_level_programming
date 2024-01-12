/* global $ */

// This script fetches a value from URL and display the content.
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
