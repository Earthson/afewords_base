;(function(jQ){
    "use strict";    
    
    /***** for log or print error ****/
    var console = window.console ? window.console : {
        log: jQ.noop,
        error: function (msg) {
            jQ.error(msg);
        }
    };
    
    function AFWEditor(){
        
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
            "bold":         {"class": "bold", "title": "加粗", "value": '&nbsp;'},
            "italic":       {"class": "italic", "title": "斜体", "value": '&nbsp;'},
            "underline":    {"class": "underline", "title": "下划线", "value": '&nbsp;'},
            "del":          {"class": "del", "title": "删除线", "value": '&nbsp;'},
            "super":        {"class": "super", "title": "上标", "value": '&nbsp;'},
            "suber":        {"class": "suber", "title": "下标", "value": '&nbsp;'},
            "ol":           {"class": "ol", "title": "有序列表", "value": '&nbsp;'},
            "ul":           {"class": "ul", "title": "无序列表", "value": '&nbsp;'},
            "separator":    {"class": "part", "title": "分割线", "value": '~~'},
            "heading2":     {"class": "title", "title": "二级标题", "value": "T<sub><small>2</small></sub>"},
            "heading3":     {"class": "title", "title": "三级标题", "value": "T<sub><small>3</small></sub>"},
            "heading4":     {"class": "title", "title": "四级标题", "value": "T<sub><small>4</small></sub>"},
            "indent":       {"class": "indent", "title": "段落缩进", "value": '&nbsp;'},
            "table":        {"class": "table", "title": "表格库", "value": '&nbsp;'},
            "image":        {"class": "image", "title": "图片库", "value": '&nbsp;'},
            "reference":    {"class": "ref", "title": "引用库", "value": '&nbsp;'},
            "math":         {"class": "math", "title": "数学式库", "value": '&nbsp;'},
            "code":         {"class": "code", "title": "代码库", "value": '&nbsp;'},
            "letter":       {"class": "letter", "title": "特殊字符集", "value": '&nbsp;'},
            "split":        {"class": "split", "title": '', "value": '&nbsp;'} 
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
            "reference":{ "title": '', "body": '', "source": ''}     
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
        
        
        this.default_pop_page_html: function( paras ){
            if(typeof paras != "object" ) paras = {};
                        
        }
        
        
        
        

        
        
        
    }






})(jQuery);