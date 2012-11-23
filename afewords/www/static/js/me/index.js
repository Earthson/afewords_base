jQuery(document).ready(function(){
// bind event handler for pages

var $Tools = jQuery.afewords.tools;
var Global_Funs = $Tools.Global_Funs;


(function(){
    // for head userself nav 
    var $head_user_block = jQuery("#head_user_block"),
        $head_user_link = $head_user_block.find("#head_user_link"),
        $head_user_ul = $head_user_block.find("ul");
    $head_user_link.live('mouseover', function(){
        $head_user_ul.slideDown();
    });
    $head_user_block.live('mouseout', function(){
        $head_user_ul.hide();    
    });
    $head_user_ul.live({
        'mouseout': function(){ $(this).hide(); },
        'mouseover': function(){ $(this).show(); }    
    });
    
    // for middle body height
    var page_height = jQuery(window.document).height(),
        head_height = 91,
        footer_height = 61,
        $middle = jQuery('#middle'),
        middle_height = $middle.height(),
        page_type = AFWUser['page_type'],
        summary_height = 112,
        subpage_type = AFWUser['subpage_type'],
        surplus_height = page_height - head_height - footer_height;

    if(page_type == "write"){
        surplus_height -= summary_height;
        surplus_height += head_height;        
    }    
    if(middle_height < surplus_height){
        $middle.css("min-height", surplus_height + "px");      
    }
    
    // for go to top
    jQuery.cursor_to_top();   
    
    // for load-feed page
    if(page_type == "feed" && subpage_type == "feed"){
        jQuery(window).scroll(function(){
            if($middle.length <1)   return;
            var scroll_height = document.body.scrollHeight;
            var client_height = window.screen.height;
            var top= window.pageYOffset ||   
                        (document.compatMode == 'CSS1Compat' ?    
                        document.documentElement.scrollTop :   
                        document.body.scrollTop);
           if(top >= (parseInt(scroll_height)- client_height)){
                if(AFWUser['is_loading'])   return;
                AFWUser['is_loading'] = true;
                load_feed_fun();         
           }             
        });    
    }
    
    function load_feed_fun(){
        if(!AFWUser['id_list'].length)  {
            // some thing
            return;
        }
        var load_list = AFWUser['id_list'].splice(0, 15),
            url = '/load-feed',
            mes = {'toload': load_list},
            $body_content = jQuery("#body_content"),
            $load_process = jQuery('<div id="feed" class="feed_process">'+
                            '<div class="f-body">'+
                            '<div class="f-con"><img src="/static/img/loading_bar.gif" /></div></div></div>');
                            
        jQuery.postJSON(url, mes, function(){
            $body_content.append($load_process);
        }, function(response){
            if(response.status != 0){
                $load_process.find('.f-con').error_process(response.info);        
            }else{
                $load_process.remove();
                var feeds = response.article_list, feed;
                var feed_html = '';
                for(var i = 0; i < feeds.length; i ++){
                    feed = feeds[i];
                    var summary = feed.summary ? '<div class="f-con">' + feed['summary'] +'</div>' : '';
                    feed_html += '<div id="feed">' +
                                '<div class="f-body">' +
                                '<div class="f-control">' +
                                '<div class="f-author">' + 
                                '<a href="/blogger/' + feed.author.uid + '" target="_blank">' + feed.author.name + '</a>' +
                                '<span class="f-sub">-</span><span class="f-type">' + feed.release_time.substr(5,11) + '</span>'+
                                '</div>' +
                                '</div>' +
                                '<div class="f-con">'+
                                '<a href="/blog/' + feed.aid + '" target="_blank">' + feed['title'] + '</a>'+
                                '</div>'+
                                '<div>' + feed.content_short + '<a target="_blank" class="blog_detail" href="/blog/'+ feed.aid +'">...</a>' +
                                '</div>'+
                                '</div>'+
                                '<div class="f-pic">' +
                                '<a href="/blogger/' + feed.author['uid'] + '" target="_blank">' +
                                '<img src="'+  feed.author['thumb'] + '" />' +
                                '</a>' +
                                '</div>' +
                                '</div>';
                }
                $body_content.append(feed_html);
                AFWUser['is_loading'] = false;
                // some thing    
            }
        }, function(textStatus){
                $load_process.find('.f-con').error_process("异常：" + textStatus);                    
        });
    };
    
    // for write feedback
    jQuery("#feed-back").live('click', function(e){
        if(e.target.nodeName != "A")    return;
        var $target = jQuery(e.target),
            to_do = $target.attr("do");
        if(!to_do)  return;
        if(to_do != "write-feedback")   return;
        var login_flag = AFWUser['login'],
            info_html = '', 
            pop_height = 370;
        if(!login_flag){
            info_html = '<p>称呼  <input type="text" class="feedback" name="name" /><span class="feedback">*当前为未登陆状态，可<a href="/login">登陆</a>后反馈</span></p>' +
                        '<p>邮箱  <input type="text" class="feedback" name="email" /><span class="feedback">*方便联系您</span></p>' + 
                        '<p>验证码 <input type="text" class="feedback_token" name="token" />' + 
                            '<span id="code_img" class="feedback"><img src="/code" class="feedback" /></span>' +
                            '<a href="javascript:void(0)" onclick="change_code(\'feedback\');" class="feedback">换一张</a></p>';
            pop_height = 500;        
        }        
        var pop_html = '<div id="pop_insert_table">' + 
                        '<p class="first">反馈 - 错误/不足</p>' + 
                        info_html +
                        '<p><textarea name="feedback">想说：</textarea>' + 
                        '<p><button>提交</button><span class="t_process" style="width:70%"></span></p>'+
                        '</div>';
        var $pop_content = pop_page(600,pop_height, pop_html);
        $pop_content.bind('click', function(e){
            if(e.target.nodeName != "BUTTON")   return;
            var $target = jQuery(e.target),
                $process = $target.siblings("span"),
                mes = $pop_content.DivToDict();
            if(!login_flag){
                // not login
                if(!mes['name']){   $process.error_process("请填写称呼！"); return; }
                if(!mes['email'] || !jQuery.check_email(mes['email'])){ $process.error_process("请填写正确的邮箱！"); return;}
                if(!mes['token']){ $process.error_process("请填写验证码！");  return; }
            }      
            if(!mes['feedback'] || mes['feedback'] == "想说："){ $process.error_process("请填写反馈内容！"); return;}
            var url = '/post-feedback';
            jQuery.postJSON(url, mes, function(){
                $process.ajax_process(); $target.to_disabled();            
            }, function(response){
                if(response.status != 0){  $process.error_process(response.info);  $target.remove_disabled(); }
                else{  $process.right_process("反馈成功，感谢您！");  pop_page_close();  }            
            }, function(textStatus){
                $process.error_process("出现错误：" + textStatus); $target.remove_disabled();            
            });
        });    
    });

})();




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
        var $article_bottom = jQuery("#article_bottom_nav");
        $article_bottom.bind('click', function(e){
            if(e.target.nodeName != "SPAN") return;
            var $target = jQuery(e.target),
                to_do = $target.attr("do");
            if(!to_do)  return;  
            //alert('loading');
            var configs = Global_Funs["blog"][to_do];
            configs.call($target);   
        }).find('span.bot-getcomment').click();
        setTimeout(function(){ $article_bottom.find('span.bot-view').click(); }, 5000);
        var $article_comment = jQuery("#article_comment");
        $article_comment.live('click', function(e){
            if(e.target.nodeName != 'SPAN' && e.target.nodeName != "A") return;
            var $target = jQuery(e.target),
            to_do = $target.attr("do");
            if(!to_do)  return;
            
            var configs = Global_Funs['blog'][to_do];
            configs.call($target);        
        });
        
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
        init like nav or other
    **********************/
    var $body_content = jQuery("#body_content");
    var $like_ul = $body_content.find("ul.like_ul");
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
                mes['obj_id'] = $that.attr("obj_id");
                mes['obj_type'] = $that.attr("obj_type");
                url = '/settingpost-obj_remove';
                break; 
            case 'unlike':
                mes['obj_id'] = $that.attr("obj_id");
                mes['obj_type'] = $that.attr("obj_type");
                url = '/obj-dolike';
                break;       
            default:
                return;
                break;
        }
        
        jQuery.postJSON(url, mes, before_fun, 
            handle_fun, error_fun);
        
        function handle_fun(response){
            if(response.status != 0)   return;
            switch(to_do){
                case 'remove_tag':
                case 'remove_article':
                case 'unlike':
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
        jQuery("#footer").hide();
        $right.find('div.w-class').find('span.cursor-pointer')
        .bind('click', function(){ Global_Funs["tag"]["pop"](); });
        var $buttons = $right.find('button');
        $buttons.bind('click', function(){       
            var mes = get_paras();
           
            var url = '/update-article';
            var $button = $(this);
            var to_do = $button.attr("do");
            mes['do'] = to_do;
            
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
            switch(AFWUser['article_type'].toLowerCase()){
                case 'blog':
                    basic_url = '/blog/' +  response.article_id;
                    break;
                case 'about':
                    if(mes['env_type'] == 'user'){
                        basic_url = '/blogger/' + AFWUser['id'] + '/about';
                    }else{
                        basic_url = '/book/' + mes['env_id'] + '/about';                   
                    }
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
                $process.right_process('操作成功，1秒后跳转...');
                setTimeout( function (){ location.href=basic_url; }, 1000);   
                jQuery.close_window_alert();         
            }
             
        }
    }    

})();

;(function(){
    /****************
        init page nav of the body_content  BUTTON
        contain: password, avatar, invite
    *******************/
    var $body_content = jQuery("#body_content");
    $body_content.bind('click', function(e){
        if(e.target.nodeName != "BUTTON")   return;
        var $target = jQuery(e.target), $process = $target.siblings("span");
        var to_do = $target.attr("do");
        if(!to_do)  return;
        var configs = Global_Funs['body_content_button'];
        var mes = $body_content.DivToDict();
        if(!to_do in configs)   return;
        
        var ret = configs[to_do].call($target, $body_content, $process, mes); 
        if(!ret || !ret[0]) return;
        for(var i = 0; i < ret.length; i++) console.log(i+ ret[i]);
        var url = ret[1], right_handle = ret[2], error_handle = ret[3] || _error_handle;
        jQuery.postJSON(url, mes, function(){
            $process.ajax_process();    $target.to_disabled();        
        }, right_handle, error_handle);
        
        function _error_handle(textStatus){
            $process.error_process("出现错误：" + textStatus); $target.remove_disabled();        
        };
    });
    // init for book manage 
    $body_content.find("#book_wrap").live('click', function(e){
        if(e.target.nodeName != "SPAN") return;
        var $target = jQuery(e.target),
            to_do = $target.attr("do");
        if(!to_do)  return;
        switch(to_do){
            case "add_chapter":
            case "modify_chapter":
                Global_Funs['book_chapter_manage']["add_modify_chapter"].call($target, sort_node_fun);
                break;
            case "remove_chapter":
                Global_Funs['book_chapter_manage']["remove_chapter"].call($target, sort_node_fun);
                break;
             default:
                break;           
        }
        
    });
    //setTimeout(sort_node_fun,2000);
    function sort_node_fun(){
        //sort the node for chapter eidt
        var $catalog_ul = jQuery("ul.catalog_ul");
        var new_html = '';
        var all_li = get_all_node();
        var nest = 1;
        for(var i = 0, li_len = all_li.length; i < li_len ; i++){
            var current_li = all_li[i];
            var current_nest = current_li[0].split('.').length;
            if(current_nest > nest ){
                new_html += '<ul class="margin">';
                new_html += current_li[1].html();
                nest++;           
            }else{
                if(current_nest == nest){ new_html += current_li[1].html();  }
                else{
                    for(var j=0; j < nest - current_nest; j++){
                        new_html += '</ul>';
                    }
                    new_html += current_li[1].html();
                }
            }
        }
        $catalog_ul.html(new_html);
        
        
        function get_all_node(){
            var $li_list = $catalog_ul.find("li");
            var li_array = [], array_length = 0;
            $li_list.each(function(){
                var $li = jQuery(this);
                li_array[array_length ++] = [ $li.children("span").eq(0).html(), $li.clone().wrap('<p>').parent()];
            });
            
            li_array.sort(function(a,b){
                return sort_fun(a,b);    
            });
            return li_array;
            function sort_fun(a, b){
                var deep = 0;
                var a_list = a[0].split('.'), b_list = b[0].split('.'),
                    a_nest = a_list.length, b_nest = b_list.length;

                function my_cmp(deep){
                    var a_int = parseInt(a_list[deep], 10),
                        b_int = parseInt(b_list[deep], 10);
                
                    if(deep+1 >= Math.min(a_nest, b_nest)){
                        if(a_nest==b_nest){  return a_int - b_int;  }
                        else{
                            if(a_int == b_int ){ 
                                if(a_nest > b_nest)   return 1;//return parseInt(a_list[deep+1], 10);
                                return -1;//parseInt(b_list[deep+1], 10);
                            }
                            return a_int - b_int;
                        }             
                    }else{
                        if(a_int != b_int) return a_int - b_int;
                        else{
                            deep++;
                            return my_cmp(deep);
                        }
                    }
                }       
                return my_cmp(0);          
            };
        }    
    }
})();

(function(){
    /*  init page, for book
    */
    var page_type = AFWUser['page_type'];
    if(page_type != "book") return;
    $("div.book_node_nav").bind('click', function(e){
        if(e.target.nodeName != "A")    return;
        var $target = jQuery(e.target),
            load_page = $target.attr("page");
            
        if($target.hasClass("current1"))    return;
        $target.addClass("current1").parent().siblings().children().removeClass("current1");
        var $page_entity = $("div.book_node_con");
        $page_entity.find(".book_node_con_"+ load_page).siblings().addClass("con_current0").end().removeClass("con_current0");
    });
    
    $("div.book_node_con").bind('click', function(e){
        if(e.target.nodeName != "SPAN") return;
        var $target = jQuery(e.target),
            to_do = $target.attr("do");
        if(!to_do)  return;   
        Global_Funs["book_chapter_manage"][to_do].call($target, callback);
         
    });

    function callback(response, mes){
        var permission = AFWUser['permission'], $that = this, book_id = $that.attr("book_id"),
            node_id = $that.attr("node_id"),
            $node_con = $that.parent(),
            $node_con_ul = $node_con.find("#book_node_article"), 
            li_html = '';
        li_html = '<li relation_id="'+ response.relation_id +'">'+
                    '<a href="/blog/'+ mes['article_id'] +'" target="_blank">'+ response.article_title +'</a>';
        if(permission){
            li_html += '<span class="mark_article" do="spec_article" is_default="no">默认加载</span>'+
                        '<span class="del_article" do="remove_article">删除</span>';     
        }
        li_html += '</li>';

        if($node_con_ul.length < 1){
            li_html = '<ul id="book_node_article" class="node_style" book_id="'+ mes['book_id'] +'" node_id="'+ mes['node_id'] +'">' + li_html + '</ul>';
            $node_con.append(li_html);
        }else{
            $node_con_ul.append(li_html);
        }  
    }
})();



});