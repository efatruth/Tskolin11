"use strict";
(function() {

  function setAttributes(el, attrs) { // Fall sem léttir á að setja inn attributes í elements
    for(var key in attrs) {
      el.setAttribute(key, attrs[key]);
    }
  }  

  var gallery = document.getElementById('gallery');

  var img_1 = document.createElement("img");
  var img_2 = document.createElement("img");
  var img_3 = document.createElement("img");
  var img_4 = document.createElement("img");
  var img_5 = document.createElement("img");
  var img_6 = document.createElement("img");
  var img_7 = document.createElement("img");
  var img_8 = document.createElement("img");
  var img_9 = document.createElement("img");

  setAttributes(img_1, {'src': './images/p1.jpg', 'data-tags': 'Animators, Illustrators', 'alt': 'Rabbit'});
  setAttributes(img_2, {'src': './images/p2.jpg', 'data-tags': 'Photographers, Filmmakers', 'alt': 'Sea'});
  setAttributes(img_3, {'src': './images/p3.jpg', 'data-tags': 'Photographers, Filmmakers', 'alt': 'Deer'});
  setAttributes(img_4, {'src': './images/p4.jpg', 'data-tags': 'Designers', 'alt': 'New York Street Map'});
  setAttributes(img_5, {'src': './images/p5.jpg', 'data-tags': 'Photographers', 'alt': 'Sydney Train'});
  setAttributes(img_6, {'src': './images/p6.jpg', 'data-tags': 'Designers, Illustrators', 'alt': 'Typographic Study'});
  setAttributes(img_7, {'src': './images/p7.jpg', 'data-tags': 'Photographers, Filmmakers', 'alt': 'Trumpet'});
  setAttributes(img_8, {'src': './images/p8.jpg', 'data-tags': 'Designers', 'alt': 'Aqua Logo'});
  setAttributes(img_9, {'src': './images/p9.jpg', 'data-tags': 'Animators, Illustrators', 'alt': 'Ghost'});

  gallery.append(img_1);
  gallery.append(img_2);
  gallery.append(img_3);
  gallery.append(img_4);
  gallery.append(img_5);
  gallery.append(img_6);
  gallery.append(img_7);
  gallery.append(img_8);
  gallery.append(img_9);




  var imgs = document.querySelectorAll('#gallery img');          // Get the images
  var search = document.querySelector('#filter-search');      // Get the input element
  var cache = [];                         // Create an array called cache

  imgs.forEach(function(single_img) {                 // For each image
    cache.push({                          // Add an object to the cache array
      element: single_img,                      // This image
      text: single_img.alt.trim().toLowerCase() // Its alt text (lowercase trimmed)
    });
  });

  function filter() {                     // Declare filter() function
  var query = this.value.trim().toLowerCase();  // Get the query
    cache.forEach(function(img) {         // For each entry in cache pass image 
      var index = 0;                      // Set index to 0

      if (query) {                        // If there is some query text
        index = img.text.indexOf(query);  // Find if query text is in there
      }

      img.element.style.display = index === -1 ? 'none' : '';  // Show / hide
    });
  }

  if ('oninput' in search) {          // If browser supports input event
    search.addEventListener('input', filter);          // Use input event to call filter()
  } 
  else {                                // Otherwise
    search.addEventListener('keyup', filter);          // Use keyup event to call filter()
  }       


                 
  var buttons = document.querySelector('#buttons');                   
  var tagged = {};                                

  imgs.forEach(function(e) {                         
    var tags = e.getAttribute('data-tags');              

    if (tags) {                                   
      tags.split(',').forEach(function(tagName) { 
        if (tagged[tagName] == null) {            
          tagged[tagName] = [];                   
        }
        tagged[tagName].push(e);                
      });
    }
  });


  var showAllButton = document.createElement("button");
  var showAllText = document.createTextNode("Show All");
  showAllButton.appendChild(showAllText);
  setAttributes(showAllButton, {'class': 'active'});
  showAllButton.onclick = function () {
      for (let i of this.parentElement.children){
          i.classList.remove('active');
      }
      this.classList.add('active');
      imgs.forEach(function (img) {
          img.style.display = "";
      });
  };
  buttons.append(showAllButton);

  for (let tagName in tagged){
    var tagButtons = document.createElement('button');
    var tagText = document.createTextNode(tagName + ' (' + tagged[tagName].length + ')');
    tagButtons.appendChild(tagText);
    tagButtons.addEventListener('click', function () {
      for (let i of this.parentElement.children){
          i.classList.remove('active');
      }
      this.classList.add('active');
      imgs.forEach(function (img) {
        img.style.display = tagged[tagName].includes(img) ? "" : "none";
      });
    });
    buttons.appendChild(tagButtons);
  }

}());