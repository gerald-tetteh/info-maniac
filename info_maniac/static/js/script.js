function saving(userId, title, company, source_url, image_url, source_name, job_type){
    var url = "/add-to-wishlist";
    const e = { userId: `${userId}`, title: `${title}`, company:`${company}`, source_url:`${source_url}`, image_url:`${image_url}`, source_name:`${source_name}`, job_type:`${job_type}` };
    fetch(url,{method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
    },
   
    body:JSON.stringify(e)
})
  .then(function(data) {
        return data;
    })
    .then(function(data){
        console.log(data);
    })
 
  .catch(function(error) {

  });
}

function removeWishlistItem(id) {
    var url = "/remove-wishlist-item";
    const e = { id: `${id}`};
    fetch(url, 
        {
            method: 'POST', // or 'PUT'
            headers: {
            'Content-Type': 'application/json',
            },

        body:JSON.stringify(e)
        }) .then(function(data) {
                location.reload();
            })
            .catch(function(error) {

            });
}

function savetowishlist(id, userId, title, company, source_url, image_url, source_name, job_type,itemId){
    var icon = document.getElementById(id);
    var style = getComputedStyle(icon);
    console.log(style['color']);

    if(style['color']=="rgb(255, 223, 0)"){
        console.log("barbie");
        icon.style.color="black";
        removeWishlistItem(itemId)
    } else {
        console.log("here")
        icon.style.color="#FFDF00";
        saving(userId, title, company, source_url, image_url, source_name, job_type)
    }

}
