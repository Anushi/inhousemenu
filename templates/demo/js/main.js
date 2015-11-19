$(function () {
    var availableTags = [
        "ActionScript",
        "AppleScript",
        "Asp",
        "BASIC",
        "C",
        "C++",
        "Clojure",
        "COBOL",
        "ColdFusion",
        "Erlang",
        "Fortran",
        "Groovy",
        "Haskell",
        "Java",
        "JavaScript",
        "Lisp",
        "Perl",
        "PHP",
        "Python",
        "Ruby",
        "Scala",
        "Scheme"];
    $("#tags").autocomplete({
        source: availableTags
    });
});

$(document).ready(function () {
    $('#myAutocomplete').on('change', function () {
        $('#tagsname').html('You selected: ' + this.value);
    }).change();
    $('#myAutocomplete').on('autocompleteselect', function (e, ui) {
        $('#tagsname').html('You selected: ' + ui.item.value);
    });
});