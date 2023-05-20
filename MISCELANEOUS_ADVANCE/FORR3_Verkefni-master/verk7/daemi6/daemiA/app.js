"use strict";

function myFunction(event) { 
    var x = event.target;
    var elem = document.getElementsByTagName("SPAN");
    
    for (var i = 0; i < elem.length; i++){
    	if (elem[i].textContent === x.textContent){
        	elem[i].setAttribute("class", "redColor");
        }
    }
}