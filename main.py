##导入模块
import os	##执行系统指令
import requests	##脚本获取与更新
import rf	##读取config用
import sys	##退出用

os.system('clear')	##清屏
print('--- Simple APP Store CLI ---\n')

##检查config是否配置好
if rf.ok!=1:
	print('请打开config.yaml进行配置后再运行脚本！')
	sys.exit(0)
else:
	pass

if rf.ac==1:
	rf.clean()
else:
	pass

##检查仓库源是否为官方
if rf.src=='https://ghproxy.com/https://raw.githubusercontent.com/wzk0/repo-of-app/main/'or'https://raw.githubusercontent.com/wzk0/repo-of-app/main/':
	print('当前脚本源为：官方源')
else:
	print('当前脚本源为：其他源，不确定是否成功安装')

##检查是否安装了requests依赖
try:
	import requests
	import pyyaml
	print('已安装了相关依赖，可以通过输入 update 更新Store')
	pass
except ImportError:
	print("没有安装依赖，正在安装...")
	##根据config里的设置判断是否需要sudo
	if rf.su==1:
		os.system('sudo pip install requests')
		os.system('sudo pip install pyyaml')
	else:
		os.system('pip install pyyaml')

##get云端列表并输出
print('目前已有的应用：\n')
ls=requests.get(rf.src+'list')
print(ls.text)

##输入一个东西
分类=input('\n请先输入分类或其他已有的指令：')

##对输入进行不同的判断
if 分类=='clean':
	rf.autoclean()

if 分类=='update':
	url = "https://raw.githubusercontent.com/wzk0/app-installation-script/main/main.py" 
	rfurl='https://raw.githubusercontent.com/wzk0/app-installation-script/main/rf.py'
	r = requests.get(url)
	rr=requests.get(rfurl)
	with open('main.py', 'w') as f: 
		f.write(r.text)
	with open('rf.py', 'w') as ff: 
		ff.write(rr.text)
	print("更新完毕！")	##这是一种通过requests实现的更新方式，跟wget相比，它的好处是不会产生新文件，直接覆盖旧文件

if 分类=="工具":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root=rf.src+'%E5%B7%A5%E5%85%B7/'	##定义一个url片段
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)	##获取安装脚本并执行
	dele='rm '+name
	os.system(dele)	##执行完后把获取的脚本删除

##以下同上
if 分类=="办公":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root=rf.src+'%E5%8A%9E%E5%85%AC/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="编辑器":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root=rf.src+'%E7%BC%96%E8%BE%91%E5%99%A8/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="音频":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root=rf.src+'%E9%9F%B3%E9%A2%91/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="游戏":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root=rf.src+'%E6%B8%B8%E6%88%8F/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="浏览器":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root=rf.src+'%E6%B5%8F%E8%A7%88%E5%99%A8/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="聊天":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root=rf.src+'%E8%81%8A%E5%A4%A9/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)
