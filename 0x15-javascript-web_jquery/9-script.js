$(document).ready(function (){
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data){

    var name = data.hello;
    $("#hello").text(name);

    });
});
