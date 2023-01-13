//when back arrow is clicked, onpopstate

window.onpopstate = (event) => {
    console.log(event.state.section)
    showSection(event.state.section)
}

//function to show a particular section of page
function showSection(section){
    console.log(section)

    fetch(`section/${section}`)
    .then(response => response.text())
    .then(text => {
           console.log('recieved text from server :- ' + text)
           document.querySelector("#section").innerHTML = text
    }).catch(err => {
            console.log('There has been an Error!')
    })
}

document.addEventListener('DOMContentLoaded', function(){
        //get all the buttons
        var buttons = document.querySelectorAll('button');

        //for every click log the value in the console
        buttons.forEach((button) => {
            button.onclick = () => {

                const section  = button.dataset.section 
               history.pushState({section: section}, "", `${section}`)
               console.log(section)
               showSection(section)
            }
        })  

    
});