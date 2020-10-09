<h1 align="center">AwdAttackFramwork</h1>
<p align="center">
<img src="https://img.shields.io/badge/version-2020.09.30-green.svg?longCache=true&style=for-the-badge">
<img src="https://img.shields.io/badge/license-MIT-blue.svg?longCache=true&style=for-the-badge">
</p>



## 简介
参加一个线下awd比赛(广东省信息通信行业第三届网络安全技能大赛)之前写的一个结合[burp插件copy-as-python-requests](https://github.com/portswigger/copy-as-python-requests)和[AoiAWD](https://github.com/DasSecurity-Labs/AoiAWD)和[Platypus](https://github.com/WangYihang/Platypus)的批量攻击小框架。

## 功能
| 组件                    | 版本       | 描述                |
| ----------------------- | ---------- | ------------------- |
| attack_with_burp        | 2020/09/30 | 快速构造web批量攻击 |
| attack_with_aoiawd      | 2020/09/30 | 快速构造pwn批量攻击 |
| modify_ssh_password     | 2020/09/30 | 批量修改ssh密码     |
| batch_cmd_with_platypus | 2020/09/30 | 快速管理shell       |

## 使用指南

### 准备工作

1. 克隆或[下载](https://github.com/Dawnnnnnn/AwdAttackFramework)本代码仓库
2. 本项目仅支持<strong>Python 3.6.5</strong>以上版本，不能向下兼容
3. pip安装相关依赖(pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/)
4. burp插件商店安装`copy-as-python-requests`插件(实现attack_with_burp)
5. 搭建`AoiAWD`平台(实现attack_with_aoiawd)
6. 搭建`Platypus`平台(实现batch_cmd_with_platypus)
7. 4、5、6 都是可选项，这次比赛也就只用到了4的环境...不过AoiAWD还是可以装一个，挺好用的

### 目录结构
```tree
├── READEME.md
├── batch_cmd_with_platypus
│   └── cmd_batch.py
├── config
│   └── config.py
├── framework
│   └── attack_framework.py
├── modify_ssh_password
│   ├── ssh.py
│   └── ssh.txt
├── requirements.txt
├── templates
│   ├── pwn1.txt
│   ├── pwn_exp_template.py
│   ├── web1.txt
│   └── web_exp_template.py
├── pwn1.txt
├── pwn1_exp.py
├── web1.txt
└── web1_exp.py
```

### 功能介绍

#### attack_with_burp
```
得益于burp插件的强大，我们可以直接把利用成功的payload从burp中复制出来，
只需简单修改即可使用框架进行批量攻击，具体流程参见demo.mp4
```

#### attack_with_aoiawd
```
得益于AoiAWD的Guardian模块(二进制PWN的影子外壳)，
我们可以透明记录STDIN与STDOUT的流量，
以此实现流量的重放，用别人的payload打其他人...
(主要是我们没有pwn...只能间接做题)
```

#### modify_ssh_password
```
为了抓到不改密码的队伍，可以跑一下这个，万一成功了呢....
```

#### batch_cmd_with_platypus
```
利用platypus提供的restful api实现批量执行命令
```

### 使用方法
attack_with_burp(具体流程参见demo.mp4)：
1. 新建一个web{n}_exp.py
2. 从templates中复制模板内容粘贴到web{n}_exp.py
3. 新建一个web{n}.txt，在里面填入要打的ip，同时修改web{n}_exp.py中的 target_file = "web{n}.txt"
4. 在burp中右键 copy as requests session
5. 粘贴到payload函数中
6. 删掉burp生成的requests.session，用fstring修改url，使变量ip嵌入url中
7. 处理请求的返回值(比如正则匹配flag等)/直接输出返回值

attack_with_aoiawd：
1. 新建一个pwn{n}_exp.py
2. 从templates中复制模板内容粘贴到pwn{n}_exp.py
3. 新建一个pwn{n}.txt，在里面填入要打的ip，同时修改pwn{n}_exp.py中的 target_file = "pwn{n}.txt"
4. 在payload函数中用pwntools写攻击流程...
5. 处理请求的返回值(比如正则匹配flag等)/直接输出返回值

modify_ssh_password：
1. 修改config/config.py中的参数
2. 填充modify_ssh_password/ssh.txt
3. 运行modify_ssh_password/ssh.py

batch_cmd_with_platypus：
1. 运行platypus，监听两个端口，一个收shell，一个是restful api
2. 修改config/config.py中的参数
3. 有shell后就可以直接运行cmd_batch.py了，命令参数在该文件里直接修改即可

## 鸣谢

本项目的完成离不开以下项目或团队,在此感谢：

> [burp-requests](https://github.com/silentsignal/burp-requests)

> [AoiAWD](https://github.com/DasSecurity-Labs/AoiAWD)

> [Platypus](https://github.com/WangYihang/Platypus)

> [GSE](https://game.163.com/)
