import yaml
import os

config=yaml.load(open('config.yaml'),Loader=yaml.FullLoader)
pac=config['main']['pac']
su=config['main']['su']
ok=config['main']['ok']
src=config['main']['src']
ac=config['main']['ac']

def autoclean():
	deb='*.deb'
	tar='*.tar.*'
	rpm='*.rpm'
	if not os.path.exists(tar):
		print('没有检测到tar压缩包！')
	else:
		print('已下载的tar压缩包有：')
		os.system('ls *.tar.*')
	if pac=='apt':
		if not os.path.exists(deb):
			print('没有检测到.deb安装包！')
		else:
			print('已下载的.deb安装包有：')
			os.system('ls *.deb')
	else:
		if not os.path.exists(rpm):
			print('没有检测到.rpm安装包！')
		else:
			print('已下载的.rpm安装包有：')
			os.system('ls *.rpm')
	print('是否全部清理？')
	choose=input('y/n:')
	if choose=='y':
		os.system('rm -rf *.tar.*')
		if pac=='apt':
			os.system('rm -rf *.deb')
		else:
			os.system('rm -rf *.rpm')
		print('清理完毕！')	##清理不必要的文件

def clean():
	os.system('rm -rf *.tar.*')
	if pac=='apt':
		os.system('rm -rf *.deb')
	else:
		os.system('rm -rf *.rpm')