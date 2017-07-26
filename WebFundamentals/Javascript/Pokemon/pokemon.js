"use strict";

$(document).ready(function() {
    var url = "http://pokeapi.co/media/img/";
    for(var i = 1; i <= 151; i++) {
        $("div").append("<img src=" + url + i + ".png>");
        console.log()
    }
});