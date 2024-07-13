import subprocess
import glob
import sys
from os import makedirs, path, system

#限时2秒（单位为秒）
TIMEOUT = 2

def in_current_dir(name):
    current_name_len = sys.argv[0].rfind("/")
    if current_name_len == -1:
        current_name_len = sys.argv[0].rfind("\\")

    return sys.argv[0][:current_name_len + 1] + name

def get_data_num(file_dir):
    index_dir = file_dir.rfind('\\')
    index_name = file_dir.rfind('.')
    return int(file_dir[index_dir + 1: index_name])

def output_authentic_files(task_files, data_out_files, data_in_files):
    for i in range(len(data_in_files)):
        with open(data_in_files[i], 'r') as input_file, open(data_out_files[i], 'w') as output_file:
            # 输入为 data/*.in 输出为 data/your_output_files.out
            try:
                subprocess.run([task_files[0]], stdin=input_file, stdout=output_file, stderr=subprocess.PIPE, text=True, timeout=TIMEOUT)

            except subprocess.TimeoutExpired:
                print(f"{i + 1}.in is invalid!")

def output_your_files(data_in_files, your_out_files):
    for i in range(len(data_in_files)):
        isTimeOut = False
        with open(data_in_files[i], 'r') as input_file, open(your_out_files[i], 'w') as output_file:
            # 输入为 data/*.in 输出为 data/your_output_files.out
            try:
                run_result = subprocess.run(['.\\main'], stdin=input_file, stdout=output_file, stderr=subprocess.PIPE, text=True, timeout=TIMEOUT)
                if run_result.returncode != 0:
                    print(f"{i + 1}.in failed in execution!")
                    print(run_result.stderr)
            except subprocess.TimeoutExpired:
                isTimeOut = True
        
        if isTimeOut:
            with (open(your_out_files[i], 'w')) as output_file:
                output_file.write("Time Out!")

def modify_authentic_output_files(data_out_files):
    for i in range(len(data_out_files)):
        with open(data_out_files[i], 'r') as read_file:
            new_line = []
            lines = read_file.readlines()
            for line in lines:
                #替换Task?.exe中不合理的输出
                new_line += line.replace("pet", "slime")\
                            .replace("starts", "start")\
                            .replace("You sends", "You send")\
                            .replace("Enemy start", "Enemy starts")\
                            .replace("Battle start!", "Battle starts!")\
                            .replace("Enemy WIN! You LOSE!", "You Lose\n")\
                            .replace("You WIN! Enemy LOSE!", "You Win\n")\
                            .replace("DRAW!", "Draw\n")
        
        with open(data_out_files[i], "w") as write_file:
            write_file.writelines(new_line)

def del_hp_print(your_content):
    for i in range(len(your_content)):
        if "||" in your_content[i]:
            del your_content[i]
            break

    for i in range(len(your_content) - 1, -1, -1):
        if "Draw" in your_content[i]:
            del your_content[i - 1]
            break

def compare_files(data_out_files, your_out_files):
    for i in range(len(data_out_files)):
        # 比较 data/*out.out 与 data/your_output_files.out
        with open(data_out_files[i], 'r') as fstandard, open(your_out_files[i], 'r') as fyours:
            standard_content = fstandard.readlines()
            your_content = fyours.readlines()
            del_hp_print(your_content) #放弃检测第一次hp输出和平局的最后一次hp输出（Task?.exe的bug）
            isCorrect = True

            for line_i in range(min(len(standard_content), len(your_content))):
                if standard_content[line_i] != your_content[line_i]:
                    if isCorrect:
                        print(f"{i + 1}.out is WRONG. Compare data\\{i + 1}.out and data\\your_output_files\\{i + 1}.out to find out.")
                        print("\nDetail:") 
                    print(f"line {line_i + 1}: ")
                    print(f"Correct answer: {standard_content[line_i]}")
                    print(f"Your answer: {your_content[line_i]}")
                    print("\n")
                    isCorrect = False

            if (isCorrect and len(standard_content) == len(your_content)):
                print(f"{i + 1}.out is correct.")
            elif (isCorrect):
                print(f"{i + 1}.out is WRONG. Compare data\\{i + 1}.out and data\\your_output_files\\{i + 1}.out to find out.")

#初始化
if not path.exists(in_current_dir("data\\your_output_files")):
    makedirs(in_current_dir("data\\your_output_files"))         


# 文件目录               
data_in_files = glob.glob(in_current_dir('data\\*.in'))
data_out_files = [in_current_dir(f'data\\{i + 1}.out') for i in range(len(data_in_files))]
your_out_files = [in_current_dir(f'data\\your_output_files\\{i + 1}.out') for i in range(len(data_in_files))]
cpp_files = glob.glob(in_current_dir('*.cpp'))
task_files = glob.glob(in_current_dir('Task?.exe'))

data_in_files.sort(key=lambda string : get_data_num(string))
data_out_files.sort(key=lambda string : get_data_num(string))
your_out_files.sort(key=lambda string : get_data_num(string))


if not cpp_files:
    print("No .cpp files found in the current directory")
else:
    # 编译所有的.cpp文件 (启用c++11标准)
    compile_result = subprocess.run(['g++', '-std=c++11', '-o', 'main'] + cpp_files, capture_output=True, text=True)

    if compile_result.returncode != 0:
        #编译失败
        print("Compilation failed")
        print(compile_result.stderr)
    else:
        #编译成功
        output_authentic_files(task_files, data_out_files, data_in_files)
        modify_authentic_output_files(data_out_files)

        output_your_files(data_in_files, your_out_files)
        compare_files(data_out_files, your_out_files)
