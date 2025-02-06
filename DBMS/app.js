document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#add-btn").addEventListener("click", function() {
        let addSection = document.querySelector("#hidden-section");
        let searchSection = document.querySelector("#search-form");

        addSection.classList.toggle("show");
        if (searchSection.classList.contains("show")) {
            searchSection.classList.remove("show");
        }
    });

    document.querySelector("#search-btn").addEventListener("click", function() {
        let searchSection = document.querySelector("#search-form");
        let addSection = document.querySelector("#hidden-section");

        searchSection.classList.toggle("show");
        if (addSection.classList.contains("show")) {
            addSection.classList.remove("show");
        }
    });
});





let rollSet = new Set();
let students = [];
function inputGiven(){
    let Roll = document.querySelector("#r").value;
    if(rollSet.has(Roll)){
        window.alert("Roll");
        return;
    }
    let stud = {
        Name : document.querySelector("#nam").value,
        Roll : document.querySelector("#r").value,
        addR : document.querySelector("#address").value,
        dept : document.querySelector("#dept-select").value,
        ph : document.querySelector("#contact").value
    };
    students.push(stud);
}

