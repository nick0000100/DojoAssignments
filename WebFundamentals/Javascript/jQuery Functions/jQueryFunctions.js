$(document).ready(function() {
    //Creates alert onclick
    $("button[name=click]").click(function() {
        alert("sdfsdf");
    });
    //Hides an element onclick
    $("button[name=hide]").click(function(){
        $("#hide").hide();
    });
    //Shows an element onclick
    $("button[name=show]").click(function() {
        $("#hide").show();
    });
    //Toggle show/hidden an element onclick
    $("button[name=toggle]").click(function() {
        $("#toggle").toggle();
    });
    //Slides down the stuff
    $("button[name=slideDown]").click(function() {
        $("#slideDownP").slideDown();
    });
    //Slides up the stuff
    $("button[name=slideUp]").click(function() {
        $("#slideDownP").slideUp();
    });
    //Slides up and down stuff
    $("button[name=slideToggle").click(function() {
        $("#slideToggle").slideToggle();
    });
    $("button[name=fadeIn]").click(function() {
        $("#fade").fadeIn();
    });
    $("button[name=fadeOut]").click(function() {
        $("#fade").fadeOut();
    });
    $("button[name=addClass]").click(function() {
        $("#giveClass").addClass("red");
    });
    $("button[name=before]").click(function() {
        $("button[name=before]").before("<p>NEW HERE BEFORE BUTTON</p>");
    });
    $("button[name=after]").click(function() {
        $("button[name=after]").after("<p>NEW HERE AFTER BUTTON</p>");
    });
    $("button[name=append]").click(function() {
        $("#append li").append("<p>This is new</p>");
    });
    $("button[name=html]").click(function() {
        $("#html li").html("THIS HAS CHANGED");
    });
    $("button[name=attr]").click(function() {
        var check = $("input[name=radio]").attr("name");
        $("#attr li").html(check);
    });
    $("button[name=val]").click(function() {
        var copy = $("#take").val();
        $("input[type=text]").val(copy);
    });
    $("button[name=text]").click(function() {
        var text = $("#text").text();
        console.log(text);
    });
    $("button[name=data]").click(function() {
        $("#data").data("look", "AHHHHH");
        var data = $("#data").data("look");
        console.log(data);
    });
});