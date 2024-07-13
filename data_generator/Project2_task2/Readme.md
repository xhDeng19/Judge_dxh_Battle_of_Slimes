# Data Generator 使用教程
### 制作 by 邓熙涵
### 2024/07/13

## 0.注意事项
1. `Project2`的`task1`应使用`Project1`文件夹下`data_generator`
2. 本案例生成程序用法与`Project1`的`data_generator`一样，这里不再赘述。本文档只说明`Project2`的`task2`的`data_generator`的不同之处。
3. `Project2`的`task2`要求敌人以**均匀分布的概率**来随机选择首先上场的史莱姆，因此生成的案例不光要包含最终回合数的信息，也需要包含敌人首先选上场的史莱姆的类型信息，这样才能在使用该案例时生成一样的结果。因而本`data_generator`生成的案例如下

<div align=center><img src="..\\..\\pic\\p2_record_dir_task_2.png" width=100%></div>

之后使用案例时可以将它们重命名为 `数字.敌方首先选择的史莱姆名称.in`（名称应首字母大写），注意这样命名的文件类型仍为IN文件，可用记事本打开并编辑。