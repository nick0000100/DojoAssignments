$(document).ready(function() {
    $("img").click(function() {
        var newSource = $(this).attr("data-alt-src");
        var oriSource = $(this).attr("src");
        $(this).attr("data-alt-src", oriSource);
        $(this).attr("src", newSource);
    });
});