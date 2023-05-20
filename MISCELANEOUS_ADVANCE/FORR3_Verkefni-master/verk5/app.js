"use strict"; 
function createQandA(spurning, svor){
	var text = "";
	for (var i=0; i < svor.length; i++){
		text += "<br>" + svor[i];
	}
	this.spurning = spurning;
	this.svor = text
}

var spurningSvor_1 = new createQandA("Hvar býrðu?", ["Ísland", "Bandaríkín", "Bretland", "Holland"]);
var spurningSvor_2 = new createQandA("Hvað ertu gamall?",["0-20", "20+"]);


document.getElementById("spurning").innerHTML = spurningSvor_1.spurning;
document.getElementById("svor").innerHTML = spurningSvor_1.svor;