function highlightsearch(element, bool, type) {
    if (type == 'search') {

    
        if (bool) {
        element.setAttribute('src', '../static/images/search_highlighted.png')
        }
        else {
        element.setAttribute('src', '../static/images/search.png')
        }
    }
    else if (type == 'cart') {
        if (bool) {
            element.setAttribute('src', '../static/images/cart_highlighted.png')
            }
            else {
            element.setAttribute('src', '../static/images/cart.png')
            }
    }
    
}

