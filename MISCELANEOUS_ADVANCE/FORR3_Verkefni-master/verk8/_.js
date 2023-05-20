"use strict";

const roads = [
  "Alice's House-Bob's House",   "Alice's House-Cabin",
  "Alice's House-Post Office",   "Bob's House-Town Hall",
  "Daria's House-Ernie's House", "Daria's House-Town Hall",
  "Ernie's House-Grete's House", "Grete's House-Farm",
  "Grete's House-Shop",          "Marketplace-Farm",
  "Marketplace-Post Office",     "Marketplace-Shop",
  "Marketplace-Town Hall",       "Shop-Town Hall"
]; //Þetta er array af upphafstöðum sem geta farið beint í áfangastað.


function buildGraph(edges) {

  let graph = Object.create(null); //Object með engum 'property' eða 'keys'.

  function addEdge(from, to) { //Fall sem finnur hvort það er til gata sem fer beint frá upphafsstað og til áfangastað (Það sem ég er að meina hérna er að ef það er gata sem fer frá upphafsstað til áfangastað)
    if (graph[from] == null) {
      graph[from] = [to];
    } else {
      graph[from].push(to);
    }
  }

  for (let [from, to] of edges.map(r => r.split("-"))) { //For loopa sem loopar yfir argument og spiltar streng þar sem '-' kemur fyrir
    addEdge(from, to); //Hér er verið að kalla á fallið hérna fyrir ofan og finnur alla áfangastaði sem upphafsstaðurinn getur farið beint til
    addEdge(to, from); //EINNIG til baka (upphafsstaðir sem áfangastaðir get farið beint til)
  }
  return graph; //Hér er verið að skila Object með alla upphafstaði sem 'key' sem eru með lista sem value og inni í listanum eru allar mögulegu áfangastaðir sem upphafsstaður getur farið bein til
}

const roadGraph = buildGraph(roads); //Breyta sem bendir á buildGraph fallið með Arrayið roads sem argument.

//----------------------------------------------------------


class VillageState { //Class
	constructor(place, parcels) { //Smiður
		this.place = place;
		this.parcels = parcels;
	}

	move(destination) { 
		if (!roadGraph[this.place].includes(destination)) { //Ef það er EKKI til gata sem fer frá núverandi stað til áfangastað
		  return this;
		} 
		else { //Annars 'fer' vélmennið í nýja staðinn. Þá breytist núverandi stað í áfangastað (því vélmennið fór frá gamla núverandi staðinn og í áfangastaðinn. Þannig áfangastaðurinn verður nýji núverandi staðurinn). Þá verður pakkinn afhent og við fáum nýjan pakka (við fáum nýjan pakka þegar við komum áfangastað).
			let parcels = this.parcels.map(p => {if (p.place != this.place) return p; 
	  		return {place: destination, address: p.address};}).filter(p => p.place != p.address);
		  	return new VillageState(destination, parcels);
		}
	}
}


let first = new VillageState( //Hér er verið að kalla á classan VillageState með núverandi stað sem 'Post Office' og pakka sem er frá 'Post Office' til 'Alice's House'
  "Post Office", // Núverandi staður
  [{place: "Post Office", address: "Alice's House"}] //Pakkinn til Alice
);
let next = first.move("Alice's House");


console.log(next.place); //Sýna áfangastað
// → Alice's House
console.log(next.parcels); //Sýna næsta pakka (eftir þegar við erum komnir að áfangastað)
// → []
console.log(first.place); //Sýna núverandi stað
// → Post Office


//----------------------------------------------------------


/*
let object = Object.freeze({value: 5}); //Með freeze leyfir það þér ekki að breyta valueið
object.value = 10; //Hérna er verið að reyna breyta value frá 5 og í 10. En með freeze verður það hunsað
console.log(object.value); //Skilar 5
*/

//ATH!!!! KÓÐINN VIRKAR EKKI EF ÞÚ ERT Í STRICT MODE

//----------------------------------------------------------

//Kóðinn hér fyrir neðan er þannig að vélmennið er á upphafsstað og fer í random áfangastað sem vélmennið getur farið beint í (upphafsstaður og áfangastaður eru í sömu götu)
//Það loopast þangað til það er búið að afhenda alla pakka
//Þetta er virkar en gallinn við þetta er að það er bara random hvert hann fer þannig það getur verið möguleiki að vélmennið geti tekið margar ferðir


function runRobot(state, robot, memory) {
  for (let turn = 0;; turn++) {
    if (state.parcels.length == 0) { //Ef það er búið að afhenda alla pakka
      console.log(`Done in ${turn} turns`); //Turn er hversu oft þú skiptir um stað
      break;
    }
    //
    let action = robot(state, memory);
    state = state.move(action.direction); //Hérna er vélmennið að skipta um stað
    memory = action.memory; 
    console.log(`Moved to ${action.direction}`); //Skilar nýja staðnum
  }
}

function randomPick(array) { //Random index fyrir Array
  let choice = Math.floor(Math.random() * array.length);
  return array[choice]; 
}

function randomRobot(state) { //Vélmannið fer í random áfangastað sem þú getur farið beint í frá upphafstað
  return {direction: randomPick(roadGraph[state.place])};
}

VillageState.random = function(parcelCount = 5) {
  let parcels = [];
  for (let i = 0; i < parcelCount; i++) {
    let address = randomPick(Object.keys(roadGraph)); //Velur einn random stað
    let place;
    do { //Finna staðin sem passar við áfangastaðin sem pakkin á að vera sendur til
      place = randomPick(Object.keys(roadGraph)); //Velur einn random stað
    } while (place == address); 
    parcels.push({place, address}); //Bættist við pakka
  }
  return new VillageState("Post Office", parcels);
};

runRobot(VillageState.random(), randomRobot);


//----------------------------------------------------------

//Þetta er svipað og verið var að gera hér fyrir ofan núna eru göturnar í raðaðar í Array þannig að ef þú ferð eftir þessu myndiru ná alla pakka
//Kóðinn er þannig að þú þurfir bara að minnsta kosti fara tvisvar. Þá ertu búinn að afhenda alla pakka
//Gallinn með þessa leið er að röð í Arrayinu er harð kóðað

const mailRoute = [ 
  "Alice's House", "Cabin", "Alice's House", "Bob's House",
  "Town Hall", "Daria's House", "Ernie's House",
  "Grete's House", "Shop", "Grete's House", "Farm",
  "Marketplace", "Post Office"
];

function routeRobot(state, memory) {
  if (memory.length == 0) {
    memory = mailRoute;
  }
  return {direction: memory[0], memory: memory.slice(1)}; //Bættir við nýtt minni og eyðir hinu gamla
}

runRobot(VillageState.random(), routeRobot, []);

//----------------------------------------------------------



function findRoute(graph, from, to) { //Fall sem finnur styðstu leiðina frá X til Y
  let work = [{at: from, route: []}];
  for (let i = 0; i < work.length; i++) {
    let {at, route} = work[i];
    for (let place of graph[at]) {
      if (place == to) return route.concat(place);
      if (!work.some(w => w.at == place)) {
        work.push({at: place, route: route.concat(place)});
      }
    }
  }
}

function goalOrientedRobot({place, parcels}, route) {
  if (route.length == 0) {
    let parcel = parcels[0];
    if (parcel.place != place) { //Ef robotið er ekki með pakkan
      route = findRoute(roadGraph, place, parcel.place); //Þá finnur það styðstu leiðina til að ná í hann
    } else { //Ef robotið er með pakkan
      route = findRoute(roadGraph, place, parcel.address); //Þá finnur það styðstu leiðina til að afhenda pakkanum
    }
  }
  return {direction: route[0], memory: route.slice(1)}; //Bættir við nýtt route og eyðir gamla
}

runRobot(VillageState.random(), goalOrientedRobot, []);
