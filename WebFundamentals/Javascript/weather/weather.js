"use strict";

$(document).ready(function() {
    $('form').submit(function() {
        
        // Gets items for url
        var url = "http://api.openweathermap.org/data/2.5/weather?q=";
        var key = "&&appid=3edd1206c4f698f92edcc1367b545b85";
        var location = $("#location").val();
        $.get(url + location + key, function(data) {
            console.log(data);
            // Finds variables
            var name = data.name;
            var temperature = data.main.temp;
            temperature = Math.floor(temperature * (9/5) - 459.67);

            // Adds to screen
            $("div").html("<h1>" + name + "</h1>");
            $("div").append("<p>Temperature: " + temperature + "</p>");
        }, 'json');
        return false;
    });
});
