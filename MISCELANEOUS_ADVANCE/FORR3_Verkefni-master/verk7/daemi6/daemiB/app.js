"use strict";

function myFunction(event) { 
    //var x = event.target;
    var elem = document.getElementsByTagName("SPAN");
    elem.addEventListener("touchend", pressButton);
    
    //for (var i = 0; i < elem.length; i++){
    //	if (elem[i].textContent === x.textContent){
    //    	elem[i].setAttribute("class", "redColor");
    //    }
    //}
}


// Dæmi B
function pressButton(e)
{
    e.target.style.backgroundColor = "red";
}
