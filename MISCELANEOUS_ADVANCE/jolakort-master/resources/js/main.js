const hero = document.querySelector('.hero');
const text = document.querySelector('h1');
const walk = 200; // 200px max sem shadow ferðast

function shadow(e) {
  // Allt of töff ES6 syntax
  const {
    offsetWidth: width,
    offsetHeight: height
  } = hero;

  let {
    offsetX: x,
    offsetY: y
  } = e;

  if (this !== e.target) { // Ef að hero elementið er ekki það sem er hoverað yfir
    // Bætt er við offset
    x += e.target.offsetLeft;
    y += e.target.offsetTop;
  }

  // Útreikningar til að fá x og y hnit fyrir shadow
  const xWalk = Math.round((x / width * walk) - (walk / 2));
  const yWalk = Math.round((y / height * walk) - (walk / 2));


  text.style.textShadow = `${xWalk}px ${yWalk}px 0 rgba(219, 80, 74, .6)`; // Bætt er við/uppfært textShadow style á text element
}

// Event listener á hero element sem hlustar eftir músahreyfingum, kallar svo á fallið shadow
hero.addEventListener('mousemove', shadow);