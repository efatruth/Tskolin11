"use strict";
function pizza(name, price, size, toppings){
	var pizza_text = size + " " + name.bold() + "(" + toppings + ") kr. " + price;
	return pizza_text;
}

var pizza_1 = pizza("Magherita", "2195", "Stór", ["ostur", "oregano"]);
var pizza_2 = pizza("Pepperoni", "4000", "Miðlungs", ["rjómaostur", "pepperoni"]);
var pizza_3 = pizza("Meat & Cheese", "6000", "Lítill", ["rjómaostur", "pepperoni", "skinka", "oregano"]);

var pizzur = [pizza_1, pizza_2, pizza_3];
var text = "";
for (var i = 0; i < pizzur.length; i++) {
    text += pizzur[i] + "<br>";
}
document.getElementById("message").innerHTML = text;
