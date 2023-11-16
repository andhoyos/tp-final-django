let close_alert_error = document.querySelector(".alert-danger__close")
let close_alert_success = document.querySelector(".alert-success__close")
let content_alert_error = document.querySelector(".alert-danger")
let content_alert_success = document.querySelector(".alert-success")

if (close_alert_error) {    
    close_alert_error.addEventListener("click", ()=>{
        content_alert_error.style.display = "none"
        
    })
}else{
    if (close_alert_success) {    
        close_alert_success.addEventListener("click", ()=>{
            content_alert_success.style.display = "none"
            
        })
    } 
}


function toggleDropdown(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    dropdown.classList.toggle("show");
}

// Cerrar el dropdown si se hace clic fuera de él
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

