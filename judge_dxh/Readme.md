# Judge_dxh 使用教程
### 制作 by 邓熙涵
### 创建日期：2024/06/30
下载整个文件：https://github.com/xhDeng19/Judge_dxh_Battle_of_Slimes/archive/refs/heads/main.zip

## 0.文件结构
```
judge_dxh
|- Windows
|   |- task1
|   |  |- judge_dxh.py
|   |  |- Task1.exe
|   |  |- data
|   |     |- 1.in
|   |     |- 2.in
|   |     |- ...
|   |
|   |- task2
|   |  |- judge_dxh.py
|   |  |- Task2.exe
|   |  |- data
|   |     |- 1.in
|   |     |- 2.in
|   |     |- ...
|   |
|   |- task3
|   |  |- judge_dxh.py
|   |  |- Task3.exe
|   |  |- data
|   |     |- 1.in
|   |     |- 2.in
|   |     |- ...
|- macOS
|   |- task1
|   |  |- judge_dxh.py
|   |  |- data
|   |     |- 1.in
|   |     |- 1.out
|   |     |- ...
```
```
|   |- task2
|   |  |- judge_dxh.py
|   |  |- data
|   |     |- 1.in
|   |     |- 1.out
|   |     |- ...
|   |
|   |- task3
|   |  |- judge_dxh.py
|   |  |- data
|   |     |- 1.in
|   |     |- 1.out
|   |     |- ...
```
## 1.注意事项
1. 如果你使用的是**Windows**/**macOS**系统，请用`Windows/macOS`文件夹下的程序。
2. 此测评程序仅针对Project1的task1、task2和task3。
3. 提交作业时记得删掉该测评程序的**所有**文件。
4. 测试时，需将所有的 .cpp 文件与所有的 .h 文件放到**同一个**文件夹下
5. 每个task里面的data文件夹均**不**一样，不能替换成其他task的data文件夹。
6. 每个data文件夹下的your_output_files文件夹用来存放每次运行后你的程序输出的结果，在首次运行前**不存在**。
7. 每个data文件夹下的 `*.in` 文件为测试所用案例，均用 `data generator生成`。运行程序后每个data文件夹下的 `*.out` 文件为官方提供的二进制程序的输出结果（注意**没有**第一次slime的血量输出）。
8. 此程序提供的案例的结果必须是**获胜**、**平局**或**失败**，无法评测一个尚未终止的对局。
9.  此程序不会检测**第一次slime的血量输出**，因二进制程序没有第一次slime的血量输出，无法保证案例的准确性。
10. 如果你的程序输出`Time Out!`，则证明程序**运行超时**，即没有达到**获胜**、**平局**或**失败**，请检查你的代码逻辑。
11. 如果有错误或者有好的案例请联系 DanielDeng12321@163.com 。

## 2.使用说明
**以Windows下的task3为例** (macOS程序中无Task.exe文件，运行结束后多了compile文件夹，记得删除即可)
1. 将 `judge_dxh/Project1/task3` 下的**全体**移动至你的 `P1-姓名-任务3` 文件夹下，如下
```
P1-姓名-任务3
|- judge_dxh.py
|- Task3.exe
|- data
|  |- 1.in
|  |- 2.in
|  |- ...
```
```
|- main.cpp
|- *.cpp
|- *.h
|- ...
```
2. 在**当前目录**打开cmd，输入 `python judge_dxh.py` 并回车，`P1-姓名-任务3` 文件夹变为如下
```
P1-姓名-任务3
|- judge_dxh.py
|- Task3.exe
|- data
|  |- your_output_files
|     |- 1.out
|     |- 2.out
|     |- ...
|  |- 1.in
|  |- 1.out
|  |- 2.in
|  |- 2.out
|  |- ...
|
|- main.cpp
|- *.cpp
|- *.h
|- ...
```
* 若cmd输出 `1.out is correct`，则证明你的程序**成功编译**且第一个案例**完全正确**
* 若cmd输出 `1.out is WRONG. Compare data/1.out and data/your_output_files/1.out to find out."`，则证明你的程序**成功编译**但第一个案例**输出有误**，`cmd窗口`中会显示具体的错误和错误所在的行数，如下（案例来自一个复活的slime的血量均为50的小朋友）

<img src="..\\pic\\cmd_wrong_answer.png">

* 若cmd输出其他提示，则证明你的程序**编译失败**或者命令行输入有误，请检查你的文件是否完好，你的程序是否含有bug，你当前的目录是否正确

3. 如果你的程序输出`Time Out!`，则证明程序**运行超时**（见下图），即没有达到**获胜**、**平局**或**失败**，请检查你的代码逻辑。更改 judge_dxh.py 程序里的 `TIMEOUT = 2` 语句（单位为**秒**）**没有**实质性作用，因为提供的测试案例都是达到**获胜**、**平局**或**失败**的对局。

<img src="..\\pic\\cmd_time_out.png">
