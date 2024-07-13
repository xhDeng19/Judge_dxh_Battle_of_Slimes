# Judge_dxh 使用教程
### 制作 by 邓熙涵
### 创建日期：2024/07/13
下载整个文件：https://github.com/xhDeng19/Judge_dxh_Battle_of_Slimes/archive/refs/heads/main.zip

## 0.文件结构
```
judge_dxh
|- task1
|   |- judge_dxh.py
|   |- data
|      |- 1.in
|      |- 1.out
|      |- 2.in
|      |- 2.out
|      |- 3.in
|      |- 3.out
|      |- ...
|      |- 数字.in
|      |- 数字.out
|
|- task2
|   |- judge_dxh.py
|   |- data
|      |- 1.Green.in
|      |- 1.Green.out
|      |- 2.Yellow.in
|      |- 2.Yellow.out
|      |- 3.Blue.in
|      |- 3.Blue.out
|      |- ...
|      |- 数字.史莱姆名称.in
|      |- 数字.史莱姆名称.out
|
|- ...
```
## 1.注意事项
1. 如果终端显示 `ModuleNotFoundError: No module named 'tqdm'`，请在`powershell`里使用指令`pip install tqdm`
2. 此测评程序仅针对`Project2`的`task1`和`task2`，且同时支持**Windows**和**macOS**系统
3. 提交作业时记得删掉该测评程序的**所有**文件。
4. 测试时，需将所有的 .cpp 文件与所有的 .h 文件放到**同一个**文件夹下
5. 每个`task`里面的文件均**不**一样，不能替换成其他task的文件。
6. 每个`data`文件夹下的`your_output_files`文件夹用来存放每次运行后你的程序输出的结果，在首次运行前**不存在**。
7. 与`judge_dxh.py`在同一目录下的`compile`文件夹用来存放每次运行后你的程序编译出的二进制可执行文件，在首次运行前**不存在**，且在**Windows**系统下为.exe文件，在**macOS**系统下为Unix可执行文件。
8. 每个data文件夹下的 `*.in` 文件为测试所用案例，均用 `data generator生成`。运行程序后每个data文件夹下的 `*.out` 文件为**非官方**提供的输出结果（**结果可能有错，请及时反馈**）。
9.  此程序提供的案例的结果必须是**获胜**、**平局**或**失败**，无法评测一个尚未终止的对局。
10. 如果你的程序输出`Time Out!`，则证明程序**运行超时**，即没有达到**获胜**、**平局**或**失败**，请检查你的代码逻辑。
11. 如果你的程序输出`There's a great chance that the enemy didn't randomly select their slime with a uniform probability`，则说明你的`task2`下的程序大概率没有实现敌方以以**均匀分布的概率**来随机选择首先上场的史莱姆（本测评程序每个案例默认检查20轮，如果20轮内你的程序首次选上的敌方史莱姆**没有一次**符合案例中首次选上敌方史莱姆，则会报错），注意随机数种子的使用
12. 如果有错误或者有好的案例请联系 DanielDeng12321@163.com 。

## 2.使用说明
**task1与Project1的使用方法基本一样，下面介绍task2**

**task2的测评程序运行较慢，需花费约20秒时间**
1. 将 `judge_dxh/Project2/task2` 下的**全体**移动至你的 `P2-姓名-任务2` 文件夹下，如下
```
P2-姓名-任务2
|- judge_dxh.py
|- data
|  |- 1.Green.in
|  |- 1.Green.out
|  |- 2.Yellow.in
|  |- 2.Yellow.out
|  |- 3.Blue.in
|  |- 3.Blue.out
|  |- ...
|
|- main.cpp
|- *.cpp
|- *.h
|- ...
```
1. 在**当前目录**打开cmd，输入 `python judge_dxh.py` 并回车，`P2-姓名-任务2` 文件夹变为如下
```
P2-姓名-任务2
|- judge_dxh.py
|- compile
|  |- main.exe (或main)
|
|- data
|  |- your_output_files
|     |- 1.Green.out
|     |- 2.Yellow.out
|     |- 3.Blue.out
|     |- ...
|  |
|  |- 1.Green.in
|  |- 1.Green.out
|  |- 2.Yellow.in
|  |- 2.Yellow.out
|  |- 3.Blue.in
|  |- 3.Blue.out
|  |- ...
|
|- main.cpp
|- *.cpp
|- *.h
|- ...
```
* 若cmd输出 `1.Green.out is correct`，则证明你的程序**成功编译**且`1.Green.out`案例**完全正确**
* 若cmd输出 `1.Green.out is WRONG. Compare data/1.Green.out and data/your_output_files/1.Green.out to find out."`，则证明你的程序**成功编译**但第一个案例**输出有误**，`cmd窗口`中会显示具体的错误和错误所在的行数 (特殊的错误情况请参考**使用说明**)
* 若cmd输出其他提示，则证明你的程序**编译失败**或者命令行输入有误，请检查你的文件是否完好，你的程序是否含有bug，你当前的目录是否正确

