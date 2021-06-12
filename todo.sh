#!/bin/bash

# 注册到全局命令
# alias todo="sh ~/Desktop/automation/todo.sh"

function show() {
	# 展示读取的列表
	# 取用状态/完成未完成
	# 按照序列操作
	loop=1
	cat ~/.todo/main.md | while read line
	do
		echo -e "\e[2m $loop) $line \e[0m"
		#echo -e “Default \e[39mDefault”
		#echo -e "\e[1;32m Green \e[0m"
		loop=`expr $loop + 1`
	done	
	# 列出当前目录下排除git之后的所有可识别后缀的文件中的注释TODO
	# 选中TODO时使用工具打开并跳到指定行
	# echo -e "\e[1;32m Green \e[0m"
}

case $1 in
	"" | list)
		show
		;;
	add | create)
		if [ -d '~/.todo/' ]; then
			echo "todo init"
			mkdir ~/.todo/
		fi
		echo $2 >> ~/.todo/main.md
		show
		;;
	rm | del | remove | delete)
		for i in $*
		do
			case $i in
				[0-9]*)
					sed -i "${2}d" ~/.todo/main.md
					;;
			esac
		done
		show
		;;
	[0-9]*)
		sed -n "${1}p" ~/.todo/main.md
		;;
	*)
		cat <<-EOF
		**************************
		TODO version 0.1
		**************************
		1) Add
		2) Delete
		3) Copy
		4) Exit
		**************************
		EOF
		;;
esac


