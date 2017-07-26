"use strict";

$(document).ready(function(){
    $("button").click(function(){
        var login = $("#login").val();
        $.getJSON("https://api.github.com/users/" + login, function(data) {                   
        var bio = data.bio;                      
        var name = data.name;
        $("#cards").append("<div></div>");
        $("#cards div").last().append("<h2>" + name +"</h2>");
        $("#cards div").last().append("<p>Click for description!</p>");
        $("#cards div").last().append("<p id='desc'> " + bio +"</p>");
        $("#first").val("");
        });
        return false;
    });
    
    $(document).on('click', '#cards div', function(){
        $(this).children().toggle();
    });
});