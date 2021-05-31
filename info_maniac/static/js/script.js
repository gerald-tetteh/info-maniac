function savetowishlist(id){
    var icon = document.getElementById(id);
    var style = getComputedStyle(icon);
    console.log(style['color']);

    if(style['color']=="rgb(255, 223, 0)"){
        console.log("barbie");
        icon.style.color="black";
    }else{
        icon.style.color="#FFDF00";
    }
    
    

}