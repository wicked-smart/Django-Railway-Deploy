//function to show a particular section of page
function showSection(section){

    

    document.querySelectorAll('div').forEach((div) => {
        div.style.display = 'none';
    })

    var foo = document.querySelector(`#${section}`)
    foo.style.display = 'block'
}

document.addEventListener('DOMContentLoaded', function(){
        //get all the buttons
        var buttons = document.querySelectorAll('button');

        //for every click log the value in the console
        buttons.forEach((button) => {
            button.onclick = () => {
               showSection(button.dataset.section);
            }
        })

    
});