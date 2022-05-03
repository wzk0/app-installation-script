## Linux应用安装脚本集合

> 集中Linux应用安装过程中的指令以实现懒人式快速安装。

PS：长期未维护脚本库，有些软件版本会变老，同时也有部分软件未测试。如发现问题，请提Issues！

## Why？

自从切换使用Linux后，就觉得每次到网上搜索安装教程比较费事；

同时，安装步骤有时候五花八门，更是雪上加霜，还容易把源搞坏。

所以，我制作了这个类似应用商店的东西，

并花费了一下午的时间，从列表中所有软件的官网找到了不同系统的安装方式；

然后把一些步骤集合起来，又加上了一些中文说明（如果可能的话）：

做好了这个零技术含量但是工作量比较大的东西。

## How？

前提是需要安装`python3，git，python3-pip`:

```
sudo apt install python3-pip git -y
```

接着clone仓库：

```git
git clone https://github.com/wzk0/app-installation-script
```

随后编辑`config.yaml`：

```yaml
##感谢使用！

main:
  pac: apt      ##在此输入包管理器的全称，例如 apt、yum等；强烈建议使用Debian系的系统，因为软件相对而言比较全；
  su: 1     ##如果为1， 则执行安装时会以sudo执行；其他值则说明无需sudo；
  src: https://ghproxy.com/https://raw.githubusercontent.com/wzk0/repo-of-app/main/     ##这里填脚本源，可以填入自己fork的仓库地址；
  ac: 2     ##如果为1，则会在每一次启动脚本时清理不必要文件；
  ok: 2     ##如果为1，则说明配置完成；其他值则说明没有完成配置。
```

只需在配置完成后，把ok改为1，然后执行`python3 main.py`即可。

> 注意：需要`requests`模块以获取安装脚本；这个依赖好像默认安装了。

## About

为了方便及时更新和修复错误，以及添加与删除软件，同时也为了节省空间，我把实际进行安装的脚本放在了另一个仓库： https://github.com/wzk0/repo-of-app ，超级希望大家可以归纳贡献（pr）自己安装过程中的步骤，说明一些可能的坑，以及分享更好的软件，从而让Linux得到更好的推广！（说得有点大。。）

（如果你是社恐，也可以考虑私发我单文件，联系方式什么的在博客里！）

另外，安装脚本几乎全部考虑了不同系统的安装方式，以及是否拥有sudo权限，只需要在`config.yaml`中设置即可；但是还是推荐大家使用Debian系的系统，能保证列表中所有软件的安装。

> PS：Chrome和WPS-Office的下载需要打开网页验证，目前不知道怎么搞，或许可以用releases的方式。

## List

目前已有的软件：

```
.
├── 办公
│   ├── 钉钉
│   ├── Joplin
│   ├── Typora
│   └── WPS-Office
├── 编辑器
│   ├── Sublime-Text
│   └── VS-Code
├── 工具
│   ├── 阿里云盘
│   ├── 搜狗输入法
│   ├── Clash
│   └── PicGo
├── 开发
├── 聊天
│   ├── Discord
│   ├── QQ
│   └── Telegram
├── 浏览器
│   ├── Brave
│   ├── Chrome
│   ├── Firefox
│   └── Vivaldi
├── 视频
├── 图形
├── 音频
│   ├── 网易云音乐
│   ├── Harmony
│   ├── Spotify
│   └── YesPlayMusic
├── 游戏
└   └── Steam
```

准备添加的软件：

* ~~yesplay music~~ 完成
* ~~picgo~~ 完成
* ~~阿里云小白羊~~ 完成
* ~~搜狗输入法~~ 完成
* ...

额外的指令：

* `update` - 更新Store
* `clean `- 清除不必要文件

## END

感谢watching的你，一起来写写吧！
