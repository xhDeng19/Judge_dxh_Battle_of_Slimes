import subprocess
import glob
import os

#限时2秒（单位为秒）
TIMEOUT = 2


def in_current_dir(name):
    return os.path.join(os.path.dirname(__file__), name)

def get_data_num(file_dir):
    file_name = os.path.basename(file_dir)
    return int(os.path.splitext(file_name)[0])


def output_your_files(data_in_files, your_out_files, exe_files):
    for i in range(len(data_in_files)):
        isTimeOut = False
        with open(data_in_files[i], 'r') as input_file, open(your_out_files[i], 'w') as output_file:
            # 输入为 data/*.in 输出为 data/your_output_files.out
            try:
                run_result = subprocess.run(exe_files, stdin=input_file, stdout=output_file, stderr=subprocess.PIPE, text=True, timeout=TIMEOUT)
                if run_result.returncode != 0:
                    print(f"{i + 1}.in failed in execution!")
                    print(run_result.stderr)
            except subprocess.TimeoutExpired:
                isTimeOut = True
        
        if isTimeOut:
            with (open(your_out_files[i], 'w')) as output_file:
                output_file.write("Time Out!")


def compare_files(data_out_files, your_out_files):
    for i in range(len(data_out_files)):
        # 比较 data/*out.out 与 data/your_output_files.out
        with open(data_out_files[i], 'r') as fstandard, open(your_out_files[i], 'r') as fyours:
            standard_content = fstandard.readlines()
            your_content = fyours.readlines()
            #del_hp_print(your_content) #放弃检测第一次hp输出和平局的最后一次hp输出（Task?.exe的bug）
            isCorrect = True

            for line_i in range(min(len(standard_content), len(your_content))):
                if standard_content[line_i] != your_content[line_i]:
                    if isCorrect:
                        print(f"{i + 1}.out is WRONG. Compare {os.path.join('data', f'{i + 1}.out')} and {os.path.join('data', 'your_output_files', f'{i + 1}.out')} to find out.")
                        print("\nDetail:") 
                    print(f"line {line_i + 1}: ")
                    print(f"Correct answer: {standard_content[line_i]}")
                    print(f"Your answer: {your_content[line_i]}")
                    print("\n")
                    isCorrect = False

            if (isCorrect and len(standard_content) == len(your_content)):
                print(f"{i + 1}.out is correct.")
            elif (isCorrect):
                print(f"{i + 1}.out is WRONG. Compare {os.path.join('data', f'{i + 1}.out')} and {os.path.join('data', 'your_output_files', f'{i + 1}.out')} to find out.")

#初始化
if not os.path.exists(os.path.join(in_current_dir('data'), 'your_output_files')):
    os.makedirs(os.path.join(in_current_dir('data'), 'your_output_files'))     
if not os.path.exists(in_current_dir('compile')):
    os.makedirs(os.path.join(in_current_dir('compile')))    


# 文件目录               
data_in_files = glob.glob(os.path.join(in_current_dir('data'), '*.in'))
data_out_files = [os.path.join(in_current_dir('data'), f'{i + 1}.out') for i in range(len(data_in_files))]
your_out_files = [os.path.join(in_current_dir('data'), 'your_output_files', f'{i + 1}.out') for i in range(len(data_in_files))]
cpp_files = glob.glob(in_current_dir('*.cpp'))
task_files = glob.glob(in_current_dir('Task?.exe'))
exe_files = [os.path.join(in_current_dir('compile'), 'main')]

data_in_files.sort(key=lambda string : get_data_num(string))

if not cpp_files:
    print("No .cpp files found in the current directory")
else:
    # 编译所有的.cpp文件 (启用c++11标准)
    compile_result = subprocess.run(['g++', '-std=c++11', '-o'] + exe_files + cpp_files, capture_output=True, text=True)

    if compile_result.returncode != 0:
        #编译失败
        print("Compilation failed")
        print(compile_result.stderr)
    else:
        #编译成功
        output_your_files(data_in_files, your_out_files, exe_files)
        compare_files(data_out_files, your_out_files)
