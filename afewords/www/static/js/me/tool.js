(function($){
// tools for the all pages
$.extend({
    encode: function(value){
                var html_encode_dict = {'&': "&amp", '<':"&lt;", '>':"&gt;", "'":"&#39;", '"':'&quot;' };
                if(typeof(value) == "string"){
                    return ret_fun(value);
                }else{
                    for(var ii in value){
                        if(typeof value[ii] == "string")  value[ii] = ret_fun(value[ii]);        
                    }    
                    return value;
                }
    
                function ret_fun(str){
                    return str.replace(/'|"|>|</g, function(tt){
                        return html_encode_dict[tt];
                    })  
                }
            },
    decode: function(value){
                var html_decode_dict = {"&amp":'&', "&lt;":'<', "&gt;":'>', "&#39;":"'", '&quot;':'"' };
                if(typeof value == "string"){
                    return ret_fun(value);
                }else{
                    for(var ii in value){
                        if(typeof value[ii] == "string")  value[ii] = ret_fun(value[ii]);        
                    }
                return value;    
                }
    
                function ret_fun(str){
                    return str.replace(/&amp;|&lt;|&gt;|&#39;|&quot;/g, function(tt){
                        return html_decode_dict[tt];
                    });   
                }
            },
    getCookie: function(name){
                    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
                    return r ? r[1] : undefined;
            },
    getQuery: function(name){
                    var reg = new RegExp("(^|\\?|&)"+ name +"=([^&]*)(\\s|&|$)", "i");
                    if (reg.test(location.href)) return unescape(RegExp.$2.replace(/\+/g, " ")); return "";
            },
    postJSON: function(url, args, callback_before,callback_success , callback_error ){
                    args._xsrf = jQuery.getCookie("_xsrf");
                    $.ajax({
                        url: url, 
                        data: $.param(args), 
                        dataType: "json", 
                        type: "POST",
                        contentType:"application/x-www-form-urlencoded; charset=utf-8",
    		                  beforeSend:function(){  callback_before();  },
                        success:function(response) {   if(callback_success) callback_success(response);   }, 
    		                  error: function(response, textStatus) { callback_error(textStatus);   }
	                   });
            }	
    
});

jQuery.fn.extend({
    FormToDict: function(){
                    var fields = this.serializeArray();
                    var json = {}
                    for (var i = 0; i < fields.length; i++) {
                        json[fields[i].name] = fields[i].value;
                    }
                    if (json.next) delete json.next;
                    return json;
                },
    DivToDict: function(){
                    var json = {};
                    var root_this = $(this),
                        self_this,
                        input_type,
                        key,
                        value;
                    root_this.find('input').each(function(){
                        self_this = $(this); input_type = self_this.attr("type");
                        key = self_this.attr("name"); value = jQuery.trim(self_this.val());
                        switch(input_type){
                            case 'radio':
                                if(self_this.attr('checked') != undefined ){
                                    json[key] = value;
                                }
                                break;
                            case 'checkbox':
                                if(self_this.attr("checked") != undefined){
                                    if(key in json){ 
                                        json[key].push(value);                    
                                    }else{
                                        json[key] = []; json[key].push(value);                    
                                    }			     
                                }
                                break;
                            default:
                                json[key] = value;
                                break;  
                        }
                    });
                    root_this.children().find('textarea').each(function(){
                        json[$(this).attr("name")] = $.trim($(this).val());	
                    });
                    root_this.children().find('select').each(function(){
                        json[$(this).attr("name")] = $.trim($(this).val());	
                    });
                    return json;
                }
});


pop_page = function(_width , _height , _content){
    var page_height = $(document).height(),
        page_width = $(document).width(),
        screen_height = $(window).height(),
        screen_width = $(window).width();

    if(screen_height < _height)	screen_height = _height;
    if(screen_width < _width)	screen_width = _width;
    var top_length = ( screen_height - _height )/2 - 30;
    if(top_length <=0) top_length = 0;
    var left_length = ( screen_width - _width )/2 - 15;
    if(left_length <=0) left_length = 0;
	
    var $pop_overlay = jQuery(document.getElementById("pop-overlay")),
        $pop_wrap = jQuery(document.getElementById("pop-wrap")),
        $pop_content = jQuery(document.getElementById("pop-content")); 
               
    $pop_overlay.css({"height": parseInt(page_height) + "px","width":parseInt(page_width) + "px"})
                .fadeIn(200,function(){
                        $pop_wrap.css({"width":parseInt(_width) + "px", 
			                             "height": parseInt(_height) +"px",
			                             "top":parseInt(top_length) + "px",
			                             "left":parseInt(left_length)+"px"
			                             }).fadeIn(200);
                        $pop_content.css({"width":parseInt(_width)-20 +"px","height":parseInt(_height)-20 + "px"});
                        if(typeof _content == "object"){
                            $pop_content.html('').append(_content);			
                        }else{
                            $pop_content.html(_content);
                        }
                });
    setTimeout(function(){}, 0);
    return $pop_content;
}

/******************pop page close **************************************/
pop_page_close = function(){
    $("#pop-wrap").fadeOut(200,function(){
        $("#pop-overlay").fadeOut(200);
        $("#pop-content").html('');
    });	
}




})(jQuery);