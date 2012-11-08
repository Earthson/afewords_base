jQuery(document).ready(function(){
// bind event handler for pages

//head nav (user self)
$("#head_user_block").bind({
    click: function(event){ event.stopPropagation(); },
    mouseover: function(event){ 
                    var target = event.target, $target = $(target);
                    if(target.id == "head_user_link" ){
                        var $ul = $target.siblings().eq(0);
                        
                        if($ul.css("display") == "none")
                        $ul.slideDown();//.bind('mouseout', function(){
                        //    $(this).slideUp();                        
                        //});                    
                    }
                    event.stopPropagation();
            //$(this).siblings().slideDown(); 
        }
});

$(document.body).bind('click', function(){
    $("#head_user").hide();
});


});