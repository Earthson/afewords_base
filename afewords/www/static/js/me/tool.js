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

jQuery.afewords = jQuery.afewords || {};
jQuery.afewords.tools = jQuery.afewords.tools || {};
jQuery.extend(jQuery.afewords.tools, {
    repeat_mail:    function(_mail_, $process, _end){
                        var _start =  0;
                        if(_end == undefined){ _end = 30; }
                        
                        function ajax_submit(obj){
                            var mes = { 'email': jQuery(obj).attr("email") };
                            jQuery.postJSON('/repeat-mail', mes, function(){ $process.ajax_process(); },
                                function(response){
                                    if(response.status != 0){
                                        var texts = '发送失败，<span id="repeat_time_all">点击重新发送<span>！';
                                        var end_time = 0;
                                    }else{
                                        var end_time = 30;
                                        var texts = '验证邮件已经发送至您的邮箱！<span id="repeat_time_all"><span id="repeat_time" class="font-14">30</span>秒后可重新发送验证邮件！</span>';
                                    }                                        
                                    $process.right_process(texts);
                                    var interval = jQuery.afewords.tools.repeat_mail(_mail_, $process, end_time);
                                    interval["interval"]();                                         
                                },
                                function(textStatus){
                                    var texts = '出现错误，<span id="repeat_time_all"><span id="repeat_time" class="font-14">30</span>秒后重新发送<span>！';
                                    $process.error_process( texts); 
                                    var interval = jQuery.afewords.tools.repeat_mail(_mail_, $process, 0);
                                    interval["interval"]();                                    
                                });
                        }
                        return {
                            "interval": function(){
                                            if(_start++ < _end){
                                                $("#repeat_time").html(_end - _start);
                                                setTimeout(arguments.callee, 1000);
                                                                                            
                                            }else{
                                                var $tmp_link = $('<a></a>');
                                                $tmp_link.attr({"href":"javascript:void(0);", "email": _mail_});
                                                $tmp_link.text('重新发送邮件');
                                                $("#repeat_time_all").html('').append($tmp_link);
                                                $tmp_link.bind('click', function(){ ajax_submit(this)} );   
                                            }
                                        }                     
                        }
                    }
})

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
                    root_this.find('textarea').each(function(){
                        json[$(this).attr("name")] = $.trim($(this).val());	
                    });
                    root_this.find('select').each(function(){
                        json[$(this).attr("name")] = $.trim($(this).val());	
                    });
                    return json;
                },
    // for button
    to_disabled:    function(){
                        $(this).attr("disabled", "disabled").css("color", "#ccc");    
                    },
    remove_disabled: function(){
                        $(this).removeAttr("disabled").css("color", "black");
                    },
    // for process
    right_process:  function(_text_, _color_){
                        _color_ = _color_ || "blue";
                        $(this).html(_text_).css("color", _color_);    
                    },
    error_process:  function(_text_, _color_ ){
                        _color_ = _color_ || "red";
                        $(this).html(_text_).css("color", _color_);    
                    },
    ajax_process:   function(){
                        $(this).html('<img src="/static/img/ajax.gif" />'); 
                    },
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