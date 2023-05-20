"use strict";
let q = "<h1> What did Farrah Moan get clocked on? </h1>";
document.getElementById("question").innerHTML = q; 



let look = new Array('Eyeliner', 'Highlighter', 'Foundation', "Wig");

let i;
for (i = 0; i < look.length; i++) {
	let answers = '<h4>' + look[i] + '</h4>';
	document.getElementById("answer-box").innerHTML += answers;
}


//Nota smið og nota .innerHTML einu sinni.
let test;
function Questions(question, answers) {
    this.question = document.getElementById("question").innerHTML = test;
    this.answers = ;

}

