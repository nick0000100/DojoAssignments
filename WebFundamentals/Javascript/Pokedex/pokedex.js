"use strict";

$(document).ready(function() {
    var url = "http://pokeapi.co/media/img/";
    for(var i = 1; i <= 151; i++) {
        $("#pokemon").append("<img id='" + i +"' src=" + url + i + ".png>");
        console.log()
    }
    $(document).on("click", "img", function() {
        var pokeURL = "http://pokeapi.co/api/v2/";
        var id = $(this).attr("id");
        console.log(id);
        $.getJSON(pokeURL + "pokemon/" + id + "/", function(data) {

            // Resets info box
            $("#info").html("");

            // Gets the information from the JSON object
            var height = data.height;
            var weight = data.weight;
            var name = data.name;
            var type = [];
            for(var i = 0; i <= data.types.length - 1; i++) {
                type.push(data.types[i].type.name);
            }

            // Adds name
            $("#info").append("<h2>" + name + "</h2>");

            // Adds image
            $("#info").append("<img src=" + url + data.id + ".png>")
            
            // Adds Types
            $("#info").append("<h3>Types</h3>");
            for(var i = 0; i <= type.length - 1; i++) {
                $("#info").append("<li>" + type[i] + "</li>");
            }

            // Adds Height and Weight
            $("#info").append("<h3>Height</h3><p>" + height + "</p>");
            $("#info").append("<h3>Weight</h3><p>" + weight + "</p>");
        }, "json");
    });
});