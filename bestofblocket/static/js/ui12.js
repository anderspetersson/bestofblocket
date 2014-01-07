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
    jsonPath : "http://www.bestofblocket.se/api/",
    jsonSuccess : customDataSuccess,
    afterMove: afterMove
  });
var content = "";
  function customDataSuccess(data){
      n = 0
      for(var i in data["items"]){
         
         var img = data["items"][i].img;
         var bodytext = data["items"][i].bodytext;
         var titletext = data["items"][i].titletext;
         var slug = "<input id=\""+n+"\" type=\"hidden\" value=\""+data["items"][i].slug+"\">";
         
         if (img){
          imghtml = "<img src=\"" +img+ "\" alt=\"" +titletext+ "\">";
         }
         else{
          imghtml = "";
         }

         content += "<div class=\"item\"><h1>"+titletext+"</h1>"+imghtml+"<p>"+bodytext+"</p>"+slug+"</div>"
         
         n += 1
    }
    $("#owl-demo").html(content);
  }

  function afterMove(){
    href = '/'+$('#'+this.owl.currentItem).val()+'/';
    if (location.pathname != href){
      history.pushState(null, null, href);
    }
  }

  window.addEventListener("popstate", function(e) {
    owl.trigger('owl.prev');
  });
  
  $("#owl-demo").html(content);
  // Custom Navigation Events
  $(".next").click(function(){
    owl.trigger('owl.next');
  })
  $(".prev").click(function(){
    owl.trigger('owl.prev');
  })
 
});