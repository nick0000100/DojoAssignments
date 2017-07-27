"use strict";

$(document).ready(function() {
    $("img").click(function() {
        var url = "https://anapioficeandfire.com/api/houses/";
        var id = $(this).attr("id");
        $.getJSON(url + id + "/", function(data) {
            $("#info").html("");
            var name = data.name;
            var words = data.words;
            console.log(name);
            console.log(words);
            var titles = [];
            for(var i = 0; i <= data.titles.length - 1; i++) {
                titles.push(data.titles[i]);
            }
            titles = titles.toString();

            // Append things
            $("#info").append("<p>Name: " + name + "</p>");
            $("#info").append("<p>Words: " + words + "</p>");
            $("#info").append("<p>Titles: " + titles + "</p>");
        });
    });
});