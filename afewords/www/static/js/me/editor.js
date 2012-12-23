
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
            //SEE http://www.tamasoft.co.jp/en/general-info/unicode.html
            "Greece": {
                        "name": "希腊字符",  // see  http://zh.wikipedia.org/wiki/%E5%B8%8C%E8%85%8A%E5%AD%97%E6%AF%8D
                        "exec": function(){
                                    
                                    var unicode_range = [ ["03A6", "03FF"], ["2100", "214E"]],
                                        return_list = [],
                                        ii = jj = 0,
                                        tmp_unicode = 0;
                                        
                            
                                    for(var ii = 0; ii < unicode_range.length; ii++){
                                        for(var jj = parseInt(unicode_range[ii][0], 16); jj <= parseInt(unicode_range[ii][1], 16); jj++){
                                            return_list.push( String.fromCharCode(jj));                                
                                        }                            
                                    }
                                    return return_list;
                                                   
                                }    
                     },
            "Latin": {
                        "name": "拉丁字符", // see http://zh.wikipedia.org/wiki/Unicode%E4%B8%AD%E7%9A%84%E6%8B%89%E4%B8%81%E5%AD%97%E6%AF%8D
                        "exec": function(){
                                    var unicode_range = [ ["1D00", "1DBF"], ["2100", "210F"],
                                                            ["2110", "214E"] ];   
                                    var ii = jj = 0,
                                        return_list = [];
                                    for(var ii = 0; ii < unicode_range.length; ii++){
                                        for(var jj = parseInt(unicode_range[ii][0], 16); jj <= parseInt(unicode_range[ii][1], 16); jj++){
                                            return_list.push(String.fromCharCode(jj));                                        
                                        }                                    
                                    }
                                    return return_list;                             
                            }                        
                    },
            "Alphabet":{
                        "name": "国际音标", // see http://zh.wikipedia.org/wiki/%E5%9C%8B%E9%9A%9B%E9%9F%B3%E6%A8%99
                        "exec": function(){
                                   var unicode_range = [ ["0250", "02AF"] ];   
                                   var ii = jj = 0,
                                       return_list = [];
                                   for(var ii = 0; ii < unicode_range.length; ii++){
                                       for(var jj = parseInt(unicode_range[ii][0], 16); jj <= parseInt(unicode_range[ii][1], 16); jj++){
                                           return_list.push(String.fromCharCode(jj));                                        
                                       }                                    
                                   }
                                   return return_list;     
                            }            
                        },
            "Letter": {
                    "name": "特殊符号",
                    "exec": function(){
                                    var unicode_range = [ ["25A0", "26BD"], ["2701", "2775"], ["2795", "27FF"] ];   
                                    var ii = jj = 0,
                                        return_list = [];
                                    for(var ii = 0; ii < unicode_range.length; ii++){
                                        for(var jj = parseInt(unicode_range[ii][0], 16); jj <= parseInt(unicode_range[ii][1], 16); jj++){
                                            return_list.push(String.fromCharCode(jj));                                        
                                        }                                    
                                    }
                                    return return_list;["~", "|", "¡", "¿", "†", "‡", "↔", "↑", "↓", "•", "¶", "#", 
                                "½", "⅓", "⅔", "¼", "¾", "⅛", "⅜", "⅝", "⅞", "∞", "‘", "’", 
                                "“", "”", "„", "“", "„", "”", "«", "»", "¤", "₳", "฿", "₵", 
                                "¢", "₡", "₢", "$", "₫", "₯", "€", "₠", "₣", "ƒ", "₴", "₭", 
                                                                "₤" , "ℳ", "₥", "₦","№", "₧", "₰", "£", "៛", "₨", "₪", "৳", "₮", "₩", "¥", "♠", "♣",
                                "♥", "♦", "m", "²", "m", "³", "–", "—", "…", "‘", "’", "“", 
                                "”", "°", "′", "″", "≈", "≠", "≤", "≥", "±", "−", "×", "÷", 
                                "←", "→", "·", "§"];                    
                    }    
            },
            "Number":   {
                            "name": "序号",
                            "exec": function(){
                                    var unicode_range = [ ["2776", "2783"], ["2460", "24FE"], ["2150", "216B"], ["2170", "217B"] ];   
                                    var ii = jj = 0,
                                        return_list = [];
                                    for(var ii = 0; ii < unicode_range.length; ii++){
                                        for(var jj = parseInt(unicode_range[ii][0], 16); jj <= parseInt(unicode_range[ii][1], 16); jj++){
                                            return_list.push(String.fromCharCode(jj));                                        
                                        }                                    
                                    }
                                    return return_list;                            
                            }
                    
            }
        }
            
        this.default_support_code = function (){
            return ['AS3','AppleScript','Bash','C#','ColdFusion','C++','CSS','Delphi','Diff',
                    'Erlang','Groovy', 'Go', 'JavaScript','Java','JavaFX','Lisp' ,'Perl','Php','Plain',
                    'PowerShell','Python','Ruby','Sass','Scala','SQL','VB','XML'];
        }
        
        this.default_support_markup = function(){
            return ['Default', 'Markdown'];        
        }
        
        /****** editor panel *****/
        this.default_panel = {
            "bold":         {   
                                "class": "bold", 
                                "title": "加粗", 
                                "value": '&nbsp;', 
                                "exec":  function(){
                                            var args = { "prefix":"++", "suffix":"++", "content": '加粗内容'},
                                                args_markdown = { "prefix":"**", "suffix": "**", "content": '加粗内容' },
                                                args_dict = {"default": args, "markdown": args_markdown };
                                            this.set_character(args_dict[arguments[arguments.length-1]]);
                                        },
                            },
            "italic":       {
                                "class": "italic", 
                                "title": "斜体", 
                                "value": '&nbsp;', 
                                "exec": function(markup){
                                            var args = { "prefix": "_", "suffix":"_", "content": '斜体内容'};
                                            this.set_character(args);                                
                                        }
                            },
            "underline":    {
                                "class": "underline", 
                                "title": "下划线", 
                                "value": '&nbsp;', 
                                "exec": function(markup){
                                            var args = { "prefix": "..", "allow_empty": false, "content": '下划线内容'};
                                            this.set_character(args);                                
                                        }
                            },
            "del":          {
                                "class": "del", 
                                "title": "删除线", 
                                "value": '&nbsp;', 
                                "exec": function(markup){
                                            var args = { "prefix": "--", "allow_empty": false, "content": '删除线内容' };
                                            this.set_character(args);                                
                                        }
                            },
            "super":        {
                                "class": "super", 
                                "title": "上标", 
                                "value": '&nbsp;', 
                                "exec": function(markup){
                                            var args = {"prefix": "^{", "suffix": "}", "allow_empty": false, "content": '上标内容' };
                                            this.set_character(args);                                
                                        }
                            },
            "suber":        {
                                "class": "suber", 
                                "title": "下标", 
                                "value": '&nbsp;', 
                                "exec": function(markup){
                                            var args = { "prefix": "_{", "suffix": "}", "allow_empty":false, "content": '下标内容' };
                                            this.set_character(args);                                
                                        }
                            },
            "ol":           {
                                "class": "ol", 
                                "title": "有序列表", 
                                "value": '&nbsp;', 
                                "exec": function(markup){
                                            var args = { "prefix": "\n#", "prefix_l": true, "suffix": "\n", "suffix_r": true, "content": '列表项内容' },
                                                args_markdown = { "prefix": "\n1. ", "prefix_l": true, "suffix": "\n", "suffix_r": true, "content": '列表项内容' },
                                                args_dict = {"default": args, "markdown": args_markdown};
                                            this.set_character(args_dict[arguments[arguments.length-1]]);                                
                                        }
                            },
            "ul":           {
                                "class": "ul", 
                                "title": "无序列表", 
                                "value": '&nbsp;', 
                                "exec": function(markup){
                                            var args = { "prefix": "\n+ ", "prefix_l": true, "suffix": "\n", "suffix_r": true, "content": '列表项内容' };
                                            this.set_character(args);                                
                                        }
                            },
            "separator":    {
                                "class": "part", 
                                "title": "分割线", 
                                "value": '~~', 
                                "exec": function(markup){
                                            var args = { "prefix": "", "suffix": "\n~~~~~~~~~~\n", "suffix_l": true, "allow_empty": true },
                                                args_markdown = { "prefix": "", "suffix": "\n* * *\n", "suffix_l": true, "allow_empty": true },
                                                args_dict = {"default": args, "markdown": args_markdown};
                                            this.set_character(args_dict[arguments[arguments.length-1]]);                                
                                        }
                            },
            "heading2":     {
                                "class": "title", 
                                "title": "二级标题", 
                                "value": "T<sub><small>2</small></sub>", 
                                "exec": function(markup){
                                            var args = { "prefix": "\n==", "suffix": "==\n", "suffix_r": true, "prefix_l": true, "content": '二级标题'},
                                                args_markdown = { "prefix": "\n##", "suffix": "##\n", "suffix_r": true, "prefix_l": true, "content": '二级标题'},
                                                args_dict = {"default": args, "markdown": args_markdown};
                                            //console.log(args_dict[arguments[arguments.length-1]]);
                                            this.set_character(args_dict[arguments[arguments.length-1]]);                                
                                        }
                            },
            "heading3":     {
                                "class": "title", 
                                "title": "三级标题", 
                                "value": "T<sub><small>3</small></sub>", 
                                "exec": function(){
                                            var args = { "prefix": "\n===", "suffix": "===\n", "suffix_r": true, "prefix_l": true, "content": '三级标题'},
                                                args_markdown = { "prefix": "\n###", "suffix": "###\n", "suffix_r": true, "prefix_l": true, "content": '三级标题'},
                                                args_dict = {"default": args, "markdown": args_markdown};
                                            this.set_character(args_dict[arguments[arguments.length-1]]);                                 
                                        }
                            },
            "heading4":     {
                                "class": "title", 
                                "title": "四级标题", 
                                "value": "T<sub><small>4</small></sub>", 
                                "exec": function(markup){
                                            var args = { "prefix": "\n====", "suffix": "====\n", "suffix_r": true, "prefix_l": true, "content": '四级标题'},
                                                args_markdown = { "prefix": "\n####", "suffix": "####\n", "suffix_r": true, "prefix_l": true, "content": '四级标题'},
                                                args_dict = {"default": args, "markdown": args_markdown};
                                            this.set_character(args_dict[arguments[arguments.length-1]]);                                 
                                        }
                            },
            "indent":       {
                                "class": "indent", 
                                "title": "段落缩进", 
                                "value": '&nbsp;', 
                                "exec": function(){
                                            var args = { "prefix": "\n>=", "suffix": "", "prefix_l": true, "allow_empty": true };
                                            this.set_character(args);                              
                                        }
                            },
            "table":        {
                                "class": "table", 
                                "title": "表格库", 
                                "value": '&nbsp;',
                                "exec": function(obj){ this.change_lib_bar(obj); },
                                "one_exec": function(_index_){
                                                var args = {"prefix": "", "suffix": "\n[table:" + _index_ +"]\n",
                                                            "suffix_l": true, "suffix_r": true, "allow_empty": true}
                                                this.set_character(args);                                
                                            }
                            },
            "image":        {
                                "class": "image", 
                                "title": "图片库", 
                                "value": '&nbsp;',
                                "exec": function(obj){  this.change_lib_bar(obj);  }, 
                                "one_exec": function(_index_){
                                                var args = {"prefix": "", "suffix": "\n[img:"+ _index_ +"]",
                                                            "suffix_l": true, "suffix_r": true, "allow_empty": true}
                                                this.set_character(args);                             
                                            }
                            },
            "reference":    {
                                "class": "ref", 
                                "title": "引用库", 
                                "value": '&nbsp;', 
                                "exec": function( obj ){ this.change_lib_bar(obj);  },
                                "one_exec": function(_index_){
                                                var args = {"prefix": "", "suffix": "\n[ref:"+ _index_ +"]",
                                                            "suffix_l": true, "suffix_r": true, "allow_empty": true}
                                                this.set_character(args);                              
                                            }
                            },
            "math":         {
                                "class": "math", 
                                "title": "数学式库", 
                                "value": '&nbsp;',
                                "exec": function( obj ){  this.change_lib_bar(obj);  },
                                "one_exec": function(_index_){
                                                var args = {"prefix": "", "suffix": "\n[math:"+ _index_ +"]",
                                                            "suffix_l": true, "suffix_r": true, "allow_empty": true}
                                                this.set_character(args);                              
                                            }
                            },
            "code":         {
                                "class": "code", 
                                "title": "代码库", 
                                "value": '&nbsp;',
                                "exec": function( obj ){  this.change_lib_bar(obj);  }, 
                                "one_exec": function(_index_){
                                                var args = {"prefix": "", "suffix": "\n[code:"+ _index_ +"]",
                                                            "suffix_l": true, "suffix_r": true, "allow_empty": true}
                                                this.set_character(args);   
                                            }
                            },
            "letter":       {
                                "class": "letter", 
                                "title": "特殊字符集", 
                                "value": '&nbsp;', 
                                "exec": function( obj ){ this.change_lib_bar(obj);  },
                                "one_exec": function(_unicode_){
                                                var args = {"prefix":"", "suffix": _unicode_, "allow_empty": true};
                                                this.set_character(args);                                
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
            "code":     {"id": "write_code_bar"},
            "letter":   {"id": "write_letter_bar"}        
        }
        
        this.default_editor_attrs = {
            "editor_menu_id": "write_menu",
            "editor_textarea_id": "write_textarea",
            "lib_bar": this.default_lib_bar     
        }        
        
        this.default_menu_attrs = {
            "menu_id": '1',
            "article_id": '-1',
            "article_type": 'blog',
            "env_id": '-1',
            "env_type": 'user',
            "father_id": '-1',
            "father_type": 'blog',
            "markup": "markdown",
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
                            "math": { "width": 760, "height": 380 },
                            "image": { "width": 360, "height": 240 },
                            "reference": { "width": 760, "height": 390 },
                            "code": { "width": 760, "height": 400 },
                            "table": { "width": 760, "height": 390 }
                        },
            "tip":      {
                            "math": "数学式",
                            "image": "图片",
                            "reference": "引用",
                            "code": "代码",
                            "table": "表格"            
                        }
        
        }
        
        this.default_block_html = {
        
            "src_image_lib":    '<div id="bar_nav"><div class="new src_new" title="添加新图片" src_type="image">添加</div>'+
                                '<div class="div" title="图片库">图片库</div></div><div id="bar_body"><div class="i"></div></div>',
            
            "src_math_lib":     '<div id="bar_nav"><div class="new src_new" title="添加新数学式" src_type="math">添加</div>'+
                                '<div class="div" title="数学式库">数学式库</div></div><div id="bar_body"><div id="crtm"></div></div>',
                                
            "src_code_lib":     '<div id="bar_nav"><div class="new src_new" title="添加新代码" src_type="code">添加</div>'+
                                '<div class="div" title="代码库">代码库</div></div><div id="bar_body"><div id="crtm"></div></div>',
                                
            "src_reference_lib":'<div id="bar_nav"><div class="new src_new" title="添加新引用" src_type="reference">添加</div>'+
                                '<div class="div" title="引用库">引用库</div></div><div id="bar_body"><div id="crtm"></div></div>',
            
            "src_table_lib":    '<div id="bar_nav"><div class="new src_new" title="添加新表格" src_type="table">添加</div>'+
                                '<div class="div" title="表格库">表格库</div></div><div id="bar_body"><div id="crtm"></div></div>',
            
            "src_letter_lib":   '<div id="bar_nav">'+
                                //'<span id="l1" class="lbutton" kind="word4">希腊字符</span>'+           
                                //'<span class="lbutton" kind="word1">拉丁字符</span> ' +
                                //'<span class="lbutton" kind="word2">国际音标</span>' +
                                //'<span class="lbutton" kind="word3">字符</span>' +
                                '</div>'+
                                '<div id="bar_body"><div class="l"></div></div>',
                                                            
            "src_image_one":   '<div class="one" src_alias="xx" src_type="image" style="display:none">'+
                                '<div class="ileft"><span class="ititle" id="src_view_title">图x</span></div>'+
                                '<div class="icontrol">'+
                                '<span class="idel src_del" title="删除此图片">删除</span>'+
                                '<span class="imodify src_edit">修改</span>'+
                                '<span class="iinsert src_insert">插入</span>'+
                                '</div>'+
                                '<div class="iright" title="title">'+
                                '<input type="hidden" id="src_title" />' +
                                '<table><tbody><tr><td><img id="src_path" src="/static/img/afewords-user.jpg"></td></tr></tbody></table>'+
                                '</div></div>',
                                    
            "src_math_one":     '<div class="one" src_alias="xx" src_type="math" style="display:none">'+
                                '<div><span class="cname" id="src_view_title">数式x</span></div>'+
                                '<div class="control">'+
                                '<span class="cdel src_del" title="删除">删除</span>' +
                                '<span class="cedit src_edit" title="修改">修改</span>' + 
                                '<span class="cinsert src_insert">插入</span>'+
                                '</div>'+
                                '<div>'+
                                '<span>'+
                                '<input type="text" id="src_title" readonly="readonly" value="">'+
                                '<input type="hidden" id="src_math_mode" value="display" />'+
                                '</span>'+
                                '<textarea id="src_body"></textarea>'+
                                '</div></div>',
                                
            "src_reference_one":'<div class="one" src_alias="xx" src_type="reference" style="display:none">'+
                                '<div><span class="cname" id="src_view_title">引用x</span></div>'+
                                '<div class="control">'+
                                '<span class="cdel src_del" title="删除">删除</span>'+
                                '<span class="cedit src_edit" title="修改">修改</span>'+
                                '<span class="cinsert src_insert">插入</span>'+
                                '</div>'+
                                '<div>'+
                                '<span><input type="text" id="src_title" readonly="readonly"></span>'+
                                '<input type="hidden" id="src_source" /><textarea id="src_body"></textarea>'+
                                '</div></div>',
                                
            "src_code_one":     '<div class="one" src_alias="xx" src_type="code" style="display:none">'+
                                '<div><span class="cname" id="src_view_title">代码x</span></div>'+
                                '<div class="control">'+
                                '<span class="cdel src_del" title="删除">删除</span>'+
                                '<span class="cedit src_edit" title="修改">修改</span>'+
                                '<span class="cinsert src_insert">插入</span></div>'+
                                '<div><span><input type="text" id="src_title" readonly="readonly" /></span>'+
                                '<input type="hidden" id="src_code_type" /><textarea id="src_body"></textarea>'+
                                '</div></div>',
                                
            "src_table_one":    '<div class="one" src_alias="xx" src_type="table" style="display:none">'+
                                '<div><span class="cname" id="src_view_title">表x</span></div>'+
                                '<div class="control">'+
                                '<span class="cdel src_del" title="删除">删除</span>'+
                                '<span class="cedit src_edit" title="修改">修改</span>'+
                                '<span class="cinsert src_insert">插入</span></div>'+
                                '<div><span><input type="text" id="src_title" readonly="readonly" /></span>'+
                                '<textarea id="src_body"></textarea>'+
                                '</div></div>',
            
            "init": {
                        "math": function( math_obj ){  // this must be jq object
                                        if(math_obj["do"] == "new"){
                                            math_obj["src_alias"] = math_obj["src_alias"] || math_obj["alias"] || '1';
                                            this.find("#src_view_title").html("数式" + math_obj.src_alias);
                                            this.attr("src_alias", math_obj.src_alias);
                                        }
                                        math_obj["math_mode"] = math_obj["math_mode"] || math_obj["mode"] || 'display';
                                        math_obj["title"] = math_obj["title"] || math_obj["name"] || '';

                                        this.find("#src_math_mode").val(math_obj.math_mode);
                                        this.find("#src_body").val(math_obj.body);
                                        this.find("#src_title").val(math_obj.title);                        
                                },
                        "image": function( image_obj ){
                                        if(image_obj["do"] == "new"){
                                            image_obj["src_alias"] = image_obj["src_alias"] || image_obj["alias"] || '-1';
                                            this.attr("src_alias", image_obj.src_alias);
                                            this.find("#src_view_title").html("图" + image_obj.src_alias);
                                            image_obj["img_url"] = image_obj["img_url"] || image_obj["thumb_name"] || '';
                                            this.find("#src_path").attr("src", image_obj.img_url);                                        
                                        }
                                        image_obj["title"] = image_obj["title"] || image_obj["name"] || '';
     
                                        this.find("#src_title").val(image_obj.title);                        
                                },
                        "table": function(table_obj ){
                                        if(table_obj["do"] == "new"){
                                            table_obj["src_alias"] = table_obj["src_alias"] || table_obj["alias"] || '-1';
                                            this.attr("src_alias", table_obj.src_alias);
                                            this.find("#src_view_title").html("表" + table_obj.src_alias);
                                        }
                                        table_obj["title"] = table_obj["title"] || table_obj["name"] || '';
                                        
                                        this.find("#src_title").val(table_obj.title);
                                        this.find("#src_body").val(table_obj.body);                        
                                },
                        "code": function( code_obj ){
                                        if(code_obj["do"] == "new"){
                                            code_obj["src_alias"] = code_obj["src_alias"] || code_obj["alias"] || '-1';
                                            this.attr("src_alias", code_obj.src_alias);
                                            this.find("#src_view_title").html("代码" + code_obj.src_alias);
                                        }
                                        code_obj["title"] = code_obj["title"] || code_obj["name"] || '';
                                        code_obj["code_type"] = code_obj["code_type"] || code_obj["lang"] || 'python';
                                        
                                        this.find("#src_title").val(code_obj.title);
                                        this.find("#src_body").val(code_obj.body);
                                        this.find("#src_code_type").val(code_obj.code_type);
                                },
                        "reference": function( ref_obj ){
                                        if(ref_obj["do"] == "new"){
                                            ref_obj["src_alias"] = ref_obj["src_alias"] || ref_obj["alias"] || '-1';
                                            this.attr("src_alias", ref_obj.src_alias);
                                            this.find("#src_view_title").html("引用" + ref_obj.src_alias);
                                        }
                                        ref_obj["title"] = ref_obj["title"] || ref_obj["name"] || '';
                                        ref_obj["source"] = ref_obj["source"] || ref_obj["url"] || '';
                                        
                                        this.find("#src_title").val(ref_obj.title);
                                        this.find("#src_body").val(ref_obj.body);
                                        this.find("#src_source").val(ref_obj.source);                        
                                }
                    }
                                                 
        }
        
        
        this.default_pop_page_html= function( paras ){
        
            var _self_ = this;
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
            var control_tag = paras["do"] == "new" ? "添加新" : "修改";
            //alert(control_tag);
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
            
            result_html = '<div id="pop_insert_'+ paras["src_type"] +'">' + result_html + '</div>';
            return result_html;
            
            
            
            function create_reference_pop_html(){
                return hidden_paras_html + 
                    '<p class="first">'+ control_tag +'引用 <span class="all_example" title="查看说明"><a href="/help-editor-reference" target="_blank">说明</a></span></p>'+
                    '<div style="display:block">'+
                    '<p title="设置引用的名称">名称<input type="text" name="title" autocomplete="off" value="'+ paras["title"] +'" /></p>'+
                    '<p title="出处">出处<input type="text" name="source" autocomplete="off" value="'+ paras["source"] +'" /></p>'+
                    '<p title="引用内容"><textarea name="body" autocomplete="off">'+ paras["body"] +'</textarea></p>'+
                    '<p><span><button type="submit">提交</button></span><span class="r_process" id="src_process">&nbsp;</span></p>'+
                    '</div>';
            }; 
            
            function create_table_pop_html(){
                return hidden_paras_html + 
                    '<p class="first">'+ control_tag +'表格 <span class="all_example" title="说明"><a target="_blank" href="/help-editor-table">实例</a></span></p>'+
                    '<div style="display:block">'+
                    '<p title="表格名称">表名<input type="text" name="title" autocomplete="off" value="'+ paras["title"] +'" /></p>' +
                    '<p title="表格内容"><textarea name="body" autocomplete="off">'+ paras["body"] +'</textarea></p>'+
                    '<p><span><button type="submit">提交</button></span><span class="t_process" id="src_process">&nbsp;</span></p>'+
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
                    '<p><span><button type="submit">提交</button></span><span class="m_process" id="src_process">&nbsp;</span></p>';            
            }
            
            function create_code_pop_html(){
                var code_select_html = '';
                var code_type_list = _self_.default_support_code();
                for(var ii = 0; ii < code_type_list.length; ii++){
                    if(code_type_list[ii].toLowerCase()== paras["code_type"]){
                        code_select_html += '<option selected value="' + code_type_list[ii].toLowerCase()+'">' + code_type_list[ii] +'</option>';    
                        continue;
                    }
                    code_select_html += '<option value="' + code_type_list[ii].toLowerCase()+'">' + code_type_list[ii] +'</option>'; 
                }
                
                return hidden_paras_html + 
                    '<p class="first">'+ control_tag +'代码 <span class="all_example" title="说明"><a target="_blank" href="/help-editor-code">说明</a></span></p>'+
                    '<p title="代码名称">名称<input type="text" autocomplete="off" name="title" value="'+ paras["title"] +'" /></p>'+
                    '<p title="代码种类">种类<select name="code_type">'+ code_select_html+ '</select></p>'+
                    '<p title="代码"><textarea name="body" autocomplete="off">'+ paras["body"] +'</textarea></p>'+
                    '<p><span><button type="submit">提交</button></span>'+
                    '<span class="c_process" id="src_process">&nbsp;</span></p>';            
            }
            
            function create_image_pop_html(){
                if(paras["do"] == "new"){
                    return '<p class="first">添加图片<span class="all_example" title="说明"><a target="_blank" href="/help-editor-picture">说明</a></span></p>'+
                            '<form action="/article-src-control" id="up_picture" enctype="multipart/form-data" method="post" target="up_picture_iframe">'+
                            '<input type="hidden" name="picture_type" value="article" />' +
                            '<input type="hidden" name="_xsrf" value="' + jQ.getCookie("_xsrf") + '" />'+
                            hidden_paras_html + 
                            '<p><input class="i_file" type="file" name="picture" /></p>'+
                            '<p>标题<input class="i_title" name="title" autocomplete="off" type="text" /></p>'+
                            '<p><button class="i_button" type="submit">上传图片</button>'+
                            '<span class="i_process" id="src_process">&nbsp;</span></p></form>'+
                            '<iframe id="up_picture_iframe" name="up_picture_iframe" style="display:none;"></iframe>';                
                }else{
                    return hidden_paras_html + 
                        '<p class="first">修改图片属性</p>'+
                        '<p>标题<input class="i_title" name="title" type="text"  value="'+paras["title"]+'" /></p>'+
                        '<p><span class="i_button"><button type="button">确认修改</button>'+
                        '</span><span class="i_process" id="src_process">&nbsp;</span></p>';              
                };          
            }
            
                        
        }
        
    }

    
    var Editor_Config = new AFWEditor_attrs();
    
    function Textarea(){
    
        this.textarea = null;  // must be a DOM
        this.menu = null;
        this.close_prompt = false;
        this.$lib_bars = {}; // OBJECT, key/value(JQ object)
        this.editor_config = Editor_Config;
        this.markup = "default";
        this.$markup = null;
        
        /*********************** cursor process in textarea **************************/
        this.get_position = function(){
            var s,e,range,stored_range;
            if(this.textarea.selectionStart == undefined){
                var selection = document.selection;
                if (this.textarea.nodeName.toLowerCase() != "textarea") {
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
            return this.textarea.value.substring(pos_s, pos_e);
            //this.set_position(pos_s,pos_e);
            //return this.get_position().text;
        };
        
        this.set_position = function(pos_s, pos_e){
            this.textarea.focus();
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

        
        this.set_character = function (args){
            if(typeof args != "object" || !("prefix" in args) ) return false;
            var prefix = args["prefix"],
                suffix = "suffix" in args ? args["suffix"] : prefix,
                prefix_l = args["prefix_l"] || false,
                prefix_r = args["prefix_r"] || false,
                suffix_l = args["suffix_l"] || false,
                suffix_r = args["suffix_r"] || false,
                allow_empty = args["allow_empty"] || false,
                status_info = args["status"] || "请选中文字",
                default_content = args["content"] || false;
            
            var pos = this.get_position(),
                pos_s = pos.start,
                pos_e = pos.end;

            if(!allow_empty && pos_s == pos_e){
                if(!default_content){
                    console.log(status_info);
                    return false;
                }
                prefix = prefix + default_content;
            }            
            
            if(prefix_l) {
                if( pos_s == 0 || this.get_position_string(pos_s - 1, pos_s) == "\n"){
                    prefix = prefix.replace(/^\n/, '');             
                }     
            }
            if(prefix_r) {
                if( pos_s == 0 || this.get_position_string(pos_s - 1, pos_s) == "\n"){
                    prefix = prefix.replace(/\n$/, '');                
                }            
            }
            //alert(prefix);
            if(suffix_l){
                if(pos_e == 0 || this.get_position_string(pos_e - 1, pos_e) == "\n"){
                    suffix = suffix.replace(/^\n/, '');                
                }            
            }
            if(suffix_r){
                if(pos_e == 0 || this.get_position_string(pos_e - 1, pos_e) == "\n"){
                    suffix = suffix.replace(/\n$/, '');                
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
            
            var last_pos_e = pos_e + suffix.length + prefix.length;
            this.set_position(last_pos_e, last_pos_e);
            
        } 
        
        /********************* textarea tool  *********************/
        this.div_to_dict = function( $div ){
            return $div.DivToDict();           
        }  
        
        this.window_close_prompt = function(){
            
            jQ(window).bind('beforeunload', function(){
                return '确认关闭？';
            });
            jQ(window).unload(function(){
                alert('即将关闭');
            });        
            this.close_prompt = true;
        }  
        
        this.window_close_prompt_close = function(){
            jQ(window).unbind('beforeunload');
            jQ(window).unload(function(){});
            this.close_prompt = false;
        }      
        
        this.get_src_attrs = function( paras){
            paras = paras || {};
            var _self_ = this,
                attrs = {},
                src_type = paras["src_type"] || "image",
                default_menu_attrs = _self_.editor_config.default_menu_attrs,
                default_src_attrs = _self_.editor_config.default_src_attrs;  
            
            for(var _para_ in default_menu_attrs){
                attrs[_para_] = this.$menu.attr(_para_) || default_menu_attrs[_para_];            
            }
            for(var _para_ in default_src_attrs["hidden"]){
                attrs[_para_] = paras[_para_] || default_src_attrs["hidden"][_para_];           
            }
            for(var _para_ in default_src_attrs[src_type]){
                attrs[_para_] = paras[_para_] || default_src_attrs[src_type][_para_];            
            }
            return attrs;
        }
        
        this.pop_page = function(_content_, _width_, _height_){
            /************ pop page and return the $pop_content(jQ object) ************/
            var $pop_content = pop_page(_width_, _height_, _content_) || jQ("#pop-content");
            return $pop_content;        
        }    
        
        this.pop_page_close = function(){
            pop_page_close();        
        } 
        
        this.ajax_post_json = function( url, paras, before_fun, success_fun, error_fun){
            jQ.postJSON(url, paras, before_fun, success_fun, error_fun);
        }      
        
        /********************** handle src and use ajax to send ****************************************/
        this.pop_content_bind = function( $pop_content ){
            /*************** bind the event handler to the pop page with control src *******************/
            var _self_ = this;
            $pop_content.unbind().bind("click", function(event){
                event.stopPropagation();
                var target = event.target,
                    $target = jQ(target),
                    attrs = {},
                    $this = jQ(this);
                
                if(target.nodeName != "BUTTON")  return false;
                attrs = _self_.div_to_dict($this);
                _self_.ajax_src_submit( $target, attrs, $this);
            });
        };
        
        this.ajax_src_submit = function($button, paras, $pop_content){
            /***************** use ajax send the submit, contain new/edit/remove the src ******************/
            var _self_ = this;
            var config = _self_.editor_config;
            
            var del_flag = paras["do"] == "del" || paras["do"] == "remove";
            
            if(Object.prototype.toString.call(paras) != "[object Object]")    return false;
            
            if( !del_flag ){
            
                var $process = $pop_content.find("#src_process"),
                    src_type = paras["src_type"],
                    process_tip = config.default_src_attrs["tip"][src_type];
                
                var src_type = paras["src_type"];
                
                if(!paras["title"] || paras["title"]==""){
                    $process.html("请填写" + process_tip + "名称！").css("color", "red");
                    return false;            
                }
                if(src_type == "reference"){
                    if(paras["source"] == ''){
                        $process.html("请填写" + process_tip + "出处！").css("color", "red");
                        return false;                
                    }            
                }
                
                if(paras["body"] == '' && src_type != "image"){
                    if(src_type != "reference"){
                        $process.html("请填写" + process_tip + "内容！").css("color", "red"); 
                        return false;               
                    }else{
                        var url_reg = /^(http|https|ftp):\/\/.+$/ig;
                        if(!url_reg.test(paras["source"])){
                            $process.html("请填写链接地址或者引用真实内容！").css("color","red");
                            return false;               
                        }         
                    }
                }   
            
            }
            
            var article_src_url = "/article-src-control";
            this.ajax_post_json(article_src_url, paras, 
                function(){
                
                    if( !del_flag ){
                        $process.html('<img src="/static/img/ajax.gif" />');
                        $button.attr("disabled", "disabled").css("color", "#ccc");
                    }
                    
                }, function(response){
                
                    if(response.article_isnew == 1){
                            _self_.$menu.attr("article_id", response.article_id);    
                            if(!_self_.close_prompt)  _self_.window_close_prompt();  
                    }
                    
                    if(response.status != 0){

                        if( !del_flag ){
                            $process.html(response.info).css("color", "red");
                            $button.removeAttr("disabled").css("color", "black");   
                        }else{
                            alert(response.info);                        
                        } 
                                      
                    }else{
                        // submit right
                        _self_.handle_src_right(response, paras);
                    }
                }, function(statusText){
                    if( !del_flag ){
                        $process.html("出现错误：" + statusText).css("color", "red");
                        $button.removeAttr("disabled").css("color", "black");  
                    }
                     
                }
            );
            // send the submit with ajax      
            
        }
           
        this.ajax_new_image_bind = function( $form ){
            var that  = this;
            //alert($form.html());
            $form.submit(function(){
                var $this = $(this),
                    mes = $this.DivToDict(),
                    $button = $this.find("button"),
                    $process = $button.siblings("span");
                if(!mes['picture']){ $process.html("请选择图片！").css("color", "red"); return false; }
                var img_reg = /.*\.(jpg|png|jpeg|gif)$/ig;
                if(!mes['picture'].match(img_reg)) {  $process.html('图片格式为jpg,png,jpeg,gif！').css("color", "red"); return false; }
                if(!mes['title']) { $process.html('请填写标题！').css("color", "red"); return false; }
                $process.html('<img src="/static/img/ajax.gif" />');
                $button.attr("disabled", "disabled").css("color", "#ccc");
                var $up_iframe = $this.find("iframe").eq(0);
                $up_iframe.load(function(){
                    var iframe_doc = window.frames["up_picture_iframe"].document;
                    var response_text = iframe_doc.getElementsByTagName("textarea")[0].value;
                    var response = window.eval('('+ response_text +')');
                    if(response.status != 0){
                        $process.html(response.info).css("color", "red");
                        $button.removeAttr("disabled").css("color", "black");                    
                    }else{
                        $process.html("上传成功！").css("color", "blue");
                        that.handle_src_right(response, mes);                    
                    }
                });         
                return true;
            });
     
        }        
        this.handle_src_right = function(response, paras){
            /**********the handler function after the ajax submit ************/
            var _self_ = this,
                src_type = paras["src_type"],
                $src_bar_contain = _self_.$lib_bars[src_type], 
                $src_one,
                init_funs = _self_.editor_config.default_block_html["init"];
            
            if(paras["do"] == "new"){
                // new src
                paras["src_alias"] = response.src_alias;
                if(src_type == "image"){
                    paras["img_url"] = response.img_url;            
                }
                $src_one = $src_bar_contain.find(".one").eq(0).clone();
                init_funs[src_type].call($src_one, paras);       
                if(paras['src_type'] != 'image'){
                    $src_bar_contain.find("#crtm").append($src_one.css("display", "block"));
                }else{
                    $src_bar_contain.find(".i").append($src_one.css("display", "block"));               
                }                
                $src_one.find(".src_insert").click();
                _self_.pop_page_close();
                return;
            }
            if(paras["do"] == "edit"){
                // edit src 
                $src_one = $src_bar_contain.find(".one[src_alias='" + paras["src_alias"] + "']");
                init_funs[src_type].call($src_one, paras);
                this.pop_page_close();
                return;
            }
            
                        
            if(paras["do"] == "del" || paras["do"] == "remove"){
                $src_one = $src_bar_contain.find(".one[src_alias='" + paras["src_alias"] + "']");
                $src_one.remove();
                return ;
            }
            
        }
                                      
         
        /************************************************* init ******************************/                             
        this.change_lib_bar = function( obj ){
            var $obj = jQ(obj),
                kind = $obj.attr("kind"),
                _self_ = this,
                lib_bars = _self_.$lib_bars;
            
            if(lib_bars["all"].css("display") == "none"){ 
                // open the lib
                $obj.addClass("menu_focus").siblings().removeClass("menu_focus");
                for(var lib_type in lib_bars){
                    if(lib_type == "all" || lib_type == kind )  continue;
                    lib_bars[lib_type].hide();                
                }
                lib_bars[kind].show();
                lib_bars["all"].slideDown("slow");
            }else{
                // close the bar
                if(lib_bars[kind].css("display") == "block"){  // close all the lib 
                    lib_bars["all"].slideUp("slow");
                    $obj.removeClass("menu_focus");                
                }else{
                    for(var lib_type in lib_bars){  // close one bar and open an new bar
                        if(lib_type == "all" || lib_type == kind)  continue;
                        lib_bars[lib_type].hide();               
                    }
                    lib_bars[kind].fadeIn("slow"); 
                    $obj.addClass("menu_focus").siblings().removeClass("menu_focus");    
                
                }    
            }
                  
        }        
        this.lib_bar_content_init = function(paras){
            // init content of each bar
            var _self_ = this, 
                init_funs = _self_.editor_config.default_block_html["init"],
                src_type = "image",
                src_list = [],
                $src_demo,
                $clone_demo,
                $clone_demo_list = [],
                tmp_obj,
                $lib_body,
                current_fun;

            for(src_type in paras){
                src_list = paras[src_type] || [];
                $lib_body = _self_.$lib_bars[src_type].find("#bar_body").children().eq(0);
                $src_demo = $lib_body.children().eq(0);
                current_fun = init_funs[src_type];
                for(var i = 0; i < src_list.length; i++){
                    tmp_obj = src_list[i];
                    tmp_obj["do"] = "new";
                    $clone_demo = $src_demo.clone();
                    current_fun.call($clone_demo, tmp_obj);
                    $clone_demo.css("display", "block");    
                    $lib_body.append($clone_demo);           
                }
            }            
                 
        };
                
        
        this.lib_bar_init = function(){
        
            var _self_ = this;
            if(!_self_.lib_flag["all"]) return false;
            
            // init lib bars
            var pop_size = _self_.editor_config.default_src_attrs["size"],
                bar_body_htmls = _self_.editor_config.default_block_html;
            
            for(var bar_type in _self_.lib_flag){
                if(_self_.lib_flag[bar_type] && bar_type !="all"){
                    _self_.$lib_bars[bar_type].find("#bar_body").children().eq(0).html( bar_body_htmls["src_" + bar_type + "_one"]);                
                }
            }

            
            // init math bar, code, reference, table, image bar
            jQ.fn.bind.call(_self_.$lib_bars["all"], "click", function(event){
                event.stopPropagation();
                var target = event.target,
                    $target = jQ(target),
                    attrs = {},
                    pop_html = '',
                    src_type = "image",
                    new_flag = $target.hasClass("src_new"),
                    edit_flag = $target.hasClass("src_edit"),
                    del_flag = $target.hasClass("src_del"),
                    insert_flag = $target.hasClass("src_insert"),
                    $pop_content;
                    
                if(new_flag || edit_flag || del_flag){
                    
                    if(new_flag){
                        // new a src
                        src_type = $target.attr("src_type");
                        attrs = _self_.get_src_attrs({ "src_type": src_type, "do": "new"});
                    }
                    
                    if(edit_flag)                    
                    {
                        // edit/update the src 
                        var $src_one = $target.parent().parent();
                        src_type = $src_one.attr("src_type");
                        attrs = {
                            "src_type" :  src_type || "image",
                            "src_alias": $src_one.attr("src_alias"),
                            "title": $src_one.find("#src_title").val() || '',
                            "body": $src_one.find("#src_body").val() || '',
                            "code_type" : $src_one.find("#src_code_type").val() || 'python',
                            "math_mode": $src_one.find("#src_math_mode").val() || 'display',
                            "source": $src_one.find("#src_source").val() || '',
                            "do": "edit"
                        };
                        attrs = _self_.get_src_attrs(attrs);
                    }
                    
                    if(del_flag){
                        // delete/remove the src 
                        var $src_one = $target.parent().parent();
                        src_type = $src_one.attr("src_type");
                        attrs = {
                            "src_type": src_type || "image",
                            "src_alias": $src_one.attr("src_alias"),
                            "do": "remove"                        
                        }
                        attrs = _self_.get_src_attrs(attrs);
                        _self_.ajax_src_submit(null, attrs, null );
                        return ;
                    }

                    
                    if(attrs["src_type"] == "image" && attrs["do"] == "new"){
                        // need get the form
                        pop_html = _self_.editor_config.default_pop_page_html(attrs);
                        var $pop_html = jQ(pop_html);
                        $pop_content = _self_.pop_page($pop_html, pop_size[src_type]["width"], pop_size[src_type]["height"]);
                        _self_.ajax_new_image_bind($pop_html);
                        return;                    
                    }
                    pop_html = _self_.editor_config.default_pop_page_html(attrs);
                    $pop_content = _self_.pop_page(pop_html, pop_size[src_type]["width"], pop_size[src_type]["height"]);
                    _self_.pop_content_bind($pop_content);
                    return ;
                };
                
                if(insert_flag){
                    // insert to the textarea
                    var $src_one = $target.parent().parent(),
                        src_alias = $src_one.attr("src_alias"),
                        src_type = $src_one.attr("src_type");
                        
                    _self_.editor_config.default_panel[src_type]["one_exec"].call(_self_, src_alias);
                    return;
                                        
                }
 
            });
            
        }


        this.lib_letter_bar_init = function(){
        
            if(!this.lib_flag["letter"])    return false;
            // init letter bar
            var _self_ = this;
            var letters = _self_.editor_config.default_support_characterset;
            
            var $letter_bar_nav = _self_.$lib_bars["letter"].find("#bar_nav"),
                $letter_bar_body = _self_.$lib_bars["letter"].find("#bar_body").children().eq(0);
                
            var letters_html = '', 
                letter_kind_html = '',
                current_letters;
                
            
            for(var letter_kind in letters){
                letter_kind_html += '<span class="lbutton" kind="'+ letter_kind +'">' + letters[letter_kind]["name"] + '</span>';
            }
            $letter_bar_nav.html(letter_kind_html);
            
            jQ.fn.bind.call($letter_bar_nav, "click", function(event){
                event.stopPropagation();
                var target = event.target,
                    $target = jQ(target);
                if(target.nodeName != "SPAN") return false;
                
                var kind = $target.attr("kind");
                if($target.hasClass("wsc_chosed"))  return;
                
                $target.addClass("wsc_chosed").siblings().removeClass("wsc_chosed");
                letters_html = '';
                current_letters = letters[kind]["exec"]();
                for(var ii = 0; ii < current_letters.length; ii++){
                    letters_html += '<span>' + current_letters[ii] + '</span>';          
                }
                $letter_bar_body.html(letters_html);
            });
            
            jQ.fn.bind.call($letter_bar_body, "click", function(event){
                event.stopPropagation();
                var target = event.target,
                    $target = jQ(target);
                
                if(target.nodeName != "SPAN")   return false;
                _self_.editor_config.default_panel["letter"]["one_exec"].call(_self_, $target.html());         
            });
        }
            
        this.markup_change_init = function(){
            var self = this;
            this.$markup.bind("change", function(){
                self.markup = $(this).val();
                self.$menu.attr("markup", self.markup);
                //alert(self.markup);
            });        
        };        
        
        this.lib_li_init = function(){
            var self = this,
                $editor_menu_base = this.$menu.find('ul'),
                editor_panel = self.editor_config.default_panel;
            jQ.fn.unbind.call($editor_menu_base).bind.call($editor_menu_base, "click", function(event){
                var target = event.target, $target = jQ(target);
                    if(target.nodeName != 'LI') return false;
                editor_panel[$target.attr("kind")]["exec"].call(self, target, self.markup);
            });                    
        }
                                                   
        this.init = function(args){
            // init the textarea 
            this.textarea = args["textarea"] || document.getElementById("write_textarea");  // JS Object
            this.$menu = args["menu"];   // JQ Object
            this.lib_flag = args["lib_flag"];
            this.$lib_bars = args["$lib_bars"];
            this.editor_config = args["editor_config"];
            this.$markup = args["$markup"];
            this.markup = args["markup"];
            
            var lib_bars = this.editor_config.default_lib_bar;
            this.lib_letter_bar_init();
            this.lib_bar_init();
            this.lib_li_init();
            this.markup_change_init();
            var src_dict = args["src"] || {};
            if(args["src"]){ this.window_close_prompt(); };
            this.lib_bar_content_init(src_dict);
        } 
    }


    jQ.fn.create_editor = function( paras , panel){
    
        paras = paras || {};
        
        var editor_config = Editor_Config,
            editor_id = editor_config.default_editor_attrs["editor_menu_id"],
            textarea_id = editor_config.default_editor_attrs["editor_textarea_id"],
            editor_panel = editor_config.default_panel,
            menu_attrs = editor_config.default_menu_attrs,
            markups = editor_config.default_support_markup();
        //paras["markup"] = "markdown";
            
        var tmp_default_panel  = ["bold", "italic", "underline", "del", "split",
                                    //"super", "suber", "split",
                                    "ol", "ul", "split",
                                    "separator", "heading2", "heading3", "heading4", "split",
                                    "table", "image", "reference", "code", "math", "letter" ];
        if(paras['iscomment']) tmp_default_panel.splice(tmp_default_panel.length - 7, 7);
        var panel = Object.prototype.toString.call(panel) == "[object Array]" ? panel : tmp_default_panel;
            
        var menu_paras = {};
        
        // init lib 
        var panel_string = panel.join(' ');
        var lib_flag = {
                    "table": panel_string.search(/\btable\b/) != -1 ? true: false,
                    "image": panel_string.search(/\bimage\b/) != -1 ? true: false,
                    "letter": panel_string.search(/\bletter\b/) != -1 ? true : false,
                    "math": panel_string.search(/\bmath\b/) != -1 ? true : false,
                    "code": panel_string.search(/\bcode\b/) != -1 ? true : false,
                    "reference": panel_string.search(/\breference\b/) != -1 ? true : false
            },
            lib_flag_all = lib_flag["letter"] || lib_flag["image"] || lib_flag["reference"] || 
                            lib_flag["math"] || lib_flag["table"] || lib_flag["code"];
        lib_flag["all"] = lib_flag_all;

        
        for(var _para_ in menu_attrs){
            menu_paras[_para_] = paras[_para_] || menu_attrs[_para_];
            //console.log(_para_ + '   ' + menu_paras[_para_])        
        }        
        
        var $editor_menu = jQ('<div id='+ editor_id +'></div>'),
            $editor_menu_base = jQ('<div id="write_menu_base"></div>'),
            $textarea = jQ(this[0]);
            
        
            
        $textarea.attr({"spellcheck": false, "resize": "none"});
        $editor_menu.attr(menu_paras);
        
        var editor_menu_base_html = ['<ul>'],
            tmp_html = '',
            tmp_panel = {};
        for(var ii = 0, len = panel.length ; ii < len; ii++){
            if(! panel[ii] in editor_panel){
                console.log("Not defined in panel!");
                continue;            
            }
            tmp_panel = editor_panel[panel[ii]];
            tmp_html = '<li kind="' + panel[ii] + '" class="'+ tmp_panel["class"] +'" title="'+ tmp_panel['title'] +'">'+ tmp_panel["value"] +'</li>';        
            editor_menu_base_html.push(tmp_html);        
        }
        editor_menu_base_html.push('</ul>');
        
        /*
        editor_menu_base_html.push('<select>');// for markup language select        
        for(var ii = 0, len = markups.length; ii < len; ii++){
            var current_option = '',
                current_markup = markups[ii];
            if(markups[ii].toLowerCase() != menu_paras["markup"]){
                editor_menu_base_html.push('<option value="' + current_markup.toLowerCase() + '">'+ current_markup + '</option>');
            }else{
                editor_menu_base_html.push('<option selected="selected" value="' + current_markup.toLowerCase() + '">'+ current_markup + '</option>');            
            }        
        }
        editor_menu_base_html.push('</select>');
        */
        
        $editor_menu_base.append(editor_menu_base_html.join(''));
        $editor_menu.append($editor_menu_base);
        $editor_menu.insertBefore(this);
        
        // lib bar 
        var lib_bar_ids = editor_config.default_lib_bar,
            $lib_bars = {},
            lib_bar_htmls = editor_config.default_block_html,
            tmp_key;
        
        for(var ii in lib_bar_ids){
            if(lib_flag[ii]){            
                $lib_bars[ii] = jQ('<div id="' + lib_bar_ids[ii]["id"] + '" src_type="' + ii + '" style="display:none;"></div>');          
                tmp_key = "src_" + ii + "_lib";
                if(tmp_key in lib_bar_htmls){
                    $lib_bars[ii].append(lib_bar_htmls[tmp_key]);  
                }
            }             
        }
        
        if(lib_flag["all"]){ // have lib
            for(var ii in lib_bar_ids){
                if(lib_flag[ii] && ii != "all"){
                    $lib_bars["all"].append($lib_bars[ii]);                
                }            
            }
            $editor_menu.append($lib_bars["all"]);
        }

        var self_textarea = new Textarea();
        var textarea_para = {   
                                "textarea": this[0], 
                                "panel": panel,
                                "editor_config": editor_config, 
                                "menu": $editor_menu, 
                                "src": paras["src"] || false,
                                "lib_flag": lib_flag,
                                "$lib_bars": $lib_bars,
                                "$markup": $editor_menu_base.find("select"),
                                "markup": menu_paras["markup"]
                            };

        // init the Textarea
        self_textarea.init(textarea_para);

    }

})(jQuery);
