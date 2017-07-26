"use strict";

// $(document).ready(function(){
//     $("button").click(function(){
//         var first = $("#first").val();
//         var last = $("#last").val();
//         var description = $("#description").val();
//         $("#cards").append("<div></div>");
//         $("#cards div").last().append("<h2>" + first + " " + last +"</h2>");
//         $("#cards div").last().append("<p>Click for description!</p>");
//         $("#cards div").last().append("<p id='desc'> " + description +"</p>");
//         $("#first").val("");
//         $("#last").val("");
//         $("#description").val("");
//         return false;
//     });
    
//     $(document).on('click', '#cards div', function(){
//         $(this).children().toggle();
//     });
// });


$(document).ready(function(){
    $("button").click(function(){
        var login = $("#first").val();
        $.getJSON("https://api.github.com/users/" + login, function(data) {                   
        var bio = data.bio;                      
        var name = data.name;
        $("#cards").append("<div></div>");
        $("#cards div").last().append("<h2>" + name +"</h2>");
        $("#cards div").last().append("<p>Click for description!</p>");
        $("#cards div").last().append("<p id='desc'> " + bio +"</p>");
        $("#first").val("");
        $("#description").val("");
        });
        return false;
    });
    
    $(document).on('click', '#cards div', function(){
        $(this).children().toggle();
    });
});