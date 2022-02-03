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

