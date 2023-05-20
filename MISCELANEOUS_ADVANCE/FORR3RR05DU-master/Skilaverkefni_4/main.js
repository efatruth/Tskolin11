


const lineSearchId= document.getElementById('lineSearch');
const lineSearchInput = document.getElementById("lineSearchInput")
const lineSearchOutput = document.getElementById("lineSearchOutput")


const binarySearchId= document.getElementById('binarySearch');
const binarySearchInput = document.getElementById("binarySearchInput")
const binarySearchOutput = document.getElementById("binarySearchOutput")

const treeSearch = document.getElementById("treeSearch");
const treeInsert = document.getElementById("treeInsert");
const treeSearchInput = document.getElementById("treeSearchInput");
const treeSearchOutput = document.getElementById("treeSearchOutput");

const addTolistInput = document.getElementById("addToListInput");
const addToListiId = document.getElementById("addToListiId");
const addToListiPrint = document.getElementById("addToListiPrint");
const addToListOutput = document.getElementById("addToListOutput");




function displayAddToList(){
	console.log(this)
	if(addTolistInput.value != ""){
		let index = addToList(addTolistInput.value);
		console.log(index);
		addToListOutput.classList.add("output");
				
		addToListOutput.innerHTML = index;
	}
}

function displayAddToListPrint(){

	console.log(this)
	addToListOutput.classList.add("output");
	

	addToListOutput.innerHTML = listi;
}

function displayLineSearch(argument) {

	let index = lineSearch(array, lineSearchInput.value);
	console.log(index);
	lineSearchOutput.classList.add("output");
	

	lineSearchOutput.innerHTML = index;

}


function displayBinarySearch(){

	let index = binarySearch(array, 0, array.length-1, binarySearchInput.value);
	console.log(index);
	binarySearchOutput.classList.add("output");
	

	binarySearchOutput.innerHTML = index;
}

function displayTreeSearch(){
	let index = t.search(treeSearchInput.value);
	treeSearchOutput.classList.add("output");
	

	treeSearchOutput.innerHTML = index;
}	

function displayTreeInsert(){
	let index = t.insert(treeSearchInput.value);
	treeSearchOutput.classList.add("output");
	

	treeSearchOutput.innerHTML = index;
}

lineSearchId.addEventListener("click", displayLineSearch);
binarySearchId.addEventListener("click", displayBinarySearch);

treeInsert.addEventListener("click", displayTreeInsert);
treeSearch.addEventListener("click", displayTreeSearch);

addToListiId.addEventListener("click", displayAddToList);
addToListiPrint.addEventListener("click", displayAddToListPrint);