// This script updates the text color of the header element
// When the user click on the tag  DIV#red_header

$(document).ready(function() {
    $('#red_header').click(function() {
        const header = $('header');

        header.css('color', '#FF0000');
    });
});
