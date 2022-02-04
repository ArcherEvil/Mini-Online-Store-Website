function search() {
    let search = document.querySelector('#inputsearch').value;
    let redirect = String(url) + '/search/?searchquery=' + encodeURIComponent(search)
    window.location.href = redirect

}