let url = window.location.origin
document.querySelector('.searchbutton').setAttribute('src', url + '/static/images/search.png')
document.querySelector('.cartbutton').setAttribute('src', url + '/static/images/cart.png')

function highlightsearch(element, bool, type) {
    if (type == 'search') {

    
        if (bool) {
        element.setAttribute('src', url + '/static/images/search_highlighted.png')
        }
        else {
        element.setAttribute('src', url + '/static/images/search.png')
        }
    }
    else if (type == 'cart') {
        if (bool) {
            element.setAttribute('src', url + '/static/images/cart_highlighted.png')
            }
            else {
            element.setAttribute('src', url + '/static/images/cart.png')
            }
    }
    
}


function mainpage() {
    window.location.href = url;
}


// Get the input field
var input = document.getElementById("inputsearch");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.querySelector('.searchbutton').click();
  }
}); 