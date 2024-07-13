# Battle of Slimes Judge by 邓熙涵
 制作日期：2024/07/01

 简介：自制SJTU程序设计实践Battle of Slimes测评程序（已提供案例）和生成测试案例程序
 
 下载整个文件：https://github.com/xhDeng19/Judge_dxh_Battle_of_Slimes/archive/refs/heads/main.zip
 ## 更新日志
 **2024/07/13更新**:
* 更新了针对Project2中的task1和task2的测评程序和生成测试案例程序，分别在`judge_dxh/Project2`和`data_generator/Project2_task2`下
* Project2提供的输出不是老师给的，不能完全保证其正确性，请酌情使用测评程序，如果有错误请反馈一下

 **2024/07/08更新**：
* judge_dxh现可支持macOS系统，请在judge_dxh文件夹下选择对应于自己系统的程序


 **2024/07/03更新**：
* 加入了仇翊宇同学提供的平局案例
* judge_dxh不会检测**平局时的最后一次slime的血量输出**，因二进制程序平局时没有最后一次slime的血量输出，无法保证结果的准确性


 **2024/07/02更新**：
* 加入了官方提供的三个任务的二进制程序（即`Task1.exe`、`Task2.exe`和`Task3.exe`）
* 删除了judge_dxh里面自带的.out文件，改为用每个任务的二进制程序实时输出data文件夹里的.out文件，保证了结果的准确性
* judge_dxh不再会检测**第一次slime的血量输出**，因二进制程序没有第一次slime的血量输出，无法保证结果的准确性



## 0.文件结构
```
Judge_dxh_Battle_of_Slimes.zip
|- data_generator
|  |- Project1
|  |- Project2_task2
|
|- judge_dxh
|  |- Project1
|  |- Project2
|
|- pic
|- ...
```
## 1.使用说明
1. 如果你想用 `judge_dxh 测评程序`，请到 judge_dxh文件夹下查看Readme说明
2. 如果你想用 `data generator 生成测试案例程序`，请到 data_generator文件夹下查看Readme说明
3. 本程序未经过大量测试与使用，如果你发现任何问题，请联系 DanielDeng12321@163.com