脚本解决问题：
(1) 处理计算细胞个数等问题

1. 先说下硬件要求:

例子1: i3+4g内存, 无显卡. 正常运行

2. 需要下载的东西:

(1)Anaconda : https://www.anaconda.com/download/#download

到"Python 3.6 version"下直接点Download就行, 下载完后直接下一步到安装完就行了;

(2)MAIN文件夹下cellnumber.py和thinkder_main.py脚本，度盘：*****



3. 搭建:
(1) 开始菜单-->Anaconda3(64-bit)-->Anaconda Prompt

出现黑窗口然后, 输入以下命令, 输入一行, 回车, 安装完后继续输入下一行, 回车:

pip install tkinter

pip install Pillow

pip install cv2



(2) 全部安装完后，退出；

从开始菜单-->Anaconda3(64-bit)-->Anaconda Prompt

4. 把玩:

(1) 首先将cellnumber.py和thinkder_main.py拷贝到一个相同目录(必须同目录)；

(2) 在Anaconda Prompt 的黑白界面里面输入python /***(path)***/thinkder_main.py ,回车

(3) 一切顺利就可以弹出一个图像界面，可以选择的控制有:

		File Open 打开目录；
		
		colour number cut 根据不同色彩进行分割，推荐150左右；
		
		area 表示细胞的面积，低于这个数值一下的抛弃；
		
		area ratio 表示面积内的所占比例，删除一些细长的结构

(4) 结果说明：

		cell number：统计出来没有经过过滤细胞个数；
		
		Maybe cell number: 统计出经过过滤的细胞个数：
		
		number ratio：未被过滤细胞个数的比例；
		
		area ratio：过滤后的细胞占整张图上的面积；
		
		图片四张，分别是黑白图和色彩图，并且在第二张图上标记统计个数对应细胞


![avatar](https://github.com/zpeng1989/Cell_number/blob/master/Other/1.png)
		
