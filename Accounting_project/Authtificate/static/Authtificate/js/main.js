"use strict"

function start(){
    fetch("api/hello")
        .then(response => response.json())
        .then(data => document.getElementById("main").innerText = data.age)
}

document.addEventListener("DOMContentLoaded", start) 

setInterval(start, 1)