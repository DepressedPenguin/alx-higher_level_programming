$(document).ready(function () {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
        var titles = [];
        
        for (var i = 0; i < data.length; i++) {
            titles.push(data[i].title);
        }

        $("#list_movies").text(titles);
    });
});
