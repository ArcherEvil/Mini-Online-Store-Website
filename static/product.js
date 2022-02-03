

function search() {
    let search = document.querySelector('#inputsearch').value;
    let redirect = String(url) + '/search/?searchquery=' + encodeURI(search)
    window.location.href = redirect

}
