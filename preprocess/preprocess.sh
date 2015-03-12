#!/bin/bash

# 输出text字段，即微博的内容字段．
# cat week1.csv | awk -F, '{te="";for(i=7;i<=NF-4;i++) te= te "," $i; print te;}' > text.txt

# 查找表情符号
# grep "\[[^0-9]\{1,15\}\]" text.txt

# 查找　"[//]@用户A："　这种格式
# grep "/* *@[0-9a-zA-Z]\+" text.txt

# 查找url链接
# grep "http:\/\/[0-9a-zA-Z&\/.]\+" text.txt


function extracttext{
    # 输出text字段，即微博的内容字段．
    cat $1 | awk -F, '{te="";for(i=7;i<=NF-4;i++) te= te "," $i; print te;}' > $2
}

function etl{

    # 生成一个临时文件名
    temp=$(mktemp -u tmp.XXXXXXXX)

    # 查找表情符号
    echo "删除表情符号"
    sed -e "s/\[[^0-9]\{1,15\}\]//g"  $1  > ${temp}
    mv ${temp} $1

    # 查找　"[//]@用户A："　这种格式
    echo "删除@引用"
    sed -e "s/\/* *@[0-9a-zA-Z]\+：//g"  $1  > ${temp}
    mv ${temp} $1

    # 查找url链接
    echo "删除url链接"
    sed -e "s/http:\/\/[0-9a-zA-Z&\/.]\+//g"  $1  > ${temp}
    mv ${temp} $1

}

files=$(ls --color=auto week*.csv)

for f in files;do
    newf="${f%.csv}.txt"
    extracttext "${f}" "${newf}"
    etl "${newf}"
done
