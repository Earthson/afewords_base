jQuery(document).ready(function(){
// bind event handler for pages

$Tools = jQuery.afewords.tools;
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

$(document.body).live('click', function(event){
    var $head_user = jQuery(document.getElementById("head_user"));
    if($head_user.css("display") == "block") $head_user.hide();
    
    /****** bind login *********/
    var target = event.target,
        $target = jQuery(target);
    if(target.nodeName == "BUTTON"){
        // afewords-in
        if(AFWUser.subpage_type == "login"){
                    
        }
    }
    
});


jQuery(document.getElementById("login_do")).bind('click', function(event){
    /****
        contains login, reg, reset page 
    ****/
    var target = event.target,
        $target = jQuery(target),
        that = this;
        $that = jQuery(that);
    //alert(0)
    if(target.nodeName != "BUTTON") return false;
    var $process = $target.siblings("span.login-process"), ret, $button = $target;
    var mes = $that.DivToDict();
    var configs = Global_Funs[AFWUser.subpage_type];
    ret = configs["check"](mes);
    if(ret[0] < 0){
        $process.html(ret[1]).css("color", "red");
        return false;
    }
    jQuery.postJSON( configs['url'], mes, 
        function(){  $button.to_disabled();
                     $process.ajax_process();
                    },
        function(response){
            if(response.status != 0){
                $button.remove_disabled();
                $process.error_process(response.info);       
            }else{
                configs["handler"](response, $process);
                var interval = $Tools.repeat_mail(mes['email'], $process, 4);
                setTimeout(interval["interval"], 1000);
            }
        },
        function(textStatus){
            $button.remove_disabled();
            $process.error_process("出现错误：" + textStatus);
        });
    // can ajax

});

(function(){
    /******* login page *********/
    if(AFWUser['subpage_type'] == "login"){
        //alert(0);
        jQuery(document.getElementById("login_do")).find("form").bind('click', function(event){
            var target = event.target, $target = jQuery(target), that = this, $form = jQuery(that);
            var $process, ret, mes;
            event.stopPropagation();
            if(target.nodeName != "BUTTON") return false;
            $process = $form.find("span.login-process");
            mes = $form.FormToDict();
            ret = Global_Funs["login"]["check"](mes);
            if(ret[0] < 0){
                $process.html(ret[1]).css("color", "red");
                event.preventDefault();
                return false;              
            }
            return true;
        })    
    }
    
})();

(function(){
    /*********** init page nav of the body_content 
                contain: avatar, domain, tag, draft, notice    
    ********************/
    var flag_str = AFWUser['subpage_type'];    
    var flag = flag_str == "domain" || flag_str == "avatar" || flag_str == "draft" 
                    || flag_str == "notice" || flag_str == "tag";
    var pop_flag = flag_str == "avatar" || flag_str == "tag" || flag_str == "domain";
    if( !flag ) return;
    
    $("#body_content").find(".page_nav").bind('click', function(e){
        var target = e.target,
            $target = jQuery(target);
        var configs = Global_Funs[flag_str];
        var url = '/';
        if(target.nodeName != "A")  return false;
        //alert('loading');
        if(pop_flag){
            configs["pop"]();
        }else{
            switch(flag_str){
                case 'notice':
                    var to_do = $target.attr("do") || 'read_all';
                    if(to_do == 'read_all')  url = '/settingpost-user_noti_markall';
                    if(to_do == 'delete_all') url = '/settingpost-user_noti_empty';
                    jQuery.postJSON(url, {}, function(){}, function(response){
                        if(response.status == 0){
                            var $notice_div = $('#body_content').find('ul');
                            if(to_do == "read_all") $notice_div.find('li').removeClass('noti-read-False').addClass('noti-read-True');
                            if(to_do == "delete_all")  $notice_div.html('<div>没有消息！</div>');                 
                        }                    
                    }, function(){});
                    break;            
            }        
        }       
    });
})();


(function(){
    /************************
        init like nav 
    **********************/
    var $like_ul = $("#body_content").find("ul.like_ul");
    if($like_ul.length){
        $like_ul.find('li').live({
        'mouseover': function(){
            $(this).children("span.hide_span").show();        
        },'mouseout': function(){
            $(this).children('span.hide_span').hide();        
        }});
        
        $like_ul.live('click', function(event){
            if(event.target.nodeName != "SPAN")     return;
            var $target = jQuery(event.target);
            var to_do = $target.attr("do");
            if(!to_do)  return;
            parse_request.call( $target );
            
        });    
    }
    
    function parse_request(){
        var $that = this;    // must be jquery object
        var to_do = $that.attr("do");
        var mes = {}, url = '/';
        var before_fun = function(){},
            error_fun = function(){},
            handler_fun = function(){};
        switch(to_do){
            case 'remove_tag':  
                mes['rm_tag'] = $that.attr("tag");
                url = '/settingpost-user_removetag';
               
                break;
            default:
                break;        
        }
        
        jQuery.postJSON(url, mes, before_fun, 
            handle_fun, error_fun);
        
        function handle_fun(response){
            if(response.status != 0)   return;
            switch(to_do){
                case 'remove_tag':
                    $that.parent().remove();
                    break;
                default:
                    break;            
            }
        }
    }

})();


(function(){
    /****************
        init page nav of the body_content
        contain: notice    
    *******************/
})()


Global_Funs = {
    "login": {
                "check": function(paras){
                            var res = { status: -1, info: ''};
                            var email_reg = (/^\w+((-\w+)|(\.\w+))*@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/);
                            if(!paras['email'] || !email_reg.test(paras['email']))
                                return [-1, '请您填写正确的邮箱！'];
                            //alert(0);
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
                            var email_reg = (/^\w+((-\w+)|(\.\w+))*@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/);
                            if(!paras['email']|| !email_reg.test(paras['email'])){ 
                                return [-1, '请您填写正确的邮箱！']; 
                            }
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
                                var email_reg = (/^\w+((-\w+)|(\.\w+))*@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/);
                                if(!paras['email']|| !email_reg.test(paras['email']))  return [-1, '请您填写正确的邮箱！'];
                                if(!paras['pwd'] || paras['pwd'].length < 4) return [-1, '设置的密码需要4位以上！'];
                                if(!paras['pwd'] != paras['pwd_again']) return [-1, "确认密码出错！"]
                                if(!paras['token']) return [-1, '请您填写验证码！']
                                return [1, '']
                    },
                    "handler": function( paras, $process ){
                            // repeat mail
                            var texts = '密码重置邮件已经发送至您的邮箱！<span id="repeat_time_all"><span id="repeat_time" class="font-14">30</span>秒后可重新发送验证邮件！</span>';
                            $process.right_process(texts);      
                    }
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
                                            '<iframe name="up_picture_iframe" id="up_picture_iframe" style="display:none"></iframe>' +
                                            '</div>';
                                $htmls = jQuery(htmls);
                                var $pop_content = pop_page(350,180, $htmls);
                                // bind 
                                $htmls.find('button').click(function(e){
                                    if(e.target.nodeName != "BUTTON")   return false;
                                    var $button = jQuery(e.target), $process = $button.siblings("span.i_process");
                                    var file_src = $htmls.find("input.i_file").val();
                                    if(!file_src){  $process.error_process("请选择图片！"); return false; }
                                    var img_reg = /.*\.(jpg|png|jpeg|gif)$/ig;
	                                   if(!file_src.match(img_reg)) {  $process.error_process('图片格式为jpg,png,jpeg,gif！'); return false; }
                                    $process.ajax_process();
                                    $button.to_disabled();
                                })
                    },
                    "check":    function(paras){},
                    "handler":  function(){}    
                },
}


});