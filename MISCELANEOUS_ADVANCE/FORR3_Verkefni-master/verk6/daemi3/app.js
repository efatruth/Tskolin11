"use strict";



/* 
<div id="quiz"></div>
*/

var div_all = document.createElement("div");
div_all.setAttribute("id", "quiz")



/*
 <div id="quiz">
 	<div id="question">Spurning 1</div>
 	<div id="answers"></div>
 </div
*/ 

var div_quest = document.createElement("div");
div_quest.setAttribute("id", "question")
var quest_text = document.createTextNode("Spurning 1")
div_quest.appendChild(quest_text);

var div_answers = document.createElement("div");
div_answers.setAttribute("id", "answers")

div_all.appendChild(div_quest);
div_all.appendChild(div_answers);


/*
<div id="quiz">
	<div id="question">Spurning 1</div>
	<div id="answers">
		<div class="answer" data-active="answer">Svarmöguleiki 1</div>
		<div class="answer" data-active="answer">Svarmöguleiki 2</div>
	</div>
<div>
*/
var div_answer_1 = document.createElement("div");
div_answer_1.setAttribute("class", "answer")
div_answer_1.setAttribute("data-active", "answer")
var div_answer_1_text = document.createTextNode("Svarmöguleiki 1");
div_answer_1.appendChild(div_answer_1_text)
div_answers.appendChild(div_answer_1)

var div_answer_2 = document.createElement("div");
div_answer_2.setAttribute("class", "answer")
div_answer_2.setAttribute("data-active", "answer")
var div_answer_2_text = document.createTextNode("Svarmöguleiki 2");
div_answer_2.appendChild(div_answer_2_text);
div_answers.appendChild(div_answer_2)

document.getElementsByTagName("body")[0].appendChild(div_all);

