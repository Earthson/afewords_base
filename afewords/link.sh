#!/bin/bash

current_path=`pwd`

link_img_src=(static/avatar static/logo static/picture)
link_js_src=(static/js/MathJax static/js/code static/js/jq)
link_css_src=(static/css/code)

link_img_dst=(www/static/avatar www/static/logo www/static/picture)
link_js_dst=(www/static/js/MathJax www/static/js/code www/static/js/jq)
link_css_dst=(www/static/css/code)

link_js_dir_fun (){
    echo "++++++++++ Create js file softlink ++++++++++"
    array_src=( "${link_js_src[@]}" )
    array_dst=( "${link_js_dst[@]}" )
    if [ ${#array_src[@]} != ${#array_dst[@]} ]
    then
        echo 'Error: two array have two length, not same'
        return 0
    else
        for((i=0;i<${#array_src[@]};i++))
        do
            tmp_src="$current_path/${array_src[$i]}"
            tmp_dst="$current_path/${array_dst[$i]}"
            if [ -d $tmp_src ]
            then
                if [ -d $tmp_dst ]
                then
                    echo "Error: $tmp_dst Softlink aready exist"
                else
                    ln -s $tmp_src $tmp_dst
                    echo "Info:  Softlink $tmp_dst create ok!"
                fi
            else
                echo "Error: the Src file $tmp_src not exist"
            fi      
        done
    fi
}


link_img_dir_fun (){
    echo "++++++++++ Create image file softlink ++++++++++"
    array_src=( "${link_img_src[@]}" )
    array_dst=( "${link_img_dst[@]}" )
    if [ ${#array_src[@]} != ${#array_dst[@]} ]
    then
        echo 'Error: two array have two length, not same'
        return 0
    else
        for((i=0;i<${#array_src[@]};i++))
        do
            tmp_src="$current_path/${array_src[$i]}"
            tmp_dst="$current_path/${array_dst[$i]}"
            if [ -d $tmp_src ]
            then
                if [ -d $tmp_dst ]
                then
                    echo "Error: $tmp_dst Softlink aready exist"
                else
                    ln -s $tmp_src $tmp_dst
                    echo "Info:  Softlink $tmp_dst create ok!"
                fi
            else
                echo "Error: the Src file $tmp_src not exist"
            fi      
        done
    fi
}


link_css_dir_fun (){
    echo "++++++++++ Create css file softlink ++++++++++"
    array_src=( "${link_css_src[@]}" )
    array_dst=( "${link_css_dst[@]}" )
    if [ ${#array_src[@]} != ${#array_dst[@]} ]
    then
        echo 'Error: two array have two length, not same'
        return 0
    else
        for((i=0;i<${#array_src[@]};i++))
        do
            tmp_src="$current_path/${array_src[$i]}"
            tmp_dst="$current_path/${array_dst[$i]}"
            if [ -d $tmp_src ]
            then
                if [ -d $tmp_dst ]
                then
                    echo "Error: $tmp_dst Softlink aready exist"
                else
                    ln -s $tmp_src $tmp_dst
                    echo "Info:  Softlink $tmp_dst create ok!"
                fi
            else
                echo "Error: the Src file $tmp_src not exist"
            fi      
        done
    fi
}

echo -e "\n"
link_js_dir_fun
echo -e "\n"
link_img_dir_fun
echo -e "\n"
link_css_dir_fun
echo -e "\n"

