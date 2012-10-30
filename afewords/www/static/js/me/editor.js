;(function(jQ){
    "use strict";    
    
    /***** for log or print error ****/
    var console = window.console ? window.console : {
        log: jQ.noop,
        error: function (msg) {
            jQ.error(msg);
        }
    };
    
    function AFWEditor_attrs(){
        
        this.default_support_characterset = {
            "itain": []        
        }    
        this.default_support_code = function (){
            return ['AS3','AppleScript','Bash','C#','ColdFusion','C++','CSS','Delphi','Diff',
                    'Erlang','Groovy','JavaScript','Java','JavaFX','Lisp' ,'Perl','Php','Plain',
                    'PowerShell','Python','Ruby','Sass','Scala','SQL','VB','XML'];
        }
        
        /****** editor panel *****/
        this.default_panel = {
            "bold":         {   
                                "class": "bold", 
                                "title": "加粗", 
                                "value": '&nbsp;', 
                                "exec":  function(){
                                            this.set_character("++", "++");
                                        }
                            },
            "italic":       {
                                "class": "italic", 
                                "title": "斜体", 
                                "value": '&nbsp;', 
                                "exec": function(){
                                        this.set_character("--", "--");                                
                                }
                            },
            "underline":    {
                                "class": "underline", 
                                "title": "下划线", 
                                "value": '&nbsp;', 
                                "exec": function(){
                                    this.set_character("__", "__");                                
                                }
                            },
            "del":          {
                                "class": "del", 
                                "title": "删除线", 
                                "value": '&nbsp;', 
                                "exec": function(){
                                    this.set_character("--", "--");                                
                                }
                            },
            "super":        {
                                "class": "super", 
                                "title": "上标", 
                                "value": '&nbsp;', 
                                "exec": function(){
                                    this.set_character("^{", "}");                                
                                }
                            },
            "suber":        {
                                "class": "suber", 
                                "title": "下标", 
                                "value": '&nbsp;', 
                                "exec": function(){
                                    this.set_character("_{", "}");                                
                                }
                            },
            "ol":           {
                                "class": "ol", 
                                "title": "有序列表", 
                                "value": '&nbsp;', 
                                "exec": function(){
                                    this.set_character("\n#", "\n", true, false, false, true);                                
                                }
                            },
            "ul":           {
                                "class": "ul", 
                                "title": "无序列表", 
                                "value": '&nbsp;', 
                                "exec": function(){
                                    this.set_character("\n*", "\n", true, false, false, true);                                
                                }
                            },
            "separator":    {
                                "class": "part", 
                                "title": "分割线", 
                                "value": '~~', 
                                "exec": function(){
                                    this.set_character("", "\n~~~~~~~~~~\n", false, false, true, true);                                
                                }
                            },
            "heading2":     {
                                "class": "title", 
                                "title": "二级标题", 
                                "value": "T<sub><small>2</small></sub>", 
                                "exec": function(){
                                    this.set_character("\n==", "==\n", true, false, false, true);                                
                                }
                            },
            "heading3":     {
                                "class": "title", 
                                "title": "三级标题", 
                                "value": "T<sub><small>3</small></sub>", 
                                "exec": function(){
                                    this.set_character("\n===", "===\n", true, false, false, true);                                 
                                }
                            },
            "heading4":     {
                                "class": "title", 
                                "title": "四级标题", 
                                "value": "T<sub><small>4</small></sub>", 
                                "exec": function(){
                                    this.set_character("\n====", "====\n", true, false, false, true);                                  
                                }
                            },
            "indent":       {
                                "class": "indent", 
                                "title": "段落缩进", 
                                "value": '&nbsp;', 
                                "exec": function(){
                                    this.set_character("\n>=", "", true, false, false, false);                              
                                }
                            },
            "table":        {
                                "class": "table", 
                                "title": "表格库", 
                                "value": '&nbsp;', 
                                "exec": function(_index_){
                                    this.set_character("", "\n[table:" + _index_ +"]\n", false, false, true, true);                                
                                }
                            },
            "image":        {
                                "class": "image", 
                                "title": "图片库", 
                                "value": '&nbsp;', 
                                "exec": function(__index__){
                                    this.set_character("", "\n[img:"+ _index_ +"]", false, false, true, true);                                
                                }
                            },
            "reference":    {
                                "class": "ref", 
                                "title": "引用库", 
                                "value": '&nbsp;', 
                                "exec": function(_index_){
                                    this.set_character("", "\n[ref:"+ _index_ +"]", false, false, true, true);                                
                                }
                            },
            "math":         {
                                "class": "math", 
                                "title": "数学式库", 
                                "value": '&nbsp;', 
                                "exec": function(_index_){
                                    this.set_character("", "\n[math:"+ _index_ +"]", false, false, true, true);                                
                                }
                            },
            "code":         {
                                "class": "code", 
                                "title": "代码库", 
                                "value": '&nbsp;', 
                                "exec": function(_index_){
                                    this.set_character("", "\n[code:"+ _index_ +"]", false, false, true, true);
                                }
                            },
            "letter":       {
                                "class": "letter", 
                                "title": "特殊字符集", 
                                "value": '&nbsp;', 
                                "exec": function(_unicode_){
                                    this.set_character("", _unicode);                                
                                }
                            },
            "split":        {
                                "class": "split", 
                                "title": '', 
                                "value": '&nbsp;', 
                                "exec": function(){}
                            } 
        }
        
        /***** editor lib bar ****/
        this.default_lib_bar = {
            "all":      {"id": "write_lib_bar"},
            "table":    {"id": "write_table_bar"},
            "image":    {"id": "write_image_bar"},
            "reference": {"id": "write_ref_bar"},
            "math":     {"id": "write_math_bar"},
            "code":     {"id": "write_code_bar"}        
        }
        
        var menu_id = 0;
        this.get_menu_id = function(){
            return menu_id++;        
        }
        this.default_editor_attrs = {
            "editor_menu_id": "write_menu",
            "editor_textarea_id": "write_textarea",
            "lib_bar": this.default_lib_bar     
        }        
        
        this.default_menu_attrs = {
            "menu_id": this.get_menu_id(),
            "article_id": '-1',
            "article_type": 'blog',
            "env_id": '-1',
            "env_type": 'User',
            "father_id": '-1',
            "father_type": 'blog',
            "iscomment": false        
        }
        
        this.default_src_attrs = {
            "hidden":   { "do": "new", "src_type": "image", "src_alias": '-1' },
            "image":    { "picture": '', "title": '' },
            "code":     { "title": '',  "code_type": 'python', "body": ''},
            "table":    { "title": '', "body": ''},
            "math":     { "title": '', "body": '', "math_mode": 'display'},
            "reference":{ "title": '', "body": '', "source": ''},
            "size":     { 
                            "math": { "width": 450, "height": 380 },
                            "image": { "width": 360, "height": 200 },
                            "reference": { "width": 450, "height": 390 },
                            "code": { "width": 760, "height": 400 },
                            "table": { "width": 450, "height": 390 }
                        }    
        }
        
        this.default_block_html = {
             "src_image_one":   '<div class="one" oid="1" type="img">'+
                                '<div class="ileft"><span class="ititle">图1</span></div>'+
                                '<div class="icontrol">'+
                                '<span class="idel" title="删除此图片">删除</span>'+
                                '<span class="imodify">修改</span>'+
                                '<span class="iinsert">插入</span>'+
                                '</div>'+
                                '<div class="iright" title="title">'+
                                '<table><tbody><tr><td><img src=""></td></tr></tbody></table>'+
                                '</div></div>',
                                    
            "src_math_one":     '<div class="one" oid="1" type="math">'+
                                '<div><span class="cname">数式1</span></div>'+
                                '<div class="control">'+
                                '<span class="cdel" title="删除">删除</span>' +
                                '<span class="cedit" title="修改">修改</span>' + 
                                '<span class="cinsert">插入</span>'+
                                '</div>'+
                                '<div>'+
                                '<span>'+
                                '<input type="text" id="otitle" readonly="readonly" value="">'+
                                '<input type="hidden" id="math_mode" value="display" />'+
                                '</span>'+
                                '<textarea id="obody"></textarea>'+
                                '</div></div>',
                                
            "src_reference_one":'<div class="one" oid="1" type="ref">'+
                                '<div><span class="cname">引用1</span></div>'+
                                '<div class="control">'+
                                '<span class="cdel" title="删除">删除</span>'+
                                '<span class="cedit" title="修改">修改</span>'+
                                '<span class="cinsert">插入</span>'+
                                '</div>'+
                                '<div>'+
                                '<span><input type="text" id="otitle" readonly="readonly"></span>'+
                                '<input type="hidden" id="osource" /><textarea id="obody"></textarea>'+
                                '</div></div>',
                                
            "src_code_one":     '<div class="one" oid="1" type="code">'+
                                '<div><span class="cname">代码1</span></div>'+
                                '<div class="control">'+
                                '<span class="cdel" title="删除">删除</span>'+
                                '<span class="cedit" title="修改">修改</span>'+
                                '<span class="cinsert">插入</span></div>'+
                                '<div><span><input type="text" id="otitle" readonly="readonly" /></span>'+
                                '<input type="hidden" id="otype" /><textarea id="obody"></textarea>'+
                                '</div></div>',
                                
            "src_table_one":    '<div class="one" oid="1" type="table">'+
                                '<div><span class="cname">表1</span></div>'+
                                '<div class="control">'+
                                '<span class="cdel" title="删除">删除</span>'+
                                '<span class="cedit" title="修改">修改</span>'+
                                '<span class="cinsert">插入</span></div>'+
                                '<div><span><input type="text" id="otitle" readonly="readonly" /></span>'+
                                '<textarea id="obody"></textarea>'+
                                '</div></div>'
                                                 
        }
        
        
        this.default_pop_page_html= function( paras ){
            if(typeof paras != "object" ) paras = {};
            for(var _para_ in this.default_menu_attrs){
                paras[_para_] = paras[_para_] || this.default_menu_attrs[_para_];            
            }
            for(var _para_ in this.default_src_attrs["hidden"]){
                paras[_para_] = paras[_para_] || this.default_src_attrs["hidden"][_para_];            
            }
            var result_html = '';
            
            var hidden_paras_html = '';  // hidden input key(name)/value
            for(var _para_ in this.default_menu_attrs){
                hidden_paras_html += '<input type="hidden" name="'+ _para_ +'" value="'+ paras[_para_] +'" />';            
            }
            for(var _para_ in this.default_src_attrs["hidden"]){
                hidden_paras_html += '<input type="hidden" name="'+ _para_ +'" value="'+ paras[_para_] +'" />';            
            }
            
            for(var _para_ in this.default_src_attrs[ paras["src_type"] ]){ // correct the paras
                paras[_para_]  = paras[_para_]  || this.default_src_attrs[paras["src_type"]][_para_];             
            }
            switch(paras["src_type"]){
                case "img":
                case "image":
                    result_html = create_image_pop_html();
                    break;
                case "table":
                    result_html = create_table_pop_html();
                    break;
                case "code":
                    result_html = create_code_pop_html();
                    break;
                case "math":
                    result_html = create_math_pop_html();
                    break;
                case "ref":
                case "reference":
                    result_html = create_reference_pop_html();
                    break;
            }
            return result_html;
            
            var control_tag = (paras["do"] == "new" ? "添加新" : "修改");
            
            function creare_reference_pop_html(){
                return hidden_paras_html + 
                    '<p class="first">'+ control_tag +'引用 <span class="all_example" title="查看说明"><a href="/help-editor-reference" target="_blank">说明</a></span></p>'+
                    '<div style="display:block">'+
                    '<p title="设置引用的名称">名称<input type="text" name="title" autocomplete="off" value="'+ paras["title"] +'" /></p>'+
                    '<p title="出处">出处<input type="text" name="source" autocomplete="off" value="'+ paras["source"] +'" /></p>'+
                    '<p title="引用内容"><textarea name="body" autocomplete="off">'+ paras["body"] +'</textarea></p>'+
                    '<p><span><button type="submit">提交</button></span><span class="r_process">&nbsp;</span></p>'+
                    '</div>';
            }; 
            
            function create_table_pop_html(){
                return hidden_paras_html + 
                    '<p class="first">'+ control_tag +'表格 <span class="all_example" title="说明"><a target="_blank" href="/help-editor-table">实例</a></span></p>'+
                    '<div style="display:block">'+
                    '<p title="表格名称">表名<input type="text" name="title" autocomplete="off" value="'+ paras["title"] +'" /></p>' +
                    '<p title="表格内容"><textarea name="body" autocomplete="off">'+ paras["body"] +'</textarea></p>'+
                    '<p><span><button type="submit">提交</button></span><span class="t_process">&nbsp;</span></p>'+
                    '</div>';     
            }        
            
            function create_math_pop_html(){
                var math_mode_html = '';
                if(paras["math_mode"] == "display"){
                    math_mode_html = '<label><input type="radio" name="math_mode" checked="checked" value="display" />行间</label>'+
                                    '<label><input type="radio" name="math_mode" value="inline" />行内</label>';
                }else{
                    math_mode_html = '<label><input type="radio" name="math_mode" value="display" />行间</label>'+
                                    '<label><input type="radio" name="math_mode" checked="checked" value="inline" />行内</label>';
                }
                
                return hidden_paras_html +
                    '<p class="first">'+ control_tag +'数学式--<font size="12px">数学式采用latex规则</font><span class="all_example" title="说明"><a href="/help-editor-math" target="_blank">说明</a></span></p>'+
                    '<p title="设置名称">名称<input type="text" name="title" autocomplete="off" value="'+ paras["title"] +'"/></p>'+
                    '<p title="设置名称">样式'+ math_mode_html +'</p>'+
                    '<p title="数学式latex内容"><textarea resize="none" autocomplete="off" name="body">'+ paras["body"] +'</textarea></p>'+
                    '<p><span><button type="submit">提交</button></span><span class="m_process">&nbsp;</span></p>';            
            }
            
            function create_code_pop_html(){
                var code_select_html = '';
                var code_type_list = this.default_support_code();
                for(var ii = 0; ii < code_type_list.length; ii++){
                    if(code_type_list[ii].toLowerCase()== paras["code_type"]){
                        code_select_html += '<option selected value="' + code_type_list[ii].toLowerCase()+'">' + code_type_list[ii] +'</option>';    
                        continue;
                    }
                    select_html += '<option value="' + code_type_list[ii].toLowerCase()+'">' + code_type_list[ii] +'</option>'; 
                }
                
                return hidden_paras_html + 
                    '<p class="first">'+ control_tag +'代码 <span class="all_example" title="说明"><a target="_blank" href="/help-editor-code">说明</a></span></p>'+
                    '<p title="代码名称">名称<input type="text" autocomplete="off" name="title" value="'+ paras["title"] +'" /></p>'+
                    '<p title="代码种类">种类<select name="code_type">'+ code_select_html+ '</select></p>'+
                    '<p title="代码"><textarea name="body" autocomplete="off">'+ paras["body"] +'</textarea></p>'+
                    '<p><span><button type="submit">提交</button></span>'+
                    '<span class="c_process">&nbsp;</span></p>';            
            }
            
            function create_image_pop_html(){
                if(paras["do"] == "new"){
                    return '<p class="first">添加图片<span class="all_example" title="说明"><a target="_blank" href="/help-editor-picture">说明</a></span></p>'+
                            '<form action="/article-src-control" id="up_picture" enctype="multipart/form-data" method="post">'+
                            '<input type="hidden" name="picture_type" value="article" />' +
                            '<input type="hidden" name="_xsrf" value="' + jQ.getCookie("_xsrf") + '" />'+
                            hidden_paras_html + 
                            '<p><input class="i_file" type="file" name="picture" onclick=clear_process(this,"i"); /></p>'+
                            '<p>标题<input class="i_title" name="title" autocomplete="off" type="text" onfocus=clear_process(this,"i"); /></p>'+
                            '<p><span class="i_button"><button type="submit">上传图片</button>'+
                            '<button type="submit" style="display:none">提交</button></span><span class="i_process">&nbsp;</span></p></form>';                
                }else{
                    return hidden_paras_html + 
                        '<p class="first">修改图片属性</p>'+
                        '<p>标题<input class="i_title" name="title" type="text"  value="'+paras["title"]+'" /></p>'+
                        '<p><span class="i_button"><button type="button">确认修改</button>'+
                        '</span><span class="i_process">&nbsp;</span></p>';              
                };          
            }
            
                        
        }
        
    }

    
    var editor_attrs = new AFWEditor_attrs();
    
    function Textarea(){
    
        this.textarea = null;  // must be a DOM
        
        this.get_position = function(){
            var s,e,range,stored_range;
            if(this.textarea.selectionStart == undefined){
                var selection = document.selection;
                if (thistextarea.tagName.toLowerCase() != "textarea") {
                    var val = this.textarea.value;
                    range = selection.createRange().duplicate();
                    range.moveEnd("character", val.length);
                    s = (range.text == "" ? val.length:val.lastIndexOf(range.text));
                    range = selection.createRange().duplicate();
                    range.moveStart("character", -val.length);
                    e = range.text.length;
                }else {
                    range = selection.createRange();
                    stored_range = range.duplicate();
                    stored_range.moveToElementText(this.textarea);
                    stored_range.setEndPoint('EndToEnd', range);
                    s = stored_range.text.length - range.text.length;
                    e = s + range.text.length;
                }
            }else{
                s = this.textarea.selectionStart,
                e = this.textarea.selectionEnd;
            }
            var _text = this.textarea.value.substring(s,e);
            return { start:s, end:e, text:_text}
        };
        
        this.get_position_string = function( pos_s, pos_e){
            this.set_position(pos_s,pos_e);
            return this.get_position().text;
        };
        
        this.set_position = function(pos_s, pos_e){
            this.textarea.onfocus();
            if(this.textarea.setSelectionRange){
                this.textarea.setSelectionRange(pos_s, pos_e);            
            }else if(this.textarea.createTextRange()){
                var range = this.textarea.createTextRange();
                range.collapse(true);
                range.moveEnd('character', pos_s);
                range.moveStart('character', pos_e);
                range.select();            
            }
        };

        
        this.set_character = function ( prefix, suffix, prefix_l, prefix_r, suffix_l, suffix_r){
            if ( arguments.length < 2 || typeof prefix != "string" || typeof suffix != "string" )  return false;
            prefix_l = arguments[2] || false;
            prefix_r = arguments[3] || false;
            suffix_l = arguments[4] || false;
            suffix_r = arguments[5] || false;
            
            var pos = this.get_position(),
                pos_s = pos.start,
                pos_e = pos.end;
            
            if(prefix_l) {
                if( pos_s != 0 && this.get_position_string(pos_s - 1, pos) == "\n"){
                    prefix = prefix.replace(/^\\n/,'');                
                }       
            }
            if(prefix_r) {
                if( pos_s != 0 && this.get_position_string(pos_s - 1, pos) == "\n"){
                    prefix = prefix.replace(/\\n$/,'');                
                }            
            }
            
            if(suffix_l){
                if(pos_e != 0 && this.get_position_string(pos_e - 1, pos_e) == "\n"){
                    suffix = suffix.replace(/^\\n/,'');                
                }            
            }
            if(suffix_r){
                if(pos_e != 0 && this.get_position_string(pos_e - 1, pos_e) == "\n"){
                    suffix = suffix.replace(/\\n$/,'');                
                }            
            }
            
            if (document.selection) {
                this.textarea.onfocus();
                var sel = document.selection.createRange(pos_s , pos_s);
                var sel2 = document.selection.createRange(pos_e + prefix.length, pos_e + prefix.length);
                sel.text = prefix;
                sel2.text = suffix;
            }
            else{
                if (this.textarea.selectionStart || this.textarea.selectionStart == '0') {
                    this.textarea.value = this.textarea.value.substring(0, pos_s) + prefix + 
                                this.textarea.value.substring(pos_s, pos_e) + suffix + 
                                this.textarea.value.substring(pos_e, this.textarea.value.length);
                }
                else {
                    this.textarea.value += prefix;
                    this.textarea.value += suffix;
                }
            }
            this.set_position(pos_e + suffix.length + prefix.length);
            
        } 
        
        this.init = function(textarea){
            if(!textarea){
                console.error("please init textarea");
                return false;            
            }
            this.textarea = textarea;
        }
        
        

        
        
        
    }


    jQ.fn.create_editor = function( paras ){
        var editor_id = editor_attrs.default_editor_attrs["editor_menu_id"],
            textarea_id = editor_attrs.default_editor_attrs["editor_textarea_id"];
        
        var $editor_menu = $('<div></div>');
        
    }




})(jQuery);