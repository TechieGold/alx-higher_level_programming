// This script updates the text of header element to New Header!!
// when the user clicks on DIV#update_header
$(document).ready(function() {
    $('DIV#update_header').click(function() {
        $('header').text('New Header!!!');
    });
});
