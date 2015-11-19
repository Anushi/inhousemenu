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
})