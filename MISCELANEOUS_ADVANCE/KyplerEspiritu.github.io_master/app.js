"use strict";

let game = document.getElementById("game");   
let canvas = document.getElementById("canvas");

let score = 0; // Byrjunar stig notanda
let obstacleHeight = 10; // Hæð á obstacles
let obstacles = []; // Listi sem mun halda öll obstacles
let obstacleSpace = 200; // Hvar fyrsti obstacle verður staddur lóðrétt
let obstacleWidthLeft;
let obstacleWidthSpace;
let leftObstacle;
let rightObstacle;

// "GAME OVER" texti
let div_message = document.createElement("div"); // Nýtt div element
div_message.setAttribute("class", "message"); // Div element fær classan message
div_message.setAttribute("id", "message");

// Stig notanda
let div_score = document.createElement("span");
div_score.setAttribute("class", "scoreDiv");
div_score.setAttribute("id", "score");

// "restart" takki
let div_restart = document.createElement("span"); // Nýtt span element
div_restart.setAttribute("class", "restartDiv"); // Span element fær classan restartDiv
div_restart.setAttribute("onClick", "window.location.reload()"); // Einning fær span element onclick sem refreshar síðuna
div_restart.setAttribute("id", "restart"); // Einning fær span element onclick sem refreshar síðuna

let context = canvas.getContext("2d");
let canvasWidth = context.canvas.width; 
let canvasHeight = context.canvas.height;

// Hérna er byrjunar staður notanda
let playerXpostion = 240; 
let playerYpostion = 820;

for (let i = 0; i < 7; i++){  // For loopa sem býr til EINNIG 7 obstacles
	obstacleWidthLeft = getRandomInt(60, canvasWidth - 250); // Random tala. Þetta er fyrir bilið að vera á random stað.
	obstacleWidthSpace = obstacleWidthLeft + 100; // Bilið er 100px
	leftObstacle = new create_obstacle(0, obstacleSpace, obstacleWidthLeft, obstacleHeight); // Vinstri obstacle
	rightObstacle = new create_obstacle(obstacleWidthSpace, obstacleSpace, canvasWidth, obstacleHeight); // Hægri obstacle
	obstacleSpace -= 200;
	obstacles.push(leftObstacle); // Vinstri obstacle settur í Array
	obstacles.push(rightObstacle);  // Hægri obstacle settur í Array
}   

function create_obstacle(x_postion, y_position, width, height){ // Fall sem býr til obstacle
	this.x_postion = x_postion,
	this.y_position = y_position,
	this.width = width,
	this.height = height;
}
 
function getRandomInt(min, max) { // Fall sem tekur inn lægstu oh hæstu tölu og finnur heila tölu á milli þeirra eða hæsta eða lægsta talan sjálf
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function render_obstacles(){
	for (let i = 0; i < obstacles.length; i++){
		if (obstacles[i].y_position >= canvasHeight){ // Ef obstacles fara yfir útaf canvas boundaries
			obstacles.splice(0, 2); // Eyðast það úr listanum og canvas


			// Kóðinn hérna er fyrir þegar 1 obstacles fer út af canvasinn þá verður nýr obstacle
			obstacleWidthLeft = getRandomInt(60, canvasWidth - 250); 
			obstacleWidthSpace = obstacleWidthLeft + 100; 
			obstacleSpace = -500;
			leftObstacle = new create_obstacle(0, obstacleSpace, obstacleWidthLeft, obstacleHeight); 
			rightObstacle = new create_obstacle(obstacleWidthSpace, obstacleSpace, canvasWidth, obstacleHeight); 
			obstacles.push(leftObstacle); 
			obstacles.push(rightObstacle); 

		}
		if (playerXpostion + 15 >= obstacles[i].x_postion && playerXpostion <= obstacles[i].x_postion + obstacles[i].width && playerYpostion >= obstacles[i].y_position && playerYpostion <= obstacles[i].y_position + obstacles[i].height){ // Ef þegar notandinn klessir á obstacles
			
			canvas.setAttribute("class", "game"); // Canvas fær classan game sem minnkar opacity
			game.appendChild(div_message); 
			game.appendChild(div_score); 
			game.appendChild(div_restart); 
			document.getElementById("score").innerHTML = score;
			document.getElementById("message").innerHTML = "GAME OVER";
			document.getElementById("restart").innerHTML = "restart";
			clearInterval(animationInterval); // Stoppar Interval
		}
		context.fillStyle = "#035c70"; // Litur fyrir context
		context.fillRect(obstacles[i].x_postion, obstacles[i].y_position += 3, obstacles[i].width, obstacles[i].height); // Obstacles að færast
		context.fillStyle = "#989e00"; // Nýr litur
		context.beginPath();
		context.fillRect(playerXpostion, playerYpostion, 15, 15); // Hringurinn að færast
		context.stroke();
		context.fillStyle = "#ffffff";
		context.font = "50px Arial";
		context.fillText("Score: " + score, 20, 50); // Stig notanda               
	}
	score++; // Stiginn að hækka endalaust

}

function animation(){ // Fall fyrir hreyfingar
	context.clearRect(0, 0, canvasWidth, canvasHeight);
	render_obstacles();
}
let animationInterval = setInterval(animation, 10);

window.addEventListener("mousemove", function(e){ // EventListener 'hlustar' á eða fylgist með hreyfingu músins
	let mouseX = e.clientX - context.canvas.offsetLeft;
	if (mouseX <= canvasWidth - 10 && mouseX >= 10){ // Ef hringurinn er ekki kominn alveg til hægri eða vinstri
		playerXpostion = mouseX; // Hringurinn 'eltir' músina
	}
}); 