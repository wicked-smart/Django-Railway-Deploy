
let counter=1;
let quantity = 20;


// load first 20 posts
document.addEventListener("DOMContentLoaded", load);

// If scrolled to the bottom , load 20 more posts
window.onscroll = () => {
    if(window.scrollY + window.innerHeight >= document.body.offsetHeight)
        load();
}


function load(){
    let start = counter
    let end = start + quantity -1
    counter = end + 1

    //fetch the posts
    fetch(`posts?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.posts.forEach(addPost)
    })
    .catch(err => {
        console.log(err)
    })
}

// add posts to the parent
function addPost(content){
    var parent = document.querySelector('#posts')

    // create div element
    var div = document.createElement('div')
    div.innerHTML = content
    div.classList.add("post")

    //add post and a <br> element to the DOM
    parent.append(div)
    parent.append(document.createElement('br'))
}