# Judge_dxh 使用教程
### 制作 by 邓熙涵
### 2024/06/30

## 0.文件结构
```
judge_dxh.zip
|- Project1
|   |- task1
|   |  |- judge_dxh.py
|   |  |- data
|   |     |- your_output_files
|   |     |- 1.in
|   |     |- 1.out
|   |     |- ...
|   |
|   |- task2
|   |  |- judge_dxh.py
|   |  |- data
|   |     |- your_output_files
|   |     |- 1.in
|   |     |- 1.out
|   |     |- ...
|   |
|   |- task3
|   |  |- judge_dxh.py
|   |  |- data
|   |     |- your_output_files
|   |     |- 1.in
|   |     |- 1.out
|   |     |- ...
```
## 1.注意事项
1. 此测评程序仅针对Project1的task1、task2和task3。
2. 提交作业时记得删掉该测评程序的**所有**文件。
3. 测试时，需将所有的 .cpp 文件与所有的 .h 文件放到**同一个**文件夹下
4. 每个task里面的data文件夹均**不**一样，不能替换成其他task的data文件夹。
5. 每个task文件夹下的your_output_files文件夹用来存放每次运行后你的程序输出的结果，在首次运行前为**空**。
6. 每个task文件夹下的 *.in 与 *.out 文件为测试所用案例，案例为同学给出，如果有错误或者有好的案例请联系 DanielDeng12321@163.com 。
7. 此程序提供的案例的结果必须是**获胜**、**平局**或**失败**，无法评测一个尚未终止的对局。

## 2.使用说明
**以task1为例**
1. 将 `judge_dxh/Project1/task1` 下的**全体**移动至你的 `P1-姓名-任务1` 文件夹下，如下
```
P1-姓名-任务1
|- judge_dxh.py
|- data
|  |- your_output_files
|  |- 1.in
|  |- 1.out
|  |- ...
|
|- main.cpp
|- *.cpp
|- *.h
|- ...
```
1. 在**当前目录**打开cmd，输入 `python judge_dxh.py` 并回车，`P1-姓名-任务1` 文件夹变为如下
```
P1-姓名-任务1
|- judge_dxh.py
|- data
|  |- your_output_files
|     |- 1.out
|     |- ...
|  |- 1.in
|  |- 1.out
|  |- ...
|
|- main.cpp
|- *.cpp
|- *.h
|- ...
```
* 若cmd输出 `1.out is correct`，则证明你的程序**成功编译**且第一个案例**完全正确**
* 若cmd输出 `1.out is WRONG. Compare data/1.out and data/your_output_files/1.out to find out."`，则证明你的程序**成功编译**但第一个案例**输出有误**
* 若cmd输出其他提示，则证明你的程序**编译失败**或者命令行输入有误，请检查你的文件是否完好，你的程序是否含有bug，你当前的目录是否正确

1. 如果你的程序成功编译但**输出有误**，有可能是程序**运行超时**，请检查是否有不合理的 while 循环。更改 judge_dxh.py 程序里的 `TIMEOUT = 2` 语句（单位为**秒**）**没有**实质性作用，因为提供的测试案例都是达到**获胜**、**平局**或**失败**的对局。
