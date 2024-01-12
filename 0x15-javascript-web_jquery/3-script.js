/* global $ */

// This script adds the class red of the header element
// when the user click on the tag  DIV#red_header

$('DIV#red_header').click(function () {
  $('HEADER').addClass('red');
});
