// This script fetches and lists the title
// for all movie using a url.
$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
        $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
    });
});
