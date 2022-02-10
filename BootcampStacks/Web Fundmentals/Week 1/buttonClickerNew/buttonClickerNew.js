function disappear(){
  var element = document.getElementById("add-button");
  element.remove();
}
function buttonUpdate(){
  var element = document.getElementById("login");
    if (element.innerText == "Login"){
        element.innerText = "Logout"} else {element.innerText = "Login"}
        console.log("Updated at" + Date)
      }
