// create posts 
function createPosts(num){
    var parent = document.querySelector('#posts')
    for(let i=1; i<=num; i++){
        let div = document.createElement('div')
        var bar = "posts #" + i 
        div.innerHTML = `<h2> ${bar} </h2>`
        div.classList.add('post')
        
        parent.append(div)
        parent.append(document.createElement('br'))
    }

}


// call createPosts on Document load
document.addEventListener("DOMContentLoaded", function(){
    createPosts(10)

    window.onscroll = () => {
        if(window.scrollY + window.innerHeight >= document.body.offsetHeight)
            document.querySelector('body').style.background = 'green'
        else
            document.querySelector('body').style.background = 'white'
    }
})