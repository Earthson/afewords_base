jQuery(document).ready(function(){
// bind event handler for pages

var $Tools = jQuery.afewords.tools;
var Global_Funs = $Tools.Global_Funs;
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





});