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
    /******* login page, blog page *********/
    var subpage = AFWUser['subpage_type'];
    var page_type = AFWUser['page_type'];
    if(subpage == "login"){
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
    if(page_type == "blog"){
        // init blog page 
        jQuery("#article_bottom_nav").bind('click', function(e){
            if(e.target.nodeName != "SPAN") return;
            var $target = jQuery(e.target),
                to_do = $target.attr("do");
            if(!to_do)  return;  
            //alert('loading');
            var configs = Global_Funs["blog"][to_do];
            configs.call($target);   
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
            $(this).children("span.hide_span").show().end().children('a.hide_a').show();
                    
        },'mouseout': function(){
            $(this).children('span.hide_span').hide().end().children('a.hide_a').hide();        
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
            case 'remove_article':
                mes['article_id'] = $that.attr("article_id");
                mes['article_type'] = $that.attr("article_type");
                url = '/settingpost-article_remove';
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
                    $that.parent().slideUp('slow').remove();
                    break;
                case 'remove_article':
                    $that.parent().slideUp('slow').remove();
                    break;
                default:
                    break;            
            }
        }
    }

})();


(function(){
    /******* 
        init page of the write_page
        contain: write
    ********/
    var subpage = AFWUser['subpage_type'];
    if(subpage == "write"){
        write_page_init();
    }

    function write_page_init(){
        var $right = jQuery("#right"),
            $menu = jQuery('#write_menu'), 
            $text = jQuery('#write_textarea'),
            $summary = jQuery("textarea.w_summary"),
            $title = jQuery("input.w_title"),
            $tags = $right.find('div.w-class'),
            $keywords = $right.find("textarea.k-text");
            $process =  $right.find("div.w-submit-result");
            
        $right.find('div.w-open').children().bind('click', function(){
            var $target = jQuery(this), to_do = $target.attr("do");
            if(!to_do)  return;
            if(to_do == "summary"){
                $summary = $("textarea.w_summary");
                if($summary.css("display") == "none"){  $target.html("隐藏摘要"); }
                else {   $target.html("展开摘要"); }            
                $summary.slideToggle("slow");
            }else{
                var $header = $("#head");
                if($header.css("display") == "none") {  $target.html("隐藏页头")}
                else{   $target.html("展开页头"); }
                $header.slideToggle("slow");
            }
        }).click();
        
        $right.find('div.w-class').find('span.cursor-pointer')
        .bind('click', function(){ Global_Funs["tag"]["pop"](); });
        var $buttons = $right.find('button');
        $buttons.bind('click', function(){       
            var mes = get_paras();
           
            var url = '/update-article';
            var $button = $(this);
            var to_do = $button.attr("do");
            mes['do'] = to_do;
            
            for(var i in mes){
                console.log(i + '  ' +  mes[i]);            
            }
            if(mes['title'] !== false){
                if(!mes['title'] || mes['title'] == "标题") {  $process.error_process("请填写标题！"); return; }           
            }
            if(mes['summary'] !== false){
                if(mes['summary'] == "摘要")  mes['summary'] = '';           
            }
            if(!mes['body'] || mes['body'] == "内容"){    $process.error_process("请填写内容！");  return;}
            
            jQuery.postJSON(url, mes, function(){
                $process.ajax_process();    $buttons.to_disabled();
            }, function(response){
                if(response.isnew != 0) $menu.attr('article_id', response.article_id);
                if(response.status != 0){
                    $process.error_process(response.info);  $buttons.remove_disabled();  return;                
                }else{
                    handle_fun(response, mes);                
                }
            }, function(textStatus){
                $process.error_process("出现错误：" + textStatus);
                $buttons.remove_disabled();            
            });
        });
        
        function get_paras(){
            var mes = {
                'env_id': $menu.attr("env_id"),
                'env_type': $menu.attr('env_type'),
                'article_id': $menu.attr('article_id'),
                'article_type': $menu.attr('article_type'),
                'father_id': $menu.attr('father_id'),
                'father_type': $menu.attr('father_type'),
                'iscomment': $menu.attr('iscomment'),
                'body': $text.val(),
                'summary': $summary.length > 0 ? $summary.val() : false,
                'title': $title.length > 0 ? $title.val() : false,
                'keywords': $keywords.val() || '',
                'tags': $tags.DivToDict()['tags'] || []
            };
            return mes;
        }
        
        function handle_fun(response, mes){
            var url_dict = { 'blog': ''}
            var basic_url = '/blog/';
            switch(mes['article_type'].toLowerCase()){
                case 'blog':
                    basic_url = '/blog/' +  response.article_id;
                    break;
                case 'about':
                    basic_url = '/blogger/' + AFWUser['id'] + '/about';
                    break;
                case 'group-topic':
                    basic_url = '/group/' + mes['env_id'] + '/topic/' + response.article_id;
                    break;
                default:
                    break;
            }
            $buttons.remove_disabled();
            if(mes['do'] == 'preview'){
                basic_url += '?preview=yes';
                $process.right_process('操作成功！预览地址<a href="'+ basic_url +'" target="_blank">预览</a>');
                return;            
            }else{
                $process.right_process('操作成功，1s后跳转到目的页！');
                setTimeout( function (){ location.href=basic_url; }, 1000);            
            }
             
        }
    }    

})();

;(function(){
    /****************
        init page nav of the body_content
        contain: notice    
    *******************/
})();




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
                                    var reply_block_html = '<div class="com_reply" id="write_comment_zone">' +
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
                                                                '<a href="javascript:void(0);" class="link_close" comment_pos="' + reply_comment_id + '">X</a>' +
                                                                '<p>'+ reply_comment_short +'<a href="/blogger/' + reply_author_id + '" class="ref_author">'+
                                                                jQuery.encode(reply_author_name)+'</a></p></div>';
                                        $reply_comment_nest.html(reply_comment_html);
                                        $reply_comment_nest.append(hidden_input);
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
                                        for(var i in mes){
                                            console.log(i + '  ' + mes[i]);                                       
                                        }
                                        return mes;
                                    }
                                    
                                    function bind_post_comment(){
                                        var $button = $reply_block.find('button'), $process = $button.siblings('.comment_process');
                                        $button.bind('click', function(){
                                            var mes = parse_comment_request();
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
                                    var $that = this,
                                        article_type = "";
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
                                                $that.html("喜欢").attr("like_status", "no");                                            
                                            }else{
                                                $that.html("取消").attr("like_status", "yes");                                            
                                            }                                        
                                        }
                                    },function(){});                    
                    },
                    "share":    function(){},
                    "view":     function(){}    
                }
}


});