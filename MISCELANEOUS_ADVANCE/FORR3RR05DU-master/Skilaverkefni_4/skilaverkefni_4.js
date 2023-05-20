


function lineSearch(array, x){
	for(i in array){
		if(array[i] == x)return i;
	}
	return -1;  
}


function binarySearch(array, l , max, tala){

	if(max >= l){
		
		mid = l+(max-l)/2
		mid = Math.round(mid)

		if(array[mid] == tala){
			return mid
		}else if(array[mid] > tala){
			return binarySearch(array, l, mid-1, tala)
		}else{
			return binarySearch(array, mid+1, max, tala)
		}
	}else{
		return -1;
	}

}


array = [1,2,3,4,5,6,7,8,9,10];
//x = 20;
//console.log(binarySearch(array,0, array.length-1, x));

//console.log(lineSearch(array, 9))

var listi = [];

function addToList(tala){
	if(listi.length < 1 || listi == undefined){
    	listi[0]  = tala;
		console.log("listinn var tómur")
    	return true;
	}
	if(listi[listi.length -1] < Number(tala)){
		listi[listi.length] = tala;
		console.log("talan er stærðst.")
		return true;
	}
	if(listi[0] > tala){
		listi.splice(0,0,tala);
		console.log("talan er minni")
		return true;
	}

	for(i in listi){
		if(tala <= listi[i]){
			listi.splice(i,0,tala)
			return true;
		}
	}
}


class Node{
	constructor(value){
		this.value = value;
		this.left = null;
		this.right = null;
	}
    
    insert(d){
        if(d == this.value){
            return false;
        }else if(this.value > d){
            
            if(this.left){
            	return this.left.insert(d);
            }else{
            	this.left = new Node(d);
                return true;
            }
        }else{
            if(this.right){
            	return this.right.insert(d);
            }else{
            	console.log("bs")
                this.right = new Node(d);
                return true;
            }
        }
    }
    
    search(d){

    	if(d == this.value){
    		return true;
    	}else if(this.value > d){
    		if(this.left){
    			return this.left.search(d)
    		}else{
    			return false;
    		}
    	}else{
    		if(this.right){
    			return this.right.search(d)
    		}else{
    			return false;
    		}
    	}

    }
}

class Tree{
	constructor(){
		this.root = null;
	}
	
	insert(d){
		if(this.root){
			return this.root.insert(d)
		}else{
			console.log("root")
			this.root = new Node(d)
			return true;
		}
	}
	
	search(d){
		if(this.root){
			return this.root.search(d);
		}else{
			return false;
		}
	}

	print(){
		console.log(this.root)
	}
}

t = new Tree;

// console.log(t.insert(6)) 
// console.log(t.insert(8))
// console.log(t.insert(7))
// console.log(t.insert(2))
// console.log(t.insert(3))
// console.log(t.insert(9))
// console.log(t.insert(22))
// console.log(t.insert(844))
// console.log(t.insert(3))



