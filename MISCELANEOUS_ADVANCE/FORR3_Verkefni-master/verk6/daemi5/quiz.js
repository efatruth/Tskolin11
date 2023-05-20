"use strict";

function Question(spurning, svor, rett_svar) {
	let text = "";
	for (var i=0; i < svor.length; i++){
		text += "<span onclick='checkAndChangeQuestion()' id='answer'>" + svor[i] + "</span><br>";
	}
	this.spurning = spurning;
	this.svor = text;
	this.rett = rett_svar;	
}

function checkAndChangeQuestion(){
	var questionContent = document.getElementById("spurning");
	var elem = document.getElementsByTagName("SPAN");
	for (let i = 0; i < elem.length; i++){ 
		if (elem[i].textContent === spurning_1.rett || elem[i].textContent === spurning_2.rett){
        	elem[i].setAttribute("class", "greenColor");
        }
        else{
        	elem[i].setAttribute("class", "redColor");
        }
	}

	if (questionContent.textContent === spurning_2.spurning){
		setTimeout(function(){
			document.getElementById("spurning").innerHTML = "";
			document.getElementById("svor").innerHTML = "";
		}, 3000);
	}
	else{
		setTimeout(function(){
			document.getElementById("spurning").innerHTML = spurning_2.spurning;
			document.getElementById("svor").innerHTML = spurning_2.svor;
		}, 3000);
	}

}

let spurning_1 = new Question('Hver var fyrst forseti Bandaríkjanna?', ['George Washington', 'Barack Obama', 'Abraham Lincoln', 'Donald Trump'], 'George Washington');
let spurning_2 = new Question('Hvað er höfuðborgin í Bandaríkjunum?', ['New York', 'Los Angeles', 'Washington D.C'], 'Washington D.C');

document.getElementById("spurning").innerHTML = spurning_1.spurning;
document.getElementById("svor").innerHTML = spurning_1.svor;
