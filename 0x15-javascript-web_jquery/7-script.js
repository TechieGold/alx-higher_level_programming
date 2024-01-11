// This script that fetches the character name from a url.
$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/people/1/?format=json', function(data) {
        $('#character').text(data.name);
    });
});
