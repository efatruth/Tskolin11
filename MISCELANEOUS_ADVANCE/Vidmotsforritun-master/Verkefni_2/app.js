/*
----------ATH----------
Fékk hjálp frá þessu myndbandi:
https://www.youtube.com/watch?v=kB0ZVUrI4Aw
*/

var vertexShaderText = 'precision mediump float;' + 
					   'attribute vec2 vertPostion;' + 
					   'void main(){gl_Position = vec4(vertPostion, 0.0, 1.5);}';

var fragmentShaderText = 'precision mediump float;' +
						 'void main(){gl_FragColor = vec4(1.0, 0.0, 10.0, 1.0);}';

let canvas = document.getElementById('canvas_surface');
let gl = canvas.getContext('webgl');

gl.clearColor(0.15, 0.15, 0.15, 1.0); // Litur fyrir canvas
gl.clear(gl.COLOR_BUFFER_BIT); // Breyta litnum á canvasinum

var vertexShader = gl.createShader(gl.VERTEX_SHADER); // Búa til vertex shader
var fragmentShader = gl.createShader(gl.FRAGMENT_SHADER); // Búa til fragment shader

gl.shaderSource(vertexShader, vertexShaderText); // Vertex shader fær source kóða
gl.shaderSource(fragmentShader, fragmentShaderText); // Fragment shader fær source kóða

gl.compileShader(vertexShader);

// Ef það var einhver villa í vertexShaderText, þá mun koma error í console
if(!gl.getShaderParameter(vertexShader, gl.COMPILE_STATUS)){
	console.error('Error compiling vertex shader!', gl.getShaderInfoLog(vertexShader));
}

// Ef það var einhver villa í fragmentShaderText, þá mun koma error í console
gl.compileShader(fragmentShader);
if(!gl.getShaderParameter(fragmentShader, gl.COMPILE_STATUS)){
	console.error('Error compiling fragment shader!', gl.getShaderInfoLog(fragmentShader));
}

var webGLProgram = gl.createProgram();
gl.attachShader(webGLProgram, vertexShader); // Lætur vertex shader inn í foritið
gl.attachShader(webGLProgram, fragmentShader); // Lætur fragment shader inn í foritið
gl.linkProgram(webGLProgram);

var triangleVertexBuffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, triangleVertexBuffer);
gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([0.0, 0.0, 0.5, 0.0, 0.3, 0.5]), gl.STATIC_DRAW);

var positionAttribLocation = gl.getAttribLocation(webGLProgram, 'vertPostion');
gl.vertexAttribPointer(positionAttribLocation, 2, gl.FLOAT, gl.FALSE, 2 * Float32Array.BYTES_PER_ELEMENT, 0);

gl.enableVertexAttribArray(positionAttribLocation);
gl.useProgram(webGLProgram);
gl.drawArrays(gl.TRIANGLES, 0, 3);


let x_1 = 0.0; // X fyrir fyrsta punkt
let x_2 = 0.5; // X fyrir annað punkt
let x_3 = -0.5; // X fyrir þriðja punkt

var rotate_triangle = function(){ // Fall fyrir animation
	requestAnimationFrame( rotate_triangle );
	gl.clear(gl.COLOR_BUFFER_BIT); 	

	gl.bindBuffer(gl.ARRAY_BUFFER, triangleVertexBuffer);
	if (x_1 >= -0.48) // Þetta er fyrir svo að þríhyrningurinn hverfur ekki, en verður alveg kyrr
		gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([x_1 -= 0.0015, Math.sqrt(0.5 ** 2 - x_1 ** 2),
													 	 x_2 -= 0.0015, Math.sqrt(0.5 ** 2 - x_2 ** 2), 
													 	 x_3 += 0.0015, -(Math.sqrt(0.5 ** 2 - x_3 ** 2))]), gl.STATIC_DRAW);
	else{
		// Hér fyrir neðan er ég að reseta X value fyrir alla punktana
		x_1 = 0.0;
		x_2 = 0.5;
		x_3 = -0.5; 
	}

	gl.drawArrays(gl.TRIANGLES, 0, 3);
}

rotate_triangle();
