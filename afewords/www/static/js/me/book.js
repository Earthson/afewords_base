(function($){



$Book = jQuery.afewords.user_book;

$Book.book_tip_chose = function(obj){
    var $obj = $(obj);
    var target = $obj.attr('page');
    if(target != 'middle_book_cover' && target != 'middle_book_summary' && target != 'middle_book_catalog'
     && target != 'middle_book_topic' && target != 'middle_book_feedback' && target != 'middle_book_node')
        return false;
    if($obj.hasClass("node_top_tip")){
        $obj.siblings().removeClass('current1');
        $obj.addClass("current1");
    }else{
        $obj.parent().siblings().removeClass('current_tip1');
        $obj.parent().addClass('current_tip1');   
    }
    var $middle_right = $('#middle-book-right').children();
    var i=0, index=0, current_show=0;
    for(var i=0; i< $middle_right.length; i++){
        var $tmp = $middle_right.eq(i);
        if($tmp.hasClass(target)){
            index = i;
        }
        if($tmp.css('display') == 'block'){
            current_show = i;
        }
    }
    
    if(index != current_show){
        if(index < current_show){
            // animate to right
            $middle_right.eq(current_show).animate({ marginLeft: '1000px', opacity: 'toggle'}, 500, 'linear', function(){
                $middle_right.eq(index).animate({ marginLeft: '0px', opacity: 'toggle'}, 500, 'swing'); 
            } );
                    
        }else{
            $middle_right.eq(current_show).animate({ marginLeft: '-1000px', opacity: 'toggle'},500, 'linear', function(){
                $middle_right.eq(index).animate({ marginLeft: '0px', opacity: 'toggle'}, 500, 'swing');  
            } ); 
        }
    }
    if($obj.hasClass("node_top_tip")){
        $('#middle_node_nav').go_to_top();
        $('#middle-book-right').go_to_top($('#middle_node_nav').offset().top - 5);
    }else{
        $('#middle-book-right').go_to_top();
   }

}






$Book.add_new_book = function(obj){
    var mes = $('#group_create_table').DivToDict();
    var $but = $(obj), $process=$but.parent().next().children('.g_c_process');
    if(mes['book_name'] == ''){
        $process.html('请您填写知识谱名！').css('color', 'red');
        return false;    
    }
    if(mes['book_name'].length > 100){
        $process.html('知识谱名在100字以内！').css('color', 'red');
        return false;    
    }
    if(mes['book_summary']==''){
        $process.html('请您填写内容摘要！').css('color', 'red');
        return false;    
    }
    
    $.postJSON('/book-create', mes, function(){
        $process.html('<img src="/static/img/ajax.gif" />');
        $but.attr("disabled", "disabled").css('color', '#ccc');
    }, function(response){
        if(response.kind==0){
            $process.html("您成功创建知识谱！").css('color', 'blue');
            setTimeout("location.href='/user-book'", 1000)
        }else{
            $process.html(response.info).css('color', 'red');
            $but.removeAttr("disabled").css('color', 'black');        
        }
    }, function(response){
        $process.html("").css('color', 'red');
        $but.removeAttr("disabled").css('color', 'black');
    });
}



$('#book_create_button').click(function(){
    $Book.add_new_book(this);
});


$Book.add_new_node = function(obj){
    var $obj = $(obj);
    var book_id = $obj.attr("book_id");
    var $html = $('<div></div>');
    $html.attr({"id":"pop_insert_table","book_id":book_id});
    var html = '<input type="hidden" name="book_id" value="'+book_id+'" />'+
                '<input type="hidden" name="do" value="add_catalog" />'+
                '<p class="first">添加新目录</p>'+
                '<p>章节<input type="text" name="section" autocomplete="off" /></p>'+
                '<p>标题<input type="text" name="title" autocomplete="off" /></p>'+
                '<p><span><button type="submit" id="catalog_add_button">提交</button></span><span class="t_process">&nbsp;</span></p>';
    $html.html(html);
    pop_page(400,200,$html);
    $html.find('#catalog_add_button').click(function(){
            node_handler(this);
    });
    
    function node_handler(obj){
        var $but = $(obj), $process = $but.parent().next('.t_process');
        var mes = $('#pop_insert_table').DivToDict();
        if(mes['section']==''){
            $process.html('章节不能为空！').css('color', 'red');
            return false;
        }
        if(mes['title'] == ''){
            $process.html('标题不能为空！').css('color', 'red');
            return false;        
        }
        if(mes['section'].search(/^\d+(\.\d+)*$/gi) == -1){
            $process.html('章节不规范！请填写数字/点，如1，又如1.2').css('color', 'red');        
        }
        
        $.postJSON('/catalog-control', mes, function(){
            $process.html('<img src="/static/img/ajax.gif" />');
            $but.attr("disabled", "disabled").css('color', '#ccc');
        },function(response){
            if(response.kind==0){
                $process.html('添加成功！').css('color', 'blue');
                //alert(response.info);
                add_node_to_html(response.info, mes['section'], mes['title'])
                pop_page_close();
            }else{
                $process.html(response.info).css('color', 'red'); 
                $but.removeAttr('disabled').css('color', 'black');           
            }
        
        },function(response){
            $process.html('提交失败！').css('color', 'red'); 
            $but.removeAttr('disabled').css('color', 'black');    
        })
        // send 
    }
    function add_node_to_html(node_id, node_section, node_title){
        var $ul = $('ul.catalog_ul');
        $ul.append('<li node_id='+ node_id +'><span class="num">'+ $.encode(node_section)+
            '</span><span><a href="#">'+ $.encode(node_title) +'</a></span></li>');
        $Book.sort_all_node(true);
    }
}

$Book.edit_book_node = function(obj){
    var $obj = $(obj);
    var book_id = $('ul.catalog_ul').attr("book_id");
    var $li = $obj.parent();
    var node_id = $li.attr('node_id');
    var $node_title = $li.find('span').eq(1).children('a');
    var $node_section = $li.find('span.num');
    var node_title = $.trim($node_title.html());
    var node_section = $.trim($node_section.html());
    var $html = $('<div></div>');
    $html.attr({"id":"pop_insert_table","book_id":book_id});
    var html = '<input type="hidden" name="book_id" value="'+book_id+'" />'+
                '<input type="hidden" name="do" value="edit_catalog" />'+
                '<input type="hidden" name="node_id" value="'+ node_id +'" />' +
                '<p class="first">修改目录</p>'+
                '<p>章节<input type="text" name="section" value="'+ node_section +'" /></p>'+
                '<p>标题<input type="text" name="title" value="'+ node_title +'" /></p>'+
                '<p><span><button type="submit" id="catalog_edit_button">提交</button></span><span class="t_process">&nbsp;</span></p>';
    $html.html(html);
    pop_page(400,200,$html);
    $html.find('#catalog_edit_button').click(function(){
            node_handler(this);
    });
    
    function node_handler(obj){
        var $but = $(obj), $process = $but.parent().next('.t_process');
        var mes = $('#pop_insert_table').DivToDict();
        if(mes['section']==''){
            $process.html('章节不能为空！').css('color', 'red');
            return false;
        }
        if(mes['title'] == ''){
            $process.html('标题不能为空！').css('color', 'red');
            return false;        
        }
        if(mes['section'].search(/^\d+(\.\d+)*$/gi) == -1){
            $process.html('章节不规范！请填写数字/点，如1，又如1.2').css('color', 'red');        
        }
        
        $.postJSON('/catalog-control', mes, function(){
            $process.html('<img src="/static/img/ajax.gif" />');
            $but.attr("disabled", "disabled").css('color', '#ccc');
        },function(response){
            if(response.kind==0){
                $process.html('修改成功！').css('color', 'blue');
                //alert(mes['section']);
                //alert(node_section);
                //alert(mes['section']== node_section)
                $node_title.html($.encode(mes['title']));
                if(mes['section'] == node_section){
                    //$node_title.html($.encode(mes['title']));                           
                }else{
                    $node_section.html(mes['section']);
                    $Book.sort_all_node(true);
                }
                pop_page_close();
            }else{
                $process.html(response.info).css('color', 'red'); 
                $but.removeAttr('disabled').css('color', 'black');           
            }
        
        },function(response){
            $process.html('提交失败！').css('color', 'red'); 
            $but.removeAttr('disabled').css('color', 'black');    
        })
        // send 
    }
}

$Book.del_book_node = function(obj){
    $obj = $(obj);
    var book_id = $('ul.catalog_ul').attr('book_id');
    var $li = $obj.parent();
    var node_id = $li.attr('node_id');
    var node_section = $obj.parent().find('.num').eq(0).html();
    var mes = {};
    mes['book_id'] = book_id, mes['node_id'] = node_id, mes['do'] = 'del_catalog';
    if (confirm('确认章节' + node_section + '?')){
        $.postJSON('/catalog-control', mes, function(){
        },
        function(response){
            if(response.kind==0){
                alert('删除成功！');
                $li.remove();
                $Book.sort_all_node(true);          
            }        
        },
        function(response){})
    }
}


$Book.edit_summary = function(obj){
    var $but = $(obj), $process = $but.next('span');
    var summary = $.trim($('#write_textarea').val());
    if(summary == ''){
        $process.html('内容摘要不能为空！').css('color', 'red');
        return false;    
    }
    var mes = {}
    var $menu = $('#write_menu');
    mes['article_type'] = $menu.attr('article_type');
    mes['article_id'] = $menu.attr('article_id');
    mes['text'] = summary;
    mes['group_id'] = $menu.attr('group_id');
    
    $.postJSON('/update-article', mes, function(){
        $process.html('<img src="/static/img/ajax.gif" />');
        $but.attr("disabled", "disabled").css('color', '#ccc');    
    },function(response){
        if(response.kind ==0){
            $process.html('修改成功！<a href="/book/'+ mes['group_id'] +'?want=summary" target="_blank">预览</a>').css('color', 'blue');
            $but.removeAttr('disabled').css('color', 'black');
            //setTimeout('location.href="/book/'+mes['group_id']+'?want=summary"', 1000);      
        }else{
            $process.html(response.info).css('color', 'red');
            $but.removeAttr('disabled').css('color', 'black');
        }
    }, 
    function(response){
            $process.html('发送失败！').css('color', 'red');
            $but.removeAttr('disabled').css('color', 'black');
    });

}



$Book.sort_all_node = function(edit){
    if(arguments.length==0){
        var edit=false;    
    }
    var all_node = get_all_node();
    var html = all_node_to_html(all_node, edit);
    $('ul.catalog_ul').replaceWith($(html));
    //console.log(html);
    
    function all_node_to_html(node_list, edit){
        if( arguments.length==1) var edit=false;
        
        var nest = 1;
        var html_list = [];
        var book_id = $('ul.catalog_ul').attr('book_id');
        if(node_list.length==0)  return '<ul class="catalog" book_id="'+ book_id +'"></ul>';
        if(!edit){   html_list.push(['<ul class="catalog_ul" book_id="' + book_id+ '">']); }
        else{  html_list.push(['<ul class="catalog_ul catalog_edit1" book_id="'+ book_id +'">']); }
        for(var i in node_list){
            var tmp_one = node_list[i]
            var tmp_nest = tmp_one[1].split('.').length;
            if (tmp_nest > nest){
                html_list.push('<ul class="margin">');
                if(!edit){
                    html_list.push('<li node_id="'+ $.encode(tmp_one[0]) +'"><span class="num">'+ $.encode(tmp_one[1]) +
                            '</span><span><a href="/book/'+ book_id +'/catalog/'+ $.encode(tmp_one[0]) +'">'+ $.encode(tmp_one[2]) +'</a></span></li>');
                }else{
                    html_list.push('<li node_id="'+ $.encode(tmp_one[0]) +'"><span class="num">'+ $.encode(tmp_one[1]) +
                            '</span><span><a href="/book/'+ book_id +'/catalog/'+ $.encode(tmp_one[0]) +'">'+ $.encode(tmp_one[2]) +'</a></span>'+
                            '<span class="catalog_edit">修改</span><span class="catalog_del">删除</span></li>');
                }
                            
                nest++;            
            }else{
                if (tmp_nest == nest){
                    if(!edit){
                        html_list.push('<li node_id="'+ $.encode(tmp_one[0]) +'"><span class="num">'+ $.encode(tmp_one[1]) +
                            '</span><span><a href="/book/'+ book_id +'/catalog/'+ $.encode(tmp_one[0]) +'">'+ $.encode(tmp_one[2]) +'</a></span></li>');    
                    }else{
                        html_list.push('<li node_id="'+ $.encode(tmp_one[0]) +'"><span class="num">'+ $.encode(tmp_one[1]) +
                            '</span><span><a href="/book/'+ book_id +'/catalog/'+ $.encode(tmp_one[0]) +'">'+ $.encode(tmp_one[2]) +'</a></span>'+
                            '<span class="catalog_edit">修改</span><span class="catalog_del">删除</span></li>');                   
                    }       
                }else{
                    for(var j=0; j < nest-tmp_nest; j++){
                          html_list.push('</ul>');                 
                    }
                    if(!edit){
                        html_list.push('<li node_id="'+ $.encode(tmp_one[0]) +'"><span class="num">'+ $.encode(tmp_one[1]) +
                            '</span><span><a href="/book/'+ book_id +'/catalog/'+ $.encode(tmp_one[0]) +'">'+ $.encode(tmp_one[2]) +'</a></span></li>');
                    }else{
                        html_list.push('<li node_id="'+ $.encode(tmp_one[0]) +'"><span class="num">'+ $.encode(tmp_one[1]) +
                            '</span><span><a href="/book/'+ book_id +'/catalog/'+ $.encode(tmp_one[0]) +'">'+ $.encode(tmp_one[2]) +'</a></span>'+
                            '<span class="catalog_edit">修改</span><span class="catalog_del">删除</span></li>');                    
                    }
                    nest = tmp_nest;
                }            
            }
        }
        html_list.push('</ul>');
        return html_list.join('');
    }


    function get_all_node(){
        var $ul = $('ul.catalog_ul');
        var $li_list = $ul.find('li');
        var node_dict = {}
        var array = [], array_length=0;
        $li_list.each(function(){
            var $tmp = $(this);
            //node_dict[$tmp.attr("node_id")] = [$tmp.]
            array[array_length++] = [$tmp.attr("node_id"), 
                $.trim($tmp.find('.num').html()), $.trim($tmp.find('span').eq(1).children('a').html())];
                                /*{'node_id':$tmp.attr("node_id"), 
                                'node_section': $.trim($tmp.find('.num').html()),
                                'node_title': $.trim($tmp.find('span').eq(1).children('a').html())}; */   
        });
        function node_sort(a,b){
            var deep = 0;
            //console.log('a:' + a[1]);
            //console.log('b:' + b[1]);
            var a_list = a[1].split('.'), b_list=b[1].split('.');
            var a_nest = a_list.length, b_nest=b_list.length;
            
            function my_cmp(deep){
                a_int = parseInt(a_list[deep], 10);
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
            var result = my_cmp(0);
            //console.log('result ' + result)
            return result; 
            //return my_cmp(0);
        };
        array.sort(function(a,b){
            return node_sort(a,b);    
        });
        //console.log(array)
        return array;
    };
}
//$Book.sort_all_node();

//$Book.sort_all_node(true);

$Book.node_page_change = function(obj){
    var $obj = $(obj), $a = $obj.parent().parent().find('a');
    $a.each(function(){ $(this).removeClass("current1"); });
    $obj.addClass("current1");
    var target_page =  $obj.attr("page"), target_class = "book_node_con_" + target_page;
    if (target_page != "main" && target_page != "article" && target_page != "catalog") return false; 
    var target_collect = $('div.book_node_con').children();
    var index = 0;
    for(var i = 0; i< target_collect.length; i++){
        var $tmp = target_collect.eq(i);
        if($tmp.hasClass(target_class)){
            index = i;
            //break;        
        }else{
            if( !$tmp.hasClass("con_current0") ){
                $tmp.addClass("con_current0");            
            }       
        }
    }
    var target_obj = target_collect.eq(index);
    if(target_obj.hasClass("con_current0")) target_obj.removeClass("con_current0");
}

$Book.relation_control = function(obj){
    var $obj = $(obj), mes = {};
    mes['do'] = $obj.attr("do"), mes['book_id'] = $('ul.node_style').attr("book_id");
    mes['node_id'] = $('ul.node_style').attr("node_id"), mes['relation_id'] = $obj.attr("relation_id");
    $.postJSON('/book-recommend', mes, function(){},
        function(response){
            if(response.kind==0){
                
                if(mes['do'] == 'del_recommend'){
                    $obj.parent().parent().remove();  
                    alert('删除成功！');              
                }else{
                   alert('设置成功！');                 
                }
            }else{
                alert(response.info);            
            }
        }, 
        function(response){});
};

$Book.recommended_to_book = function(obj){
    var $obj = $(obj), book_id = $obj.attr("book_id"), node_id=$obj.attr("node_id"), want=$obj.attr("want");
    var $html = $('<div></div>');
    $html.attr({"id":"pop_insert_table"});
    var html = '<input type="hidden" name="book_id" value="'+ book_id +'" />'+
                '<input type="hidden" name="do" value="recommended_to_book" />'+
                '<input type="hidden" name="node_id" value="'+ node_id +'" />' +
                '<p class="first">推荐到该知识谱</p>'+
                //'<p>很抱歉，我们在将来将提供更加自动化的操作，不过现在需要你填写具体的文章/知识谱的链接</p>' + 
                '<p>链接<input type="text" name="url" autocomplete="off"/></p>'+
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
            $process.html('链接不能为空！').css('color', 'red');
            return false;
        }
        var url_base = location.origin;
        var reg = new RegExp("^"+ url_base + "/blog/");
        var reg_book = new RegExp("^" + url_base + "/book/");
        if(want=="catalog"){
            if(!reg_book.exec(mes['url'])){
                $process.html("链接错误！如:" + url_base + "/book/1").css('color', 'red');
                return false;
            }
        }else{
            if(!reg.exec(mes['url'])){
                $process.html("链接错误！如:" + url_base + "/blog/1").css('color', 'red');
                return false;
            }
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


$('div.book_node_con_recommend').find('a').click(function(){
    $Book.recommended_to_book(this);
});

$('span.del_article').find('a').click(function(){
    $Book.relation_control(this);   
});

$('span.mark_article').find('a').click(function(){
    $Book.relation_control(this);   
});

$('div.book_catalog_add').live('click',function(){
    $Book.add_new_node(this);
});

$('span.catalog_edit').live('click',function(){
    $Book.edit_book_node(this);
});

$('span.catalog_del').live('click',function(){
    $Book.del_book_node(this);
});

$('button.self-intro-button').click(function(){
    $Book.edit_summary(this);
});


$('div.book_node_nav').find('a').click(function(){
    $Book.node_page_change(this);
});

/*
$('div.book_tip').find('span').click(function(){
    $Book.book_tip_chose(this);
});

$('#middle_node_nav').find('span').click(function(){
    $Book.book_tip_chose(this);
});
*/


/*
(function(){
    function ww(){
        $('#middle-book-left').fix_to_head(20);
        $('#middle_node_nav').fix_to_head(1);
    }
    setTimeout(ww, 500);
})();
*/

})(jQuery);