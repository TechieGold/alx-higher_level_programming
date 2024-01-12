/* global $ */

// This script updates the text color of the header element
// When the user click on the tag  DIV#red_header

$('DIV#red_header').click(function () {
  $('HEADER').css('#FF0000');
});
