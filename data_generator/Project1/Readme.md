# Data Generator 使用教程
### 制作 by 邓熙涵
### 2024/07/01

## 0.文件结构
```
data_generator
|- data_generator.py
|- data
|  |- your_output_files
|     |- 空
|
|- record
|  |- 空
```

## 1.注意事项
1. 此程序可以针对一个task自动生成很多**较好**的测试案例。这里的**较好**指测试的有效操作数较多，可以检测出的bug较多。因此本程序以最终达到的回合数Round的大小作为评判一个测试案例好坏的标准。最终达到的Round回合数越**大**，测试案例越**好**。
2. 此程序对Project1的task1、task2和task3均适用。
3. 生成案例时，需将所有的 .cpp 文件与所有的 .h 文件放到**同一个**文件夹下
4. data_generator.py 为主程序，data文件夹下存放一轮生成的所有测试案例和测试结果，record文件夹下存放了程序的记录结果和所有**较好**的测试案例。（详细操作见 **2.使用说明**）
5. data文件夹下的 your_output_files文件夹和 record文件夹在首次运行前为空。
6. 每次运行 data_generator.py 后均会改变 data文件夹和 record文件夹中的内容，所以运行结束后请**及时保存** record文件夹下的运行结果。
7. 此程序生成的输入案例采用随机数生成，不能保证运行时间越长，运行结果越好。

## 2.使用说明
**以task2为例**
1. 将 `data_generator` 下的**全体**移动至你的 `P1-姓名-任务2` 文件夹下，如下
```
P1-姓名-任务2
|- data_generator.py
|- data
|  |- your_output_files
|     |- 空
|
|- record
|  |- 空
|
|- main.cpp
|- *.cpp
|- *.h
|- ...
```
1. 在**当前目录**打开cmd，输入 `python data_generator.py` 并回车，**程序开始运行**，此时cmd中会间隔100轮显示一次当前运行的最好测试案例的最终回合数（间隔的轮数可在 `data_generator.py` 中的 `SHOW_ROUND_GAP = 100` 语句进行调整）
2. 运行过程中 `P1-姓名-任务2` 文件夹和 `record` 文件夹变为如下
```
P1-姓名-任务2
|- data_generator.py
|- data
|  |- your_output_files
|     |- 1.out
|     |- 2.out
|     |- ...
|
|  |- 1.in
|  |- 2.in
|  |- ...
|
|- record
|  |- record.txt
|  |- Max_Score_Operation_score_最终回合数.in （最终回合数为该输入下的最终回合数）
|  |- Max_Score_Operation_score_最终回合数.in （最终回合数为该输入下的最终回合数）
|  |- ...
|
|- main.cpp
|- *.cpp
|- *.h
|- ...
```
<div align=center><img src="..\\..\\pic\\p1_record_dir_task_2.png" width=100%></div>

1. 运行过程中 `cmd` 窗口显示如**左下**。点击 `record/record.txt` 可以查看自运行开始到现在的运行结果，如**右下**
<div align=left>
<img src="..\\..\\pic\\p1_cmd_task_2_record.png" width=38%> <img src="..\\..\\pic\\p1_record_task_2.png" width=60%>
</div>

1. 在 `cmd` 窗口内按 `Ctrl+c` 结束运行，可选取 `record` 文件夹下的最终回合数交大的 `Max_Score_Operation_score_最终回合数.in` 作为输入的测试案例，将其文件名改为 `数字.in`