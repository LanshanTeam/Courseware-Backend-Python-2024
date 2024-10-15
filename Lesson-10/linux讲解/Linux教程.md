# Linux教程
## 一、操作系统

操作系统：就是一个控制程序，是由硬件和软件组成；操作系统也是系统资源的管理者。处于应用程序和硬件之间的位置。

### 1、操作系统的结构

#### 1.1 操作系统特征

现代操作系统都支持多任务，具有并发、共享、异步和虚拟特征

```
并发：多任务操作
共享：系统中的资源可以提供给多个并发执行的进程共同使用
虚拟：常用内存的虚拟化，让用户感觉内存大于实际内存
异步：让程序不出现挂起的状态，进程的执行速度是不可预估的。
```

#### 1.2 操作系统的功能

给用户提供接口

```
1、命令接口
2、图形用户接口
3、程序接口
```

管理计算机资源

```
1、进程管理
	决定进程的执行顺序，通过操作系统提供的进程调度算法决定进程执行顺序
2、内存管理
	给程序分配内存空间，提高内存的使用效率
3、设备管理
	设备分配：程序进行I/O
4、文件管理
	给每个文件分配空间，建立目录
	对文件的读写操作进行管理
```

## 二、Linux操作系统

> 常用的Linux服务器就是一台没有用户界面的电脑！

Linux内核版、发行版

```
Linux 内核版
	内核就是操作系统的核心
	
Linux 发行版
	包含了桌面环境，办公软件 ， centos7 ， Ubuntu ， redhat
```

使用 VMware 配置 centos7 操作系统

![142RAO1-4](image.assets/142RAO1-4.jpg)

1、直接使用 centos 镜像压缩包[操作系统已经配置好的]，解压之后就可以使用[解压的路径中不要有中文]，在 vmware 中中选择打开即可。

2、使用 centos 镜像的配置进入centos 的终端

```
终端调整大小
放大： ctrl shift +
缩小： ctrl -
```

### 1、Linux的诞生

Linux 是一个开源的类 Unix 操作系统内核，最初由林纳斯·托瓦兹（Linus Torvalds）在1991年开发。：

1. **起源**：Linux 的诞生是开源软件运动的一个重要里程碑。在1991年，林纳斯·托瓦兹在赫尔辛基大学学习计算机科学时，出于对操作系统的兴趣，开始编写自己的操作系统内核。
2. **初衷**：林纳斯最初的目的并不是要创建一个全新的操作系统，而是想要一个能够运行在他个人电脑上的 Unix 系统。由于当时 Unix 系统是商业软件，价格昂贵，他决定自己编写一个内核。
3. **开源**：Linux 内核的源代码在发布时就遵循了开源许可证，允许任何人自由使用、修改和分发。这种开放性吸引了全球的程序员参与到 Linux 的开发中来，形成了一个庞大的社区。
4. **发展**：随着时间的推移，Linux 内核不断得到改进和扩展，支持更多的硬件和软件。它逐渐成为了一个功能强大、稳定可靠的操作系统内核，被广泛应用于服务器、桌面、移动设备和嵌入式系统等领域。
5. **发行版**：虽然 Linux 内核本身是免费的，但为了提供完整的操作系统，出现了许多基于 Linux 内核的发行版，如 Ubuntu、Fedora、Debian、Red Hat Enterprise Linux 等。这些发行版提供了用户友好的界面、软件包管理和额外的软件支持。
6. **影响**：Linux 的诞生对整个软件行业产生了深远的影响，它不仅推动了开源软件的发展，还促进了技术创新和协作。Linux 也成为了许多现代技术的基础，比如 Android 操作系统就是基于 Linux 内核的。

Linux 的成功证明了开源模式的强大潜力，它允许全球的开发者共同协作，创造出高质量、可靠的软件产品。

### 2、Linux的特点

Linux 操作系统具有许多独特的特点，这些特点使其在不同的应用场景中受到青睐。以下是 Linux 的一些主要特点：

1. **开源**：Linux 内核是开源的，这意味着任何人都可以查看、修改和重新分发源代码，这促进了广泛的社区参与和创新。
2. **多用户多任务**：Linux 支持多用户同时使用系统，并且能够同时运行多个任务，这对于服务器和多任务工作环境非常有用。
3. **稳定性和安全性**：Linux 通常被认为是非常稳定和安全的操作系统，适合长时间运行的服务器和关键任务。
4. **灵活性和可定制性**：Linux 提供了高度的灵活性和可定制性，用户可以根据自己的需求调整系统配置。
5. **跨平台**：Linux 可以在多种硬件平台上运行，包括个人电脑、服务器、移动设备和嵌入式系统。
6. **丰富的软件库**：Linux 拥有庞大的软件库，包括开源和商业软件，用户可以根据自己的需要选择和安装。
7. **命令行界面**：Linux 提供了强大的命令行界面（CLI），这对于自动化任务和高级用户非常有用。
8. **图形用户界面**：大多数 Linux 发行版也提供了图形用户界面（GUI），如 GNOME、KDE Plasma、XFCE 等，使得用户界面更加友好。
9. **文件系统**：Linux 支持多种文件系统，包括但不限于 ext4、XFS、Btrfs、NTFS 等，这为用户提供了灵活性。
10. **网络功能**：Linux 提供了强大的网络功能，包括对各种网络协议的支持，使其成为网络服务器和网络管理的理想选择。
11. **安全性**：Linux 提供了多种安全特性，如 SELinux、AppArmor 等，这些可以帮助保护系统免受未授权访问和攻击。
12. **社区支持**：Linux 拥有一个活跃的社区，用户可以从社区获得帮助、支持和资源。
13. **成本效益**：大多数 Linux 发行版是免费的，这使得它们对于预算有限的用户或企业来说非常有吸引力。
14. **易于维护**：Linux 的维护相对简单，系统更新和软件包管理通常可以通过包管理器轻松完成。
15. **可伸缩性**：Linux 可以从小型嵌入式系统到大型超级计算机，都能提供良好的性能和稳定性。

### 3、Linux与Windows的区别

Linux 和 Windows 是两种流行的操作系统，它们在多个方面有着显著的区别：

1. **开源与闭源**：
   - **Linux**：Linux 内核是开源的，这意味着任何人都可以查看、修改和重新分发源代码，通常遵循 GNU 通用公共许可证（GPL）或其他开源许可证。
   - **Windows**：Windows 是微软公司的闭源产品，用户不能查看或修改其源代码。
2. **成本**：
   - **Linux**：大多数 Linux 发行版是免费的，用户可以免费下载和使用。
   - **Windows**：Windows 是商业软件，通常需要购买许可证才能使用。
3. **用户界面**：
   - **Linux**：Linux 发行版通常提供命令行界面（CLI）和图形用户界面（GUI），用户可以根据自己的喜好选择使用。
   - **Windows**：Windows 主要使用图形用户界面，它提供了直观的菜单和图标，适合大多数用户。
4. **兼容性**：
   - **Linux**：Linux 通常与开源软件和应用程序兼容，但对于一些专有软件可能需要额外的配置或使用兼容层（如 Wine）。
   - **Windows**：Windows 拥有广泛的软件和硬件兼容性，特别是对于商业和游戏软件。
5. **安全性**：
   - **Linux**：由于其开源特性，Linux 通常被认为更安全，因为安全漏洞可以迅速被社区发现和修复。然而，由于用户基数较小，针对 Linux 的病毒和恶意软件也较少。
   - **Windows**：Windows 由于其广泛的用户基础，经常成为病毒和恶意软件的目标。尽管微软提供了安全更新，但用户需要保持警惕并定期更新系统。
6. **定制性**：
   - **Linux**：Linux 提供了高度的定制性，用户可以根据自己的需求定制系统。
   - **Windows**：Windows 的定制性相对较低，用户主要通过设置和应用程序来个性化系统。
7. **系统稳定性**：
   - **Linux**：Linux 通常被认为非常稳定，适合长时间运行的服务器和任务。
   - **Windows**：Windows 也可以非常稳定，但有时可能会遇到蓝屏错误或其他系统问题。
8. **社区支持**：
   - **Linux**：Linux 拥有一个庞大的社区，用户可以从社区获得帮助和支持。
   - **Windows**：Windows 由微软提供官方支持，同时也有大量的第三方资源和社区。
9. **硬件支持**：
   - **Linux**：Linux 通常能够很好地支持各种硬件，尤其是在服务器和嵌入式设备上。
   - **Windows**：Windows 通常对新硬件有很好的支持，但某些老旧或特殊的硬件可能需要额外的驱动程序。
10. **用途**：
    - **Linux**：Linux 常用于服务器、嵌入式系统、开发环境和高级用户。
    - **Windows**：Windows 适用于个人电脑、企业环境、游戏和日常使用。

## 三、Linux 常用命令

```shell
[zzt@localhost ~]$ 

zzt: 当前登录的用户
localhost：主机名
~ 表示用户当前目录
$ 表示普通用户
# 表示管理员
```

```
切换到 root 身份：su
退出： exit
```

```shell
ifconfig: 查询 ip 地址
cd 目录名称/目录路径：切换目录，打开目录
ls： 查询当前所在目录中的所有文件
```

Linux 目录

```
/: 根目录
bin：可执行的二进制文件
sbin：存放执行文件，只有root用户可以访问
boot：存放的是Linux启动需要的文件
etc：存放操作系统的配置文件，不建议在这个目录中存放可执行文件
dev：存放的是Linux系统的设备文件
home：系统用户目录
lib：存放文件系统运行时需要的模块文件
opt：给需要安装软件的存放位置
root：系统管理员的目录
tmp：存放临时文件
usr：存放共享的系统资源
```

### 1、pwd

pwd：查看当前所在目录的路径

```shell
[ac@localhost ~]$ pwd
/home/ac
```

### 2、mkdir

mkdir：创建目录

```shell
mkdir  目录名称

[ac@localhost ~]$ mkdir linux
[ac@localhost ~]$ ls
linux  公共  模板  视频  图片  文档  下载  音乐  桌面
```

### 3、touch

touch：创建文件

```shell
[ac@localhost linux]$ touch demo.txt
[ac@localhost linux]$ ls
demo.txt
```

### 4、rmdir

rmdir：删除目录(目录必须为空)

```shell
[ac@localhost ~]$ rmdir linux/
rmdir: 删除 "linux/" 失败: 目录非空
[ac@localhost ~]$ mkdir dd
[ac@localhost ~]$ rmdir dd
```

### 5、rm

rm：删除文件

```shell
rm [选项] 文件名称

-f: 强制删除
-i: 在删除文件之前会有提示是否要删除(y/n)

[ac@localhost linux]$ rm -i demo.txt 
rm：是否删除普通空文件 "demo.txt"？n
```

### 6、cat

cat：查看文件中的内容

```shell
cat [选项] 文件名

-n : 返回内容的时候会显示行号
-A ： 返回内容的时候不显示行号

[ac@localhost linux]$ cat demo.txt 
hello
ac
阿宸
是个帅哥
linux
django
python
[ac@localhost linux]$ cat -n demo.txt 
     1	hello
     2	ac
     3	linux
     4	django
     5	python
```

### 7、stat

stat：查询文件的详细信息 ， 以及文件的修改时间

```shell
[ac@localhost linux]$ stat demo.txt 
  文件："demo.txt"
  大小：49        	块：8          IO 块：4096   普通文件
设备：fd00h/64768d	Inode：35250       硬链接：1
权限：(0664/-rw-rw-r--)  Uid：( 1000/      ac)   Gid：( 1000/      ac)
环境：unconfined_u:object_r:user_home_t:s0
最近访问：2024-02-20 21:26:49.600996922 +0800
最近更改：2024-02-20 21:26:01.592997031 +0800
最近改动：2024-02-20 21:26:01.594997031 +0800
创建时间：-
```

### 8、more

more：查询文件数据 ，返回的文件数据会分页显示

```shell
more  文件名

查询下一页：空格键
查询上一页：b
查看下一行：回车键
退出：q
```

### 9、less

less：对文件内容进行分页显示，查看文件下一页使用：回车键 ， 退出：q

```shell
[ac@localhost linux]$ less test 
```

### 10、head

head：查询文件头部的部分数据

```shell
head  [选项] 文件名

tip：没有选项默认返回10行

-n数字：从文件首行计算，返回指定的行数内容
-v：返回内容的时候会返回文件名

[ac@localhost linux]$ head -n3 test 
将进酒①
君不见黄河之水天上来②，奔流到海不复回。
君不见高堂明镜悲白发③，朝如青丝暮成雪④。

[ac@localhost linux]$ head -vn5 test 
==> test <==
将进酒①
君不见黄河之水天上来②，奔流到海不复回。
君不见高堂明镜悲白发③，朝如青丝暮成雪④。
人生得意须尽欢⑤，莫使金樽空对月⑥。
天生我材必有用⑦，千金散尽还复来⑧。
```

### 11、tail

tail：查询文件尾部的部分数据

```shell
tail [选项] 文件名

-n数字：从文件首行计算，返回指定的行数内容

[ac@localhost linux]$ tail -n2  test 
凄凄不似向前声60，满座重闻皆掩泣61。
座中泣下谁最多？江州司马青衫湿
```

### 12、ls

ls：查看当前所在目录中的所有文件数据

```shell
ls [选项]

-a：返回所有文件并且包含隐藏文件
-i：返回文件的节点数
-l：返回文件的详细信息

[ac@localhost ~]$ ls -l
总用量 0
drwxrwxr-x.        2 				ac    ac      34          2月  21 20:14    linux
文件类型，文件权限  文件的引用数量	  所有者  所属组  文件大小    修改时间			文件名
```

文件类型

```shell
d:目录
-:普通文件(正常的文本文件 ， 代码文件 ， 压缩包等)
l：软链接文件
s：socket接口文件
b：块设备(硬盘 ， 光盘等)
p：管道文件
```

文件权限

```shell
文件的读写执行权限：拥有者 ， 所属组，其他人
rwx	拥有者权限
rwx 所属组权限
r-x 其他人权限


权限信息：
r：可读属性
w：可写属性
x：可执行属性
-：没有权限

设置权限的顺序：读写执行 ， 如果没有对应权限就用-代替

其他的表示权限信息的方式
rwx  rwx  r-x
111  111  101  二进制：有对应的权限用1表示 ， 没有则用0表示
 7    7    5   八进制：r = 4 , w = 2 , x = 1
```

### 13、chmod

chmod：修改文件的权限信息

```shell
修改文件的权限：
拥有者：u
所属组：g
其他人：o
所有人：a


chmod [u/g/o/a][+/-][r/w/x] 文件名

[ac@localhost linux]$ ls -l
总用量 8
-rw-rw-r--. 1 ac ac   49 2月  20 21:26 demo.txt
-rw-rw-r--. 1 ac ac 2956 2月  21 20:14 test
[ac@localhost linux]$ chmod o+w test 
[ac@localhost linux]$ ls -l
总用量 8
-rw-rw-r--. 1 ac ac   49 2月  20 21:26 demo.txt
-rw-rw-rw-. 1 ac ac 2956 2月  21 20:14 test

```

### 14、cp

cp：文件拷贝

```shell
cp [-i] 文件名 目标目录路径

-i: 如果指定的目录中已经存在同名的文件，会提示是否覆盖

[ac@localhost linux]$ cp test /home/ac/demo/
[ac@localhost linux]$ cd /home/ac/demo/
[ac@localhost demo]$ ls
test

[ac@localhost linux]$ cp -i txt /home/ac/demo/
cp：是否覆盖"/home/ac/demo/txt"？ n

```

### 15、mv

mv：可以将文件进行移动到其他目录中，也可以对文件进行重命名

```shell
mv [-i] 文件名 目标目录路径

-i:如果指定的目录中已经存在同名的文件，会提示是否覆盖

[ac@localhost demo]$ mv -i txt /home/ac/linux/
mv：是否覆盖"/home/ac/linux/txt"？ y


文件的重命名
mv 原文件名 新文件名
[ac@localhost linux]$ mv txt ac.txt
[ac@localhost linux]$ ls
ac.txt  demo.txt  test

mv 可以在移动文件的时候对文件进行重命名
mv [-i] 文件名 目标目录路径/新的文件名

[ac@localhost linux]$ mv ac.txt /home/ac/demo/aaa.py
[ac@localhost linux]$ cd /home/ac//demo/
[ac@localhost demo]$ ls
aaa.py  test
```

### 16、wc

wc：统计词频

```shell
wc [选项] 文件名

-m:返回字符数
-L：返回长行的长度
-l：返回文件的函数

[ac@localhost linux]$ wc demo.txt 
 7  7 49 demo.txt
 行数 单词数 字节数
[ac@localhost linux]$ wc test 
  60   57 2957 test

[ac@localhost linux]$ wc -m test 
1087 test

[ac@localhost linux]$ wc -L test 
56 test

[ac@localhost linux]$ wc -l test 
60 test

```

### 17、grep

grep：数据筛选 ， 获取文件中符合条件的数据行

```shell
grep 条件 文件名

-n：返回的内容会显示内容在文件对应的行号

[ac@localhost linux]$ grep 人 test 
人生得意须尽欢⑤，莫使金樽空对月⑥。
主人何为言少钱⑳，径须沽取对君酌㉑。
主人下马客在船18，举酒欲饮无管弦。
忽闻水上琵琶声，主人忘归客不发。
门前冷落鞍马稀，老大嫁作商人妇46。
商人重利轻别离，前月浮梁买茶去47。
同是天涯沦落人，相逢何必曾相识！


[ac@localhost linux]$ grep -n  人 test 
4:人生得意须尽欢⑤，莫使金樽空对月⑥。
12:主人何为言少钱⑳，径须沽取对君酌㉑。
15:主人下马客在船18，举酒欲饮无管弦。
17:忽闻水上琵琶声，主人忘归客不发。
41:门前冷落鞍马稀，老大嫁作商人妇46。
42:商人重利轻别离，前月浮梁买茶去47。
47:同是天涯沦落人，相逢何必曾相识！
```

### 18、|

|：管道命令，需要有两个命令一起使用，第二个命令需要第一个命令的结果进行操作

```shell
命令1 | 命令2

grep 操作的数据是 ll 查询出来的
[ac@localhost /]$ ll -a | grep bin
lrwxrwxrwx.   1 root root    7 2月  20 20:42 bin -> usr/bin
lrwxrwxrwx.   1 root root    8 2月  20 20:42 sbin -> usr/sbin
```

### 19、重定向

重定向：> , >>  ,把原本命令的结果应该输出在控制台的数据，保存到文件中。

```shell
>:覆盖模式的重定向
[ac@localhost ~]$ ls -l > /home/ac/linux/ac.txt
[ac@localhost ~]$ ls -la > /home/ac/linux/ac.txt

>>:追加模式的重定向
[ac@localhost /]$ ls -la >> /home/ac/linux/ac.txt 
```

### 20、ln

ln：创建文件的软硬连接文件

```shell
软链接
当两个文件其中有一个发生修改， 那么另一个文件也会跟着修改
当删除了软链接文件，主文件不受影响
当删除主文件，软链接文件是不可以使用的

硬链接
当两个文件其中有一个发生修改， 那么另一个文件也会跟着修改
不管删除两个文件中的其中一个 ， 另一个不受影响

硬链接：ln 文件名 目标目录路径
[ac@localhost demo]$ ln ac.txt /home/ac/demo/


硬链接：ln -s 目标文件路径 目标目录路径
[ac@localhost demo]$ ln -s /home/ac/demo/aaa.py  /home/ac/linux/
[ac@localhost demo]$ 
```

### 21、tar

tar：对文件进行压缩或者解压

| 选项 | 说明                                     |
| ---- | ---------------------------------------- |
| z    | 使用gzip的格式进行压缩或者解压文件(.gz)  |
| c    | 创建新的打包文件                         |
| v    | 在打包或者解压过程中显示文件信息         |
| x    | 解压文件                                 |
| f    | 这个是在打包或者解压文件命令中必要的选项 |
| C    | 指定要解压的目录                         |

```shell
打包：
tar -zcvf 压缩包名称.tar.gz 要压缩的文件和目录(所有文件进行打包 *)

[ac@localhost linux]$ tar -zcvf acac.tar.gz *
demo.txt
test


解压：
tar -zxvf 压缩包名称.tar.gz -C 指定解压的目录位置

[ac@localhost linux]$ tar -zxvf acac.tar.gz 
demo.txt
test
[ac@localhost linux]$ tar -zxvf acac.tar.gz -C /home/ac/demo/
demo.txt
test
```

## 四、Linux环境搭建

### 1、用户管理

su：切换用户

```
su 用户名
```

```
查看用户信息：cat /etc/passwd

ac:x:1000:1000:ac:/home/ac:/bin/bash
用户名：密码：UID：GID：注释：主目录：shell格式
```

```
需要管理员权限
添加新的用户
useradd 用户名

配置密码，密码的复杂度：长度不少于8位，需要使用数字和字母组合
passwd 用户名

删除用户
userdel -r 用户名

修改用户的shell格式[/bin/bash([ac@localhost ac]$) , /bin/sh(sh-4.2$ )]
usermod 用户名 -s shell格式
```

### 2、vim文本编辑器

vim是一个完全脱离鼠标的操作

```
1、vim 文件名称
2、按 i 或者 insert 进入插入文本模式(文本编辑)
3、esc 退出编辑模式
4、:q 退出(会有提示)
5、:q! 不保存并退出
6、:wq 保存并退出

不进入文本编辑模式
yy：复制光标所在的那一行数据
p:粘贴数据
x：删除光标所在的那个字符
dd：删除光标所在的那一行数据

让光标快速移动到文件首行：gg
让光标快速移动到文件末尾：G
让光标快速移动到本行的开始：^(shift + 6)
让光标快速移动到本行的末尾：$(shift + 4)
```

### 3、配置静态IP

1、将虚拟机的网络设置为 NAT 模式

![image-20240226203045312](image.assets\image-20240226203045312.png)

![image-20240226203209726](image.assets\image-20240226203209726.png)

2、到 VMware中的菜单栏中的编辑进入选择虚拟网络编辑器

网络选项【VMnet8】

点击下面的【更改设置】

![image-20240226203442803](image.assets\image-20240226203442803.png)

3、网络选项【VMnet8】

选择NAT模式，点击【NAT 设置】

![image-20240226203623661](image.assets\image-20240226203623661.png)

4、设置网关，确保网关的前三位和子网ip的前三位一致，网关的最后一位不要设置为 1。

点击 【确定】

![image-20240226204011603](image.assets\image-20240226204011603.png)

![image-20240226204048017](image.assets\image-20240226204048017.png)

5、进入操作系统。到网络配置文件中配置静态 IP

切换为管理员的身份进行操作

进入：cd /etc/sysconfig/network-scripts/

使用 vim 编辑器编辑： vim ifcfg-ens33

进入配置文件中，修改两个地方

![image-20240226204510539](image.assets\image-20240226204510539.png)

```
IPADDR=192.168.163.10  # 静态 IP 地址 ， 前三位要和刚才设置子网 ip 一致
GATEWAY=192.168.163.2	# 网关，要和刚才设置的网关一致
NETMASK=255.255.255.0	# 子网掩码
DNS1=192.168.163.2 		# 域名服务，和网关一致
```

保存并退出，重启虚拟机

防火墙

```
开启防火墙
systemctl start firewalld.service walld

关闭防火墙
systemctl stop firewalld.service walld

查看防火墙的转态
systemctl status firewalld.service walld
```

### 4、搭建Python环境

Linux 中默认自带了 python2

1、进入管理员的身份，先安装依赖的编译环境

```
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel gcc
```

2、使用 wget 命令到官网中下载 python 的安装包

```
没有 wget 命令。下载 wget
yum -y install wget
```

进入 opt 目录 ， 将安装包下载到该目录中

```
wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz
```

3、对压缩包进行解压，并且创建目录

```
tar -zxvf Python-3.8.10.tgz
mkdir /usr/local/python3.8
```

4、进入解压好的 python 安装包

```
cd /opt/Python-3.8.10
```

5、进行编译安装

```
./configure --with-ssl --prefix=/usr/local/python3.8

make

make install
```

```
出现没有编译环境 gcc 
yum  install gcc
```

6、创建 Python 环境软连接到 系统的 bin 目录中

```
ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/python3
ln -s /usr/local/python3.8/bin/pip3.8 /usr/bin/pip3
```

在终端进入Python环境

```python
python3
```

### 5、搭建 MySQL 环境

1、使用 wget 下载安装包，下载到 opt 目录中

```
wget http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
```

2、安装  MySQL 公钥

```
rpm -i mysql57-community-release-el7-10.noarch.rpm

rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022
```

3、安装 MySQL 服务

```
yum -y install mysql-community-server
```

4、启动 MySQL

```
启动 MySQL 服务
systemctl start mysqld.service
关闭 MySQL 服务
systemctl stop mysqld.service
查看 MySQL 服务状态
systemctl status mysqld.service
```

5、获取进入 MySQL 的临时密码

```
grep 'password' /var/log/mysqld.log
```

![image-20240226212436131](image.assets\image-20240226212436131.png)

进入 MySQL 服务

```
mysql -uroot -p【回车】
输入密码
```

6、配置 MySQL 的密码

```
mysql 原本的密码复杂度比较高，大小写字母和数字混合不少于8位的密码

修改密码的负责度
set global validate_password_policy=0;
set global validate_password_length=1;

配置密码
alter user "root"@"localhost" identified  by "密码";
alter user "root"@"localhost" identified  by "root";
```

退出 MySQL 服务

7、修改 MySQL 的配置文件，修改字符编码

```
vim /etc/my.cnf
```

```
[client]
default-character-set=utf8 

[mysqld]
port = 3306
character-set-server=utf8
collation-server=utf8_general_ci
```

8、关闭MySQL服务，重新启动 MySQL 服务

### 6、远程连接

ssh 远程登录操作，ssh会对用用户进行身份信息的验证，会对两台主机之间发通信数据进行加密

安装 ssh 远程登录的服务端

```
yum install -y openssh-server
```

```
启动 ssh 服务
systemctl start ssh.service
关闭 ssh 服务
systemctl stop ssh.service
查看 ssh 服务状态
systemctl status ssh.service
```

Linux 客户端的 访问

```
ssh 用户名@ip
```

window 远程连接 Linux 服务端

```
1、确保在 Linux中可以 ping 通 windows 的ip
2、确保在 windows 中可以 ping 通 Linux 的ip
```

在 cmd 中ping Linux 的ip 的时候出现请求超时

到电脑中找到【网络和Initer】

点击【更改适配器选项】

![image-20240226214444503](image.assets\image-20240226214444503.png)

右击【VMnet8】选项【属性】

![image-20240226214553072](image.assets\image-20240226214553072.png)

双击打开【Internet 协议版本4（TCP/IPv4）】

![image-20240226214638234](image.assets\image-20240226214638234.png)

选项【使用下面的IP地址】

IP 和网关 的前三位 和虚拟机系统设置的 静态ip一致

IP 地址的最后一位不要和 虚拟机系统设置的 静态ip一致

网关的最后一位默认写 1

子网掩码和设置的时候一致

![image-20240226214822021](image.assets\image-20240226214822021.png)

全部设置好之后，点击所有的【确定】

重启虚拟机。



因为 windows 是没有预安装 ssh 客户端软件，需要第三方的软件进行链接，通过 xshell 进行远程连接

使用 xshell 创建连接会话

![image-20240226215448266](image.assets\image-20240226215448266.png)

xftp远程传输

![image-20240226215909712](image.assets\image-20240226215909712.png)