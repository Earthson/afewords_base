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
            "table": {},
            "image": {},
            "reference": {},
            "math": {},
            "code": {}        
        }
        
        
        
    }






})(jQuery);