"use strict";

var imageHold = [];

var image1 = {
  "'src'": "p1.jpg", 
  "'data-tags'": "Animators, Illustrators", 
  "'alt'": "Rabbit"
};

var image2 = {
  "'src'": "p2.jpg", 
  "'data-tags'": "Photographers, Filmmakers", 
  "'alt'": "Sea"
};

var image3 = {
  "'src'": "p3.jpg", 
  "'data-tags'": "Photographers, Filmmakers", 
  "'alt'": "Deer"
};

var image4 = {
  "'src'": "p4.jpg", 
  "'data-tags'": 'Designers', 
  "'alt'": 'New York Street Map'
};

var image5 = {
  "'src'": 'p5.jpg', 
  "'data-tags'": 'Photographers', 
  "'alt'": 'Sydney Train'
};

var image6 = {
  "'src'": 'p6.jpg',
  "'data-tags'": 'Designers, Illustrators',
  "'alt'": 'Typographic Study'
};

var image7 = {
  "'src'": 'p7.jpg',
  "'data-tags'": 'Photographers, Filmmakers',
  "'alt'": 'Trumpet'
};

var image8 = {
  "'src'": 'p8.jpg',
  "'data-tags'": 'Designers',
  "'alt'": 'Aqua Logo'
};

var image9 = {
  "'src'": 'p9.jpg',
  "'data-tags'": 'Animators, Illustrators',
  "'alt'": 'Ghost'
};

imageHold.push(image1, image2, image3, image4, image5, image6, image7, image8, image9);
for (var i = 0; i < imageHold.length; i++) {
  var appendImage = $('<img />').attr('{' + imageHold[i] + '}').appendTo('#gallery');
}

/*
var image1 = $('<img />').attr({'src': 'p1.jpg', 'data-tags': 'Animators, Illustrators', 'alt': 'Rabbit'}).appendto('#gallery');
var image2 = $("<img />").attr({'src': 'p2.jpg', 'data-tags': 'Photographers, Filmmakers', 'alt': 'Sea'}).appendto('#gallery');
var image3 = $("<img />").attr({'src': 'p3.jpg', 'data-tags': 'Photographers, Filmmakers', 'alt': 'Deer'}).appendto('#gallery');
var image4 = $("<img />").attr({'src': 'p4.jpg', 'data-tags': 'Designers', 'alt': 'New York Street Map'}).appendto('#gallery');
var image5 = $("<img />").attr({'src': 'p5.jpg', 'data-tags': 'Photographers', 'alt': 'Sydney Train'}).appendto('#gallery');
var image6 = $("<img />").attr({'src': 'p6.jpg', 'data-tags': 'Designers, Illustrators', 'alt': 'Typographic Study'}).appendto('#gallery');
var image7 = $("<img />").attr({'src': 'p7.jpg', 'data-tags': 'Photographers, Filmmakers', 'alt': 'Trumpet'}).appendto('#gallery');
var image8 = $("<img />").attr({'src': 'p8.jpg', 'data-tags': 'Designers', 'alt': 'Aqua Logo'}).appendto('#gallery');
var image9 = $("<img />").attr({'src': 'p9.jpg', 'data-tags': 'Animators, Illustrators', 'alt': 'Ghost'}).appendto('#gallery');

*/
$('div').attr('data-info', '222');


(function() {                             // Lives in an IIFE
  var $imgs = $('#gallery img');          // Get the images
  var $search = $('#filter-search');      // Get the input element
  var cache = [];
  var $buttons = $('#buttons');                   // Store buttons element
  var tagged = {};                           // Create an array called cache

  $imgs.each(function() {                 // For each image
    var img = this;                               // Store img in variable
    var tags = $(this).data('tags');   
    if (tags) {                                   // If the element had tags
      tags.split(',').forEach(function(tagName) { // Split at comma and
        if (tagged[tagName] == null) {            // If object doesn't have tag
          tagged[tagName] = [];                   // Add empty array to object
        }
        tagged[tagName].push(img);                // Add the image to the array
      });
    }

    cache.push({                          // Add an object to the cache array
      element: this,                      // This image
      text: this.alt.trim().toLowerCase() // Its alt text (lowercase trimmed)
    });
  });


  $('<button/>', {                                 // Create empty button
    text: 'Show All',                              // Add text 'show all'
    class: 'active',                               // Make it active
    click: function() {                            // Add onclick handler to
      $(this)                                      // Get the clicked on button
        .addClass('active')                        // Add the class of active
        .siblings()                                // Get its siblings
        .removeClass('active');                    // Remove active from siblings
      $imgs.show();                                // Show all images
    }
  }).appendTo($buttons);                           // Add to buttons

  $.each(tagged, function(tagName) {               // For each tag name
    $('<button/>', {                               // Create empty button
      text: tagName + ' (' + tagged[tagName].length + ')', // Add tag name
      click: function() {                          // Add click handler
        $(this)                                    // The button clicked on
          .addClass('active')                      // Make clicked item active
          .siblings()                              // Get its siblings
          .removeClass('active');                  // Remove active from siblings
        $imgs                                      // With all of the images
          .hide()                                  // Hide them
          .filter(tagged[tagName])                 // Find ones with this tag
          .show();                                 // Show just those images
      }
    }).appendTo($buttons);                         // Add to the buttons
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

  if ('oninput' in $search[0]) {          // If browser supports input event
    $search.on('input', filter);          // Use input event to call filter()
  } else {                                // Otherwise
    $search.on('keyup', filter);          // Use keyup event to call filter()
  }              

}());