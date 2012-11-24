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
            },
    check_email: function(email){
                    var email_reg = (/^\w+((-\w+)|(\.\w+))*@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/);
                    if(!email || !email_reg.test(email))    return false;
                    return true;
    },
    check_chapter: function(_num){
                    var _num_reg = /^\d+(\.\d+)*$/gi;
                    if(!_num || _num.search(_num_reg) == -1)    return false;
                    return true;    
    },
    close_window_alert: function(){
        jQuery(window).unbind('beforeunload');
        jQuery(window).unload(function(){});    
    },
    get_article_from_url:   function(url){
                    var url_list = url.split('/'), list_len = url_list.length;
                    if(list_len < 3) return {'return': false};
                    return {'article_id': url_list[list_len-1], 'article_type': url_list[list_len-2], "return": true};
    },
    get_book_from_url:  function(url){
                    var url_list = url.split('/'), list_len = url_list.length;
                    if(list_len < 4)    return {'return': false};
                    return {'return': true, 'book_id': url_list[list_len-3], 'node_id': url_list[list_len-1]};
    },
    cursor_to_top: function(){
    
                    var times = 10;
                    var pass = 1,
                        $to_top = jQuery("#go-to-top");
                    jQuery(window).scroll(function(){
                        var scroll_top = $(this).scrollTop();
                        var screen_height = document.body.offsetHeight;
                        if(scroll_top > screen_height){
                            $to_top.fadeIn('slow').die().live('click', function(){
                                times = 10;
                                pass = 1;
                                go_algorithm(1);
                            });            
                        }else{
                            $to_top.fadeOut('slow');            
                        }
                    });
        
                    function go_algorithm(){
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
                            };
                        }
                    }
    },
    crop_picture_init: function(){
    
        var jcrop_api, boundx, boundy,
            $image_block = jQuery('#crop-contain>img').eq(0),
            block_width = 0,
            image_width = 0,
            new_image = new Image(),
            $pos_sx = jQuery("#pos-sx"),
            $pos_sy = jQuery("#pos-sy"),
            $pos_ex = jQuery("#pos-ex"),
            $pos_ey = jQuery("#pos-ey"),
            s_x = s_y = e_x = e_y = 0,
            $preview_120 = jQuery("#preview-120"),
            $preview_50 = jQuery("#preview-50");
            new_image.src = $image_block.get(0).src,
            $button = jQuery('#crop-button'),
            $process = jQuery('#crop-process'),
            times = 0;
        $image_block.load(function(){
            image_width = new_image.width;
            times = image_width / $image_block.width() ;
            $image_block.Jcrop({
                onChange: updatePreview,
                onSelect: updatePreview,
                aspectRatio: 1,
                minSize : [150,150],
                setSelect:[0,0,150,150],
                bgColor: 'black',
                maxSize:[400,400]
            },function(){
                var bounds = this.getBounds();
                boundx = bounds[0];
                boundy = bounds[1];
                jcrop_api = this;
            });
        });
        $image_block.error(function(){
            $process.error_process("图片打开失败！");
        });
        
        function updatePreview(c){
            if(parseInt(c.w, 10) < 0)   return;
            var rx = 120 / c.w;
            var ry = 120 / c.h;
            $preview_120.css({
                    width: Math.round(rx * boundx) + 'px',
                    height: Math.round(ry * boundy) + 'px',
                    marginLeft: '-' + Math.round(rx * c.x) + 'px',
                    marginTop: '-' + Math.round(ry * c.y) + 'px'
            });
            var rx_1 = 50/c.w;
            var ry_1 = 50/c.h;
            $preview_50.css({
                width: Math.round(rx_1 * boundx) + 'px',
                height: Math.round(ry_1 * boundy) + 'px',
                marginLeft: '-' + Math.round(rx_1 * c.x) + 'px',
                marginTop: '-' + Math.round(ry_1 * c.y) + 'px'
            });
            var true_width = c.w * times, true_height = c.h * times;
            s_x = parseInt(c.x * times, 10); s_y = parseInt(c.y * times, 10); 
            e_x = parseInt(s_x + true_width, 10), e_y = parseInt(s_y + true_height, 10);
            $pos_sx.val(s_x);
            $pos_sy.val(s_y);
            $pos_ex.val(e_x);
            $pos_ey.val(e_y);
            $button.removeAttr("disabled").css("color", "black");
        };
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

jQuery.afewords.tools.Global_Funs = {
    "login": {
                "check": function(paras){
                            if(!jQuery.check_email(paras['email'])) return [-1, '请您填写正确的邮箱！'];
                            if(!paras['pwd'])
                                return [-1, '请填写密码！'];
                            if(!paras['token'])
                                return [-1, '请填写验证码！'];
                            return [1, '']
                         }    
            },
    "reg": {
                "url": '/reg',
                "check": function(paras){
                            if(!jQuery.check_email(paras['email'])) return [-1, '请您填写正确的邮箱！'];
                            if(!paras['name']){ return [-1, '请您填写姓名！'];  }	
                            if(paras['name'].length < 2){ return [-1, '姓名至少为两个字！'];  }
                            
                            if(!paras['pwd'] || paras['pwd'].length < 4){ return [-1, '请您设置登陆密码，至少为四位！'];	}	
                            if(paras['pwd'] != paras['pwd_again']){ return [-1, '确认密码错误！'];	}
                            if(!paras['token']){ return [-1, '请填写验证码！']; }
                            return [1, '']
                },
                "handler": function( paras, $process ){
                            // repeat mail
                            var texts = '验证邮件已经发送至您的邮箱！<span id="repeat_time_all"><span id="repeat_time" class="font-14">30</span>秒后可重新发送验证邮件！</span>';
                            $process.right_process(texts);      
                }
                   
        },
    "reset":    {
                    "url": "/reset",
                    "check": function(paras){
                                if(!jQuery.check_email(paras['email'])) return [-1, '请您填写正确的邮箱！'];
                                if(!paras['pwd'] || paras['pwd'].length < 4) return [-1, '设置的密码需要4位以上！'];
                                if(paras['pwd'] != paras['pwd_again']) return [-1, "确认密码出错！"]
                                if(!paras['token']) return [-1, '请您填写验证码！']
                                return [1, '']
                    },
                    "handler": function( paras, $process ){
                            // repeat mail
                            var texts = '密码重置邮件已经发送至您的邮箱！<span id="repeat_time_all"><span id="repeat_time" class="font-14">30</span>秒后可重新发送验证邮件！</span>';
                            $process.right_process(texts);      
                    }
        },
    "mail_check": function(){
                    var pop_html = '<div id="pop_insert_table">' + 
                        '<p class="first">邮箱验证 - 未验证用户不能发表任何信息</p>' + 
                        '<p><button>发送验证邮件</button><span class="t_process" style="width:50%"></span></p>'+
                        '</div>';
                    var $pop_content = pop_page(500,150, pop_html);
                    $pop_content.bind('click', function(e){
                        if(e.target.nodeName != "BUTTON")  return;
                        var $button = jQuery(e.target), $process = $button.siblings("span"),
                            url = '/send-verification';
                        jQuery.postJSON(url, {}, function(){
                            $button.to_disabled(); $process.ajax_process();                        
                        }, function(response){
                            if(response.status != 0){ $button.remove_disabled();  $process.error_process(response.info); }
                            else{ 
                                $process.right_process("发送成功,10秒后可重新发送！");
                                var seconds = 30;
                                setTimeout(function(){
                                    if(seconds > 0) { 
                                        $process.right_process( seconds + "秒后可重新发送！");
                                        seconds--; 
                                        setTimeout(arguments.callee, 1000);                                    
                                    }
                                    else{
                                        $process.right_process("");  $button.remove_disabled();
                                    }
                                                                    
                                }, 1000);                            
                            }                        
                        }, function(textStatus){ $process.error_process("出现错误：" + textStatus); $button.remove_disabled(); } );                    
                    });
    },
    "domain":   {
                    "url": "/settingpost-user_domain",
                    "pop":  function(){
                                var tag_html = '<div id="pop_insert_table">' + 
                                                "<p class='first'>个性化</p><p>新链接后缀<input type='text' name='domain' />" + 
                                                "<p><button>修改</button><span class='t_process' style='width:70%'></span></p>"+
                                              '</div>';
                                var $pop_page = pop_page(350,180, tag_html);
                                $pop_page.bind('click', function(e){
                                    if(e.target.nodeName != "BUTTON")   return false;
                                    var mes = $pop_page.DivToDict(),  $this = jQuery(e.target), $process = $this.siblings('span.t_process');
                                    var regstr = /^[a-zA-Z0-9\.]+$/ig;
                                    if(!mes['domain'] || !regstr.test(mes['domain'])){
                                        $process.error_process('后缀为a-z，A-Z,0-9.');
                                        return false;
                                    }                                 
                                    jQuery.postJSON('/settingpost-user_domain', mes, 
                                        function(){ $process.ajax_process(); $this.to_disabled(); }, 
                                        function(response){
                                            if(response.status != 0){
                                                $process.error_process(response.info); $this.remove_disabled(); return;                                        
                                            }else{
                                                $process.right_process("设置成功！");
                                                $("div.my_domain").html('链接为：http://www.afewords.com/user/' + mes['domain']);  
                                                pop_page_close();                                          
                                            }                                       
                                        }, 
                                        function( textStatus ){
                                            $process.error_process("出现错误：" + textStatus); $this.remove_disabled();                                        
                                        });                                
                                });
                    },
                    "check": function(paras){},
                    "handler": function(){}
                },
    "tag":      {
                    "url": "/settingpost-user_addtag",
                    "pop":  function(){
                                var url = "/settingpost-user_addtag";
                                var tag_html = '<div id="pop_insert_table">'+
                                                '<p class="first">添加新分类</p>' + 
                                                '<p>新分类名<input type="text" name="tag" /></p>' +
                                                '<p><button>添加</button><span class="t_process" style="width:70%"></span></p>' + 
                                                '</div>';
                                $tag_html = jQuery(tag_html);
                                var $pop_content = pop_page(350,180, $tag_html);
                                $tag_html.find('button').click(function(){
                                    var $this = jQuery(this), $process = $this.siblings('span.t_process');
                                    var mes = $tag_html.DivToDict();
                                    
                                    if(!mes['tag']){    $process.error_process("请填写新的分类（15字内）！"); return;}
                                    mes['new_tag'] = mes['tag'];
                                    jQuery.postJSON(url, mes, function(){ $process.ajax_process(); $this.to_disabled(); },
                                        function(response){
                                            if(response.status != 0){
                                                $this.remove_disabled(); $process.error_process(response.info); return;                                            
                                            }else{
                                                // add tag ok
                                                handler(mes);
                                                pop_page_close();             
                                            }
                                        },
                                        function(textStatus){
                                            $this.remove_disabled(); $process.error_process("出现错误："+ textStatus);                                        
                                        })
                                });
                                function handler(mes){
                                    var subpage_type = AFWUser['subpage_type'];
                                    switch(subpage_type){
                                        case "write":
                                            var tag_html = '<span class="w-class"><label><input type="checkbox" name="classes" value="' + $.encode(mes['tag']) + '" />'+
                                                            $.encode( mes['tag'] )+'</label></span>';
                                            $('div.w-class').find('div').eq(1).append(tag_html);
                                            break;
                                        case "tag":
                                            var tag_html = '<li class="li"><a href="/blog-lib/?tag=' + $.encode(mes['tag']) +'" class="tag-link" >' +
                                                        $.encode(mes['tag']) +'</a><span class="tag-del hide_span" tag="' + $.encode(mes['tag']) +'" do="remove_tag">删除</span></li>';
                                            var $ul = $('div.settings').find('ul');
                                            if($ul.length){
                                                $ul.append(tag_html);                        
                                            }else{
                                                $('#tag-note').remove();
                                                $('div.settings').find(".div-20").eq(0).after('<ul class="ul like_ul">'+ tag_html +'</ul>');                        
                                            }
                                            break;                                    
                                    }                              
                                }
                    },
                    "check":    function(paras){},
                    "handler": function(){}    
                },
    "avatar":   {
                    "url":  "/settingpost-user_avatar",
                    "pop":  function(){
                                var htmls = '<div id="pop_insert_image">' + 
                                            '<p class="first">上传新头像</p>'+
                                            '<form action="/settingpost-user_avatar_upload" id="up_picture" enctype="multipart/form-data" method="post" target="up_picture_iframe">'+
                                            '<input type="hidden" name="_xsrf" value="' + jQuery.getCookie("_xsrf") + '" />'+
                                            '<p><input class="i_file" type="file" name="picture"  /></p>'+
                                            '<p><button type="submit" class="i_button">上传</button><span class="i_process" id="src_process">&nbsp;</span></p></form>' +
                                            '<iframe name="up_picture_iframe" id="up_picture_iframe" style="display:none" src="about:_blank"></iframe>' +
                                            '</div>';
                                $htmls = jQuery(htmls);
                                var $pop_content = pop_page(350,180, $htmls);
                                // bind 
                                var $form = $htmls.find("form"),
                                    $process = $form.find("#src_process"),
                                    $button = $form.find("button");
                                $form.submit(function(){
                                    var file_src = $htmls.find("input.i_file").val();
                                    if(!file_src){  $process.error_process("请选择图片"); return false; }
                                    var img_reg = /.*\.(jpg|png|jpeg|gif)$/ig;
                                    if(!file_src.match(img_reg)) {  $process.error_process('图片格式为jpg,png,jpeg,gif！'); return false; }
                                    $process.ajax_process();
                                    $button.to_disabled();
                                    
                                    var $image_iframe = $htmls.find("#up_picture_iframe").eq(0);
                                    //image_iframe = window.frames["up_picture_iframe"];
                                    $image_iframe.load(function(){

                                        var iframe_document = window.frames["up_picture_iframe"].document;
                                        var response_text = iframe_document.body.getElementsByTagName("textarea")[0].value;
                                        var response = window['eval']('(' + response_text +')');
                                        if(response.status != 0){
                                            $process.error_process(response.info);
                                            $button.remove_disabled();                                        
                                        }else{
                                            $process.right_process("上传成功！");
                                            pop_page_close();
                                            var htmls = create_crop_block(response);
                                            var $avatar_form = jQuery("#avatar_wrap_form");
                                            if(!$avatar_form.length){
                                                jQuery("#avatar_wrap_nav").after(htmls);                                            
                                            }else{
                                                $avatar_form.replaceWith(htmls);                                            
                                            }
                                            jQuery.crop_picture_init();
                                        }                                     
                                                              
                                    });
                                    
                                    $image_iframe.error(function(){
                                        alert("error");                                   
                                    });
                                    return true;                                
                                });
                                function create_crop_block(response){
                                     return '<table id="avatar_wrap_form">'+
                                            '<tr>' +
                                            '<td width="70%" rowspan="2" id="crop-contain">'+
                                            '<img src="'+ response.img_url +'" id="crop-obj" />' +
                                            '</td>' +
                                            '<td width="30%" align="center">'+
                                            '<div id="crop-120">'+
                                            '<img src="'+ response.img_url +'" id="preview-120" />' +
                                            '</div>'+
                                            '</td></tr>' +
                                            '<tr>' +
                                            '<td align="center"><div id="crop-50">'+
                                            '<img src="' + response.img_url + '" id="preview-50" />'+
                                            '</div></td></tr>'+
                                            '</table>';
                                }
                                
                                
                                
                    },
                    "check":    function(paras){},
                    "handler":  function(){}    
                },
    "blog":     {
                    "comment":  function(){ // this must be the jquery object
                                    var $that = this,
                                        reply_comment = $that.attr("iscomment") == "true" || false;
                                    var paras = {   "father_id": $that.attr("father_id"),
                                                    "father_type": $that.attr("father_type"),
                                                    "iscomment": true,
                                                    "article_type": "comment"
                                                };
                                    var create_flag = false;
                                    var $comment_block = jQuery("div.b_com"); 
                                    var info_html = '',
                                        login_flag = true || AFWUser['login'];
                                    if(!login_flag){
                                        info_html = '<div class="com_info"><p>姓名<input type="text" /><span class="note">*建议登陆后评论</span></p>' +
                                                    '<p>邮箱<input type="text" name="email" /></p>'  +
                                                    '<p>验证码<input type="text" class="token" name="token" /><span id="code_img" class="token_img"><img src="/code" /></span><a href="javascript:void(0)" onclick="change_code();" class="code">更换图片</a></p>' +                                   
                                                    '</div>';
                                    }

                                    var reply_block_html = '<div class="com_reply" id="write_comment_zone">' +
                                                            info_html + 
                                                            '<div id="ref_comment_lib">' + 
                                                            '</div>' +
                                                            '<textarea class="bcr_text" id="write_textarea" spellcheck="false" name="body"></textarea>' +
                                                            //'<input type="hidden" name="ref_comment" value="sdfsdf" />' + 
                                                            '<div class="bcr_con"><button>提交</button>'+
                                                            '<span class="comment_process">&nbsp;</span></div>' +
                                                            '</div>'
                                    var $reply_block = jQuery("#write_comment_zone");
                                    if(!$reply_block.length) {
                                        $reply_block = jQuery(reply_block_html);
                                    }else{ create_flag = true; }
                                    var $reply_comment_nest = $reply_block.find('#ref_comment_lib');
                                    var $reply_textarea = $reply_block.find('#write_textarea');
                                    if(reply_comment){
                                        var reply_comment_id = $that.attr("comment_id");
                                        var reply_author_id = $that.attr("author_id");
                                        var reply_author_name = $that.attr("author_name");
                                        var reply_comment_body= $that.parent('.com_nav').siblings(".bb_con1").children('.bb_con').text() || '';
                                        
                                        var reply_comment_short = reply_comment_body.slice(0, 100 > reply_comment_body.length ? reply_comment_body.length: 100);
                                        // reply to comment 
                                        var hidden_input = '<input type="hidden" name="ref_comment" value="'+ reply_comment_id +'" />';                                   
                                        var reply_comment_html = '<div class="ref_comment_one">'+
                                                                '<input type="hidden" name="ref_comment" value="'+ reply_comment_id +'" />' +
                                                                '<a href="javascript:void(0);" class="link_close" do="close_ref">X</a>' +
                                                                '<p>'+ reply_comment_short +'<a href="/blogger/' + reply_author_id + '" class="ref_author">'+
                                                                jQuery.encode(reply_author_name)+'</a></p></div>';
                                        $reply_comment_nest.html(reply_comment_html);
                                        //$reply_comment_nest.append(hidden_input);
                                    }
                                    $comment_block.append($reply_block);
                                    if(!create_flag){
                                        $reply_textarea.create_editor(paras); 
                                        bind_post_comment();                  
                                    }
                                    //if(AFWUser['login']){}
                                    function parse_comment_request(){
                                        var $menu = jQuery("#write_menu");
                                        var mes = $reply_block.DivToDict();
                                        var mes1 = {
                                            'do': 'post',
                                            'article_type': 'comment',
                                            'father_id': $menu.attr('father_id'),
                                            'father_type': $menu.attr('father_type')                                 
                                        }
                                        jQuery.extend(mes, mes1);
                                        return mes;
                                    }
                                    
                                    function bind_post_comment(){
                                        var $button = $reply_block.find('button'), $process = $button.siblings('.comment_process');
                                        $button.bind('click', function(){
                                            var mes = parse_comment_request();
                                            if(!login_flag){
                                                if(!mes['name']){ $process.error_process("请填写姓名！"); return; }
                                                if(!mes['email'] || !jQuery.check_email(mes['email'])) { $process.error_process("请填写正确的邮箱！"); return; } 
                                                if(!mes['token']) { $process.error_process("请填写验证码！"); return; }                                         
                                            }
                                            if(!mes['body'] || mes['body'] == "内容"){    $process.error_process("评论内容不能为空！"); return; }
                                            jQuery.postJSON('/update-article', mes, function(){
                                                    $process.ajax_process();  $button.to_disabled();                                            
                                            },function(response){
                                                if(response.status!= 0){
                                                    $process.error_process(response.info); $button.remove_disabled();  return;                                                
                                                }else{
                                                    $process.right_process("评论成功，输入框即将关闭！"); 
                                                    setTimeout(function(){  $reply_block.remove(); }, 1000);
                                                                                               
                                                }
                                            }, function(textStatus){
                                                $process.error_process("出现错误：" + textStatus);
                                                $button.remove_disabled();                                            
                                            });
                                        })                               
                                    }
                                    
                                },
                    "recommend": function(){
                                    // recommend to the book
                                    var $that = this, configs = jQuery.afewords.tools.Global_Funs;
                                    configs["book_chapter_manage"]["recommend_article"].call($that, function(){});
                                },
                    "like":     function(){
                                    var $that = this,
                                        url = '/obj-dolike',
                                        like_status = $that.attr("like_status"),
                                        mes = { 'obj_id': $that.attr("obj_id"),
                                                "obj_type": $that.attr("obj_type")};
                                    jQuery.postJSON(url, mes, function(){}, function(response){
                                        if(response.status == 0){
                                            if(like_status == "yes"){
                                                $that.html("喜欢").attr("like_status", "no"); return;                                        
                                            }else{
                                                $that.html("取消").attr("like_status", "yes"); return;                                     
                                            }                                        
                                        }
                                    },function(){});                    
                    },
                    "share":    function(){},
                    "view":     function(){
                                    var $that = this;
                                    
                                },
                    "getcomment": function(){   // this must be jquery object
                                    var $that = this;                    
                                    var mes = { 'article_id': $that.attr('article_id'),
                                                'article_type': $that.attr('article_type')};
                                    var $comment_block = jQuery('#article_comment');
                                    jQuery.postJSON('/getcomment', mes, function(){}, handle, function(){});
                                    function handle(response){
                                        if(response.status != 0){
                                            return;                                        
                                        }else{
                                            var comment_list = response.comment_list;
                                            var comment_html = '', ref_comment_html = '';
                                            var current_com ;
                                            for(var i = 0, com_len = comment_list.length; i < com_len; i++){
                                                current_com = comment_list[i];
                                                ref_comment_html = '';
                                                if(current_com.ref_comment_info){
                                                    ref_comment_html = '<div class="ref_comment_div">' + current_com.ref_comment_info + '</div>';                                                
                                                }
                                                var user_link = '/blogger/' +  current_com.author.uid;
                                                comment_html += '<div class="com_one">' +
                                                                '<div class="com_pic"><a href="'+ user_link +'"><img src="'+ current_com.author.thumb +'" /></a></div>' +
                                                                '<div class="com_body">' +
                                                                '<div class="com_con">' +
                                                                '<div class="bb_con1">' + ref_comment_html + 
                                                                '<div class="bb_con">' + current_com.content + '</div>' +
                                                                '</div>' +
                                                                '<div class="com_nav">' + 
                                                                '<span class="com_reply" iscomment="true" do="comment" father_id="'+ mes['article_id'] + '" father_type="'+ mes['article_type'] +
                                                                '" comment_id="'+ current_com.aid +'" author_id="'+ current_com.author.uid +'" author_name="'+ current_com.author.name +'"></span>' +
                                                                '<span class="com_author"><a href="'+ user_link +'" target="_blank">'+ current_com.author.name +'</a></span>' +
                                                                '</div></div></div></div>';                        
                                            }
                                            $comment_block.html(comment_html);
                                      
                                        }    
                                    }
                        },
                    "close_ref": function(){
                                    this.parent().remove();                    
                        }     
                },
    "body_content_button":{
                "crop_avatar":      function( $body_content, $process, mes ){
                                        var $button = $(this),
                                            $process = jQuery("#crop-process"),
                                            mes = $body_content.DivToDict(),
                                            url = '/settingpost-user_avatar_crop';
                                        jQuery.postJSON(url, mes, function(){
                                            $process.ajax_process(); $button.to_disabled();                                        
                                        }, function(response){
                                            if(response.status != 0){
                                                $process.error_process(response.info); $button.remove_disabled();                                            
                                            }else{
                                                $process.right_process("设置成功！");                                     
                                            }
                                        }, function(textStatus){
                                            $process.error_process("出现错误：" + textStatus); $button.remove_disabled();                                        
                                        });
                                        return false;                
                },
                "modify_password":  function( $body_content, $process, mes ){
                                        var $button = this;
                                        if(!mes['passwd_old']){ $process.error_process("请填写原密码！"); return [false]; }
                                        if(!mes['passwd_new'] || mes['passwd_new'].length < 4){ $process.error_process("新密码不少于4位"); return [false];}
                                        if(mes['passwd_new_again'] != mes['passwd_new']){   $process.error_process("确认密码不一致！");  return [false]; } 
                                        return [true, '/settingpost-user_passwd', right_handle];
                                        function right_handle(response){
                                            if(response.status != 0){
                                                $process.error_process(response.info); $button.remove_disabled();                                            
                                            }else{
                                                $process.right_process("密码修改成功！");
                                                setTimeout(function(){
                                                    $process.right_process('');
                                                    $body_content.find('input').val('');
                                                    $button.remove_disabled();                                                
                                                }, 1500);                                            
                                            }
                                        }        
                },
                "create_book":      function( $body_content, $process, mes ){
                                        var $button = jQuery(this);
                                        if(!mes['name']) { $process.error_process("请填写知识谱名称！"); return [false]; }
                                        if(!mes['keywords']) { $process.error_process("请填写关键词【for SEO】!"); return [false]; }
                                        var url = '/book-create';
                                        jQuery.postJSON(url, mes, function(){
                                            $process.ajax_process();  $button.to_disabled();                                        
                                        },function(response){
                                            if(response.status != 0){
                                                $process.error_process(response.info);  $button.remove_disabled();                                            
                                            }else{
                                                $process.right_process("创建成功！3秒后自动跳转到该知识谱的摘要编辑页面！");
                                                setTimeout(function(){
                                                    location.href = '/write?id=' + response.about_id + '&type=about';
                                                }, 3000);                                            
                                            }
                                        }, function(textStatus){
                                            $process.error_process("出现错误：" + textStatus); $button.remove_disabled();                                        
                                        });                                     
                                        return [false];                
                },
                "invite_friend":    function( $body_content, $process, mes){
                                        var $that = this;  // this must be jquery object, it is jquery(button)
                                        
                                        if(!jQuery.check_email(mes['email'])){
                                            $process.error_process("请填写正确的邮箱！");
                                            return [false];                                        
                                        }
                                        
                                        var url ='/settingpost-invite';
                                        function right_handle(response){
                                            if(response.status !=0){
                                                $process.error_process(response.info); $that.remove_disabled();                                            
                                            }else{
                                                $process.right_process("邀请成功！"); 
                                                
                                                setTimeout(function(){ 
                                                    $process.right_process("你可继续邀请！");
                                                    $body_content.find('input').val(''); 
                                                    $that.remove_disabled();
                                                    }, 1500);                                           
                                            }
                                        }
                                        return [true, url, right_handle];                 
                }    
    },
    "book_chapter_manage": {
                "add_modify_chapter":  function( callback ){
                
                                var $that = this, book_id = $that.attr("book_id"), to_do = $that.attr("do"),
                                    $li, old_title = '', old_node_id = '', old_section = '',
                                    url = '/settingpost-book_section_new', tip_str = "添加新",
                                    $catalog_ul = jQuery("#book_wrap").find("ul.catalog_ul");
                                if(to_do == "modify_chapter"){
                                    $li = $that.parent();
                                    old_title = $li.children("span").eq(1).text();
                                    old_node_id = $li.attr("chapter_id");
                                    old_section = $li.children("span").eq(0).text();
                                    
                                    book_id = $catalog_ul.eq(0).attr("book_id") || '';
                                    url = '/settingpost-book_section_modify';
                                    tip_str = "修改";
                                }

                                var pop_html = '<div id="pop_insert_table">' +
                                                '<input type="hidden" name="book_id" value="'+book_id+'" />'+
                                                '<input type="hidden" name="node_id" value="'+ old_node_id +'" />' +
                                                '<p class="first">'+ tip_str +'目录</p>'+
                                                '<p>章节<input type="text" name="section" autocomplete="off" value="'+ old_section +'" /></p>'+
                                                '<p>标题<input type="text" name="title" autocomplete="off" value="'+ old_title +'" /></p>'+
                                                '<p><button type="submit" id="catalog_add_button">提交</button><span class="t_process">&nbsp;</span></p>'+
                                                '</div>';
                                var $pop_html = jQuery(pop_html);
                                var $pop_content = pop_page(400, 200, $pop_html);
                                $pop_html.bind('click', function(e){
                                    if(e.target.nodeName != "BUTTON")   return;
                                    var $target = jQuery(e.target), $process = $target.siblings("span");
                                    var mes = $pop_html.DivToDict();
                                    if(!jQuery.check_chapter(mes['section'])){
                                        $process.error_process("章节不规范，例如1, 1.2"); 
                                        return;                                   
                                    }
                                    if(!mes['title']) { $process.error_process("请填写标题！");   return;}
                                    
                                    jQuery.postJSON(url, mes, function(){
                                        $process.ajax_process(); $target.to_disabled();                                    
                                    }, function(response){
                                        if(response.status != 0){
                                            $process.error_process(response.info);  $target.remove_disabled();                                        
                                        }else{
                                            $process.right_process("操作成功！");
                                            switch(to_do){
                                                case "add_chapter":
                                                    var li_html = '<li chapter_id='+ response.node_id +'>'+ 
                                                                '<span class="num">'+ jQuery.encode(mes['section']) +'</span>'+
                                                                '<span><a href="/book/'+ book_id +'/catalog/'+response.node_id +'">'+ jQuery.encode(mes['title']) +'</a></span>'+ 
                                                                '<span class="catalog_edit" do="modify_chapter">修改</span>' +
                                                                '<span class="catalog_del" do="remove_chapter">删除</span>' +                                                               
                                                                '</li>';
                                                    $catalog_ul.append(li_html);
                                                    callback();
                                                    break;
                                                case "modify_chapter":
                                                    $li.children("span").eq(1).find('a').html(mes['title']);
                                                    if( mes['section'] != old_section ){
                                                        $li.children("span").eq(0).html(mes['section']);
                                                        callback();                                                   
                                                    }
                                                    break;                                            
                                            }
                                            pop_page_close();                                        
                                        }                                    
                                    }, function(textStatus){    $process.error_process("出现错误：" + textStatus);  $target.remove_disabled(); });                     
                                })
                                                
                },
                "remove_chapter": function(call_back){
                        var $that = this, $catalog_ul = jQuery("ul.catalog_ul"), book_id = $catalog_ul.attr("book_id");
                        var $li = $that.parent(),
                            node_id = $li.attr("chapter_id"),
                            url = '/settingpost-book_section_del',
                            mes = {'book_id': book_id, 'node_id': node_id};
                        jQuery.postJSON(url, mes, function(){}, function(response){
                            if(response.status == 0){
                                $that.parent().remove();
                                call_back();                            
                            }                        
                        }, function(){});              
                },
                "recommend_article": function( callback){
                    // this is must be jquery object     
                    var $that = this, book_id = $that.attr("book_id") || '', node_id = $that.attr("node_id") || '',
                        article_id = $that.attr("article_id") || '',    article_type = $that.attr("article_type") || '',
                        in_page = $that.attr("in_page");
                    var pop_html = '<div id="pop_insert_table">' +
                                    '<p class="first">推荐文章到知识谱</p>'+
                                    '<input type="hidden" name="book_id" value="'+ book_id +'" />'+
                                    '<input type="hidden" name="node_id" value="'+ node_id +'" />' +
                                    '<input type="hidden" name="article_id" value="'+ article_id +'" />'+
                                    '<input type="hidden" name="article_type" value="'+ article_type +'" />' +
                                    '<p>链接<input type="text" name="url" autocomplete="off"/></p>'+
                                    '<p><button type="submit" id="recommend_button">推荐</button><span class="t_process">&nbsp;</span></p>'+
                                    '</div>';
                    var $pop_html = jQuery(pop_html);
                    var $pop_content = pop_page(450,200, $pop_html);
                    $pop_content.bind('click', function(e){
                        if(e.target.nodeName != "BUTTON")   return;
                        var $target = jQuery(e.target), $process = $target.siblings("span"),
                            mes = $pop_content.DivToDict();
                        if(!mes['url']){   $process.error_process("请填写链接！");  return;}
                        var mes1;
                        if(in_page == "book"){
                            mes1 = jQuery.get_article_from_url(mes['url']);
                        }else{
                            mes1 = jQuery.get_book_from_url(mes['url']);                        
                        }
                        if(!mes1['return']) {   $process.error_process("链接未能正确识别！"); return;}
                        jQuery.extend(mes, mes1);
                        var url = '/settingpost-book_article_rec';
                        jQuery.postJSON(url, mes, function(){
                            $process.ajax_process();    $target.to_disabled();                        
                        }, function(response){
                            if(response.status != 0){   $process.error_process(response.info);  $target.remove_disabled(); } 
                            else{
                                $process.right_process("推荐成功！");
                                if(in_page == "book"){
                                    callback.call($that, response, mes);
                                }
                                pop_page_close();                            
                            }                       
                        }, function(textStatus){
                                $process.error_process("出现错误:" + textStatus);   $target.remove_disabled();                        
                        });
                    });        
                },
                "spec_article": function(){
                    var $that = this, $li = $that.parent(), $ul = $li.parent(),
                        is_default = $that.attr("is_default") == "yes", 
                        url = '/settingpost-book_article_spec';
                    if(is_default) {  url = '/settingpost-book_article_unspec'; }
                    var mes = { 'book_id': $ul.attr("book_id"),
                                'node_id': $ul.attr("node_id"),
                                'relation_id': $li.attr("relation_id")};
                    jQuery.postJSON(url, mes, function(){}, function(response){
                        if(response.status == 0){
                            if(is_default){
                                $that.attr("is_default", "no").html("默认加载"); 
                            }else{
                                
                                $ul.find('li').each(function(){
                                    $(this).find('span.mark_article').attr("is_default", "no").html('默认加载');                         
                                });    
                                $that.attr("is_default", "yes").html("取消默认");                         
                            }                
                        }                    
                    }, function(){});

                },
                "remove_article": function(){
                    var $that = this, $li = $that.parent(), $ul = $li.parent();
                    var mes = { 'book_id': $ul.attr("book_id"),
                                "node_id": $ul.attr("node_id"),
                                "article_id": $li.attr("article_id"),
                                "article_type": $li.attr("article_type")};
                    var book_id = $ul.attr("book_id"),  node_id = $ul.attr("node_id"),
                        article_id = $li.attr("article_id"), article_type = $li.attr("article_type");
                    var url = '/settingpost-book_article_del';
                    jQuery.postJSON(url, mes, function(){}, function(response){
                        if(response.status == 0 ){
                            $li.remove();                        
                        }                    
                    }, function(){});
                }
    }  
    
}

change_code = function(classname){
    classname = classname || '';
    var $img = jQuery("#code_img");
    $img.html('<img src="/code" class="'+classname+'" />');
}


})(jQuery);