fetch("https://jsonplaceholder.typicode.com/posts/3")
    .then(response => response.json() )
    .then(json => document.getElementById("km").innerHTML = json.title)
    .catch(error => console.log(error))

fetch("https://jsonplaceholder.typicode.com/photos/3")
    .then(response => response.json() )
    .then(json => document.getElementById("img").src = json.url)
    .catch(error => console.log(error))
