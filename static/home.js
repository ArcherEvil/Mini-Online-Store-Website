function highlightsearch(element, bool) {
    if (bool) {
        element.setAttribute('src', '../static/images/search_highlighted.png')
    }
    else {
        element.setAttribute('src', '../static/images/search.png')
    }
}