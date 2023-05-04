const cardId = document.querySelector(".card_id");
var a = document.querySelector("#lib_user_1");
var b = document.querySelector("#lib_user_2");
a.addEventListener("click", function(){
    if (cardId.style.display == "none"){
      cardId.style.display = "block";
      document.getElementById("library_id").required = true
    }
});
b.addEventListener("click", function(){
    if (cardId.style.display == "block"){
        cardId.style.display = "none";
        document.getElementById("library_id").required = false
    }
})

if(a.checked){
  cardId.style.display = "block";
}