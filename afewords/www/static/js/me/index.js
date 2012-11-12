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
    if( !flag ) return;
    $("#body_content").find(".page_nav").bind('click', function(e){
        var target = e.target,
            $target = jQuery(target);
        if(target.nodeName != "A")  return false;
        alert('loading');
        
    });
    
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
        }
}


});