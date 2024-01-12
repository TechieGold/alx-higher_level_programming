/* global $ */

// This script fetches the character 'name' from a url using API.
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/1/?format=json', function (data) {
    $('#character').text(data.name);
  });
});
