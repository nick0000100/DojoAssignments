$(document).ready(function() {
    $("form").submit(function() {
        var first = $("#first").val();
        var last = $("#last").val();
        var email = $("#email").val();
        var contact = $("#contact").val();
        $("tbody").append("<tr></tr>");
        $("tr").last().append("<td>" + first + "</td>");
        $("tr").last().append("<td>" + last + "</td>");
        $("tr").last().append("<td>" + email + "</td>");
        $("tr").last().append("><td>" + contact + "</td>");
        return false;
    });
});