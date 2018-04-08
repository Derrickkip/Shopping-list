"use strict"
var editbtn = document.getElementById("editbtn");

editbtn.addEventListener('click', showeditform)

function showeditform() {
    var editform = document.getElementById("editform");
    editform.style.display = "block";
    var editname = document.getElementById("editname");
    editname.innerHTML = editname;
}