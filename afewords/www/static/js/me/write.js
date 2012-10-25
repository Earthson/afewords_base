(function($){

jQuery.com = jQuery.com || {};
jQuery.com.afewords = jQuery.com.afewords || {};
jQuery.com.afewords.www = jQuery.com.afewords.www || {};
jQuery.com.afewords.www.user_page = jQuery.com.afewords.www.user_page || {};
jQuery.com.afewords.www.user_group = jQuery.com.afewords.www.user_group || {};
jQuery.com.afewords.www.user_write = jQuery.com.afewords.www.user_write || {};
jQuery.com.afewords.www.user_page = jQuery.com.afewords.www.user_page || {};
jQuery.com.afewords.www.user_blog = jQuery.com.afewords.www.user_blog || {};
jQuery.com.afewords.www.user_init = jQuery.com.afewords.www.user_init || {};
jQuery.com.afewords.www.user_settings = jQuery.com.afewords.www.user_settings || {};
jQuery.com.afewords.www.user_URI = jQuery.com.afewords.www.user_URI || {};
$Tool = jQuery.com.afewords.www.user_tool;
$URI = jQuery.com.afewords.www.user_URI;
$Init = jQuery.com.afewords.www.user_init;
$Page = jQuery.com.afewords.www.user_page;
$Group = jQuery.com.afewords.www.user_group;
$Write = jQuery.com.afewords.www.user_write;
$Set = jQuery.com.afewords.www.user_settings;



$Write.code_type =  ['AS3','AppleScript','Bash','C#','ColdFusion','C++','CSS','Delphi','Diff',
    'Erlang','Groovy','JavaScript','Java','JavaFX','Lisp' ,'Perl','Php','Plain',
    'PowerShell','Python','Ruby','Sass','Scala','SQL','VB','XML'];
$Write.word_list1 = function(){
    //拉丁字符
    return ["Á", "á", "À", "à", "Â", "â", "Ä", "ä", "Ã", "ã", "Ǎ", "ǎ", "Ā", "ā", "Ă", "ă", "Ą", "ą", "Å", "å", "Ć", "ć", "Ĉ", "ĉ",
        "Ç", "ç", "Č", "č", "Ċ", "ċ", "Đ", "đ", "Ď", "ď", "É", "é", "È", "è", "Ê", "ê", "Ë", "ë", "Ě", "ě", "Ē", "ē", "Ĕ", "ĕ", "Ė", "ė",
        "Ę", "ę", "Ĝ", "ĝ", "Ģ", "ģ", "Ğ", "ğ", "Ġ", "ġ", "Ĥ", "ĥ", "Ħ", "ħ", "Í", "í", "Ì", "ì", "Î", "î", "Ï", "ï", "Ĩ", "ĩ", "Ǐ", "ǐ",
        "Ī", "ī", "Ĭ", "ĭ", "İ", "ı", "Į", "į", "Ĵ", "ĵ", "Ķ", "ķ", "Ĺ", "ĺ", "Ļ", "ļ", "Ľ", "ľ", "Ł", "ł", "Ŀ", "ŀ", "Ń", "ń", "Ñ", "ñ", 
        "Ņ", "ņ", "Ň", "ň", "Ó", "ó", "Ò", "ò", "Ô", "ô", "Ö", "ö", "Õ", "õ", "Ǒ", "ǒ", "Ō", "ō", "Ŏ", "ŏ", "Ǫ", "ǫ", "Ő", "ő", "Ŕ", "ŕ",
        "Ŗ", "ŗ", "Ř", "ř", "Ś", "ś", "Ŝ", "ŝ", "Ş", "ş", "Š", "š", "Ţ", "ţ", "Ť", "ť", "Ú", "ú", "Ù", "ù", "Û", "û", "Ü", "ü", "Ũ", "ũ", 
        "Ů", "ů", "Ǔ", "ǔ", "Ū", "ū", "ǖ", "ǘ", "ǚ", "ǜ", "Ŭ", "ŭ", "Ų", "ų", "Ű", "ű", "Ŵ", "ŵ", "Ý", "ý", "Ŷ", "ŷ", "Ÿ", "ÿ", "Ȳ", "ȳ",
        "Ź", "ź", "Ž", "ž", "Ż", "ż", "Æ", "æ", "Ǣ", "ǣ", "Ø", "ø", "Œ", "œ", "ß", "ð", "Þ", "þ", "Ə", "ə"];
}
$Write.word_list2 = function(){ 
    //国际音标
    return ["&#595;","&aelig;","p", "t̪", "t", "ʈ", "c", "k", "q", "ʡ", "ʔ", "b", "d̪", "d", "ɖ", "ɟ", "ɡ", "ɢ", "ɓ", "ɗ", "ʄ", "ɠ", "ʛ", "t͡s", "t͡ʃ", "t͡ɕ", "d͡z", 
        "d͡ʒ", "d͡ʑ", "ɸ", "f", "θ", "s", "ʃ", "ʅ", "ʆ", "ʂ", "ɕ", "ç", "ɧ","x", "χ", "ħ", "ʜ", "h", "β", "v", "ʍ", "ð", "z", "ʒ", "ʓ", "ʐ", "ʑ", "ʝ",
        "ɣ", "ʁ", "ʕ", "ʖ", "ʢ", "ɦ", "ɬ", "ɮ", "m̩", "m", "ɱ", 
        "ɱ̩", "ɱ̍", "n", "̪", "n̪", "n̪̍", "̩", "ɳ", "ɳ", "̩", "ɲ", "ɲ", "̩", "ŋ", "ŋ", "̍", "ŋ", "̩", "ɴ", "ɴ", "̩", "ʙ", "ʙ", "̩", 
        "r", "r", "̩", "ʀ", "ʀ", "̩", "ɾ", "ɽ", "ɿ", "ɺ", "l", "̪", "l", "̪", "̩", "l", "l", "̩", "ɫ", "ɫ", "̩", "ɭ", "ɭ", "̩", "ʎ", "ʎ", "̩", "ʟ", 
        "ʟ", "̩", "w", "ɥ", "ʋ", "ɹ", "ɻ", "j", "ɰ", "ʘ", "ǂ", "ǀ", "!", "ǁ", "ʰ", "ʱ", "ʷ", "ʸ", "ʲ", "ʳ", "ⁿ", "ˡ", "ʴ", "ʵ", "ˢ", "ˣ", "ˠ",
         "ʶ", "ˤ", "ˁ", "ˀ", "ʼ", "i", "i", "̯", "ĩ", "y", "y", "̯", "ỹ", "ɪ", "ɪ", "̯", "ɪ", "̃", "ʏ", "ʏ", "̯", "ʏ", "̃", "ɨ", "ɨ", "̯", "ɨ", "̃", 
        "ʉ", "ʉ", "̯", "ʉ", "̃", "ɯ", "ɯ", "̯", "ɯ", "̃", "u", "u", "̯", "ũ", "ʊ", "ʊ", "̯", "ʊ", "̃", "e", "e", "̯", "ẽ", "ø", "ø", "̯", "ø", "̃", "ɘ",
        "ɘ", "̯", "ɘ", "̃", "ɵ", "ɵ", "̯", "ɵ", "̃", "ɤ", "ɤ", "̯", "ɤ", "̃", "o", "o", "̯", "õ", "ɛ", "ɛ", "̯", "ɛ", "̃", "œ", "œ", "̯", "œ", "̃", "ɜ", 
        "ɜ", "̯", "ɜ", "̃", "ə", "ə", "̯", "ə", "̃", "ɞ", "ɞ", "̯", "ɞ", "̃", "ʌ", "ʌ", "̯", "ʌ", "̃", "ɔ", "ɔ", "̯", "ɔ", "̃", "æ", "æ", "̯", "æ", "̃", 
        "ɶ", "ɶ", "̯", "ɶ", "̃", "a", "a", "̯", "ã", "ɐ", "ɐ", "̯", "ɐ", "̃", "ɑ", "ɑ", "̯", "ɑ", "̃", "ɒ", "ɒ", "̯", "ɒ", "̃", "ˈ", "ˌ", "ː", "ˑ", "˘",
        ".", "‿", "|", "‖"];
}
$Write.word_list3 = function(){
    //符号
    return ["~", "|", "¡", "¿", "†", "‡", "↔", "↑", "↓", "•", "¶", "#", "½", "⅓", "⅔", "¼", "¾", "⅛", "⅜", "⅝", "⅞", "∞", "‘", "’", "“",
        "”", "„", "“", "„", "”", "«", "»", "¤", "₳", "฿", "₵", "¢", "₡", "₢", "$", "₫", "₯", "€", "₠", "₣", "ƒ", "₴", "₭", "₤", "ℳ", "₥", "₦",
                "№", "₧", "₰", "£", "៛", "₨", "₪", "৳", "₮", "₩", "¥", "♠", "♣", "♥", "♦", "m", "²", "m", "³", "–", "—", "…", "‘", "’", "“", "”", "°", "′", "″", "≈", "≠", "≤", "≥", 
        "±", "−", "×", "÷", "←", "→", "·", "§"];
}
$Write.word_list4 = function(){
    //希腊字符
    return ["Α", "Ά", "α", "ά", "Β", "β", "Γ", "γ", "Δ", "δ", "Ε", "Έ", "ε", "έ", "Ζ", "ζ", "Η", "Ή", "η", "ή", "Θ", "θ", "Ι", "Ί", "ι",
        "ί", "Κ", "κ", "Λ", "λ", "Μ", "μ", "Ν", "ν", "Ξ", "ξ", "Ο", "Ό", "ο", "ό", "Π", "π", "Ρ", "ρ", "Σ", "σ", "ς", "Τ", "τ", "Υ", "Ύ", "υ",
        "ύ", "Φ", "φ", "Χ", "χ", "Ψ", "ψ", "Ω", "Ώ", "ω", "ώ"];       
}


/**************toggle the title and summary ******************************/

$Write.write_toggle_title = function(obj){
    var target = $(obj).attr("to") || 'head';
    if (target=="summary"){
        var $summary = $("textarea.w_summary");
       if($summary.css("display")=='none'){
          $(obj).html('隐藏摘要');  
       }else{
          $(obj).html('展开摘要');
       }
       $summary.slideToggle("slow");
    }else{
        var $head = $("#head");
        if($head.css('display')=="none"){
            $(obj).html('隐藏页头');        
        }else{
            $(obj).html('展开页头');        
        }
        $head.slideToggle("slow");
    }   

}

$Write.get_menu_id = function(){
    var menu_id = 0;
    return function(){
        return menu_id++;
    }
};
$Write.window_close_alert = function(){
        $(window).bind('beforeunload', function(){
            return '确认关闭？';
        });
        $(window).unload(function(){
            alert('再见');
        });
    }
$Write.close_window_close_alert = function(){
        $(window).unbind('beforeunload');
        $(window).unload(function(){});
}


/****************console the writearea dom cursor *****************************************/
jQuery.fn.extend({
    /******* set the cursor in between pos_s and pos_e *********/
    setPosition:function(pos_s , pos_e) {  
        var e=$(this).get(0);  
        e.focus();  
        if (e.setSelectionRange) {  
            e.setSelectionRange(pos_s, pos_e);  
        } else if (e.createTextRange) {  
            var range = e.createTextRange();  
            range.collapse(true);  
            range.moveEnd('character', pos_s);  
            range.moveStart('character', pos_e);  
            range.select();  
        }
    },   
    /********** get the cursor postion of current state *****************/
    getPosition:function(){
        var s,e,range,stored_range;
        if(this[0].selectionStart == undefined){
            var selection=document.selection;
            if (this[0].tagName.toLowerCase() != "textarea") {
                var val = this.val();
                range = selection.createRange().duplicate();
                range.moveEnd("character", val.length);
                s = (range.text == "" ? val.length:val.lastIndexOf(range.text));
                range = selection.createRange().duplicate();
                range.moveStart("character", -val.length);
                e = range.text.length;
            }else {
                range = selection.createRange();
                stored_range = range.duplicate();
                stored_range.moveToElementText(this[0]);
                stored_range.setEndPoint('EndToEnd', range);
                s = stored_range.text.length - range.text.length;
                e = s + range.text.length;
            }
        }else{
            s=this[0].selectionStart,
            e=this[0].selectionEnd;
        }
        var te=this[0].value.substring(s,e);
        return {start:s,end:e,text:te}
    },
    /*************** get the  between pos_s and pos_e string ********************/
    getPositionString:function(pos_s,pos_e){
         this.setPosition(pos_s,pos_e);
         return this.getPosition().text;
    },
    /************ insert the string ***************/
    insertFormatString:function(type){
        //alert(type);
        //var type = parseInt($(obj).attr("kind"));
        pos_s = this.getPosition().start;
        pos_e =  this.getPosition().end;
        var string = '';
        var pre_str = '', end_str = '';
        lef = len = 0;
        var text_len = pos_e - pos_s;
        len = pos_e - pos_s;
        var last = false;
        if(this.val() == '内容'){ this.val(''); }
        switch(type){
            case 1: if(text_len >0 ){ pre_str='++'; end_str = '++';}; break;
            case 2:  if(text_len >0 ){ pre_str = end_str ='//'; }; break;
            case 3:  if(text_len >0 ){ pre_str = end_str = '__';}; break;
            case 4:  if(text_len >0 ){ pre_str = end_str = '--'; }; break;
            case 11: if(text_len > 0 ){ pre_str = '^{'; end_str = '}';  }; break;
            case 12: if(text_len > 0) { pre_str = '_{'; end_str = '}'; }; break;
            case 21:
                     if(!text_len > 0) break;
                    if(pos_s == 0 || this.getPositionString(pos_s - 1, pos_s) == '\n')
                    { pre_str = '#';}
                    else{ pre_str='\n#';}               
                    break;
            case 22: 
                     if(!text_len > 0) break;
                    if(pos_s == 0 || this.getPositionString(pos_s - 1, pos_s) == '\n'){
                        pre_str = '*';      
                    }else{
                        pre_str = '\n*';
                    }               
                    break;
            case 31:
                    if(pos_e == 0||this.getPositionString(pos_e - 1, pos_e) == '\n'){
                       //alert(pos_s);
                        end_str = '~~~~~~~~~~\n';
                    }else{
                       end_str = '\n~~~~~~~~~~\n'; 
                    }
                    last = true;
                    break;
            case 32: 
                     if(!text_len > 0) break;
                     if(pos_s==0||this.getPositionString(pos_s - 1, pos_s) == '\n')
                    { 
                       pre_str = end_str = '==';            
                    }
                    else{ 
                        pre_str = '\n==';
                        end_str = '==';                 
                    } 
                    break;
            case 33: 
                 if(!text_len > 0) break;
                 if(pos_s==0||this.getPositionString(pos_s - 1, pos_s) == '\n')
                    { pre_str = end_str = '==='; }
                    else{ pre_str = '\n==='; end_str = '===';}
                     break;
            case 34: 
                 if(!text_len > 0) break;
                 if(pos_s==0||this.getPositionString(pos_s - 1, pos_s) == '\n')
                    { pre_str = end_str = '====';}
                    else{ pre_str = '\n===='; end_str = '===='; }
                    break;
            
            case 35: 
                 if(!text_len > 0) break;
                 if(pos_s==0||this.getPositionString(pos_s - 1, pos_s) == '\n')
                    { pre_str = '>>';}
                    else{ pre_str = '\n>>';}
                 break;
            
            case 41:
            case 42:
            case 43:
            case 44:
            case 45:
                    var oid = arguments[1];
                    var type_list = ['table','img','ref','code','math'];
                    type_list[type-41] ;
                    if(pos_e==0||this.getPositionString(pos_e - 1, pos_e) == '\n'){
                        end_str = '['+  type_list[type-41] +':' + oid + ']\n';
                    }else{
                        end_str = '\n['+    type_list[type-41] +':' + oid + ']\n';  
                    }
                    last = true;
                    break;
            case 81:
                    string = arguments[1];
                    if(pos_s==0||this.getPositionString(pos_s - 1, pos_s) == '\n'){
                        string = string + '\n';
                        lef = string.length + 1;
                    }else{
                        string = '\n'+ string +'\n';
                        lef = string.length + 2;    
                    }
                    len = 0;
                    break;
            case 91: 
                    end_str = arguments[1];
                    last = true;
                    break;
        }

        var $t = $(this)[0];
        if (document.selection) {
                this.focus();
                sel = document.selection.createRange(pos_s , pos_s);
                //sel.text = string;
                sel.text = pre_str;
                sel2 = document.selection.createRange(pos_e + pre_str.length, pos_e + pre_str.length);
                //sel2.text = string;
                sel2.text = end_str;
                //this.focus();
                //console.log('in a');
            }
        else{
              //console.log('in b');
            if ($t.selectionStart || $t.selectionStart == '0') {
                var startPos = pos_s;//$t.selectionStart;
                var endPos = pos_e;//$t.selectionEnd;
                            //var scrollTop = $t.scrollTop;
                $t.value = $t.value.substring(0, startPos) + pre_str + 
                    $t.value.substring(startPos, endPos) + end_str + $t.value.substring(endPos, $t.value.length);
                //this.focus();
                //$t.selectionStart = startPos + string.length;
                //t.selectionEnd = startPos + string.length;
                //console.log('in c');
                            //$t.scrollTop = scrollTop;
            }
            else {
                this.value += pre_str;
                this.value += end_str;
                        //this.focus();
                        //console.log('in d');
            }
       }
       if(last){ this.setPosition( pos_e + pre_str.length+end_str.length, pos_e + pre_str.length+end_str.length);   }
       else{
           this.setPosition(pos_s, pos_e + pre_str.length+end_str.length);  
       }
    },
    /******* Create Editor ********/
    CreateEditor:function(paras){
        /*** comment don't support some lib( table, ref, code, math) and title format ***/
        var default_paras = {
            "article_type": 'blog',
            "article_id": '-1',
            "env_type": "user",
            "env_id": '-1',
            "father_id": "-1",
            "father_type": 'blog',
            "body": '',
            "iscomment": false        
        }
        if(typeof paras != "object") paras = {};
        for(var key in default_paras){
            default_paras[key] = paras[key] || default_paras[key];        
        }
        this.attr("spellcheck","false");

        var _Menu = $('<div></div>'); // the menu parent
        _Menu.attr({"id":"write_menu",
                    "menu_id": $Write.get_menu_id(),
                    "article_id":default_paras["article_id"],
                    "article_type":default_paras["article_type"], 
                    "father_id":default_paras["father_id"],
                    "father_type":default_paras["father_type"], 
                    "env_id": default_paras["env_id"], 
                    "env_type": default_paras["env_type"], 
                    "iscomment": default_paras["iscomment"]});
                        
        var _Menu_base = $('<div></div>'); // base menu tool
        _Menu_base.attr("id","write_menu_base");
        
        var _Menu_base_bar_array = [];
        _Menu_base_bar_array.push('<ul>');
        _Menu_base_bar_array.push('<li kind="1" class="bold" title="加粗">&nbsp;</li>');
        _Menu_base_bar_array.push('<li kind="2" class="italic" title="斜体">&nbsp;</li>');
        _Menu_base_bar_array.push('<li kind="3" class="underline" title="下划线">&nbsp;</li>');
        _Menu_base_bar_array.push('<li kind="4" class="del" title="删除线">&nbsp;</li>');
        _Menu_base_bar_array.push('<li class="split">&nbsp;</li>');
        _Menu_base_bar_array.push('<li kind="11" class="super" title="上标">&nbsp;</li>');
        _Menu_base_bar_array.push('<li kind="12" class="suber"  title="下标">&nbsp;</li>');
        _Menu_base_bar_array.push('<li class="split">&nbsp;</li>');
        _Menu_base_bar_array.push('<li kind="21" class="ol" title="有序列表">&nbsp;</li>');
        _Menu_base_bar_array.push('<li kind="22" class="ul" title="无序列表">&nbsp;</li>');
        _Menu_base_bar_array.push('<li class="split">&nbsp;</li>');
        _Menu_base_bar_array.push('<li kind="31" class="part" title="分隔线">~~</li>');
         if(!default_paras["iscomment"]){
            _Menu_base_bar_array.push('<li kind="32" class="title" title="二级标题">T<sub><small>2</small></sub></li>');
            _Menu_base_bar_array.push('<li kind="33" class="title" title="三级标题">T<sub><small>3</small></sub></li>');
            _Menu_base_bar_array.push('<li kind="34" class="title" title="四级标题">T<sub><small>4</small></sub></li>');
        }
        _Menu_base_bar_array.push('<li kind="35" class="indent" title="段落缩进">&nbsp;</li>');
        if( !default_paras["iscomment"]){
            _Menu_base_bar_array.push('<li class="split">&nbsp;</li>');
            _Menu_base_bar_array.push('<li class="table" title="表格库" kind="t">&nbsp;</li>');
            _Menu_base_bar_array.push('<li class="split">&nbsp;</li>');
            _Menu_base_bar_array.push('<li class="image" title="图片库" kind="i">&nbsp;</li>');
            _Menu_base_bar_array.push('<li class="split">&nbsp;</li>');
            _Menu_base_bar_array.push('<li class="ref" title="引用库" kind="r">&nbsp;</li>');
            _Menu_base_bar_array.push('<li class="split">&nbsp;</li>');
            _Menu_base_bar_array.push('<li class="code" title="程序码库" kind="c">&nbsp;</li>');
            _Menu_base_bar_array.push('<li class="split">&nbsp;</li>');
            _Menu_base_bar_array.push('<li class="math" title="数学式库" kind="m">&nbsp;</li>');
        }
        _Menu_base_bar_array.push('<li class="split">&nbsp;</li>');
        _Menu_base_bar_array.push('<li class="letter" title="特殊字符库" kind="l">&nbsp;</li>');
            
        
        _Menu_base_bar_array.push('</ul>');
        _Menu_base.html(_Menu_base_bar_array.join(''));
        _Menu_base.appendTo(_Menu);
        _Menu.insertBefore(this);

        var $lib_bar = $('<div></div>');
        $lib_bar.attr("id","write_lib_bar").css("display","none");
        
        var $letter_bar = $('<div></div>');
        $letter_bar.attr("id","write_letter_bar").css("display","none");
        
        var l_html= '<div id="bar_nav">'+
                    '<span id="l1" class="lbutton" kind="word4">希腊字符</span>'+           
                    '<span class="lbutton" kind="word1">拉丁字符</span> ' +
                    '<span class="lbutton" kind="word2">国际音标</span>' +
                    '<span class="lbutton" kind="word3">字符</span>' +
                    '</div>'+
                    '<div id="bar_body"><div class="l"></div></div>';   
        $letter_bar.html(l_html).appendTo($lib_bar);
        
        if(!default_paras["iscomment"]){
            
            /*** image bar ***/
            var $image_bar = $('<div></div>');
            $image_bar.attr("id","write_image_bar").css("display","none");
            var i_html = '<div id="bar_nav"><div class="new" title="添加新图片" src_type="img">添加</div>'+
                    '<div class="div" title="图片库">图片库</div></div><div id="bar_body"><div class="i"></div></div>';
            $image_bar.html(i_html).appendTo($lib_bar);
        
            /*** code bar ***/
            var $code_bar = $('<div></div>');
            $code_bar.attr("id","write_code_bar").css("display","none");
            var c_html = '<div id="bar_nav"><div class="new" title="添加新代码" src_type="code">添加</div>'+
                     '<div class="div" title="代码库">代码库</div></div><div id="bar_body"><div id="crtm"></div></div>';
            $code_bar.html(c_html).appendTo($lib_bar);
        
            /*** math bar ***/
            var $math_bar= $('<div></div>');
            $math_bar.attr("id","write_math_bar").css("display","none");
            var m_html = '<div id="bar_nav"><div class="new" title="添加新数学式" src_type="math">添加</div>'+
                     '<div class="div" title="数学式库">数学式库</div></div><div id="bar_body"><div id="crtm"></div></div>';
            $math_bar.html(m_html).appendTo($lib_bar);
        
            /*** ref bar ***/
            var $ref_bar =$('<div></div>');
            $ref_bar.attr("id","write_ref_bar").css("display","none");
            var r_html = '<div id="bar_nav"><div class="new" title="添加新引用" src_type="ref">添加</div>'+
                    '<div class="div" title="引用库">引用库</div></div><div id="bar_body"><div id="crtm"></div></div>';
            $ref_bar.html(r_html).appendTo($lib_bar);
        
            /*** table bar ***/
            var $table_bar = $('<div></div>');
            $table_bar.attr("id","write_table_bar").css("display","none");
            var t_html = '<div id="bar_nav"><div class="new" title="添加新表格" src_type="table">添加</div>'+
                    '<div class="div" title="表格库">表格库</div></div><div id="bar_body"><div id="crtm"></div></div>';
            $table_bar.html(t_html).appendTo($lib_bar); 

        }
        $lib_bar.appendTo(_Menu);   
        this.bind_function_init();
        this.self_init();
        //this.focus();
    },
    _support_code_type: function(){
        return ['AS3','AppleScript','Bash','C#','ColdFusion','C++','CSS','Delphi','Diff',
                'Erlang','Groovy','JavaScript','Java','JavaFX','Lisp' ,'Perl','Php','Plain',
                'PowerShell','Python','Ruby','Sass','Scala','SQL','VB','XML'];
    },
    _support_unicode: function(unicode_type){
        return [];
    },
    /********** insert src to textarea ************************/
    insert_src_to_textarea:function(obj){
        var obj_one = $(obj).parent().parent();
        var kind = obj_one.attr('type'), oid = obj_one.attr('oid');
        var kind_dict = {"img": 42, "math": 45, "code": 44, "table": 41, "ref": 43};
        this.insertFormatString(kind_dict[kind], oid);
    },
    /******** create new src ***********************/
    create_new_src: function(obj){
        var _self_textarea = self_textarea = this;
        var $menu = this.siblings("#write_menu");
        var menu_id = $menu.attr("menu_id"), article_id = $menu.attr("article_id"), article_type = $menu.attr("article_type"), 
            father_id = $menu.attr("father_id"), father_type= $menu.attr("father_type"), kind = $(obj).attr("type"),
            env_type = $menu.attr("env_type"), env_id = $menu.attr("env_id");
        var hidden_paras = {
                        "article_id":  $menu.attr("article_id"), 
                        "article_type": $menu.attr("article_type"), 
                        "env_id": $menu.attr("env_id"), 
                        "env_type": $menu.attr("env_type"),
                        "father_id": $menu.attr("father_id"), 
                        "father_type": $menu.attr("father_type"), 
                        "src_type": $menu.attr("src_type"), 
                        "do": "new"
        };
        var id_dict = {"img": "pic", "math": "math", "code":"code", "table":"table", "ref": "ref"};
        var $body = $('<div></div>');
        $body.attr({"id": "pop_insert_"+ id_dict[ hidden_paras["src_type"] ], "menu_id": menu_id});
        var wd = 200, hg = 200;
        var html = '', paras_html = '';
        for(var ii in hidden_paras){
            paras_html += '<input type="hidden" name="'+ ii +'" value="'+ $.encode(hidden_paras[ii]) +'" />';        
        }
        switch( hidden_paras["src_type"] ){
           case 'img':
           case 'image':
            /** new image /upload-image**/
            html =  
            '<p class="first">添加图片<span class="all_example" title="说明"><a target="_blank" href="/help-editor-picture">说明</a></span></p>'+
            '<form action="/article-src-control" id="up_picture" enctype="multipart/form-data" method="post">'+
            '<input type="hidden" name="picture_type" value="article" />' +
            '<input type="hidden" name="_xsrf" value="' + $.getCookie("_xsrf") + '" />'+
            paras_html + 
            '<p><input class="i_file" type="file" name="picture" onclick=clear_process(this,"i"); /></p>'+
            '<p>标题<input class="i_title" name="title" autocomplete="off" type="text" onfocus=clear_process(this,"i"); /></p>'+
            '<p><span class="i_button"><button type="submit">上传图片</button>'+
            '<button type="submit" style="display:none">提交</button></span><span class="i_process">&nbsp;</span></p></form>';
            //'<iframe name="up_picture_iframe" id="up_picture_iframe" style="display:none"></iframe>';
            wd = 360, hg = 240;
            break;
        case 'math':
            /** new math **/
            html = paras_html+
                   '<p class="first">添加数学式--<font size="12px">数学式采用latex规则</font><span class="all_example" title="说明"><a href="/help-editor-math" target="_blank">说明</a></span></p>'+
                        '<p title="设置名称">名称<input type="text" name="title" autocomplete="off" /></p>'+
                        '<p title="设置名称">样式<label><input type="radio" name="math_mode" checked="checked" value="display" />行间</label>'+
                        '<label><input type="radio" name="math_mode" value="inline" />行内</label></p>'+
                        '<p title="数学式latex内容"><textarea resize="none" autocomplete="off" name="body" ></textarea></p>'+
                        '<p><span><button type="submit">提交</button></span><span class="m_process">&nbsp;</span></p>';
            wd = 450, hg = 380;
            break;
        case 'code':
            /** new code **/
            
            var select_html = '';
            //var CodeType = $Write.code_type;
            var CodeType = $(self_textarea)._support_code_type();
            for(ii=0;ii<CodeType.length;ii++){
                if(CodeType[ii].toLowerCase()=='python'){
                    select_html += '<option selected value="' + CodeType[ii].toLowerCase()+'">' + CodeType[ii] +'</option>';    
                    continue;
                }
                select_html += '<option value="' + CodeType[ii].toLowerCase()+'">' + CodeType[ii] +'</option>'; 
            }
            html = paras_html+
            '<p class="first">添加代码 <span class="all_example" title="说明"><a target="_blank" href="/help-editor-code">说明</a></span></p>'+
            '<p title="代码名称">名称<input type="text" autocomplete="off" name="title" /></p>'+
            '<p title="代码种类">种类<select name="code_type">'+ select_html+
            '</select></p>'+
            '<p title="代码"><textarea name="body" autocomplete="off"></textarea></p>'+
            '<p><span><button type="submit">提交</button></span>'+
            '<span class="c_process">&nbsp;</span></p>';
            wd = 760, hg = 400;
            break;
        case 'table':
            /** new table **/
            html = paras_html +
                    '<p class="first">添加表格 <span class="all_example" title="查看表格实例"><a target="_blank" href="/help-editor-table">实例</a></span></p>'+
                    '<div style="display:block">'+
                    '<p title="表格名称">表名<input type="text" name="title" autocomplete="off" /></p>' +
                    '<p title="表格内容"><textarea name="body" autocomplete="off"></textarea></p>'+
                    '<p><span><button type="submit">提交</button></span><span class="t_process">&nbsp;</span></p>'+
                    '</div>';
            wd = 450, hg = 390;
            break;
        case 'ref':
        case 'reference':
            /** new reference **/
            html = paras_html +
                    '<p class="first">添加引用 <span class="all_example" title="查看说明"><a href="/help-editor-reference" target="_blank">说明</a></span></p>'+
                    '<div style="display:block">'+
                    '<p title="设置引用的名称">名称<input type="text" name="title" autocomplete="off" /></p>'+
                    '<p title="出处">出处<input type="text" name="source" autocomplete="off" /></p>'+
                    '<p title="引用内容"><textarea name="body" autocomplete="off"></textarea></p>'+
                    '<p><span><button type="submit">提交</button></span><span class="r_process">&nbsp;</span></p>'+
                    '</div>';
            wd = 450, hg = 390;
            break;
       }
       var $html = jQuery(html);
       $body.html($html);
       pop_page(wd,hg,$body);
       if(kind!='image' && kind != 'img') $html.find('button').bind('click', function(){   $Write.new_lib_src_submit(this); });
       if(kind == 'image' || kind == 'img'){
            var $image_form = $body.find('form');
            var $process = $image_form.find('.i_process');
            var $button  = $image_form.find('button');
            //alert($button.html());
            //alert($process.html())
            var image_title = '';
            var image_path = '';
            $image_form.submit( function(){
                            
              $(this).ajaxSubmit({
                dataType: 'json',
                beforeSubmit: function(){ 
                    image_title = $image_form.find("input.i_title").val() || '';
                    image_path = $image_form.find(".i_file").val() || '';
                    //alert(image_title);
                    //alert(image_path);
                    //return false;
                    var img_reg = /.*\.(jpg|png|jpeg|gif)$/ig;
    
                    if(!image_path.match(img_reg)){
                        $process.html('图片格式为jpg,png,jpeg,gif！').css("color","red");
                        return false;
                    }
                    
                    if(!$.trim(image_title)){
                        $process.html('请设置标题！').css("color","red");
                        alert("set title");
                        return false;   
                    }
                    $button.attr("disabled","disabled").css("color","#ccc");
                    $process.html('<img src="/static/img/ajax.gif" title="执行中" />');
                    //$process.html('图片上传中...');  
                },
                success: function(response, status){
                    //var response = eval('(' + xhr.responseText + ')');
                    if(response.status == 0){
                        $process.html("图片上传成功！").css('color', 'blue');
                        if(response.article_isnew == 1){
                            $menu.attr("article_id", response.article_id);                        
                        }
                        /****** append to the image lib *****/
                        var current_textarea = $menu.siblings("#write_textarea");
                        $Write.window_close_alert();
                        $process.html('处理成功！').css("color","blue");
            
        
                        // insert a new image in the image lib
                        var new_image = $('<div></div>');
                        new_image.attr({'class':'one','oid':response.src_alias,'type':'img'});
        
                        var new_image_html = //'<div class="one" oid ="'+ response.src_alias +'" type="i">'+
                                '<div class="ileft">'+
                                '<span class="ititle">图'+ response.src_alias+'</span>'+
                                '</div>'+                               
                                '<div class="icontrol">' +
                                '<span class="idel" title="删除此图片">删除</span>'+
                                '<span class="imodify">修改</span>'+
                                '<span class="iinsert">插入</span>'+
                                '</div>' +

                                '<div class="iright" title="'+ $.encode(image_title) +'"><table><tr><td><img src="'+ $.encode(response.img_url) +'" /></td></tr></table></div>';
                                //'<div class="ibottom"><input title="描述" type="text" value="'+ name +'" readonly="readonly" /><div class="iname">插入</div></div>'+
                                //'</div>';
                        new_image.html(new_image_html);
                        var image_bar = $menu.find("#write_image_bar").find(".i");
                        image_bar.append(new_image);
            
                        new_image.find(".imodify").bind('click',function(){
                            current_textarea.update_old_src(this);
                        }).end().find(".iinsert").bind('click', function(){
                            current_textarea.insert_src_to_textarea(this);
                        }).click().end().find(".idel").bind('click', function(){
                            current_textarea.delete_lib_src(this);
                        });
                        pop_page_close();            
                    }else{
                        $process.html(response.info).css("color", "red"); 
                        $button.removeAttr("disabled","disabled").css("color", "black");               
                    }            
               }
               });
               return false;
           });
       }

    },
    /****** submit src, new, edit, remove ****/
    _submit_src: function(_paras){
        var _default_paras = '';
        var src_dict = {'table':"表","math":'数学式',"code":"代码","reference":'引用',"ref":'引用'};
        //var 
        var mes = {};
        var warn = {'table':"表","math":'数学式',"code":"代码","reference":'引用',"ref":'引用'};
        mes = $("#pop-content").DivToDict();
        var process = $(obj).parent().next("span");
        var type = mes['src_type'];
    
        if(mes['title'] == ''){
            process.html("请填写"+ warn[type]+"名称！").css("color","red");
            //$(obj).removeAttr("disabled").css("color","#000");
            return false;           
        }
        if(type == 'reference' || type == 'ref'){
            if(mes['source'] == ''){
                process.html("请填写" + warn[type] + "出处！").css("color","red");
                //$(obj).removeAttr("disabled").css("color","#000");
                return false;
            }   
        }
        if(mes['body'] == ''){
            if(type != 'reference'){
                process.html("请填写" + warn[type] + "内容！").css("color","red");
                //$(obj).removeAttr("disabled").css("color","#000");
                return false;   
            }else{
                var url_reg = /^(http|https|ftp):\/\/.+$/ig;
                if(!url_reg.test(mes['source'])){
                    process.html("请填写链接地址或者引用真实内容！").css("color","red");
                    //$(obj).removeAttr("disabled").css("color","#000");
                    return false;           
                }   
            }
        }
        
    },     
    /******************** update old src *****************************/
    update_old_src:function(obj){
        var obj_one = $(obj).parent().parent();
        var self_textarea = this;
        var $menu = this.siblings("#write_menu");
        var mid = $menu.attr("menu_id"), article_id = $menu.attr("article_id"), 
            article_type = $menu.attr("article_type"), env_id= $menu.attr('env_id'), env_type= $menu.attr("env_type"), 
            father_id = $menu.attr("father_id"), father_type = $menu.attr("father_type"),
            kind = obj_one.attr('type'), oid = obj_one.attr('oid');
        var hidden_paras = {"article_id": article_id, "article_type": article_type, "env_id": env_id, "env_type": env_type,
            "father_id": father_id, "father_type": father_type, "src_type": kind, "do": "edit", "oid": oid, "src_alias": oid};
        var id_dict = {"img": "pic", "math": "math", "code":"code", "table":"table", "ref": "ref"};
        var $body = $('<div></div>');
        $body.attr({"id": "pop_insert_"+ id_dict[kind], "menu_id": mid});
        var html = '', paras_html = '';
        for(var ii in hidden_paras){
            paras_html += '<input type="hidden" name="'+ ii +'" value="'+ $.encode(hidden_paras[ii]) +'" />';        
        }
        var wd = 200, hg = 200;
        switch(kind){
         case 'image':
         case 'img':
            var image_name = $.encode($(obj).parent().siblings(".iright").attr("title"));
            html = '<p class="first">修改图片属性</p>'+
                    paras_html +
                    '<p>标题<input class="i_title" name="title" type="text"  value="'+image_name+'" /></p>'+
                    '<p><span class="i_button"><button type="button">确认修改</button>'+
                    '</span><span class="i_process">&nbsp;</span></p>';
            wd = 360,hg = 200;
            break;
        case 'math':
            var math_name = $.encode(obj_one.find("#otitle").val());
            var math_body = $.encode(obj_one.find("#obody").val());
            var math_mode = $.encode(obj_one.find("#math_mode").val());

            html = paras_html +
                    '<p class="first">修改数学式--<font size="12px">数学式采用latex规则</font></p>'+
                    '<p title="设置名称">名称<input type="text" name="title" value="'+math_name+'" /></p>'+
                    '<p title="设置样式">样式';
                    if(math_mode == "inline"){
                        html += '<label><input type="radio" name="math_mode"  value="display" />行间</label>'+
                            '<label><input type="radio" name="math_mode" checked="checked" value="inline" />行内</label>';
                    }else{
                        html += '<label><input type="radio" name="math_mode" checked="checked" value="display" />行间</label>'+
                            '<label><input type="radio" name="math_mode" value="inline" />行内</label>';
                    }
                  html +='</p>'+
                    '<p title="数学式latex内容"><textarea resize="none" name="body" >'+math_body+'</textarea></p>'+
                    '<p><span><button type="submit">确认</button></span><span class="m_process">&nbsp;</span></p>';
            wd = 450,hg = 380;
            break;
        case 'code':
            var code_title = $.encode(obj_one.find("#otitle").val());
            var code_type = obj_one.find("#otype").val();
            var code_body = $.encode(obj_one.find("#obody").val());
            
            var CodeType = $Write.code_type;
            var select_html = '';
            for(ii=0;ii<CodeType.length;ii++){
                if(CodeType[ii].toLowerCase() == code_type){
                    select_html += '<option selected value="' + CodeType[ii].toLowerCase()+'">' + CodeType[ii] +'</option>';    
                    continue;
                }
                select_html += '<option value="' + CodeType[ii].toLowerCase()+'">' + CodeType[ii] +'</option>'; 
            }
            
            html = paras_html +
            '<p class="first">修改代码 <span class="all_example" title="说明" onclick="toggle_example(this);">说明</span></p>'+
            '<p title="代码名称">名称<input type="text" name="title" value="'+code_title+'" /></p>'+
            '<p title="代码种类">种类<select name="code_type">'+ select_html+
            '</select></p>'+
            '<p title="代码"><textarea name="body">'+code_body+'</textarea></p>'+
            '<p><span><button type="submit">确认</button></span><span class="c_process">&nbsp;</span></p>';
            wd = 760, hg = 400;
            break;
        case 'table':
            var table_title = $.encode(obj_one.find("#otitle").val());
            var table_body = $.encode(obj_one.find("#obody").val());
            html =  paras_html + 
                    '<p class="first">修改表格 <span class="all_example" title="查看表格实例" onclick="toggle_example(this);">实例</span></p>'+
                    '<div style="display:block">'+
                    '<p title="表格名称">表名<input type="text" name="title" value="'+table_title+'" /></p>' +
                    '<p title="表格内容"><textarea name="body">'+ table_body +'</textarea></p>'+
                    '<p><span><button type="submit">提交</button></span><span class="t_process">&nbsp;</span></p>'+
                    '</div>';
            wd = 450, hg = 390;
            break;
        case 'reference':
        case 'ref':
            var ref_name = $.encode(obj_one.find("#otitle").val());
            var ref_source = $.encode(obj_one.find("#osource").val());
            var ref_body = $.encode(obj_one.find("#obody").val());
            html = paras_html +
                    '<p class="first">添加引用 <span class="all_example" title="查看说明" onclick="toggle_example(this);">说明</span></p>'+
                    '<div style="display:block">'+
                    '<p title="设置引用的名称">名称<input type="text" name="title" value="'+ ref_name+'" /></p>'+
                    '<p title="出处">出处<input type="text" name="source" value="'+ ref_source+'" /></p>'+
                    '<p title="引用内容"><textarea name="body">'+ref_body+'</textarea></p>'+
                    '<p><span><button type="submit">确认</button></span><span class="r_process">&nbsp;</span></p>'+
                    '</div>';
            wd = 450, hg = 390;
            break;
       }
       $body.html(html);
       pop_page(wd,hg,$body);
       $body.find('button').bind('click', function(){ $Write.update_lib_src_submit(this); });
    },

    /*********** delete lib src ************************/
    delete_lib_src:function(obj){
        var obj_one = $(obj).parent().parent();
        var $menu = this.siblings("#write_menu");
    
       var oid = obj_one.attr("oid"), kind = obj_one.attr("type"), article_id = $menu.attr("article_id"),
            env_id = $menu.attr('env_id'), article_type = $menu.attr("article_type"), env_type = $menu.attr("env_type"),
            father_id = $menu.attr("father_id"), father_type = $menu.attr("father_type");
       result = confirm("确认删除？");
        if(result){
            var mes = {
                "oid": oid,
                "do": "remove",
                "src_type": kind,
                "src_alias": oid,
                "article_id": article_id, "article_type": article_type,
                "father_id": father_id, "father_type": father_type,
                "env_id": env_id, "env_type": env_type            
            };
        $.postJSON('/article-src-control',mes,
            function(){},
            function(response){
                if(response.status == 0){
                    obj_one.remove();
                }else{
                    alert(response.info);   
                }   
            },
            function(response){ alert('数据提交出错！'); }
        );
    }
    },
    /******** bind function init *****************/
    bind_function_init:function(){
        var write_menu = this.siblings("#write_menu");
        var self_textarea = this;
        if(write_menu.html()){
            { // bind new_lib_src function 
                var lib_new = write_menu.find("#bar_nav").find(".new");
                lib_new.bind('click',function(){
                    //new_lib_src(this);
                    self_textarea.create_new_src(this);
                });
            }
            
            /***************** bind textarea_basic block start *******************************/
            { // bind textarea_basic
                var menu_base_li = write_menu.find("#write_menu_base").find("li");
                menu_base_li.bind('click', function(){
                    var tmp_kind = $(this).attr("kind");
                    var lib_bar = write_menu.find("#write_lib_bar");
                    if(tmp_kind && tmp_kind < 'a'){
                        self_textarea.insertFormatString(parseInt(tmp_kind));
                        if(lib_bar.css("display")=="none"){
                            $(this).siblings("li").removeClass("menu_focus");
                        }
                    }else if(tmp_kind && tmp_kind>='a'){
                        // manage lib bar 
                         //manage_lib_bar(this, tmp_kind);
                        $(this).addClass("menu_focus").siblings("li").removeClass("menu_focus");
                        
                        var letter_bar = lib_bar.find("#write_letter_bar"), code_bar = lib_bar.find("#write_code_bar");
                        var image_bar =lib_bar.find("#write_image_bar"), math_bar = lib_bar.find("#write_math_bar");
                        var ref_bar = lib_bar.find("#write_ref_bar"), table_bar = lib_bar.find("#write_table_bar");
                        var list = [{ kind:'m',obj:math_bar},{kind:'i',obj:image_bar},
                                     {kind:'r',obj:ref_bar},{kind:'t',obj:table_bar},
                                    {kind:'c',obj:code_bar},{kind:'l',obj:letter_bar}];
                        var list_o = {'m':math_bar,'i':image_bar,'r':ref_bar,'t':table_bar,'c':code_bar,'l':letter_bar};
                        if(lib_bar.css("display")=='none'){
                            for(var i = 0; i<list.length;i++){
                                  cur_list = list[i];
                                  if( cur_list.kind==tmp_kind) continue;        
                                  cur_list.obj.hide();
                            }
                            list_o[tmp_kind].show();
                            lib_bar.slideDown("slow");
                        }else{
                            if(list_o[tmp_kind].css("display")=='block'){       
                                  lib_bar.slideUp("slow");
                                  $(this).removeClass("menu_focus");
                            }
                            else
                            { // hide other 
                                 for(var i = 0; i<list.length;i++){
                                    cur_list = list[i];
                                    if( cur_list.kind==tmp_kind) continue;      
                                    cur_list.obj.hide();
                                 }
                                 list_o[tmp_kind].fadeIn("slow");
                            }   
                       }


                    } 
                });
            }
            /***************** bind textarea_basic block end *******************************/

            /***************** bind letter function block start **************************************/
            {
                var letter_bar = write_menu.find("#write_letter_bar");
                var letter_bar_span = letter_bar.children("#bar_nav").find("span");
                var dict_letter = {'word1': $Write.word_list1(), 'word2': $Write.word_list2(), 
                                'word3': $Write.word_list3(), 'word4': $Write.word_list4()};
                letter_bar_span.bind('click', function(){
                       $(this).addClass("wsc_chosed");
                        //this.className = this.("class", "wsc_chosed");
                       // this.setAttribute("className", "wsc_chosed");
                       $(this).siblings().removeClass("wsc_chosed");
                       var _string = '';
                       var Word = dict_letter[$(this).attr("kind")];
                       var target_ = $(this).parent().siblings("#bar_body").children(".l");
                       target_.html('');
                       for(var i=0;i<Word.length;i++){
                          var tmp_string = $('<span></span>');
                          tmp_string.html(Word[i]);
                          tmp_string.bind('click', function(){
                                self_textarea.insertFormatString(91,$(this).html());    
                          });
                          tmp_string.appendTo(target_);
                        }
                });
                letter_bar.find("#l1").click();
            }
            /***************** bind letter function block end **************************************/
            /******************* bind update src **************************/
            {
                
            }
        }
    },
    /*********** lib init ******************/
    lib_init:function(paras)
    {
        var default_paras = {
            "image_list": [],
            "math_list": [],
            "table_list":[],
            "code_list": [],
            "reference_list": []        
        }
        if(typeof paras != "object") paras = {};
        for(var ii in default_paras){
            default_paras[ii] = paras[ii] || default_paras[ii];        
        }
        var self_textarea = this;
        var target = this.siblings("#write_menu").children("#write_lib_bar");
        var target_img = target.children("#write_image_bar").find(".i");
        var target_math = target.children("#write_math_bar").find("#crtm");
        var target_code = target.children("#write_code_bar").find("#crtm");
        var target_table = target.children("#write_table_bar").find("#crtm");
        var target_ref = target.children("#write_ref_bar").find("#crtm");
        var tmp;
        var _html = '';
        for(var i in default_paras["image_list"]){
            tmp = default_paras["image_list"][i];
            _html += '<div class="one" oid="'+ tmp.alias +'" type="img">'+
            '<div class="ileft"><span class="ititle">图' + tmp.alias + '</span></div>'+
            '<div class="icontrol">'+
                '<span class="idel" title="删除此图片">删除</span>'+
            '<span class="imodify">修改</span>'+
            '<span class="iinsert">插入</span>'+
            '</div>'+
            '<div class="iright" title="' + tmp.name + '">'+
            '<table><tbody><tr><td><img src="' + tmp.thumb_name + '"></td></tr></tbody></table>'+
            '</div>'+
            '</div>';
            
        }
        target_img.html(_html);
        var img_list = target_img.find(".one");
        img_list.find(".imodify").bind('click', function(){
            self_textarea.update_old_src(this);
        }).end().find(".iinsert").bind("click", function(){
            self_textarea.insert_src_to_textarea(this);
        }).end().find(".idel").bind("click", function(){
            self_textarea.delete_lib_src(this);
        });


        _html = '';
        for(var i in default_paras["math_list"]){
            tmp = default_paras["math_list"][i];
            _html += '<div class="one" oid="'+ tmp.alias + '" type="math">'+
                '<div><span class="cname">数式'+ tmp.alias +'</span></div>'+
                '<div class="control"><span class="cdel" title="删除">删除</span>' +
                '<span class="cedit" title="修改">修改</span><span class="cinsert">插入</span></div>'+
                '<div><span><input type="text" id="otitle" readonly="readonly" value="'+ tmp.name +'"><input type="hidden" id="math_mode" value="'+ tmp.mode +'" /></span>'+
                '<textarea id="obody">'+ tmp.body +'</textarea></div></div>';
        }
        target_math.html(_html);
        var math_list = target_math.find(".one");
        math_list.find(".cedit").bind('click', function(){
            self_textarea.update_old_src(this);
        }).end().find(".cinsert").bind("click", function(){
            self_textarea.insert_src_to_textarea(this);
        }).end().find(".cdel").bind("click", function(){
            self_textarea.delete_lib_src(this);
        });

        _html = '';
        for(var i in default_paras["table_list"]){
            tmp = default_paras["table_list"][i];
            _html += '<div class="one" oid="'+ tmp.alias +'" type="table">'+
            '<div><span class="cname">表'+ tmp.alias +'</span></div>'+
            '<div class="control"><span class="cdel" title="删除">删除</span>'+
            '<span class="cedit" title="修改">修改</span>'+
            '<span class="cinsert">插入</span></div>'+
            '<div><span><input type="text" id="otitle" readonly="readonly" value="'+ tmp.name +'"></span>'+
            '<textarea id="obody">'+ tmp.body +'</textarea></div></div>';
        }
        target_table.html(_html);
        var table_list = target_table.find(".one");
        table_list.find(".cedit").bind('click', function(){
            self_textarea.update_old_src(this);
        }).end().find(".cinsert").bind("click", function(){
            self_textarea.insert_src_to_textarea(this);
        }).end().find(".cdel").bind("click", function(){
            self_textarea.delete_lib_src(this);
        });

        _html = '';
        for(var i in default_paras["reference_list"]){
            tmp = default_paras["reference_list"][i];
            _html += '<div class="one" oid="'+ tmp.alias +'" type="ref">'+
            '<div><span class="cname">引用'+ tmp.alias +'</span></div>'+
            '<div class="control"><span class="cdel" title="删除">删除</span>'+
            '<span class="cedit" title="修改">修改</span>'+
            '<span class="cinsert">插入</span></div>'+
            '<div><span><input type="text" id="otitle" readonly="readonly" value="'+tmp.name+'"></span>'+
            '<input type="hidden" id="osource" value="'+ tmp.url +'"><textarea id="obody">'+ tmp.body +'</textarea></div></div>';
        }
        target_ref.html(_html);
        var ref_list = target_ref.find(".one");
        ref_list.find(".cedit").bind('click', function(){
            self_textarea.update_old_src(this);
        }).end().find(".cinsert").bind("click", function(){
            self_textarea.insert_src_to_textarea(this);
        }).end().find(".cdel").bind("click", function(){
            self_textarea.delete_lib_src(this);
        });


        _html = '';
        for(var i in default_paras["code_list"]){
            tmp = default_paras["code_list"][i];
            _html += '<div class="one" oid="'+ tmp.alias +'" type="code">'+
            '<div><span class="cname">代码'+ tmp.alias +'</span></div>'+
            '<div class="control"><span class="cdel" title="删除">删除</span>'+
            '<span class="cedit" title="修改">修改</span>'+
            '<span class="cinsert">插入</span></div>'+
            '<div><span><input type="text" id="otitle" readonly="readonly" value="'+ tmp.name +'"></span>'+
            '<input type="hidden" id="otype" value="'+tmp.lang+'"><textarea id="obody">'+ tmp.body +'</textarea></div></div>';
        }
        target_code.html(_html);
        var code_list = target_code.find(".one");
        code_list.find(".cedit").bind('click', function(){
            self_textarea.update_old_src(this);
        }).end().find(".cinsert").bind("click", function(){
            self_textarea.insert_src_to_textarea(this);
        }).end().find(".cdel").bind("click", function(){
            self_textarea.delete_lib_src(this);
        });
    },
    self_init: function(){
        var write_ = $(this);
        if(write_.val() == '' || write_.val() == '内容'){
            write_.css({"line-height":'200px','text-align':'center','color':'#ccc'}).val('内容')
          .change(function(){clear_content_process();})
          .focus(function(){ 
                $(this).css({"color":"#000","line-height":"25px",'text-align':'left'});
                    if($(this).val() == '内容') {
                        $(this).val('');
                        }
                    })
          .blur(function(){ 
            if($.trim($(this).val())==''){
                $(this).css({"color":"#ccc","line-height":'200px','text-align':'center'}).val('内容');      
            }       
          });    
        }
    },
    summary_title_init: function(){
        var summary = $(this).siblings(".w_summary");
    //alert(summary);
        if(summary.val() =='' || summary.val() == '摘要'){
            summary.css({"line-height":'100px','text-align':'center','color':'#ccc'}).val('摘要')
            .change(function(){clear_content_process();})
            .focus(function(){
               $(this).css({"color":"#000","line-height":"25px",'text-align':'left'});
                   if($(this).val()=='摘要') $(this).val('');
               })
            .blur(function(){
              if($.trim($(this).val())==''){
                  $(this).css({"color":"#ccc","line-height":'100px','text-align':'center'}).val('摘要');        }
           });
        }
        
        var tmp_title = $(this).siblings(".w_title");
        tmp_title.focus(function(){
           $(this).css("color","#000");
               if($(this).val()=='标题') $(this).val('');
           }).blur(function(){
              if($.trim($(this).val())==''){ $(this).css("color","#ccc").val('标题');}
       });

    },


    
    
})



//write tool function
/******************************************
    this function  is userd for to insert kinds of string to the textarea
    * (0 ,bold),(1,italic),(2,underline),(3,del),(4,superscript),(5,suberscript),(6,indent),(7,ol),(8,ul),(9,h2)
    * (10,h3),(11,h4),(12,h5),(13,page),..........
******************************************/


/***************Toggle help or note page in the pop page ******************/
toggle_example = function(obj){
    $(obj).parent().siblings().toggle();
}

//Insert Help
want_help = function( _obj )
{
    alert('help');
}







/******************check the picture right or not the user want to upload *************************/
$Write.picture_check = picture_check =  function(obj){

    var image = $(obj).parent().parent().siblings().children(".i_file");
    var title = $(obj).parent().parent().siblings().children(".i_title");
    var process = $(obj).parent().siblings(".i_process");
    var src = $.trim(image.val());
    if( src == ''){
        process.html('请选择图片！');
        process.css("color","red");
        //$(obj).removeAttr("disabled").css("color","#000");
        return false;
    }
    var img_reg = /.*\.(jpg|png|jpeg|gif)$/ig;
    
    if(src.match(img_reg) == null ){
        process.html('图片格式为jpg,png,jpeg,gif！');
        process.css("color","red");
        //$(obj).removeAttr("disabled").css("color","#000");
        return false;
    }
    if($.trim(title.val())==''){
        process.html('请设置标题！');
        process.css("color","red");
        //$(obj).removeAttr("disabled").css("color","#000");
        return false;   
    }
    //$(obj).attr("type","submit");
    $(obj).attr("disabled","disabled").css("color","#ccc");
    process.html('<img src="/static/img/ajax.gif" title="执行中" />');
    $(obj).next().click();
    //alert('in test');
    return true;
}


/****************** upload picture response handler ****************************/
picture_upload_handler = function(type, info, alias, name ,isnew , article_id ){
    //alert('in img up handler');
    var obj = $("#pop_insert_pic");
    var menuid = obj.attr("menu_id");
    var process = obj.find("span.i_process");
    var buttons = obj.find("span.i_button").find('button');
    var str = "#write_menu[menu_id="+menuid+"]";
    var menu = $("body").find(str);
    if (isnew >= 0) {
        menu.attr("article_id",article_id);
    }
    var image_bar = menu.find("#write_image_bar").find(".i");
    buttons.removeAttr("disabled").css("color","#000");
    if(type == 1){
        process.html(info).css("color","red");  
    }else{
        var current_textarea = menu.siblings("#write_textarea");
        $Write.window_close_alert();
        process.html('处理成功！').css("color","blue");
            
        
        // insert a new image in the image lib
        var new_image = $('<div></div>');
        new_image.attr({'class':'one','oid':alias,'type':'img'});
        
        var new_image_html = //'<div class="one" oid ="'+ alias +'" type="i">'+
                                '<div class="ileft">'+
                                '<span class="ititle">图'+ alias+'</span>'+
                                '</div>'+                               
                                '<div class="icontrol">' +
                                '<span class="idel" title="删除此图片">删除</span>'+
                                '<span class="imodify">修改</span>'+
                                '<span class="iinsert">插入</span>'+
                                '</div>' +

                                '<div class="iright" title="'+ $.encode(name) +'"><table><tr><td><img src="'+ $.encode(info) +'" /></td></tr></table></div>';
                                //'<div class="ibottom"><input title="描述" type="text" value="'+ name +'" readonly="readonly" /><div class="iname">插入</div></div>'+
                                //'</div>';
        new_image.html(new_image_html);
        image_bar.append(new_image);
            
        new_image.find(".imodify").bind('click',function(){
             current_textarea.update_old_src(this);
        }).end().find(".iinsert").bind('click', function(){
            current_textarea.insert_src_to_textarea(this);
       }).click().end().find(".idel").bind('click', function(){
           current_textarea.delete_lib_src(this);
       });
       pop_page_close();
    }
}



/**************** insert a new source : submit moudle ******************/
$Write.new_lib_src_submit = function(obj)
{
    //$(obj).attr("disabled","disabled").css("color","#ccc");
    var mes = {};
    var warn = {'table':"表","math":'数学式',"code":"代码","reference":'引用',"ref":'引用'};
    mes = $("#pop-content").DivToDict();
    var process = $(obj).parent().next("span");
    var type = mes['src_type'];

    if(mes['title'] == ''){
        process.html("请填写"+ warn[type]+"名称！").css("color","red");
        //$(obj).removeAttr("disabled").css("color","#000");
        return false;           
    }
    if(type == 'reference' || type == 'ref'){
        if(mes['source'] == ''){
            process.html("请填写" + warn[type] + "出处！").css("color","red");
            //$(obj).removeAttr("disabled").css("color","#000");
            return false;
        }   
    }
    if(mes['body'] == ''){
        if(type != 'reference'){
            process.html("请填写" + warn[type] + "内容！").css("color","red");
            //$(obj).removeAttr("disabled").css("color","#000");
            return false;   
        }else{
            var url_reg = /^(http|https|ftp):\/\/.+$/ig;
            if(!url_reg.test(mes['source'])){
                process.html("请填写链接地址或者引用真实内容！").css("color","red");
                //$(obj).removeAttr("disabled").css("color","#000");
                return false;           
            }   
        }
    }

    var mid = $("#pop-content").children().attr("menu_id");
    var write_str = '#write_menu[menu_id="' + mid + '"]';
    var write_menu = $("body").find(write_str); 
    var list = {'math':'#write_math_bar','reference':'#write_ref_bar', 'ref':'#write_ref_bar',
               'table':'#write_table_bar','code':'#write_code_bar'};
    mes['do'] = 'new';
    mes['src_alias'] = mes['oid'];
    /** send the mes **/
    $.postJSON('/article-src-control', mes,
        function(){ 
        process.html('<img src="/static/img/ajax.gif" title="执行中" />');
        $(obj).attr("disabled","disabled").css("color","#ccc");
    },
        function(response){
            //alert(response.kind);
            mes = $.encode(mes);
            if(response.status==0){
                // right    
                var current_textarea = write_menu.siblings("#write_textarea");  
                $Write.window_close_alert();
                var info = response.info;
                if(response.article_isnew == 1){
                    write_menu.attr("article_id",response.article_id);
                }
                var obj_bar = write_menu.find(list[type]);
                var obj_body = obj_bar.find("#crtm");
                var obj_one = $('<div></div>');
                obj_one.attr({"class":'one','oid':response.src_alias,"type":type});
                var obj_html= '';
                var alias = response.src_alias;
                //alert(type);
                switch(type){
                    case 'reference':
                    case 'ref':
                        obj_html =  '<div><span class="cname">引用'+ alias+'</span></div>'+
                            '<div class="control"><span class="cdel" title="删除">删除</span>'+
                            '<span class="cedit" title="修改">修改</span>'+
                            '<span class="cinsert">插入</span></div>'+
                            //'<div><span class="cdes">名称：</span></div>'+
                            '<div><span><input type="text" id="otitle" readonly="readonly" value="'+mes['title']+'" /></span>' + 
                            '<input type="hidden" id="osource" value="'+mes['source']+'" /><textarea id="obody">'+mes['body']+'</textarea></div>';
                        break;
                    case 'code':
                        obj_html = '<div><span class="cname">代码'+ alias +'</span></div>'+
                                '<div  class="control"><span class="cdel" title="删除">删除</span>'+
                                '<span class="cedit" title="修改">修改</span>'+
                                '<span class="cinsert">插入</span></div>'+
                                //'<div><span class="cdes">名称：</span></div>'+
                                '<div><span><input type="text" id="otitle" readonly="readonly" value="'+mes['title']+'" /></span>'+
                                '<input type="hidden" id="otype" value="'+ mes['code_type'] +'" />' +
                                '<textarea id="obody">'+mes['body'] +'</textarea>' +
                                '</div>';
                        break;
                    case 'table':
                        obj_html = '<div><span class="cname">表'+alias+'</span></div>'+
                                '<div  class="control"><span class="cdel" title="删除">删除</span>'+
                                '<span class="cedit" title="修改">修改</span>'+
                                '<span class="cinsert">插入</span></div>'+
                                //'<div><span class="cdes">名称：</span></div>'+
                                '<div><span><input type="text" id="otitle" readonly="readonly" value="'+mes['title']+'" /></span>'+
                                '<textarea id="obody">'+mes['body']+'</textarea>'+                              
                                '</div>';
                        break;
                    case 'math':
                        obj_html = '<div><span class="cname">数式'+alias+'</span></div>'+
                                '<div class="control"><span class="cdel" title="删除">删除</span>'+
                                '<span class="cedit" title="修改" >修改</span>'+
                                '<span class="cinsert">插入</span></div>'+
                                //'<div><span class="cdes">名称：</span></div>'+
                                '<div><span><input type="text" id="otitle" readonly="readonly" value="'+mes['title']+'" />'+
                                    '<input type="hidden" id="math_mode" value="'+ mes['math_mode'] +'" /></span>'+
                                '<textarea id="obody">'+mes['body']+'</textarea>'+                              
                                '</div>';
                        //alert(obj_html);
                        break;
                }   
                        
                obj_one.html(obj_html);
                obj_one.appendTo(obj_body);
                process.html('添加成功！').css("color",'blue');
                
                
                obj_one.find(".cedit").bind('click',function(){
                    current_textarea.update_old_src(this);
                });
                obj_one.find(".cinsert").bind('click', function(){
                    current_textarea.insert_src_to_textarea(this);
                }).click();
                obj_one.find(".cdel").bind('click', function(){
                    current_textarea.delete_lib_src(this);
                });
                pop_page_close();
            }else{
                process.html(response.info).css("color","red"); 
                $(obj).removeAttr("disabled").css("color","#000");
                return false;
            }
        },
        function(response){
            process.html('数据提交出错！').css("color","red");  
            $(obj).removeAttr("disabled").css("color","#000");
            return false;
        }
    );  
}





/**************** update the  source : insert moudle ******************/
$Write.update_lib_src_submit = function( obj )
{
    $(obj).attr("disabled","disabled").css("color","#ccc");
    var mes = {};
    var warn = {'table':"表","math":'数学式',"code":"代码","reference":'引用','image':'图片',"ref":'引用','img':'图片'};
    mes = $("#pop-content").DivToDict();
    var process = $(obj).parent().next("span");
    var type = mes['src_type'];
    var oid = mes['oid'];
    if(mes['article_id'] == '' || type == '' || oid == ''){
            process.html("出现错误！").css("color","red");
            $(obj).removeAttr("disabled").css("color","#000");
            return false;
    }
    
    var url = '/article-src-control';
    
    if(mes['title'] == ''){
        process.html("请填写"+ warn[type]+"名称！").css("color","red");
        $(obj).removeAttr("disabled").css("color","#000");
        return false;           
    }
    if(type == 'reference' || type == 'ref'){
        if(mes['source'] == ''){
            process.html("请填写" + warn[type] + "出处！").css("color","red");
            $(obj).removeAttr("disabled").css("color","#000");
            return false;
        }   
    }
    if(mes['body'] == ''){
        if(type!='reference' && type != 'ref'){
            process.html("请填写" + warn[type] + "内容！").css("color","red");
            $(obj).removeAttr("disabled").css("color","#000");
            return false;
        }else{
            var url_reg = /^(http|https|ftp):\/\/.+$/ig;
            if(!url_reg.test(mes['source'])){
                process.html("请填写链接地址或者引用真实内容！").css("color","red");
                $(obj).removeAttr("disabled").css("color","#000");
                return false;           
            }
        }
    }
    var menu_id = $("#pop-content").children().attr("menu_id");
    var str = "#write_menu[menu_id="+menu_id+"]";
    var menu = $("body").find(str);
    var list = {'image':'#write_image_bar','math':'#write_math_bar', 'img':'#write_image_bar', 'ref':'#write_ref_bar',
               'reference':'#write_ref_bar','code':'#write_code_bar','table':'#write_table_bar'};
    
    /** send the mes **/
    $.postJSON(url,mes,
        function(){ process.html('<img src="/static/img/ajax.gif" title="执行中" />'); },
        function(response){
            /** right response **/  
             //mes = $.encode(mes);      
             if(response.status == 0){
                process.html('修改成功！').css("color","blue");
                var obj_bar = menu.find(list[type]);
                var obj_one_str = ".one[oid="+mes['oid']+"]";
                var obj_one = obj_bar.find(obj_one_str);
                //alert(obj_one.html());
                switch(type){
                    case 'image':
                    case 'img':
                        obj_one.find(".iright").attr("title",mes['title']);
                        break;
                    case 'reference':
                    case 'ref':
                        obj_one.find("#otitle").val(mes['title']);
                        obj_one.find("#osource").val(mes['source']);
                        //alert(mes['body']);
                        obj_one.find("#obody").val(mes['body']);
                        break;  
                    case 'code':
                        obj_one.find("#otitle").val(mes['title']);
                        obj_one.find("#otype").val(mes['code_type']);
                        
                        obj_one.find("#obody").val(mes['body']);
                        break;
                    case 'table':
                        obj_one.find("#otitle").val(mes['title']);
                        obj_one.find("#obody").val(mes['body']);
                        break;
                    case 'math':
                        obj_one.find("#otitle").val(mes['title']);
                        obj_one.find("#obody").val(mes['body']);
                        obj_one.find("#math_mode").val(mes['math_mode']);
                        //alert(mes['math_mode']);
                        break;
                }
                pop_page_close();
             }else{
                process.html(response.info).css("color","red");
                $(obj).removeAttr("disabled").css("color","#000");  
                return false;
             }
             
        },
        function(response){
            process.html('数据提交出错！').css("color","red");
            $(obj).removeAttr("disabled").css("color","#000");
            return false;
        }
    );      
}



/***************** clear the process *************************/
clear_process = function(obj,type){
    switch(type){
        case 'i':
            var process = $(obj).parent().siblings().find(".i_process");
            process.css("color","#000").html('');   
            break;
    }
}


/**************** write preview **************************/
$Write.preview_write = function(obj){
    var process = $(".w-submit-result");
    var submit_button = $(".w-submit").find("button");
    //alert(submit_button.html());
    $Write.send_write_blog(
    function(){
        process.html('<img src="/static/img/ajax.gif" />');
        $(obj).next('span').html('');
         submit_button.attr("disabled","disabled").css("color","#ccc");
        },function(response){
        submit_button.removeAttr("disabled").css("color","#000");   
        if(response.kind == 0){
            process.html('存储成功！<a href="/blog/'+response.info+'?preview=yes" target="_blank" >预览地址</a>').css("color",'blue');
            $("#write_menu").attr("article_id",response.info);  
            string = '<a href="/blog/'+response.info+'?preview=yes" target="_blank" >预览地址</a>'
            $(obj).next('span').html(string);
            $Write.window_close_alert();
        }else{
            process.html(response.info).css("color",'red'); 
        }
    },
    function(response){
        submit_button.removeAttr("disabled").css("color","#000");   
        process.html('提交出现错误！').css("color",'red');  
    }, {'do':'preview'});
}

$Write.new_tag = function(page, obj){
    var tag_html = [];
    tag_html.push('<div id="pop_insert_table">');
    tag_html.push("<p class='first'>添加新分类</p>");
    tag_html.push("<p>类别名<input type='text' name='tag' />");
    tag_html.push("<input type='hidden' name='do' value='add' />");
    tag_html.push("<input type='hidden' name='page' value='" +page+ "' />");
    if(arguments.length >=2)
        tag_html.push("<input type='hidden' name='group_id' value='"+ ($(obj).attr("group_id") || '-1') +"' />");
    tag_html.push("</p>");
    tag_html.push("<p><button>添加</button><span class='t_process' style='width:70%'></span></p>");
    tag_html.push('</div>');
    _html = tag_html.join('');
    $html = jQuery(_html);
    pop_page(350,180, $html);
    $html.find('button').bind('click', function(){ $Write.new_tag_submit(this, page); })
    .end().find('input').focus();
};

$Write.new_tag_submit = function(obj, page){
    var page = page || 'write';
    var mes = $("#pop_insert_table").DivToDict() || {};
    var $process = $(obj).siblings('span');
    if(mes['tag'] == ''){
        wrong('请您填写分类！');
        return false;
    }
    if(mes['tag'].length > 15){
        wrong('分类字数请在15个字内');   
        return false;
    }
    
    // send XHR
    jQuery.postJSON('/tag-control', mes, 
        function(){ $(obj).attr('diabled', 'disabled');  $process.html('<img src="/static/img/ajax.gif" />'); },
        function(response, status){  
            if(response.kind == 0){
                $process.html('添加分类成功！').css('color', 'blue'); setTimeout(pop_page_close(),1000);
                switch(page){
                    case 'write':
                         var tag_html = '<span class="w-class">'+
                            '<label><input type="checkbox" name="classes" value="' + $.encode(mes['tag']) + '" />'+
                            $.encode( mes['tag'] )+'</label></span>';
                        $('div.w-class').find('div').eq(1).append(tag_html);
                        break;
                    case 'settings-tag':
                        var tag_html = '<li class="li">'+
                                '<a href="/blog-lib/?tag=' + $.encode(mes['tag']) +'" class="tag-link" >'
                                 + $.encode(mes['tag']) +'</a> <span class="tag-del" tag="' + $.encode(mes['tag']) +'">删除</span></li>';
                        var $ul = $('div.settings').find('ul');
                        if($ul.length > 0){
                            $ul.append(tag_html);                        
                        }else{
                            $('#tag-note').remove();
                            $('div.settings').find(".div-20").eq(0).after('<ul class="ul">'+ tag_html +'</ul>');                        
                        }
                        break;
                    case 'group-tag':
                        if(mes['group_id']){
                            var tag_html = '<span><a href="/group/' + mes['group._id']+'/doc?tag=' + $.encode(mes['tag']) + 
                            '">'+ $.encode(mes['tag']) +'</a><a href="javascript:void(0)" class="del_tag" tag="'+ 
                            $.encode(mes['tag']) +'" group_id="' + mes['group_id'] + '">删除</a></span>';
                            $('div.board_con').append(tag_html);
                        }
                        break;
                    default:
                        break;                
                }
                
                // add to the chosen block
               
            }else{
                wrong(response.info);           
            }    
        },
        function(response, status){  wrong('出错,错误代码：' + status);}    
    );
    function wrong(info){
        $process.html(info).css('color', 'red');
        $(obj).removeAttr('disabled');    
    };
}

$Write.delete_tag_submit = function(obj){
    var mes = {};
    mes['tag'] = $(obj).attr('tag');
    mes['page'] = 'user-tag';
    if($(obj).attr('group_id')){
        mes['page'] = 'group-tag';
        mes['group_id'] = $(obj).attr('group_id'); 
    }
    mes['do'] = "remove";
    var res = window.confirm("确认删除分类'"+ mes['tag'] + "'?");
    if(res){
        $.postJSON('/tag-control', mes, 
            function(){},
            function(response){
                if(response.kind == 0){
                    alert('删除成功！');
                    if(mes['page'] == 'group-tag'){
                        $(obj).parent('span').remove();
                    }else{
                        $(obj).parent('li').remove();   
                    }             
                }else{
                    alert(respone.info);                
                }
            },
            function(response){
                alert("提交出错！")
            })
    }
}



$Write.post_write = function(obj){
    var process = $(".w-submit-result");
    //
    $Write.send_write_blog(
        function(){
        process.html('<img src="/static/img/ajax.gif" />');
          $(obj).next('span').html('');
          $(obj).attr("disabled","disabled").css("color","#ccc");
          
        },function(response){
        
        if(response.kind == 0){
            process.html('文章发布成功！').css("color",'blue');
            $("#write_menu").attr("article_id",response.info);
            $Write.close_window_close_alert();
            newurl = "/blog/" + response.info;
            setTimeout('location.href=' + 'newurl', 1000);
        }else{
            process.html(response.info).css("color",'red'); 
            $(obj).removeAttr("disabled").css("color","#000");  
        }
    },
    function(response){
        process.html('提交出现错误！').css("color",'red');  
        $(obj).removeAttr("disabled").css("color","#000");  
    }, {'do':'post'});
}

$Write.post_write_all = function(obj){
    /*********** post article *******************/
    var $obj = $(obj), $menu = $('#write_menu'), $text=$('#write_textarea'), 
        $process = $("div.w-submit-result");
    var mes = {};
    mes['do'] = $obj.attr("do") || 'post', mes['father_id'] = $menu.attr('father_id')|| '-1',
    mes['father_type'] = $menu.attr('father_type'), mes['group_id'] = $menu.attr('group_id') || '-1',
    mes['env_type'] = $menu.attr("env_type"), mes['env_id'] = $menu.attr("env_id"),
    mes['article_type'] = $menu.attr('article_type'), mes['article_id'] = $menu.attr('article_id');
    mes['privilege'] = $('#write-permission').DivToDict()['permission'] || 'public';
    var classes = $("div.w-class").DivToDict();
    if('classes' in classes)  classes = classes['classes'];
    else classes = [];
    mes['tags'] = classes;
    mes['title'] = $.trim($(".w_title").val()) || '', mes['summary'] = $.trim($(".w_summary").val()) || '',
    mes['body'] = $.trim($("#write_textarea").val()) || '', mes['keywords']=$("#write-keys").DivToDict()['keys']||'';
    
    if(mes['title']=='' || mes['title']=='标题'){
        if( mes['article_type'] != 'about' && mes['article_type'] != 'group-info'){
            wrong('请您填写标题！');
            return false;        
        }
    }
    if(mes['body'] == '' || mes['body'] == '内容'){
        wrong('请您填写内容！'); return false;  
    }
    var  str = '存储成功！<a href="/blog/?preview=yes" target="_blank" >预览地址</a>';
    $.postJSON('/update-article', mes, 
        function(){
            $process.html('<img src="/static/img/ajax.gif" />');
            $('button').attr('disabled', 'disabled').css('color', '#ccc');
        }, function(response){
            if(response.status != 0){
                wrong(response.info);            
            }else{
                if(response.isnew != 0) $menu.attr('article_id', response.article_id);
                var preview_url = '';
                switch(mes['article_type']){
                    case 'blog':
                        preview_url = '/blog/'+ response.article_id; 
                        break;
                    case 'about':
                        preview_url = '/bloger';
                        break;
                    case 'group-info':
                        preview_url = '/group/'+mes['env_id']+'/info'
                        break;
                    case 'group-topic':
                        preview_url = '/group/'+ mes['env_id'] + '/topic/' + response.article_id
                        break;
                    case 'group-notice':
                        preview_url = '/group/' + mes['env_id'] + '/notice/' + response.article_id
                        break;
                    case 'group-feedback':
                        preview_url = '/group/' + mes['env_id'] + '/feedback/' + response.article_id
                        break;
                    case 'group-doc':
                        preview_url = '/group/' + mes['env_id'] + '/doc/' + response.article_id
                        break;                
                }
                if(mes['do'] == 'preview'){
                    preview_url += '?preview=yes'
                    correct('操作成功！预览地址<a href="'+ preview_url +'" target="_blank">预览</a>');   
                    $Write.window_close_alert();             
                }else{
                    $Write.close_window_close_alert();
                    correct('操作成功！');
                    setTimeout( function (){ location.href=preview_url }, 1000);               
                }
            }
        }, function(response){
            wrong('数据提交出错！');        
     })
    $('button').removeAttr('disabled').css('color', 'black');
    function wrong(str){
        $process.html(str).css('color', 'red');
    }
    function correct(str){
        $process.html(str).css('color', 'blue');    
    }

}



/**************** send the write **************************************/
$Write.send_write_blog = function(before_handler,right_handler,error_handler, arg){
    var arg = arg || {} ;
    var title = $.trim($(".w_title").val());
    var summary = $.trim($(".w_summary").val());
    var body = $.trim($("#write_textarea").val());
    var $menu = $("#write_menu");
    var article_id = $menu.attr("article_id"), article_type = $menu.attr("article_type"),
        env_id = $menu.attr("env_id"), env_type = $menu.attr("env_type"),
        father_id = $menu.attr("father_id"), father_type = $menu.attr("father_type"),
        keywords = $("#write-keys").DivToDict()['keys'], permission = $("#write-permission").DivToDict()['permission'];
       var tags = $("div.w-class").DivToDict();
       if('classes' in tags)  tags = tags['classes'];
       else tags = [];
    //alert(classes['classes']);
       var process = $(".w-submit-result");
       var mes = {};
       mes['tags'] = tags;
    //alert(mes['classes']);
    //alert(typeof mes['classes']);
    mes['title'] = title;
    mes['summary'] = summary;
    mes['body'] = body;
    mes['article_id'] = article_id;
    mes['article_type'] = art_type;
    mes['keywords'] = keywords;
    mes['privilege'] = permission;
    mes['father_id'] = father_id;
    mes['father_type'] = father_type;
    mes['env_id'] = env_id;
    mes['env_type'] = env_type;
       
    if(mes['title'] == '' || mes['title'] == '标题'){
        process.html('请填写标题！').css("color",'red');
        return false;   
    }
    if(mes['body'] == '' || mes['body'] == '内容'){
        process.html('请写正文！').css("color",'red');
        //alert("in body");
        return false;   
    }
    var url = '/update-article'
       jQuery.extend(mes, arg);
           $.postJSON(url,mes,
              function(){ before_handler(); },
              function(response){
            right_handler(response);
        },
        function(response){
            error_handler(response);
        }
       );   
}



clear_content_process = function(){
    var process = $(".w-submit-result");
    process.html('');   
}


$Write.comment_create = function(obj){
    var $bollean = $('body').find('#write_comment_zone');
    var blog_id = $('.b_com').attr('blog_id')||0;
    var $obj = $(obj);
    var paras = {
        "article_id": '-1',
        "article_type": 'comment',
        "env_id": $obj.attr("env_id"),
        "env_type": $obj.attr("env_type"),
        "father_id": $obj.attr("article_id"),
        "father_type": $obj.attr("article_type"),
        "iscomment": true
    }
    
    
    var article_type = $obj.attr('article_type') || 'blog';
    var father_id = $obj.attr("father_id")||'-1';
    var father_type = $obj.attr("father_type") || 'blog';
    var ref_comment_pos = $.trim($obj.attr("pos")) || '';
    //if($(obj).attr("ref_type")!="comment")
    var ref_comment_body = $(obj).parent('.com_nav').siblings(".bb_con1").children('.bb_con').text() || '';
    var ref_author_id = $obj.attr("author_id")||'0';
    var ref_author_name = $obj.attr("author_name")||'';
    
    var reply_comment = true;
    
    if($obj.attr("ref_type") != "comment") reply_comment = false;
    
    var tmp_ref_comment_body = ref_comment_body.slice(0, 100 > ref_comment_body.length ? ref_comment_body.length: 100);

    //$.log(ref_comment_body.slice(0, 100 > ref_comment_body.length ? ref_comment_body.length: 100));
    
    if($bollean.html()==null){
        //alert(1);
        // create new comment box
        var target = $('.b_com');
        var $box = $('<div></div>');
        $box.attr({'class':'com_reply', 'id':'write_comment_zone'});
        if(reply_comment){
            // reply to comment 
            $box.html('<input type="hidden" id="ref_comment_input" name="ref_comment" value="'+ ref_comment_pos +
            '" /><div id="ref_comment_lib">'+
            '<div class="ref_comment_one">'+
            '<a href="javascript:void(0);" class="link_close" comment_pos="' + ref_comment_pos + '">X</a>' +
            '<p>'+ tmp_ref_comment_body +'<a href="/bloger/' + ref_author_id + '" class="ref_author">'+
            $.encode(ref_author_name)+'</a></p></div></div>' + 
            '<textarea class="bcr_text" id="write_textarea"></textarea>'+
            '<div class="bcr_con"><button>提交</button>'+
            '<span class="comment_process">&nbsp;</span></div>');
        }else{
            // reply to blog 
            $box.html('<input type="hidden" id="ref_comment_input" name="ref_comment" value="" />'+
            '<div id="ref_comment_lib"></div>' + 
            '<textarea class="bcr_text" id="write_textarea"></textarea>'+
            '<div class="bcr_con"><button>提交</button>'+
            '<span class="comment_process">&nbsp;</span></div>');
        }
        //alert(target.html());
        $box.appendTo(target);
        //$.log($box)
        //alert(0);
        $box.find("a.link_close").bind('click', function(){
            close_reply(this);
        });
        var textarea = $box.find("#write_textarea");
        //alert(textarea.val());
        //art_id, art_type, art_con, father_id, father_type, group_id
        textarea.CreateEditor(paras);
        textarea.focus();
        $box.find('button').bind('click', function(){  $Write.comment_post("#write_comment_zone");  });
    }else{
        var textarea = $('body').find("#write_textarea");
        var ref_comment_input = $("#ref_comment_input");
        if(reply_comment){
            var all_id = ref_comment_input.val();
            var all_id_list = all_id.split(',');
            for(var i =0; i<all_id_list.length;i++){
                if(ref_comment_pos == all_id_list[i])  break;            
            }
            if(i>=all_id_list.length){
                // not contain the comment id
                //$.log("1".split(','));
                //$.log( all_id_list);
                //$.log('all id length ' + all_id_list.length);
                //$.log('id ' + ref_comment_id );
                //$.log('id in all:' + (ref_comment_id in all_id_list));
                all_id_list.push(ref_comment_pos);
                ref_comment_input.val(all_id_list.join(','));
                var $restr = $('<div class="ref_comment_one">'+
                    '<a href="javascript:void(0);" class="link_close" comment_pos="' + ref_comment_pos +'">X</a>'+
                    '<p>'+ tmp_ref_comment_body +
                    '<a href="/bloger/' + ref_author_id + '" target="_blank" class="ref_author">'+$.encode(ref_author_name)+'</a></p></div>');
                $("#ref_comment_lib").append($restr);
                $restr.find('a.link_close').bind('click', function(){  close_reply(this); });
            }
        }
        
        textarea.focus();
    }
    
    function close_reply(obj){
        var $obj = $(obj);
        var remove_id = $.trim($obj.attr("comment_pos")) || '';
        var all_id = $("#ref_comment_input").val();
        var all_id_list = all_id.split(",");
        for(var i=0;i<all_id_list.length;i++){
            if(all_id_list[i] == remove_id) { 
                all_id_list.splice(i,1);
                break; 
            }        
        }
        $(obj).parent().remove();
        var all_id_str = all_id_list.join(',');
        $("#ref_comment_input").val(all_id_str);
    }
};


$Write.comment_post = function(tag){
    // post comment by tag , tag must be the father of the textarea 
    var $tag = $(tag);
    var process = $tag.find('.comment_process');
    var textarea = $tag.find('textarea');
    var menu = $tag.find('#write_menu');
    var $button = $tag.find('button');
    var ref_comment = $("#ref_comment_input").val() || '';
    var mes = {};
    mes['body'] = textarea.val();
    mes['article_id'] = menu.attr("aritcle_id")||0;;
    mes['article_type'] = 'comment';
    mes['father_id'] = menu.attr("father_id")||0;
    mes['father_type'] = menu.attr('father_type') || 'blog';
    mes['env_id'] = menu.attr("env_id");
    mes['env_type'] = menu.attr("env_type");
    mes['ref_comment'] = ref_comment;

    if(!mes['body'] || $.trim(mes['body']) =='' || mes['body'] == "内容"){
        process.html('评论内容不能为空！').css('color','red');
        return false;
    }
    $.postJSON('/update-article',mes,
        function(){ 
            process.html('<img src="/static/img/ajax.gif" />');
            $button.attr("disabled","disabled").css("color","#ccc");
        },
        function(response){
            if(response.status == 0){
                process.html('评论成功，评论框2s后关闭！').css('color','blue');
                setTimeout('', 2000);
                setTimeout("$('body').find('#write_comment_zone').slideUp('slow',function(){ $(this).remove(); });", 1000);
            }else{
                process.html(response.info).css("color",'red'); 
                $button.removeAttr("disabled").css("color","#000"); 
            }
        },
        function(response){
          process.html('提交出现错误！').css("color",'red');    
          $button.removeAttr("disabled").css("color","#000");   
        }
    );  
}




$Write.comment_get = function(obj){
    // page is the content of the tag
    // need give the page index of all comments, for example, current page is 4, we need staticis 5, 6, 7 and so on
    var $obj = $(obj);
    var mes = {
        "env_id": $obj.attr("env_id") || "-1",
        "env_type": $obj.attr("env_type")|| "User",
        "article_id": $obj.attr("article_id"),
        "article_type": $obj.attr("article_type") || 'blog',
        "father_id": $obj.attr("father_id"),
        "father_type": $obj.attr("father_type")    
    };
    /*
    mes['pos'] = $obj.attr("pos") || 0;
    mes['load_one'] = $obj.attr("load_one") || 'no';
    mes['before_pos'] = $obj.attr("before_pos")||mes['pos'];
    mes['load_before'] = $obj.attr("load_before")||'no';
    mes['article_type'] = $obj.attr("article_type") || 'blog';
    mes['article_id'] = $obj.attr("article_id");
    mes['env_type'] = $obj.attr("env_type")|| 'User';
    mes['env_id'] = $obj.attr("env_id") || '-1';
    */
    
    $.postJSON('/getcomment', mes,
        function(){
            // nothing will be done
        },
        function(response){
            if(response.status == 0){
                // ok
                var comment_con = '';//$('<div></div>').addClass('com_one');
                var back_info = response.info;
                var result = response.comment_list;
                var ref_result = response.ref_comment_dict;
                for(var i in result){
                    var tmp_ref_comment_list = result[i].ref_comment_list;
                    var tmp_ref_comment_body = '';
                    for(var j = 0; j < tmp_ref_comment_list.length; j++){
                        var tmp_one = result[tmp_ref_comment_list[j]] || 
                            ref_result[tmp_ref_comment_list[j]] || '';
                        if (tmp_one == '')  { 
                            tmp_ref_comment_body += '<div class="ref_comment_div">回复的原评论已经被删除！</div>'; 
                            continue;    
                        }
                        tmp_ref_comment_body += '<div class="ref_comment_div">';;
                        var tmp_tmp_body = $('<div></div>');
                        tmp_tmp_body.html(tmp_one.content);
                        var short_body = '<div class="ref_comment_short"><span class="com_body1">' + 
                                tmp_tmp_body.text().slice(0, 100 > tmp_tmp_body.text().length ? tmp_tmp_body.text().length: 100)+
                                '</span><span class="com_author1"><a href="/bloger/'+ tmp_one.author.uid +'" target="_blank">'+ tmp_one.author.name +'</a></span>'+
                                '<span class="com_open1">详细</span></div>';
                        var all_body = '<div class="ref_comment_all bb_con" style="display:none;">'+ tmp_one.content +
                                '<div class="com_nav1"><span class="com_time1">'+ tmp_one.release_time +'</span>'+
                                '<span class="com_author1"><a href="/bloger/'+ tmp_one.author.id +'">'+ tmp_one.author.name +'</a></span>'+
                                '<span class="com_close1">收起</span></div></div>';
                        tmp_ref_comment_body += short_body;
                        tmp_ref_comment_body += all_body;
                        tmp_ref_comment_body += '</div>';
                    }
                   // $.log(result[i].ref_comments);
                    comment_con += '<div class="com_one" comment_id="' + result[i].aid + '">' +
                        '<div class="com_pic"><a href="/bloger/'+ result[i].author.id +'" target="_blank">'+
                          '<img src="'+ result[i].author.thumb +'" /></a></div>'+
                            '<div class="com_body"><div class="com_con">'+
                            '<div class="bb_con1">'+ tmp_ref_comment_body + '<div class="bb_con">' + 
                            result[i].content + '</div></div>'+
                            '<div class="com_nav">'+
                            '<span class="com_reply" ref_type="comment"'+ 'father_id="'+ mes['article_id'] +'" father_type="'+mes['article_type']+'"'+
                            'ref_comment_id="'+ result[i].aid +'" pos="'+i+'" author_name="'+ result[i].author.name +'" author_id="'+result[i].author.id+'"></span>'+
                            '<span class="com_author"><a href="/bloger/'+ result[i].author.id +'" target="_blank">'+result[i].author.name+'</a></span>'+
                            //'<span class="com_time">2012-3-12 14:00</span>'+
                            '</div></div></div></div>';
                }
                //alert(comment_con);
                $b_com = $(".b_com");
                //$(".com_one").remove();
                $b_com.append(comment_con);
                /*
                var $write_zone_tag = $("#write_comment_zone");
                var $page_tag = $b_com.find('div.com_page');
                var $before_page_tag = $b_com.find('div.com_page_before');
                var before_page_html = '' ;               
                var page_html = '<div class="com_page"><span pos="'+ back_info.last_pos+'" article_id="'+ mes['article_id'] 
                    +'" article_type="'+ mes['article_type'] +'">加载更多评论...</span></div>';
                if(back_info.load_one=="yes"){
                    // load for only one comment, find the reply.
                    before_page_html =  '<div class="com_page_before">'+
                            '<span pos="0" before_pos="'+ back_info.first_pos +'" load_before="yes" article_id="'+ 
                            mes['article_id'] +'" article_type="'+mes['article_type']+'">加载之前的评论...</span>'+
                            '</div>';
                    
                    $b_com.prepend(before_page_html);
                    $b_com.append(comment_con);
                    if(back_info.len > back_info.last_pos){ $b_com.append(page_html);}
                    if($write_zone_tag.length>0)  { $write_zone_tag.clone(true).appendTo($b_com); $write_zone_tag.remove();}
                }else{
                    if(back_info.load_before=="yes"){
                         $before_page_tag.before(comment_con).remove();                
                    }else{
                        $b_com.append(comment_con);
                        if($page_tag.length>0){
                            // hava the page tag 
                            if(back_info.len > back_info.last_pos){
                                $page_tag.children("span").attr("pos", back_info.last_pos);
                                $page_tag.appendTo($b_com);
                            }else{
                               $page_tag.remove();                             
                            }
                        }else{
                            // don't have the tag
                            if(back_info.len > back_info.last_pos){
                                $b_com.append(page_html);                                
                            }
                        }                    
                    }
                    
                    if($write_zone_tag.length>0)  { $write_zone_tag.appendTo($b_com);}
                }
                $b_com.find(".com_reply").die().unbind().bind('click', function(){
                    $Write.comment_create(this);
                }).end().find(".com_page>span").die().unbind().bind('click', function(){
                    $Write.comment_get(this);
                }).end().find('div.com_page_before>span').die().unbind().bind('click', function(){
                    $Write.comment_get(this);
                    return false;
                });
                */
                $b_com.find("span.com_open1").unbind().bind('click', function(){  $(this).parent().hide().next().slideDown(); });
                $b_com.find("span.com_close1").unbind().bind('click', function(){ $(this).parent().parent().hide().prev().slideDown();  });
            }else{
                // something is wrong
            }
        },
        function(response){
            // nothing will be done
        }    
    );

}

$Write.page_control = function(current_page, id_length){
// control pages 
    current_page = parseInt(current_page);
    id_length = parseInt(id_length);
    if(id_length<=0) return [];
    
    var page_cap = 10;
    var all_page = parseInt(id_length/page_cap);
    if((id_length % page_cap) != 0 ) all_page++;
    //alert(id_length);
    //alert(all_page);
    var min_page = Math.max(current_page-3,1);//?(current_page-3):1;
    var max_page = Math.min(current_page+3,all_page);//?all_page:(current_page+3);
    if(min_page == max_page ) return [];
    //alert(id_length);
    //alert(max_page);
    return [min_page, max_page]
};

$Write.group_write_post = function(){
    var $title = $('#group_write_title');

    
    var classes = $("#group_write_class").DivToDict();
    if('classes' in classes)  classes = classes['classes'];
    else classes = [];
    
    if($title.length==0){ title_value='title'; } else{ title_value= $.trim($title.val()); };
    var $text = $('#write_textarea'), text_value=$.trim($text.val());
    var $button = $('button.self-intro-process');
    var $process = $('span.self-info-process');
    var mes = {};
    mes['classes'] = classes;
    //alert(title_value);
    if (title_value ==''){
        $process.html('请您填写标题！').css('color', 'red');
        $title.focus();
        return false;
    }
    if(text_value == ''){
        $process.html('请您填写内容！').css('color', 'red');
        $text.focus();
        return false;    
    }
    mes['title'] = title_value;
    mes['text'] = text_value;
    var $menu =  $('#write_menu');
    mes['article_type'] = $menu.attr('article_type');
    mes['article_id'] = $menu.attr('article_id');
    mes['group_id'] = $menu.attr('group_id');
    mes['edit'] = $menu.attr('edit');
    mes['father_id'] = $menu.attr('father_id');
    mes['father_type'] = $menu.attr('father_type');
    //alert(mes['group_id']);
    
    $.postJSON('/update-article', mes,
        function(){
            $process.html('<img src="/static/img/ajax.gif" />');
            $button.attr('disabled', 'disabled').css('color', '#ccc');
        },
        function(response){
            if(response.kind ==0 ){
                $process.html('操作成功！').css('color', 'blue');
                
                var next_url = '';
                switch(mes['article_type']){
                    case 'group-info':
                        next_url = '/' + 'group/' + mes['group_id'] +'/info' ;
                        break;
                    case 'group-notice':
                        next_url= '/'+'group/'+ mes['group_id'] + '/notice/' + response.info;
                        break;
                    case 'group-topic':
                        next_url = '/'+'group/' + mes['group_id'] + '/topic/'+response.info;
                        break;
                    case 'group-doc':
                        next_url = '/' + 'group/'+ mes['group_id'] +'/doc/' + response.info;
                        break;
                    case 'group-feedback':
                    default:
                        next_url = '/' + 'group/'+mes['group_id'];
                        break;                
                }
                //alert(next_url);
                $Write.close_window_close_alert();
                var restr = 'location.href="' + next_url+'"';
                setTimeout(restr, 1000);
                
            }else{
                $process.html(response.info).css('color', 'red');
                $button.removeAttr('disabled').css('color', 'black');
            }
        },
        function(response){
            $process.html('提交出现错误！').css('color', 'red');
            $button.removeAttr('disabled').css('color', 'black');
        })
}

$Write.recommend_to_book = function(obj){
    var $obj = $(obj), mes = {};
    mes['do'] = 'recommend_to_book';
    mes['article_id'] = $obj.attr("article_id");
    mes['article_type'] = $obj.attr("article_type");
    var $html = $('<div></div>');
    $html.attr({"id":"pop_insert_table"});
    var html = '<input type="hidden" name="article_id" value="'+ mes['article_id']+'" />'+
                '<input type="hidden" name="do" value="recommend_to_book" />'+
                '<input type="hidden" name="article_type" value="'+ mes['article_type'] +'" />' +
                '<p class="first">推荐到知识谱</p>'+
                '<p>很抱歉，我们在将来将提供更加自动化的操作，不过现在需要你填写具体的目录链接（具体到章节），如http://www.afewords.com/book/1/catalog/1</p>' + 
                '<p>章节链接<input type="text" name="url" autocomplete="off" /></p>'+
                '<p><span><button type="submit" id="recommend_button">推荐</button></span><span class="t_process">&nbsp;</span></p>';
    $html.html(html);
    pop_page(450,300,$html);
    $html.find('#recommend_button').click(function(){
        do_recommend(this);    
    });
    function do_recommend(obj){
        var $but = $(obj), $process =$but.parent().next('.t_process');
        var mes = $('#pop_insert_table').DivToDict();
        if(mes['url']==''){
            $process.html('章节链接不能为空！').css('color', 'red');
            return false;
        }
        var url_base = location.origin;
        var reg = new RegExp("^"+ url_base + "/book/");
        if(!reg.exec(mes['url'])){
            $process.html("章节链接错误！如:" + url_base + "/book/1/catalog/1").css('color', 'red');
            return false;
        }
        $.postJSON('/book-recommend', mes, function(){
            $process.html('<img src="/static/img/ajax.gif" />');
            $but.attr("disabled", "disabled").css('color', '#ccc');        
        },function(response){
            if(response.kind==0){
                $process.html(response.info).css('color', 'blue');
                setTimeout(pop_page_close, 1000);
            }else{
                $process.html(response.info).css('color', 'red');
                $but.removeAttr("disabled").css('color', 'black');
            }
        },function(response){
            $process.html('信息发送失败！').css('color', 'red');
            $but.removeAttr("disabled").css('color', 'black');
        })
    };

}


})(jQuery);
