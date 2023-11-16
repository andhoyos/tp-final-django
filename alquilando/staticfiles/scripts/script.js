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