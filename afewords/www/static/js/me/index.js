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
    var $process = $target.siblings("span.login-process"), ret;
    var mes = $that.DivToDict();
    ret = Global_Funs[AFWUser.subpage_type]["check"](mes);
    if(ret[0] < 0){
        $process.html(ret[1]).css("color", "red");
        return false;
    }
    jQuery.postJSON();
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
                }
                   
        }
}


});