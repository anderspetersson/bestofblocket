$(document).ready(function() {
var owl = $("#owl-demo");
  $("#owl-demo").owlCarousel({
    lazyLoad : true,
    navigation : false, // Show next and prev buttons
    slideSpeed : 300,
    paginationSpeed : 400,
    singleItem:true,
    pagination:false,
    autoHeight:true,
    rewindNav:false,
    jsonPath : "http://localhost:8000/api/",
    jsonSuccess : customDataSuccess
  });
var content = "";
  function customDataSuccess(data){
      
      for(var i in data["items"]){
         
         var img = data["items"][i].img;
         var bodytext = data["items"][i].bodytext;
         var titletext = data["items"][i].titletext;
   
         content += "<div class=\"item\"><h1>"+titletext+"</h1><img src=\"" +img+ "\" alt=\"" +titletext+ "\">"+"<p>"+bodytext+"</p></div>"
    }
    $("#owl-demo").html(content);
  }
  
  $("#owl-demo").html(content);
  // Custom Navigation Events
  $(".next").click(function(){
    owl.trigger('owl.next');x
  })
  $(".prev").click(function(){
    owl.trigger('owl.prev');
  })
 
});