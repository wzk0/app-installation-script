import os
import requests
import rf
import sys

os.system('clear')
print('--- Simple APP Store CLI ---\n')
if rf.ok!=1:
	print('请打开config.yaml进行配置后再运行脚本！')
	sys.exit(0)
else:
	pass
print('目前已有的应用：\n')
ls=requests.get('https://ghproxy.com/https://raw.githubusercontent.com/wzk0/repo-of-app/main/list')
print(ls.text)

分类=input('\n请先输入分类：')

if 分类=="工具":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root='https://ghproxy.com/https://raw.githubusercontent.com/wzk0/repo-of-app/main/%E5%B7%A5%E5%85%B7/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="办公":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root='https://ghproxy.com/https://raw.githubusercontent.com/wzk0/repo-of-app/main/%E5%8A%9E%E5%85%AC/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="编辑器":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root='https://ghproxy.com/https://raw.githubusercontent.com/wzk0/repo-of-app/main/%E7%BC%96%E8%BE%91%E5%99%A8/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="音频":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root='https://ghproxy.com/https://raw.githubusercontent.com/wzk0/repo-of-app/main/%E9%9F%B3%E9%A2%91/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="游戏":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root='https://ghproxy.com/https://raw.githubusercontent.com/wzk0/repo-of-app/main/%E6%B8%B8%E6%88%8F/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="浏览器":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root='https://raw.githubusercontent.com//wzk0/repo-of-app/main/%E6%B5%8F%E8%A7%88%E5%99%A8/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)

if 分类=="聊天":
	name=input('请输入需要下载的应用名（注意大小写）：')
	root='https://ghproxy.com/https://raw.githubusercontent.com/wzk0/repo-of-app/main/%E8%81%8A%E5%A4%A9/'
	act='wget '+root+name+' && python3 '+name
	print('正在获取'+name+'的安装脚本...')
	os.system(act)
	dele='rm '+name
	os.system(dele)
