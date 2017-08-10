"use strict";

$(document).ready(function() {
    var url = "http://localhost:5000/"
    $("red").click(function() {
        // $.get(url + "static/img/raphael", function(data) {
        //     console.log(data)

            // Adds to Screen
            $("div").html("<img src={{ url_for('static', filename='imgs/donatello.jpg') }}>");
        // }, "json");
    });
        // return false;
});