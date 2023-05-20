"use strict";
/// Dæmi A
document.getElementsByTagName("div")[0].setAttribute("class", "changeColor"); 


/// Dæmi B
var last_elem = document.getElementsByTagName("div")[2];
last_elem.parentNode.removeChild(last_elem);
