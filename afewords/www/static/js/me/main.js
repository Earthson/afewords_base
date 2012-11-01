(function($){

jQuery.com = jQuery.com || {};
jQuery.afewords = jQuery.afewords || {};
jQuery.afewords.user_group = {};
jQuery.afewords.user_book = {};
jQuery.com.afewords = jQuery.com.afewords || {};
jQuery.com.afewords.www = jQuery.com.afewords.www || {};
jQuery.com.afewords.www.user_group = jQuery.com.afewords.www.user_group || {};  // for group
jQuery.com.afewords.www.user_write = jQuery.com.afewords.www.user_write || {};  // for write page
jQuery.com.afewords.www.user_blog = jQuery.com.afewords.www.user_blog || {};  // for blog
jQuery.com.afewords.www.user_init = jQuery.com.afewords.www.user_init || {};  // for init
jQuery.com.afewords.www.user_settings = jQuery.com.afewords.www.user_settings || {};  // for settings
jQuery.com.afewords.www.user_tool = jQuery.com.afewords.www.user_tool || {};  // tools
jQuery.com.afewords.www.user_URI = jQuery.com.afewords.www.user_URI || {};  // URI
jQuery.com.afewords.www.user_login = jQuery.com.afewords.www.user_login || {};  // for login,reg,reset
jQuery.com.afewords.www.user_control = jQuery.com.afewords.user_control || {};  // for all user's control 

$Control = jQuery.com.afewords.www.user_control;

jQuery.extend({
    log: function(value){
        if(console && typeof console.log == "function")
            console.log(value);    
    }
});

$URI = jQuery.com.afewords.www.user_URI;
$URI.login_url = '/';
$URI.register_url = '/reg';
$URI.wrtie_url = '/write';
$URI.write_new_src = '/new';
$URI.write_update_src = '/update';
$URI.write_delete_src = '/del';
$URI.crop_image_url = '/crop-image';
$URI.upload_image_url = '/upload-image';


$Tool = jQuery.com.afewords.www.user_tool;
$Login = jQuery.com.afewords.www.user_login;
$Control = jQuery.com.afewords.www.user_control || {};


/******** form to dict **************/
jQuery.fn.FormToDict = function() {
    var fields = this.serializeArray();
    var json = {}
    for (var i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value;
    }
    if (json.next) delete json.next;
    return json;
};

/************ ALL DIV input textarea select to dict ********************/
jQuery.fn.DivToDict = function() {
	var json = {};
    var root_this = $(this);
	root_this.find('input').each(function(){
        var self_this = $(this);
        var input_type = self_this.attr("type");
        var key = self_this.attr("name");
        var value = $.trim(self_this.val());
        switch(input_type){
            case 'radio':
                if(self_this.attr('checked') == 'checked'){
				    json[key] = value;
			    }
			    break;
			case 'checkbox':
			     if(self_this.attr("checked") == 'checked'){
			         //alert(value);
                    if(key in json){
                        json[key].push(value);                    
                    }else{
                        json[key] = new Array();
                        json[key].push(value);                    
                    }			     
			     }
			     break;
			default:
			    json[key] = value;  
			    //alert(json[key]);      
        
        }
	});
	root_this.children().find('textarea').each(function(){
		json[$(this).attr("name")] = $.trim($(this).val());	
	});
	root_this.children().find('select').each(function(){
		json[$(this).attr("name")] = $.trim($(this).val());	
	});
	
	return json;
};


getQueryStringRegExp = function(name)
{
    var reg = new RegExp("(^|\\?|&)"+ name +"=([^&]*)(\\s|&|$)", "i");
    if (reg.test(location.href)) return unescape(RegExp.$2.replace(/\+/g, " ")); return "";
};


jQuery.getCookie =function(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
};

jQuery.postJSON = function(url, args, callback_before,callback_success , callback_error ){
    args._xsrf = jQuery.getCookie("_xsrf");
    $.ajax({
            url: url, 
            data: $.param(args), 
            dataType: "json", 
            type: "POST",
            contentType:"application/x-www-form-urlencoded; charset=utf-8",
    		beforeSend:function(){
    			callback_before();
    		},
            success:function(response) {
        		if(callback_success) callback_success(response);
    		}, 
    		error: function(response, textStatus) {
    			callback_error(textStatus);
		    }
	});
};	

/*********** fixed the width and height ***************/
web_page_fixed = function(){
    var url = location.href;
    /********* for different page  ************/
    if(url){
        page_height = $(document).height();
 		page_width = $(document).width();
        if(page_height<600)	page_height = 600;
 		page_height -= 160;
        if(url.search('reg')!=-1 || url.search('login')!=-1 ){
            /**** login page ****/
  		    $("#middle-in").css("height",parseInt(page_height) + "px");
  		    $("#login").find("table").css("margin-top",parseInt((page_height-400)/3) + "px");
            return;
        }
        if(url.search('settings')!=-1 ){
  		    $("#middle-in").css("height",parseInt(page_height) + "px");
  		    $("#login").find("table").css("margin-top",parseInt((page_height-400)/2) + "px");
            return ;
        }
        if(url.search('user-lib')!=-1 || url.search('feed')!=-1){
            $("#right1").css("height",parseInt(page_height) + "px");
            return ;
        }
    }
}

$Tool.change_code = change_code = function(){
	$("#code_img").html('<img src="/code" alt="验证图片" class="code-img" >');
}


$Tool.image_upload_handler = image_upload_handler = function(image_for, image_process, image_path, image_more_info){
    // image upload handler, contains user avatar, group logo, article
    switch(image_for){
        case 'avatar':
            avatar_handler(image_process, image_path);
            break;
        case 'logo':
            avatar_handler(image_process, image_path, image_more_info);
            break;
        case 'article':
            picture_upload_handler(image_process, image_path, 0, 0 ,-1 , 0);
            break;
        default: break;    
    
    }
    
    function avatar_handler(result, src){
          
          var $process = $('.self-upload-process');
          var $tag = $("#crop-contain");
          var $up_but = $("#self-img-up-upb");    
          var img_src = src;
          var append_html = '';
          if(result == 1 || result == '1'){
            $up_but.removeAttr("disabled").css("color","#555");
            $process.html(src).css('color','red');	 
               
            return  false;    
          }
          $process.html('头像上传成功，在下面区域您可以裁剪它！').css('color','blue');
          if($tag.length < 1){
            // create new block to crop image 
            
            append_html = '<div class="self-img-up" style="margin-top:20px;" id="self-img-up-tag">裁剪头像：</div>'+
                        '<table style="margin-top:5px;" id="form-avatar" style="display:none">' +
                        '<tr>'+
                    	'<td rowspan="5" id="crop-contain">'+
		                '<img src="' + img_src + '" id="crop-obj" />'+
	                   '</td>' +
                        '</tr>' +
                        '<tr><td align="center" width="150px;">'+
	                    '<div style="width:120px;height:120px;overflow:hidden;">'+
		                '<img src="' + img_src + '" id="preview-120" alt="Preview" />'+
	                    '</div>'+
	                    '</td>'+
                        '</tr>'+
                        '<tr><td align="center" height="100px;">'+
	                   '<div style="width:50px;height:50px;overflow:hidden;">'+
		             '<img src="'+ img_src +'" id="preview-50" alt="Preview" />'+
		            '</div>'+
                    '</td></tr>' +
                    '<tr><td align="center" id="crop-process">&nbsp;</td></tr>'+ 
                    '<tr><td align="center">'+
                    
                    '<input type="hidden" name="pos-x" id="pos-x" value="0" />' +
                    '<input type="hidden" name="pos-y" id="pos-y" value="0" />' +
                    '<input type="hidden" name="pos-w" id="pos-w" value="0" />' +
                    '<input type="hidden" name="pos-time" id="pos-time" value="1" />';
               if(arguments.length >= 3){
                    append_html += '<input type="hidden" name="crop_type" value="logo" />'+
                        '<input type="hidden" name="group_id" value="' + arguments[2] + '" />';
               }else{
                    append_html += '<input type="hidden" name="crop_type" value="logo" />';
               }
               append_html += '<button class="self-intro-button" style="margin-left:20px;">提交</button>'+
                    '</td></tr>' +
                    '</table>';
                $append_html = $(append_html);
                $("#self").append($append_html);
                $("#self").find("button.self-intro-button").bind('click', function(){
                       $Set.do_crop_image(this); 
                }); 
                $('#crop-contain>img').load(function(){
                    $Set.do_crop_init(); 
                }).error(function(){
                    $('#crop-process').html('图片加载失败！').css('color', 'red');                
                });
                        
          }else{
          
            $('#crop-contain').empty().append("<img id='crop-obj'/>");  
		  //$("#target").attr('src','/static/avatar/650/'+info);
		    $('#crop-obj').attr('src', img_src);  
		    $('#preview-120').attr('src', img_src); 
		    $('#preview-50').attr('src',img_src); 
		    $('#crop-contain>img').load(function(){
                    $Set.do_crop_init(); 
                }).error(function(){
                    $('#crop-process').html('图片加载失败！').css('color', 'red');                
                });      
          }
    }
    
    
}














/*************** pop page function ***********************/
pop_page = function(_width , _height , _content){
	var page_height = $(document).height();
	var page_width = $(document).width();
	var screen_height = $(window).height();
	var screen_width = $(window).width();
	//alert(screen_height);
	if(screen_height < _height)	screen_height = _height;
	if(screen_width < _width)	screen_width = _width;
	var top_length = ( screen_height - _height )/2 - 30;
	if(top_length <=0) top_length = 0;
	var left_length = ( screen_width - _width )/2 - 15;
	if(left_length <=0) left_length = 0;
	
    var $pop_overlay = $("#pop-overlay"),
        $pop_wrap = $("#pop-wrap"),
        $pop_content = $("#pop-content");        
        	//alert(top_length);
	$pop_overlay.css({"height": parseInt(page_height) + "px","width":parseInt(page_width) + "px"})
	           .fadeIn(200,function(){
			                 $pop_wrap.css({"width":parseInt(_width) + "px", 
			                         "height": parseInt(_height) +"px",
			                         "top":parseInt(top_length) + "px",
			                         "left":parseInt(left_length)+"px"
			                         })
			         .fadeIn(200);
			         $pop_content.css({"width":parseInt(_width)-20 +"px","height":parseInt(_height)-20 + "px"});

			         if(typeof _content == "object"){
                $pop_content.html('').append(_content);			
			         }else{
			             $pop_content.html(_content);
			         }
		  });
		  return $pop_content;
}

/******************pop page close **************************************/
pop_page_close = function(){
	$("#pop-wrap").fadeOut(200,function(){
		$("#pop-overlay").fadeOut(200);
		$("#pop-content").html('');
	});	
}


/************************ do follow *******************************/

do_follow = function(obj){
    var mes = {}
    var $obj = $(obj);
    var page = $obj.attr("page") || "author";
    var want = $obj.attr("do") || "follow";
    var follow_id = $obj.attr("follow_id");
    var follow_type = $obj.attr('follow_type') ||'author';

    mes['do'] = want;
    mes['id'] = follow_id;
    mes['follow_type'] = follow_type;
    //alert(want);
    $.postJSON('/do-follow',mes,
		function(){ 
        },
		function(response){
			if(response.kind == 0){
		          switch(page){
		          case 'settings-follow':
                        $obj.parent().parent().parent().remove();
                        break;
                  case 'group-home':
                    if(want=="follow"){
                            $obj.attr("do",'unfollow').html("退出小组");
                     }else{
                            $obj.attr("do",'follow').html("加入小组");
                     }
                     break;
                  case 'follow':
                    $obj.parent().parent().parent().fadeOut('slow');
                    break;
                  case 'settings-follower':
                  default:
                    if(want=="follow"){
                            $obj.attr("do",'unfollow').html("取消关注");
                     }else{
                            $obj.attr("do",'follow').html("关注");
                     }
                     break;
                }
            }else{
			     return false;
            }
		},
		function(response){
			return false;
		}
	);	 
}

do_like = function(obj){
    var mes = {};
    var $obj = $(obj);
    var page = $obj.attr("page") || 'blog';
    var want = $obj.attr("do");
    var like = $obj.attr("obj_id");
    var kind = $obj.attr("kind") || 'blog';
    
    mes['do'] = want;
    mes['id'] = like;
    mes['type'] = kind;
    
    //alert(want);
    $.postJSON('/do-like',mes,
		function(){ 
        },
		function(response){
			if(response.kind == 0){
			     switch(page){
			         case 'blog':
			             if(want=='view'){
                            $obj.html(parseInt($obj.html()) + 1);     
                            return;                   
                        }
                        if(want=="like"){
                            $obj.attr("do",'unlike').html('-1').prev().html( function(index, old){
                                return '' + (parseInt(old) + 1);
                            });
                        }else{
                            $obj.attr("do",'like').html('+1').prev().html(function(index, old){
                                return '' + (parseInt(old)- 1);
                         });
                        };
                        
                    
                    break;
                 case 'settings':
                    $obj.parent('li').slideUp(300, function(){ $(this).remove()});
                    break;                
                }
            }else{
			     return false;
            }
		},
		function(response){
			return false;
		}
	);	 
}




draft_del_open = function(obj){
    $(obj).find(".draft-del-style").show();
}
draft_del_close = function(obj){
    $(obj).find(".draft-del-style").hide();
}

do_draft_del = function(obj){
    result = confirm("确认删除？");
	if(result){
		// delete the draft
		var mes = {};
		mes['article_id'] = $(obj).attr("article_id");
        mes['article_type'] = $(obj).attr("type");
		$.postJSON('/del-draft',mes,
			function(){},
			function(response){
				if(response.kind == 0){
					//delete the source
                    alert('删除成功！');
					$(obj).parent().slideUp();
				}else{
					//alert(response.info);	
				}	
			},
			function(response){  }
		);
	}
}


$Control.do_noti_flag_set = function(obj){
    var $li = $(obj).parent();
    var noti_index = $li.attr("index") || -1;
    var noti_do = $li.attr("do") || 'read';
    var mes = {};
    mes['index'] = noti_index;
    mes['do'] = noti_do;
    mes['is_all'] = $li.attr("is_all") || 'no';
    $.postJSON('/notice', mes, 
    function(){
    
    },function(response){
        if(response.kind == 0){
            
            if($li[0].nodeName == "LI"){
                $li.removeClass("noti-read-False").addClass("noti-read-True");   
            }else{
                if($li[0].nodeName == "SPAN"){
                    var $notice_div = $('#body_content').find('ul');
                    $notice_div.find('li').removeClass('noti-read-False').addClass('noti-read-True');
                    if(noti_do=="delete" && mes['is_all'] == "yes"){
                        $notice_div.html('<div>没有消息！</div>');                    
                    }                
                }            
            }
        }
    },function(response){
        
    });

}

afewords_marquee = function(){
    var $ul = $('ul.afw_info');
    var $li = $ul.find('li');
    $li.eq(0).slideUp('slow', function(){
        $(this).appendTo($ul).show();
    });
    setTimeout(afewords_marquee, 2000);
}

$Tool.html_encode = function(value){
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
}

$Tool.html_decode =  function(value){
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
}
jQuery.extend({
    encode: jQuery.com.afewords.www.user_tool.html_encode,
    decode: jQuery.com.afewords.www.user_tool.html_decode,
    back_to_top: function(){
        var times = 10;
        var pass = 1;
        $(window).scroll(function(){
            var scroll_top = $(this).scrollTop();
            var screen_height = document.body.offsetHeight;
            if(scroll_top > screen_height){
                $("#go-to-top").fadeIn('slow').die().live('click', function(){
                    times = 10;
                    pass = 1;
                    go_algorithm(1);
                    
                });            
            }else{
                $("#go-to-top").fadeOut('slow');            
            }
        });
        
        function go_algorithm(){
            //console.log(pass);
            //console.log(times);
             var scroll_top = $(window).scrollTop();
             var screen_height = document.body.offsetHeight;
             var dif = scroll_top - screen_height;
             if( dif > 0){
                 if(dif < 40){
                    document.body.scrollTop = 0;
                    dif = 0;
                 }else{
                    document.body.scrollTop = dif - dif/times;
                    dif = dif - dif/times;
                    pass++;
                    times = (10 - pass) <= 0 ? 5 : (10-pass);
                    setTimeout(go_algorithm,50);   
                 }
             }
        }

    }
});

jQuery.fn.extend({
    fix_to_head : function(want_top) {
        if (arguments.length ==0)
            var want_top = 0;
	    var position = function(element) {
		  var top = element.position().top, pos = element.css("position");
		  var left = element.offset().left, width=element.width();
		  var absolute_top = element.offset().top;
          var height = element.height();
          var margin_top = element.css('margin-top');
          if(height > $(window).height()) return false;
		  $(window).scroll(function() {
			var scrolls = $(this).scrollTop();
			if (scrolls > absolute_top) {
				if (window.XMLHttpRequest) {
					element.css({ 'position': "fixed", 'top': want_top, 'left':left, 'width':width, 'margin-top':'0px'});	
				} else {
					element.css({
						top: scrolls
					});	
				}
			}else {
				element.css({position: pos, 'top':top, 'left':0, 'margin-top':margin_top});	
			}
		  });
        };

        function position_to_left(element){
            if(element.parent().get(0).tagName == 'BODY'){
                //console.log(element.position().left);
                return element.position().left;            
            }else{
                
                return element.position().left + arguments.callee(element.parent());         
            }
        }        
        
	   return $(this).each(function() {
		  position($(this));						 
	   });
    },
    go_to_top : function(want){
        if(arguments.length <= 0){ var want = $(this).position().top; }
        document.body.scrollTop = want;
    }
});



})(jQuery);