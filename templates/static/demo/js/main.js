$(function(){
	var availableTags = [
	    "Chicken",
	    "Spinach",
	    "Apple",
	    "Tofu",
	    "Noodle",
	    "Carrot",
	    "Beef",
	    "Fish",
	    "Cabbage",
	    
	];
	$('#myAutocomplete').autocomplete({
        source: availableTags,
        multiselect: true
    });

    
});

/*$(document).ready(function () {
    $('#myAutocomplete').on('change', function () {
        $('#tagsname').html('You selected: ' + this.value);
    }).change();
    $('#myAutocomplete').on('autocompleteselect', function (e, ui) {
        $('#tagsname').html('You selected: ' + ui.item.value);
    });
});*/

